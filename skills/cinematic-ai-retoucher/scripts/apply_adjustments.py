#!/usr/bin/env python3
"""Apply explicit tonal/color layers to source pixels; no model or image synthesis.

Requires Python 3.9+, Pillow and NumPy. See references/adjustment-workflow.md.
"""
import argparse
import hashlib
import io
import json
import math
import struct
import sys
from pathlib import Path

import numpy as np
from PIL import Image, ImageCms, ImageDraw, ImageFilter, __version__ as pillow_version


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def number(value, lo, hi, label):
    if isinstance(value, bool) or not isinstance(value, (int, float)) or not math.isfinite(value) or not lo <= value <= hi:
        raise ValueError(f"{label} must be a finite number in {lo}..{hi}.")
    return float(value)


def keys(obj, allowed, label):
    if not isinstance(obj, dict) or set(obj) - set(allowed):
        raise ValueError(f"Invalid {label}; supported fields: {', '.join(allowed)}.")


def load_source(path):
    with Image.open(path) as im:
        if getattr(im, "n_frames", 1) != 1 or im.mode not in ("RGB", "RGBA"):
            raise ValueError("Export a single 8-bit RGB/RGBA sRGB image from your editor first.")
        if im.getexif().get(274, 1) != 1:
            raise ValueError("Normalize EXIF orientation in your editor first; this helper does not rotate pixels.")
        if im.format == "PNG" and path.read_bytes()[24] != 8:
            raise ValueError("16-bit PNG is unsupported; use a native 16-bit editor or an explicit 8-bit export.")
        if im.format == "TIFF" and any(v != 8 for v in im.tag_v2.get(258, (8,))):
            raise ValueError("16-bit TIFF is unsupported; use a native 16-bit editor or an explicit 8-bit export.")
        alpha = im.getchannel("A").copy() if im.mode == "RGBA" else None
        rgb = im.convert("RGB")
        icc = im.info.get("icc_profile")
        srgb = ImageCms.ImageCmsProfile(ImageCms.createProfile("sRGB"))
        conversion = "untagged input assumed sRGB"
        if icc:
            profile = ImageCms.ImageCmsProfile(io.BytesIO(icc))
            rgb = ImageCms.profileToProfile(rgb, profile, srgb, outputMode="RGB")
            conversion = "embedded ICC converted to sRGB by LittleCMS"
        profile_data = bytearray(srgb.tobytes())
        # LittleCMS stamps a generated ICC with the wall clock. Canonicalize
        # only the output profile metadata so identical exports hash equally.
        profile_data[24:36] = struct.pack(">6H", 2000, 1, 1, 0, 0, 0)
        profile_data[84:100] = bytes(16)  # No optional ICC profile-ID assertion.
        return rgb, alpha, bytes(profile_data), conversion


