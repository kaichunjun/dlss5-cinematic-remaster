# Complete requirements and method contract — v3

The brief was confirmed on 2026-09-30 to concern this Skill's complete requirements, rather than a competition rulebook. Latest explicit feedback overrides earlier sample preferences.

| Requirement | Implementation | How to assess |
|---|---|---|
| One reusable look across different images | Fresh source inspection, explicit input roles, scene-free lighting core | Next image carries no unrelated person/prop/palette |
| Normal and Deep, decide before execution | Internal mode decision, one-line explanation; infer from intent | Explicit mode respected; ambiguity questions only when necessary |
| Clearly visible effect, especially Deep | Strengthen named source-supported light/shadow relationships | Fit-to-screen full pair shows lighting uplift, not just exposure/chroma |
| Strong atmosphere and an impressive frame | Existing environmental bounce, localized glow, focal light hierarchy and readable occlusion | Light wraps coherently; subject remains readable |
| Color is currently too saturated | Source chroma default; protect neutral materials/skin; local spill | Check lit/unlit surfaces separately; reject a global vividness increase |
| Preserve characters and composition | Preservation map, include tiny subjects, inspect face/gaze/gesture/costume | Critical anatomy, expression, design/count/layout changes fail |
| Keep crisp detail, avoid smear | Local glow only; preserve medium/texture vocabulary | Inspect hair locks, ornaments, contour edges and hands at native size |
| Minor stylized shadow freedom is acceptable | Deep may accentuate existing shade/contact, provided the relationship stays coherent | No inexplicable dark patches, erased features or alternate light direction |
| Professional comparison presentation | Full side-by-side for assessment; source-left/result-right center wipe for display | Wipe is labeled and never the sole fidelity check |
| Stable execution | Actual controls/provenance, bounded retries, outcome gates, retained failures | Process is inspectable; model determinism is claimed only if evidenced |
| Complete reusable publication | Skill entry, recipes, tool adapters, review helper, audit, test records, bilingual README | Installed files match release; linked files exist; remote commit verified |

## What the method does

Original image → observable-content brief → mode and edit contract → real image editor → four-gate visual review → one-axis correction if needed → output + comparisons + provenance.

This is a **DLSS5-inspired cinematic image-relighting workflow**. The visual inspiration is broad light transport, coherent material response and atmosphere; actual DLSS runtime provenance cannot be inferred from appearance. A prompt Skill changes instructions, not model weights, and does not run NVIDIA neural rendering, ray tracing, intrinsic decomposition or a PBR renderer.

## Capability boundaries that affect the result

- A generative full-frame editor can redraw fine lines despite preservation instructions. Exact text/logo/costume replication needs an available deterministic/protected-region route or explicit qualification; avoid promising 100% preservation.
- When the editor hides model version/seed, retain the exact inputs and prompt but call reproduction approximate. Repeated images are trials, not independent source cases.
- A static remaster skill supports still images. Batch consistency needs representative samples; video needs temporal processing and contiguous-frame checks. It is not a Windows installer, game injection tool or always-on desktop filter.
- Missing source pixels are unknown, not recoverable ground truth. Enlarging an output or requesting “8K” does not establish newly recovered detail.
- A newly requested redesign, vivid palette, removal or new image can expand the brief. Name that change explicitly; the original faithful-remaster constraints are defaults, not prohibitions on authorized creative work.
