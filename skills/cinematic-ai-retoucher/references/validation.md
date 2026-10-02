# Pure-adjustment evidence inherited from v4 — 2026-09-30

## Actual execution

One archived rain-night portrait source, 1672×941, executed with two per-image recipes (Normal and Deep). Deep was independently replayed. NumPy 2.3.5, Pillow 12.3.0, Python 3.12.14; exact recorded versions/hashes in [v4-test-results.json](v4-test-results.json). Check that file rather than assuming the prose version matches another host.

No generative service, model, artwork blur or geometric resampling was used. Existing source lines/motifs were adjusted through tonal/color calculations. The source image's earlier origin is separate from this test: this execution edits an archived image traditionally, and does not claim that source itself was hand-drawn.

| Variant | Changes inspected | Assistant outcome |
|---|---|---|
| Normal | Restrained face illumination, deeper backlit sleeve and clearer existing material values | `passed-on-this-image`; user approval pending |
| Deep | More visible face/front illumination and light/shadow separation, original alley and motifs retained | `passed-on-this-image`; user approval pending |

Review used full matched-size pairs and native face/sleeve detail crops. Face expression, hair-lock borders, emblems, hand and sword geometry remained intact; no smear was introduced. Deep's light design is a broad tonal interpretation, with soft selection overlap, not a precise material-boundary mask or physically reconstructed 3D transport. Colors remain source-related; no saturation layer was used. The slight local warm offset is documented.

## Computational checks

14 checks passed: decoded RGBA no-op; zero-mask no-op; alpha retention; transparent hidden-RGB retention; source dimensions; repeat export bytes; original file hash; invalid curve rejection; misrouted parameter rejection; unsupported 16-bit rejection; existing-output protection; ICC parse; real portrait repeat pixels; real portrait repeat PNG bytes.

An initial real replay had identical pixels but different generated-ICC timestamps, so file hashes differed. The helper now canonicalizes only generated sRGB profile date/optional ID metadata. Checks were rerun on the final helper, with matching pixel arrays and PNG hashes. This fixes metadata reproducibility, not visual quality.

## Limits

This is **one source case, two variants and one replay**, not a stability percentage. Photos, crowded scenes, 16-bit/HDR editing, native Photoshop layer exports and continuous video have no fresh v4 visual test. The local helper exports PNGs, masks and JSON, not PSDs. Reproduction is for identical source, recipe, external mask files and dependencies. Traditional adjustment preserves geometry while clipping/poor masks could still obscure content; inspect every new result.

Generative examples belong to the separate AI-dispatch Skill and cannot establish this route’s quality. [Recipes](v4-portrait-deep.json) are specific to this source; do not copy coordinates to unrelated pictures.

## Split release — 2026-10-01

The adjustment engine, source and recipes are unchanged. The packaged example was replayed after splitting; that check verifies packaging and reproducibility, not a fresh visual benchmark. This Skill never invokes generative reconstruction; if reconstruction is wanted, the user selects the independent AI-dispatch Skill.