def mask_for(spec, source, plan_dir):
    keys(spec, ("type", "center", "radius", "points", "path", "range", "invert", "feather_px"), "mask")
    height, width = source.shape[:2]
    kind = spec.get("type", "all")
    fields = {"all": (), "ellipse": ("center", "radius"), "polygon": ("points",),
              "file": ("path",), "luminance": ("range",)}
    if kind not in fields:
        raise ValueError(f"Unknown mask type: {kind}.")
    keys(spec, ("type", "invert", "feather_px") + fields[kind], f"{kind} mask")
    if kind == "all":
        mask = np.ones((height, width), dtype=np.float32)
    elif kind == "ellipse":
        if len(spec.get("center", [])) != 2 or len(spec.get("radius", [])) != 2:
            raise ValueError("An ellipse needs center [x,y] and radius [x,y].")
        cx, cy = [number(v, 0, 1, "center") for v in spec["center"]]
        rx, ry = [number(v, 0.001, 2, "radius") for v in spec["radius"]]
        y, x = np.mgrid[:height, :width]
        distance = np.sqrt(((x / max(width - 1, 1) - cx) / rx) ** 2 + ((y / max(height - 1, 1) - cy) / ry) ** 2)
        t = np.clip(1 - distance, 0, 1)
        mask = (t * t * (3 - 2 * t)).astype(np.float32)
    elif kind == "polygon":
        points = spec.get("points", [])
        if len(points) < 3 or any(len(p) != 2 for p in points):
            raise ValueError("A polygon requires at least three [x,y] points.")
        xy = [(number(p[0], 0, 1, "x") * (width - 1), number(p[1], 0, 1, "y") * (height - 1)) for p in points]
        img = Image.new("L", (width, height), 0)
        ImageDraw.Draw(img).polygon(xy, fill=255)
        mask = np.asarray(img, dtype=np.float32) / 255
    elif kind == "file":
        if not isinstance(spec.get("path"), str):
            raise ValueError("A file mask needs a path relative to the recipe or an absolute path.")
        with Image.open((plan_dir / spec["path"]).resolve()) as img:
            if img.mode != "L" or img.size != (width, height) or getattr(img, "n_frames", 1) != 1:
                raise ValueError("External masks must be single 8-bit grayscale images matching source dimensions.")
            mask = np.asarray(img, dtype=np.float32) / 255
    elif kind == "luminance":
        points = spec.get("range", [])
        if len(points) != 4:
            raise ValueError("A luminance range needs [start,full_start,full_end,end].")
        a, b, c, d = [number(v, 0, 1, "luminance boundary") for v in points]
        if not a < b <= c < d:
            raise ValueError("Luminance boundaries require start < full_start <= full_end < end.")
        y = source @ np.array([.2126, .7152, .0722], dtype=np.float32)
        up = np.clip((y - a) / (b - a), 0, 1)
        down = np.clip((d - y) / (d - c), 0, 1)
        mask = np.minimum(up, down)
    else:
        raise ValueError(f"Unknown mask type: {kind}.")
    feather = number(spec.get("feather_px", 0), 0, max(width, height), "feather_px")
    if feather:
        # Feather the selection only: the artwork is never blurred.
        img = Image.fromarray(np.rint(mask * 255).astype(np.uint8)).filter(ImageFilter.GaussianBlur(feather))
        mask = np.asarray(img, dtype=np.float32) / 255
    if not isinstance(spec.get("invert", False), bool):
        raise ValueError("invert must be true or false.")
    return 1 - mask if spec.get("invert", False) else mask


