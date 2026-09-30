---
name: dlss5-cinematic-remaster
description: Shape cinematic light in existing illustrations, game images, CG and photos using tonal/color adjustments and local masks. Use Normal or Deep for source-preserving Photoshop-style grading; generative redraw is opt-in. This is a still-image editing workflow, not a DLSS runtime.
---

# Cinematic light through adjustments — v4

AI analyzes the image and executes the edit; **the default image treatment is traditional adjustment of existing pixels**, not generative reconstruction. Build apparent light, shadow hierarchy and material separation with curves, masked dodge/burn, selective color and layer opacity. Keep the original drawing, faces, motifs and layout. The legacy DLSS5 name describes visual inspiration; this package invokes no NVIDIA model.

## 1. Choose intensity and retain the adjustment route

First ask yourself **Normal or Deep?** Respect an explicit choice; infer Deep for “明显／深度／帅／氛围强／拉满”, Normal for restrained improvement. State the mode briefly; ask only for a preference that materially changes the task.

| Mode | Intended effect | Shared protection |
|---|---|---|
| Normal | Clear but restrained light hierarchy, form shading and material separation | Original geometry, linework, identity and source color intensity |
| Deep | Obvious focal light, shaped shadows, coherent local light wrap and spatial atmosphere | Same protections; stronger luminance contrast, not automatic saturation, blur or redraw |

**Deep is intensity, never permission to generate.** “重绘／remaster／DLSS风格” alone is not opt-in to synthesis in this Skill. Use a generative editor only when the user explicitly requests generative reconstruction, new content or a new image. Missing adjustment tools are a capability gap: report it or provide an executable adjustment plan; never silently substitute a model.

## 2. Inspect the source and design the layers

Inspect the current target; label optional references by role. Record visible subjects (including tiny figures), faces, gestures/contacts, costume motifs, props, crop and text. References lend selected lighting ideas only; they supply no replacement face, palette or setting.

Identify existing lights, lit/backlit sides, neutral surfaces and readable material differences. Plan a small stack: tonal foundation → masked light/shadow shaping → optional local color balance → restrained finishing. Each layer needs purpose, location, operation, opacity and protection. Derive masks from this image, never a prior example's coordinates.

Default to source chroma. Protect skin, whites, contours, ornaments and lettering from clipping or obscuring shade. Create impact through luminance contrast and local adaptation. Leave saturation boosts, global fog, whole-image blur, invented texture and artificial sharpness off. Optional source-derived glow stays on a separate masked layer with the sharp original underneath; inspect spill before retaining it.

## 3. Execute with a real adjustment tool

Read [adjustment-workflow.md](references/adjustment-workflow.md) for Photoshop guidance and the local helper. Prefer reversible adjustment layers/masks in an available editor. Otherwise use [apply_adjustments.py](scripts/apply_adjustments.py) with a per-image JSON recipe; it returns a result, masks, step PNGs and provenance. It performs deterministic tonal/color calculations without synthesis, resampling, inpainting or image blur; it writes no PSD and does not exactly reproduce Photoshop algorithms.

Retain the original, actual layer/recipe parameters and separate export. Check profile, bit depth and alpha; keep unsupported HDR/16-bit masters in a suitable native editor. Record only exposed controls. Read [tool-adapters.md](references/tool-adapters.md) for another tool, batch, video or explicit generative work. Optional detection/segmentation is analysis, not synthesis; manual masks support a fully traditional pipeline.

## 4. Inspect and correct the stack

Apply [evaluation.md](references/evaluation.md)'s four gates: **content/identity, visible lighting uplift, source-faithful color, clarity/coherence**. View full images at matched size plus native detail crops. Verify no geometric transform or synthesis; also check that shade has not hidden expressions, lines or tiny figures. An unchanged contour can still become unreadable.

Weak effect: strengthen one existing lit/shadow relationship. Overcolored: reduce the responsible color layer. Muddy: reduce broad shade/veil. Modify the stored stack and recompute from the original, rather than repeatedly grading a flattened export. Initial candidate plus at most two targeted corrections; retain failed/qualified previews without silently switching routes.

## 5. Deliver actual output and editable evidence

Deliver the result and its actual editable form: native layers if available, otherwise JSON + masks + step exports. Label the format honestly; PNG steps are not Photoshop adjustment layers. Use [review_artifact.py](scripts/review_artifact.py) for a full source-left/result-right pair and optional center wipe. These previews supplement master/detail inspection.

Report `passed-on-this-image`, `qualified-preview`, `failed` or `unassessed`. Deterministic computation means reproducibility for identical inputs, recipe and dependencies; it does not prove universal aesthetics or physically accurate 3D relighting. User approval differs from assistant assessment.

## Conditional references

- [Requirements](references/requirements.md): complete brief and current method contract.
- [v4 validation](references/validation-v4.md): executed adjustment examples and limitations.
- [Audit](references/skill-audit.md): source review and adopted practices.
- [Generative recipes](references/prompt-recipes.md): legacy optional route, **only after explicit opt-in**; [v3 tests](references/validation-v3.md) are historical generative evidence.
- [Runtime notes](references/runtime-controls.md): historical community-app notes for explicit runtime requests; this package provides no real-time desktop/game processing.
