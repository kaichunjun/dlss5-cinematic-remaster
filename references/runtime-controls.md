# Optional runtime control notes

Read only when the user specifically asks to configure NeuralScreen, Visual Enhancer or another runtime. This repository contains no DLSS binary/model and cannot establish which implementation a community build runs. Confirm the exact project/version and its own documentation before assigning meaning to controls.

Earlier repository values were empirical suggested starting points, not official, scientific or broadly validated recommendations. Retain them only as legacy notes, not a stable preset:

| Legacy mode | Style | Intensity | Local tone | Local structure | Skin structure | Passes |
|---|---|---:|---:|---:|---:|---:|
| Normal | Natural / Cinematic | 0.55–0.75 | 0.30–0.45 | 0.70–0.90 | -0.7 to -0.3 | 1 |
| Deep | Cinematic | 0.80–1.00 | 0.45–0.65 | 0.80–1.00 | -0.5 to 0.0 | 1 |

Control ranges/semantics vary across builds; verify accepted values and effect on a matched frame. Do not blindly copy these values. Prefer a single processing pass and sufficient network resolution when the documented implementation supports them. Assess faces, original texture and temporal flicker; do not promise that a high structure value removes smear.
