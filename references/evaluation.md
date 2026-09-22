# Evaluation and test record

## Visual QA rubric

Score each core dimension from 0 to 2. A reusable result needs at least 9/12 and no zero in structure preservation.

| Dimension | 0 | 1 | 2 |
|---|---|---|---|
| Identity and face | replaced or distorted | small drift | clearly same identity and proportions |
| Geometry and composition | pose/layout/object changes | minor movement | locked |
| Material separation | universal gloss or flatness | partial differentiation | distinct plausible skin/hair/cloth/leather/metal response |
| Light transport | incoherent or merely brighter | some depth improvement | coherent contact shadows, bounce, transmission and reflections |
| Art-direction fidelity | different genre/person | recognizable with drift | same anime/game identity |
| Artifact control | severe wax, halos or texture hallucination | minor artifacts | clean and restrained |

For Deep, also score these dimensions from 0 to 2. A passing Deep result needs at least 4/6 here and must pass the core rubric.

| Deep dimension | 0 | 1 | 2 |
|---|---|---|---|
| Atmospheric depth | flat or global fog | some layering | clear foreground, subject and background atmosphere |
| Hero lighting and color | random or uniformly boosted | stronger but unfocused | coherent key/fill/rim rhythm and controlled color separation |
| Readability under intensity | smeared or bloom-erased | minor loss | face, hair, hands, costume and edges stay readable |

## Visual comparison gallery

The public gallery presents the user-provided game frames as matched center-wipe comparisons. They define reusable qualities rather than a single preset scene:

- cool material depth without waxy smoothing;
- controlled bright cores and readable highlight gradients;
- atmospheric glow with protected faces, hands, clothing and foreground edges;
- strong hero lighting, silhouette separation and environmental scale.

Every new input still requires a fresh inventory of its visible subjects, materials, palette, light sources, composition and protected details.

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
