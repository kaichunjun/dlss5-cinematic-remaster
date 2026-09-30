# Visual assessment and artifact review — v3

## Four independent gates

| Gate | Pass evidence | Fail / concern examples |
|---|---|---|
| A — content and identity | Same visible subjects/counts, face design/gaze/expression, gestures/contacts, costume motifs, objects, crop/layout | Missing tiny figure, changed grip or expression, new decoration, redraw of a defining symbol |
| B — visible lighting uplift | At least two named changes in existing lighting/material response; Deep clearly stronger at fit-to-screen size | Nearly identical result, uniform exposure change, global vividness, new scenery mistaken for enhancement |
| C — color restraint | Source-faithful skin/whites/neutrals/unlit background; colored spill local and source-supported | Orange neutral material, neon blue sky, broad complementary wash, gray blanket used to hide oversaturation |
| D — clarity and coherence | Readable hair locks/ornaments/edges, clean gradient highlights, plausible shared light direction | Painted smear, eye/hand blur, clipped cores, black crush, wet-looking matte surfaces, sharpening halos |

First inspect full source and output at the same display scale. Then inspect every visible face, hands/props, motifs and tiny subjects in native-resolution crops. Do not claim a crop was inspected at 100% when it was upscaled or shown as a small thumbnail. Different output dimensions mean different detail capacity; state this limitation. Text and linework can drift even with perfect large-scale layout.

A center wipe is a presentation aid: it hides half of each image and cannot establish full-image fidelity. Use a full pair and complete source/output inspection. For multi-reference input, inspect each reference against its declared role; a prettier face is not proof of preserved identity.

## Outcomes

- `passed-on-this-image`: all four gates met at the delivered resolution; distinguish assistant assessment from user approval. This does not mean exact-pixel identity.
- `qualified-preview`: visible uplift and preserved broad layout, but noncritical detail/color concerns remain. Show the concerns; never call this fully approved.
- `failed`: a critical gate breaks or the requested uplift is absent after the bounded attempts. The best failed image may be shown only as a labeled failed preview.
- `unassessed`: output or necessary comparisons were not actually reviewed.

A gate can be unknown when the source is unclear. Do not convert unknown to pass or calculate precise identity percentages. Keep failed trials, user feedback and evaluation revisions. At most initial + two targeted corrections per job; always retain the original target. Stable-across-images claims need an explicitly described varied sample, repeats, failure counts and known model/settings. There is no universal minimum sample size or guaranteed success rate here.

## Repeatable evidence helper

Requires Python 3, FFmpeg and ffprobe available on PATH. It does not generate/edit the artwork, alter source masters, apply color correction, or decide aesthetics. It creates preview comparisons, optional native crops and a metadata record. Use a **new output directory** for each review.

```bash
python3 scripts/review_artifact.py \
  --source /absolute/path/original.png \
  --candidate /absolute/path/result.png \
  --output-dir /absolute/path/review-new \
  --run-card /absolute/path/run-card.json \
  --roi face=0.30,0.05,0.25,0.30
```

ROI coordinates are fractions of the whole frame: x,y,width,height. The named source and candidate crop files retain native pixels; the main comparison previews use downscaling/fit only, without stretching unequal aspect ratios. Aspect differences over the helper's 1% comparison tolerance stop generation of a misleading wipe; this is an engineering guard, not an aesthetic similarity threshold. No face detection or automatic fidelity score is claimed.

The report records sizes, hashes, output files, preview scaling, tool versions and optional provided run-card data. Its `visual_review` is deliberately `unassessed`; inspection notes go in a separate assessment record. A successful script/Skill validator proves formatting/execution, not successful remastering. See [validation-v3.md](validation-v3.md) for current tests.

## Historical evidence follows

Older wording below is retained as dated observation, not current acceptance or universal parameter advice. Use the v3 four gates for new work.

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

Both modes are `tested-on-this-setup`. Other retained v1 examples are historical visual references across different scenes; their exact prompt provenance and acceptance evidence are incomplete. One former cosmic comparison is absent from the current checkout. Results can still vary by model, source image and editor settings.

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

## User feedback — 2026-09-30 color correction

The user reported the first v2 ensemble as too saturated. Earlier direction consistency remains an observation, but these samples are not user-approved aesthetic targets. Default recipes now preserve source chroma in both modes and strengthen luminance/shading rather than saturation. v3 adds a fresh original-based corrected preview; see [validation-v3.md](validation-v3.md). It remains pending user assessment.
