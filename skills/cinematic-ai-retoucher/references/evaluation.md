# Visual assessment and artifact review — v4

## Four independent gates

| Gate | Pass evidence | Fail / concern examples |
|---|---|---|
| A — content and identity | Same visible subjects/counts, face design/gaze/expression, gestures/contacts, costume motifs, objects, crop/layout | Missing tiny figure, changed grip or expression, new decoration, redraw of a defining symbol |
| B — visible lighting uplift | At least two named changes in existing lighting/material response; Deep clearly stronger at fit-to-screen size | Nearly identical result, uniform exposure change, global vividness, new scenery mistaken for enhancement |
| C — color restraint | Source-faithful skin/whites/neutrals/unlit background; colored spill local and source-supported | Orange neutral material, neon blue sky, broad complementary wash, gray blanket used to hide oversaturation |
| D — clarity and coherence | Readable hair locks/ornaments/edges, clean gradient highlights, plausible shared light direction | Painted smear, eye/hand blur, clipped cores, black crush, wet-looking matte surfaces, sharpening halos |

For the default adjustment route also verify source/export geometry, absence of synthesis/resampling, intact alpha and replay settings. These are computational checks, separate from whether new shading hides lines or expressions. The local helper preserves RGB geometry but ICC conversion and tonal/color layers change pixel values; compare its working-source baseline.

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

The report records sizes, hashes, output files, preview scaling, tool versions and optional provided run-card data. Its `visual_review` is deliberately `unassessed`; inspection notes go in a separate assessment record. A successful script/Skill validator proves formatting/execution, not successful remastering. See [validation.md](validation.md) for this route’s historical test evidence and limitations.

