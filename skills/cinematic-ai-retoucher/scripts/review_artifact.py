#!/usr/bin/env python3
"""Create faithful review previews/native crops; never grade aesthetic success."""
import argparse
import hashlib
import json
import math
import re
import shutil
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path


def run(args):
    return subprocess.run(args, check=True, capture_output=True, text=True).stdout


def probe(path, ffprobe):
    result = json.loads(run([ffprobe, "-v", "error", "-select_streams", "v:0",
                            "-show_streams", "-of", "json", str(path)]))
    streams = result.get("streams", [])
    if not streams:
        raise ValueError(f"No readable image stream: {path}")
    s = streams[0]
    if s.get("nb_frames", "1") not in ("1", "N/A"):
        raise ValueError("This helper is for still images, not a video review.")
    if s["width"] < 2 or s["height"] < 2:
        raise ValueError("Image dimensions must be at least 2x2.")
    digest = hashlib.sha256()
    with path.open("rb") as f:
        for block in iter(lambda: f.read(1024 * 1024), b""):
            digest.update(block)
    return {"path": str(path), "sha256": digest.hexdigest(),
            **{k: s.get(k, "unknown") for k in
               ("width", "height", "codec_name", "pix_fmt", "color_space",
                "color_transfer", "color_primaries")}}


