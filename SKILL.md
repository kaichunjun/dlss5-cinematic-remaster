---
name: dlss5-cinematic-remaster
description: Relight existing anime, game, CG and photographic images with Normal or Deep cinematic enhancement. Use for DLSS5-inspired image remastering with visible atmosphere, source-faithful color, protected identity/layout and inspected comparisons; this is an image-edit workflow, not a DLSS runtime.
---

# Cinematic relighting — v3

Create visibly stronger illumination, readable form shadows, environmental light wrap and differentiated existing materials on the **same image**. The reusable style is light coherence and dimensionality, not a fixed palette, scene, character or photorealistic makeover. Deep increases lighting amplitude, while retaining Normal's content protections. Prompts guide an editor; they do not lock pixels or reconstruct render buffers.

## 1. Choose the mode first

Ask yourself **Normal or Deep?** Follow an explicit selection; otherwise infer Deep for “明显／深度／帅／氛围强／拉满”, Normal for restrained enhancement. State the choice in one sentence. Ask only when a missing preference materially changes the task. Crowded images call for tighter preservation, not automatically weaker enhancement.

| Mode | Visible target | Color/content rule |
|---|---|---|
| Normal | Clear, restrained improvement to form shading, material separation and highlight rolloff | Preserve source palette intensity, identity and layout |
| Deep | Obvious light/shadow hierarchy, environmental bounce, deliberate existing highlights and spatial separation | Same protections; extra saturation, new effects and scene redesign require an explicit request |

## 2. Inspect and freeze the edit brief

Inspect each current input. Label every image **edit target**, **style/light reference**, or **supporting input**. The original target controls content and color; a reference lends only explicitly chosen visual properties. Do not carry subjects, settings, colors or example-specific restrictions into another job.

Record a compact preservation map: visible subjects (including distant figures), faces/gaze/expression, pose/contacts, silhouettes, costume motifs, props, crop/layout, text/overlays and original medium. Mark invisible/unclear details unknown rather than inventing them. Identify the actual bright regions, light direction, neutral surfaces and two or three existing material differences. Read [requirements.md](references/requirements.md) only for a scope audit.

Define the edit as **lighting/shading/existing material response**. Default to the source's chroma; increase impact through luminance, contact shadows and coherent highlights. Protect skin, whites and neutrals. Colored bounce stays local to surfaces reached by existing lights. Deep does not authorize orange parchment, electric-blue backgrounds, added planets, extra particles, new fog or costume redesign. Never repair saturation by adding a gray veil or flattening the requested light hierarchy.

## 3. Match the real tool and medium

Read [prompt-recipes.md](references/prompt-recipes.md); fill only current-image observations and append one mode. Adapt to illustration, CG or photography without changing medium. For strict pixel/geometry preservation, say whether the selected tool actually supports protected masks or reversible adjustments. A prompt-based full-frame edit remains approximate.

Use the available built-in image editor by default, respecting its imagegen instructions and preserving transparency. Read [tool-adapters.md](references/tool-adapters.md) for an explicitly selected external/controlled pipeline, batch, video or new-image request. Check live schemas before setting knobs; unavailable seed, denoise, mask or conditioning controls stay `not exposed`. Do not switch services or install models merely to conceal a limitation.

## 4. Generate, inspect, correct

Generate one candidate non-destructively. Save the exact prompt, ordered input roles, available settings, tool/model identity (unknown if unexposed), returned file and lineage to the original.

Read [evaluation.md](references/evaluation.md). Inspect full images at matched display scale **and** native-size detail views. Apply four independent gates: **content/identity**, **visible lighting uplift**, **source-faithful color**, **clarity/coherence**. Inspect every visible face, hand/held prop, emblem and small figure; identify limitations at the delivered resolution. A flattering face, stronger color or center wipe alone cannot pass the result.

Allow at most two targeted corrections after the initial candidate. Return to the original; change one diagnosed axis. Weak effect: strengthen one existing lit/shadow relationship. Drift: narrow the operation or use a supported protected-region workflow. Excess color: name the overcolored regions while preserving shading. Smear: reduce reconstruction demand; sharpening does not recover lost linework. Do not chain generated frames, keep appending adjectives or retry indefinitely.

## 5. Deliver verifiable results

Deliver the actual output, source-left/result-right complete comparison and center wipe when useful/requested. Use [scripts/review_artifact.py](scripts/review_artifact.py) for repeatable comparison files and metadata if Python + FFmpeg/ffprobe are available; it formats evidence, **never decides aesthetic success**. See [evaluation.md](references/evaluation.md) for its invocation. Preserve the master; label resized comparisons as previews.

Report `passed-on-this-image`, `qualified-preview`, `failed` or `unassessed`, with concrete changes and remaining issues. A critical content failure cannot win; if no candidate meets the brief, report failure with a labeled preview rather than claiming completion. User approval is distinct from assistant assessment. File/schema validation is distinct from visual quality; single frames do not prove temporal stability.

## Optional references

- [Skill audit](references/skill-audit.md): dated review scope, adopted/rejected patterns and primary sources; read for methodology/research, not every edit.
- [Validation record](references/validation-v3.md): actual sample observations, failures and unknowns; read before making reliability claims.
- [Runtime notes](references/runtime-controls.md): separate historical community-app notes, only for an explicit runtime request. This package contains no DLSS binary/model and does not process a desktop or game in real time.