def operation(rgb, layer):
    kind = layer.get("operation")
    fields = {"curve": ("points",), "exposure": ("ev",), "saturation": ("factor",), "color_balance": ("offset_rgb",)}
    if kind not in fields:
        raise ValueError(f"Unknown operation: {kind}.")
    keys(layer, ("name", "purpose", "operation", "opacity", "masks") + fields[kind], f"{kind} layer")
    y = rgb @ np.array([.2126, .7152, .0722], dtype=np.float32)
    if kind == "curve":
        points = layer.get("points", [])
        if len(points) < 2 or any(len(p) != 2 for p in points):
            raise ValueError("A curve requires at least two [input,output] points.")
        pts = np.array([[number(v, 0, 1, "curve point") for v in p] for p in points], dtype=np.float32)
        if pts[0, 0] != 0 or pts[-1, 0] != 1 or np.any(np.diff(pts[:, 0]) <= 0) or np.any(np.diff(pts[:, 1]) < 0):
            raise ValueError("Curve input must span 0..1 and increase strictly; output must be monotonic.")
        new_y = np.interp(y, pts[:, 0], pts[:, 1])
    elif kind == "exposure":
        new_y = np.clip(y * (2 ** number(layer.get("ev"), -3, 3, "ev")), 0, 1)
    elif kind == "saturation":
        factor = number(layer.get("factor"), 0, 2, "factor")
        return np.clip(y[..., None] + (rgb - y[..., None]) * factor, 0, 1)
    elif kind == "color_balance":
        offsets = layer.get("offset_rgb", [])
        if len(offsets) != 3:
            raise ValueError("color_balance needs offset_rgb [R,G,B].")
        delta = np.array([number(v, -.2, .2, "color offset") for v in offsets], dtype=np.float32)
        return np.clip(rgb + delta, 0, 1)
    else:
        raise ValueError(f"Unknown operation: {kind}.")
    # Tonal layers preserve RGB channel differences until the original gamut's
    # headroom is exhausted. Cap the delta rather than clip individual channels.
    delta = np.clip(new_y - y, -rgb.min(axis=2), 1 - rgb.max(axis=2))
    return rgb + delta[..., None]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source", type=Path, required=True)
    parser.add_argument("--recipe", type=Path, required=True)
    parser.add_argument("--output-dir", type=Path, required=True)
    args = parser.parse_args()
    source, recipe, out = args.source.resolve(), args.recipe.resolve(), args.output_dir.resolve()
    if out.exists() or source.is_relative_to(out) or recipe.is_relative_to(out):
        raise ValueError("Use a new output directory separate from the inputs; nothing is overwritten.")
    plan = json.loads(recipe.read_text(encoding="utf-8"))
    keys(plan, ("version", "mode", "intent", "layers"), "recipe")
    if plan.get("version") != 1 or plan.get("mode") not in ("Normal", "Deep"):
        raise ValueError("Recipe needs version 1 and mode Normal or Deep.")
    if not isinstance(plan.get("layers"), list) or len(plan["layers"]) > 30:
        raise ValueError("layers must be a list with at most 30 adjustment layers.")
    image, alpha, icc, conversion = load_source(source)
    original = np.asarray(image, dtype=np.float32) / 255
    current = original.copy()
    prepared = []
    external_inputs = []
    for layer in plan["layers"]:
        keys(layer, ("name", "purpose", "operation", "points", "ev", "factor", "offset_rgb", "opacity", "masks"), "layer")
        opacity = number(layer.get("opacity", 1), 0, 1, "opacity")
        if not isinstance(layer.get("name"), str) or not layer["name"].strip():
            raise ValueError("Every layer needs a nonempty name.")
        operation(current, layer)  # Validate parameters before creating outputs.
        masks = layer.get("masks", [{"type": "all"}])
        if not isinstance(masks, list) or not masks:
            raise ValueError("masks must be a nonempty list; components are multiplied.")
        mask = np.ones(original.shape[:2], dtype=np.float32)
        for spec in masks:
            mask *= mask_for(spec, original, recipe.parent)
            if spec.get("type") == "file":
                path = (recipe.parent / spec["path"]).resolve()
                external_inputs.append({"path": str(path), "sha256": sha(path)})
        if alpha is not None:
            mask *= np.asarray(alpha) > 0
        prepared.append((layer, mask, opacity))
    out.mkdir(parents=True)

    def save(rgb, path):
        img = Image.fromarray(np.rint(np.clip(rgb, 0, 1) * 255).astype(np.uint8))
        if alpha is not None:
            img.putalpha(alpha)
        img.save(path, icc_profile=icc)

    save(original, out / "working-source.png")
    records = []
    for index, (layer, mask, opacity) in enumerate(prepared, 1):
        target = operation(current, layer)
        next_rgb = np.clip(current + (target - current) * (mask * opacity)[..., None], 0, 1).astype(np.float32)
        prefix = f"{index:02d}"
        Image.fromarray(np.rint(mask * 255).astype(np.uint8)).save(out / f"{prefix}-mask.png")
        save(next_rgb, out / f"{prefix}-step.png")
        records.append({"index": index, "layer": layer, "mask_file": f"{prefix}-mask.png", "step_file": f"{prefix}-step.png",
                        "effective_mask_mean": float((mask * opacity).mean()), "max_channel_change": float(np.abs(next_rgb - current).max())})
        current = next_rgb
    save(current, out / "result.png")
    (out / "recipe.json").write_text(json.dumps(plan, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    working = np.rint(original * 255).astype(np.uint8)
    delivered = np.rint(current * 255).astype(np.uint8)
    report = {"route": "deterministic-adjustments", "source": str(source), "source_sha256": sha(source),
              "helper_sha256": sha(Path(__file__).resolve()),
              "recipe_sha256": sha(recipe), "result_sha256": sha(out / "result.png"), "mode": plan["mode"],
              "dimensions": list(image.size), "color_management": conversion, "output_profile": "sRGB",
              "external_mask_inputs": external_inputs,
              "source_geometry_resampled": False, "alpha_preserved": alpha is not None,
              "image_blur_applied": False, "generative_model_used": False, "layers": records,
              "changed_pixel_fraction": float(np.any(working != delivered, axis=2).mean()),
              "dependencies": {"numpy": np.__version__, "pillow": pillow_version, "python": sys.version.split()[0]},
              "visual_review": "unassessed", "note": "PNG steps and masks plus a recipe; not a layered PSD or bit-identical Photoshop Curves."}
    (out / "report.json").write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"result": str(out / "result.png"), "report": str(out / "report.json"), "visual_review": "unassessed"}))


if __name__ == "__main__":
    try:
        main()
    except (ValueError, OSError, KeyError, TypeError) as error:
        print(f"Adjustment failed: {error}", file=sys.stderr)
        sys.exit(1)