def parse_roi(value):
    name, sep, coordinates = value.partition("=")
    if not sep or not re.fullmatch(r"[A-Za-z0-9_-]+", name):
        raise argparse.ArgumentTypeError("ROI must be name=x,y,width,height; simple name only.")
    try:
        x, y, w, h = map(float, coordinates.split(","))
    except ValueError as e:
        raise argparse.ArgumentTypeError("ROI needs four fractional coordinates.") from e
    if not all(math.isfinite(n) for n in (x, y, w, h)) or not (
            0 <= x < 1 and 0 <= y < 1 and 0 < w <= 1 and 0 < h <= 1
            and x + w <= 1 and y + h <= 1):
        raise argparse.ArgumentTypeError("ROI must fit inside the image in fractions 0..1.")
    return name, (x, y, w, h)


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--source", type=Path, required=True)
    ap.add_argument("--candidate", type=Path, required=True)
    ap.add_argument("--output-dir", type=Path, required=True)
    ap.add_argument("--preview-width", type=int, default=1200, help="Maximum width per pane.")
    ap.add_argument("--roi", type=parse_roi, action="append", default=[])
    ap.add_argument("--run-card", type=Path, help="Optional actual prompt/tool/lineage JSON.")
    args = ap.parse_args()
    ffmpeg, ffprobe = shutil.which("ffmpeg"), shutil.which("ffprobe")
    if not ffmpeg or not ffprobe:
        raise ValueError("Requires FFmpeg and ffprobe on PATH; no automatic installation.")
    if args.preview_width < 16:
        raise ValueError("Preview width must be at least 16.")
    source, candidate = args.source.resolve(), args.candidate.resolve()
    for path in (source, candidate):
        if not path.is_file() or path.suffix.lower() not in (".png", ".jpg", ".jpeg", ".webp", ".bmp", ".tif", ".tiff"):
            raise ValueError(f"Requires an existing supported still-image file: {path}")
    if source == candidate:
        raise ValueError("Source and candidate must be distinct files.")
    if len({r[0] for r in args.roi}) != len(args.roi):
        raise ValueError("ROI names must be unique.")
    sm, cm = probe(source, ffprobe), probe(candidate, ffprobe)
    sar, car = sm["width"] / sm["height"], cm["width"] / cm["height"]
    aspect_difference = abs(car / sar - 1)
    if aspect_difference > .01:
        raise ValueError(f"Aspect ratio differs by {aspect_difference:.2%}; review framing before making a wipe.")
    card = json.loads(args.run_card.read_text()) if args.run_card else None
    out = args.output_dir.resolve()
    if out.exists():
        raise ValueError("Output directory already exists. Choose a new directory; existing reviews are preserved.")
    if source.is_relative_to(out) or candidate.is_relative_to(out):
        raise ValueError("Output must not contain an input file.")
    # Comparison only: fit both originals into one canvas; never stretch or upscale.
    width = min(args.preview_width, sm["width"], cm["width"])
    height = min(round(width / sar), round(width / car), sm["height"], cm["height"])
    out.mkdir(parents=True)
    fit = (f"scale={width}:{height}:force_original_aspect_ratio=decrease:flags=lanczos,"
           f"pad={width}:{height}:(ow-iw)/2:(oh-ih)/2,setsar=1")
    outputs = []
    base = [ffmpeg, "-hide_banner", "-loglevel", "error", "-nostdin", "-n"]
    for label, path in (("source", source), ("candidate", candidate)):
        target = out / f"{label}-preview.png"
        run(base + ["-i", str(path), "-vf", fit, "-frames:v", "1", str(target)])
        outputs.append(target)
    inputs = ["-i", str(outputs[0]), "-i", str(outputs[1])]
    side = out / "side-by-side.png"
    run(base + inputs + ["-filter_complex", "[0:v][1:v]hstack=inputs=2[v]",
                         "-map", "[v]", "-frames:v", "1", str(side)])
    mid = width // 2
    wipe = out / "center-wipe.png"
    filt = (f"[0:v]crop={mid}:{height}:0:0[l];"
            f"[1:v]crop={width-mid}:{height}:{mid}:0[r];"
            f"[l][r]hstack=inputs=2,drawbox=x={mid-1}:y=0:w=2:h=ih:color=white:t=fill[v]")
    run(base + inputs + ["-filter_complex", filt, "-map", "[v]", "-frames:v", "1", str(wipe)])
    outputs.extend([side, wipe])
    regions = []
    for name, (x, y, w, h) in args.roi:
        record = {"name": name, "normalized_box": [x, y, w, h], "native_crops": []}
        for label, meta, path in (("source", sm, source), ("candidate", cm, candidate)):
            ix, iy = int(x * meta["width"]), int(y * meta["height"])
            iw = max(1, min(int(w * meta["width"]), meta["width"] - ix))
            ih = max(1, min(int(h * meta["height"]), meta["height"] - iy))
            target = out / f"{name}-{label}-native.png"
            run(base + ["-i", str(path), "-vf", f"crop={iw}:{ih}:{ix}:{iy}:exact=1",
                        "-frames:v", "1", str(target)])
            record["native_crops"].append({"role": label, "path": str(target),
                                           "box_pixels": [ix, iy, iw, ih], "resized": False})
            outputs.append(target)
        regions.append(record)
    report = {"created_utc": datetime.now(timezone.utc).isoformat(), "source": sm,
              "candidate": cm, "aspect_difference_fraction": aspect_difference,
              "preview_canvas": {"width": width, "height": height, "order": "source-left/candidate-right",
                                 "treatment": "fit/downscale only; minimal padding if aspect rounding differs"},
              "regions": regions, "outputs": [str(p) for p in outputs], "run_card": card,
              "tools": {"ffmpeg": run([ffmpeg, "-version"]).splitlines()[0],
                        "ffprobe": run([ffprobe, "-version"]).splitlines()[0]},
              "visual_review": "unassessed", "warning": "Metadata and comparisons do not establish fidelity or aesthetic success."}
    (out / "review.json").write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n")
    print(json.dumps({"review": str(out / "review.json"), "preview_canvas": report["preview_canvas"],
                      "visual_review": "unassessed"}, ensure_ascii=False))


if __name__ == "__main__":
    try:
        main()
    except (ValueError, OSError, subprocess.CalledProcessError) as error:
        detail = getattr(error, "stderr", "") or str(error)
        print(f"Review failed: {detail.strip()}", file=sys.stderr)
        sys.exit(1)
