# Traditional adjustment workflow — v4

## Native Photoshop or equivalent editor

Lock the source base, retain its profile/bit depth and add only layers this image needs:

| Layer | Operation | Selection and check |
|---|---|---|
| Foundation | Curves, usually Luminosity blend for tonal work | Shape midtones/shadows; retain highlight gradients and readable blacks |
| Key light | Brighter Curves/Exposure | Paint a black mask white on the actual lit side; protect facial lines and ornament cores |
| Shadow shaping | Darker Curves | Backlit surfaces/contacts; feather the mask, not the artwork |
| Local environment color, optional | Color Balance or channel curves, low opacity | Existing light spill only; inspect skin/neutral chroma |
| Light wrap, optional | Source-bright-pixel duplicate, separate Screen/Soft Light layer | Restrict glow to existing highlights; blur only that duplicate and retain a sharp base |
| Finishing | Layer opacity and targeted tone adjustment | No automatic vividness, whole-frame haze or sharpening halo |

Follow surface boundaries rather than shining one radial spotlight across every material. Prefer manual masks for precise drawn boundaries. Soft Light painted dodge/burn is an optional alternative; 50% gray is a native layer choice, not a generative prompt. Deep intensifies selected light/shadow differences; both modes preserve content and source chroma. Opacity values are per-image choices, not universal research-backed percentages.

Save a layered PSD/TIFF only when the real editor creates one. A connector may return a flattened image: retain its actual settings and masks and label it flattened. Primary references: Adobe [adjustment layers](https://helpx.adobe.com/au/photoshop/desktop/create-manage-layers/color-adjustment-fill-layers/work-with-adjustment-and-fill-layers.html) and [masked Curves for lightening/darkening](https://www.adobe.com/learn/photoshop/web/lighten-darken-photos-with-curves). These explain mechanisms, not a universal style recipe.

## Local deterministic helper

Requires **Python 3.9+, NumPy and Pillow**. Comparisons via the existing review helper also require FFmpeg/ffprobe. Check available dependencies; keep optional installation in an isolated environment, not global Python. No standalone Windows executable is included.

```bash
python scripts/apply_adjustments.py --source original.png --recipe per-image.json --output-dir grade-new
```

Use a new output directory. Outputs: `working-source.png`, `result.png`, `recipe.json`, `report.json`, numbered `*-mask.png` and `*-step.png`. This is a replayable PNG/JSON workflow, **not a PSD**. No model, resampling, rotation, warp, denoising, filling or artwork blur is used. Only masks can be feathered. Alpha is retained; fully transparent pixels are excluded from adjustment.

Input: single 8-bit RGB/RGBA images. Embedded ICC is converted by LittleCMS to sRGB; output is tagged. Untagged inputs are assumed sRGB and this assumption is recorded. EXIF orientation other than 1, 16-bit PNG/TIFF, palette/grayscale/CMYK and animation are rejected rather than silently converted. Keep HDR/16-bit masters in an appropriate native editor. ICC conversion can change decoded RGB, so compare the exported `working-source.png` with the result. The original file remains untouched.

### Recipe

Root: `version: 1`, `mode: "Normal" | "Deep"`, optional `intent`, and `layers` (0–30). Mode is a label, **not an automatic strength preset**: design operations for this image. Layers have `name`, optional `purpose`, `operation`, `opacity` (0–1), `masks`, and the operation's parameters:

| Operation | Parameter | Calculation |
|---|---|---|
| `curve` | Monotonic `points: [[0,0],[0.3,0.27],[0.7,0.74],[1,1]]` | Piecewise-linear gamma-encoded sRGB weighted-luma mapping |
| `exposure` | `ev` in −3..3 | Multiply weighted luma by `2**ev`; not calibrated RAW exposure |
| `saturation` | `factor` in 0..2; source-strength default 1 | Scale channel differences around weighted luma, then clamp |
| `color_balance` | `offset_rgb: [R,G,B]`, each −0.2..0.2 | Add gamma-encoded channel offsets, then clamp; not Photoshop's Color Balance algorithm |

Tonal layers add luma delta equally to RGB. Cap that delta by each pixel's available channel headroom to retain channel differences without separate channel clipping. This is an approximation, **not** Photoshop Luminosity blend, linear-light rendering or colorimetric luminance. Color-offset/saturation operations can still clip or shift hues. Float calculations precede 8-bit export. No automatic aesthetic score is produced.

Masks multiply, evaluate from the working original and optionally have boolean `invert` and pixel-radius `feather_px` (Gaussian selection feather). Supported:

- `{"type":"all"}`.
- `{"type":"ellipse","center":[x,y],"radius":[rx,ry]}`: normalized coordinates, smooth falloff to zero at ellipse boundary.
- `{"type":"polygon","points":[[x,y],...]}`: at least three normalized points.
- `{"type":"file","path":"selection.png"}`: same-size, single 8-bit grayscale mask, relative to input recipe.
- `{"type":"luminance","range":[start,full_start,full_end,end]}`: trapezoidal source-luma selection with strictly rising/falling edges.

Exported mask PNGs are rounded 8-bit inspection/handoff files. Replay uses the original recipe and original referenced files, not these rounded masks. Keep external mask files alongside the original recipe; copying JSON alone cannot package those files.

Small format example, **not a reusable position/strength preset**:

```json
{"version":1,"mode":"Normal","intent":"Shape this image's existing light",
 "layers":[{"name":"lit side","operation":"exposure","ev":0.3,"opacity":0.5,
 "masks":[{"type":"ellipse","center":[0.5,0.4],"radius":[0.2,0.3]}]}]}
```

Inspect full source/result and masks. Retain source/recipe/dependency hashes in `report.json`. Replayability proves execution, not that broad ellipses precisely follow every surface or that 3D shadows were reconstructed.
