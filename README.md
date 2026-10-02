# Two cinematic-light Skills: AI dispatch and AI retoucher

[简体中文](README.zh-CN.md)

Two independently installable Skills in one GitHub repository. Both analyze the current source and choose **Normal or Deep**; execution routes stay separate.

| | [AI dispatch](skills/cinematic-ai-remaster) | [AI retoucher](skills/cinematic-ai-retoucher) |
|---|---|---|
| Invocation | `cinematic-ai-remaster` | `cinematic-ai-retoucher` |
| Method | Orchestrate a generative image editor to redraw light/material response | Traditional curves, local masks, dodge/burn and restrained color |
| Best fit | More flexible reconstruction, accepting generated variation | Preserve existing faces, lines, motifs and layout |
| Fidelity | Prompt goals plus inspection; details can drift | Existing-pixel adjustments; inspect obscured detail and clipping |
| Normal / Deep | Both, with source-content/color protections | Both; Deep remains adjustment-only |
| Evidence delivered | Image, exact prompt, exposed settings and assessment | Image, actual layers or masks/steps/replayable recipe |

DLSS5 is the legacy repository name and visual inspiration. Neither package contains NVIDIA/DLSS models, a runtime, or an always-on game/desktop filter.

## Separate downloads

- [AI-dispatch ZIP](https://github.com/kaichunjun/dlss5-cinematic-remaster/releases/download/v5.0.0/cinematic-ai-remaster-v5.0.0.zip): generative relighting.
- [AI-retoucher ZIP](https://github.com/kaichunjun/dlss5-cinematic-remaster/releases/download/v5.0.0/cinematic-ai-retoucher-v5.0.0.zip): traditional adjustments.
- [Release and SHA-256 checks](https://github.com/kaichunjun/dlss5-cinematic-remaster/releases/tag/v5.0.0).

## Install only the route you need

Download the selected Skill package or copy its complete folder from `skills/` into `~/.codex/skills/` (Windows: `%USERPROFILE%\.codex\skills\`). You may install either or both. Restart Codex if needed, attach a source, and invoke:

```text
$cinematic-ai-remaster Deep: generative cinematic relighting, retain source characters/layout and restrained color.
```

```text
$cinematic-ai-retoucher Deep, traditional adjustments only: use curves and local masks, retain original faces/lines/motifs.
```

The dispatch route needs an available host generation tool. The retoucher prefers a native image editor and bundles an optional Python/NumPy/Pillow fallback. Each folder documents real dependencies, capability limits and output formats; PNG steps/JSON are never claimed as PSD layers.

## Same subject, distinct routes

Each pair is **source left, result right**. These are historical examples: generative Normal versus adjustment Deep, with different modes/dates. They explain methods, not a controlled same-setting ranking. No new generation was performed for this split.

Generative dispatch, inherited v3 example:

![Generative dispatch pair](skills/cinematic-ai-remaster/assets/v3-portrait-side-by-side.png)

Traditional retoucher, inherited v4 example and package replay:

![Traditional retoucher pair](skills/cinematic-ai-retoucher/assets/v4-portrait-deep-side-by-side.png)

[Generative evidence](skills/cinematic-ai-remaster/references/validation.md) · [Adjustment evidence](skills/cinematic-ai-retoucher/references/validation.md)

## Compatibility and rights

The root `dlss5-cinematic-remaster` remains the legacy v4 entry with traditional adjustments as default. New installation uses the two separate names above. Historical files/evidence are retained; neither new route silently switches to the other when its result is weak.

Own text/scripts: [MIT License](LICENSE). Underlying sample/character rights: [NOTICE.md](NOTICE.md). Package/schema validation and aesthetic reliability are distinct; no universal image-quality guarantee is claimed.
