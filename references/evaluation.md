# v2 evaluation and evidence

## Two mandatory gates

**Gate A — fidelity:** inspect full images at matched scale and face/hand/costume/background crops at 100%. Reject changed expressions, defining facial proportions, gestures, clothing motifs, object/subject count, crop, camera, layout or scene decoration. Minor raster variations are expected in generative output; describe them rather than claiming exact pixels. Geometry preservation is an instruction plus visual check, not a guaranteed tool capability.

**Gate B — visible uplift:** identify at least two observable improvements to existing illumination/material response. Deep must show a meaningful lit/shadow hierarchy or environmental light relationship at fit-to-screen size. A uniform exposure/saturation change, extra stars/fireworks, or newly invented objects does not count as success. Reject smear, clipped bright cores, illegible material boundaries, a gray veil and halo sharpening.

A candidate passes only when both gates pass. Use `passed-on-this-image`, `failed-fidelity`, `failed-uplift`, or `unassessed`; never trade one gate for the other. Record subjective observations and remaining uncertainty separately from objective file metadata.

## 2026-09-30 failure that prompted v2

Crowded Genshin ensemble: the earlier restrained pass was reported by the user as too similar. A maximum-strength retry added celestial bodies, rebuilt background fireworks/nebulae and altered details. It is a failed fidelity case even though the atmosphere was stronger. These are observations of this editor/setup, not proof that every v1 invocation fails.

## Validation status

v2 workflow/document changes are not a stability benchmark. Record fresh tests below before advertising reliability. Repeated varied-image passes are needed; retain failures in the count. User approval is separate from the assistant's visual assessment. Video stability is untested until contiguous frames are inspected for flicker/identity drift.


## v2 practical checks — 2026-09-30

Tool: built-in `image_gen` edit with the supplied original as reference. Its underlying model version, seed and denoise were not exposed; repeatability here is an observed result, not deterministic reproduction. No masks or conditioning buffers were supplied.

| Input / mode | Attempts | Visible uplift | Structure observation | Status |
|---|---:|---|---|---|
| Eight-character ensemble plus two distant figures / Deep | 2 independent calls, identical prompt | Strong gold illumination on existing parchment/characters, cooler blue shadows and existing music highlights | Same subject count, poses and overall layout; no new planets or redesigned cosmic setting. Fine costume markings/face lines show small redraw differences at inspection scale. | Qualified visual result; strict exact-detail fidelity remains unproven |
| Orange-gold graphic poster / Normal | 1 | Deeper existing skirt folds, clearer hair shading and metal highlights | Main figure/pose and surrounding props retained; fine line and texture variations remain. | Qualified visual result; no exact-pixel preservation claim |

This is **three executions on two images**, not three independent image cases or a broad stability study. No catastrophic scene redesign was observed in these three outputs. This limited comparison suggests v2 reduces the observed world-building failure; it does not establish a universal pass rate. Small line changes are retained as an issue rather than hidden by a total score. Neither source has received fresh user approval. Portrait fidelity and temporal video stability are untested in v2.

Exact prompts: `references/v2-test-prompts.json`. Gallery previews: `assets/v2-ensemble-center-wipe.png` and `assets/v2-poster-center-wipe.png`. Wipes aid presentation; acceptance used full comparisons plus upper/lower face crops.

## Historical v1 notes — not v2 validation

The following notes are historical observations from the previous workflow. Their positive wording and gallery images do not establish v2 reliability or a measured success rate.

## Controlled Normal versus Deep test — 2026-09-21

- **Source:** user-provided orange-gold anime poster with a central dancing character, circular graphic design, cards, masks and surrounding props.
- **Normal:** balanced texture-preserving material, highlight and structure recovery.
- **Deep:** same source and structure locks; stronger supported key/fill/rim hierarchy, gold atmosphere, burgundy shadow shaping, foreground separation and selective bloom.
- **Comparison:** `assets/comparison-01-orange-deep.jpg`, with source on the left and Deep on the right.
- **Execution:** image-edit workflow using the same source for both modes.

### Observed result

- Both modes retained the face, pose, costume silhouette, circular layout, surrounding props and orange-gold palette.
- Normal restored character, costume and prop readability while preserving the clean graphic-poster treatment.
- Deep created a stronger hero-frame impression through warmer rim light, darker edge framing, denser foreground layering and more decisive gold/burgundy separation.
- Face, hair locks, limbs, costume edges, circular composition and props remained readable at matched scale.
- Deep avoided broad denoising smear, a global fog blanket, crushed blacks and bloom-erased anatomy.

### Status

Both modes are `tested-on-this-setup`. Four additional pairs in `assets/comparison-02-cosmic.jpg` through `assets/comparison-05-hero-tree.jpg` test portability across different colors, compositions, materials and lighting problems. Results can still vary by model, source image and editor settings.

## Failure diagnosis

- **Looks like ordinary sharpening:** add named material differences, contact-shadow locations, bounce sources and transmission behavior.
- **Face becomes realistic or different:** lower strength/denoise; repeat anime facial-proportion lock; increase face protection or mask it.
- **Everything looks wet:** remove generic gloss language; specify roughness by material and limit rain beads to exposed surfaces.
- **Palette changes:** reduce tone strength; require source color preservation; use a detail-only or tone-preservation mode.
- **New patterns or accessories appear:** strengthen object/costume lock and remove open-ended words such as ornate, intricate, embellished or luxurious.
- **Video flickers:** use temporal guidance and optical flow or motion vectors; lower local structure and pass count before adding prompt detail.

## User-supplied actual DLSS 5 runtime reference — 2026-09-21

- **Reference:** `assets/reference-actual-dlss5-nr-portrait.jpg`, identified by the user as Visual Enhancer DLSS 5 Neural Rendering output.
- **Observed signature:** broad warm transmission through blonde hair, cyan environmental spill, lifted shadow color, smooth high-luminance diffusion, softened background contrast, and a coherent atmospheric veil across the portrait.
- **Useful behavior:** lighting wraps around the subject at low spatial frequency instead of looking like ordinary sharpening; the face, hair and ornaments share the same environment; bright regions retain colored gradients.
- **Observed weakness:** the veil lowers local contrast, merges some hair-lock and material boundaries, softens crown and crystal edges, and gives the frame a slightly washed, painted surface.
- **Calibration target:** retain the warm/cool light transport and atmospheric cohesion, then restore mid-frequency separation without clarity halos, black crush, aggressive sharpening, or added texture.
- **Evidence boundary:** the image is a user-labeled runtime result. A processing log and exact source/output frame pair were not supplied with this reference, so use it for visual-direction calibration rather than pixel-level runtime validation.
