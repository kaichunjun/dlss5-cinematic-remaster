---
name: cinematic-ai-remaster
description: Orchestrate available generative image tools to remaster existing illustrations, game images, CG or photos with Normal or Deep cinematic lighting. Use when the user selects AI-generated relighting or redraw; traditional adjustment-only requests belong to the separate retoucher Skill.
---

# AI dispatch — generative cinematic remaster

AI directs a real image-generation editor to reshape apparent light and material response. Explicitly invoking this Skill selects the generative route for the requested asset. Preservation is a goal; generated pixels can change lines, faces or motifs. Keep each result inspectable rather than promising exact fidelity. This Skill contains no DLSS runtime or NVIDIA model.

## 1. Choose Normal or Deep

Decide the intensity before editing: respect an explicit mode, infer Deep for obvious/impressive atmosphere and Normal for restrained improvement. State mode and **generative route** briefly. Both modes protect source content and source-strength color; Deep strengthens existing light/shadow relationships rather than adding scenery or saturation.

## 2. Inspect and write a source-specific brief

Inspect the original target and label any references separately. Record visible subjects/counts including distant figures, identity/expression, pose/contacts, costume motifs, props, crop, text and original medium. The original controls content and palette; lighting references lend only selected properties. Do not transfer example-specific characters, settings or coordinates.

Identify real bright regions/light direction and two or three existing material differences. Fill [prompt-recipes.md](references/prompt-recipes.md) with these observations and one mode suffix. Keep colors restrained, faces in the original design, and light wrap localized. No guessed invisible detail, world-building, extra objects, beautification, global haze or painted smear merely to make the effect obvious.

## 3. Dispatch to an available image tool

Use the available built-in image editor by default and follow its current instructions/schema. Inspect local source files before editing; pass the original as the edit target, identify references, and preserve alpha unless a change is requested. Record the prompt, input roles, tool/model identity, actual exposed settings and returned file. Hidden seed, denoise, masks or dimensions stay `not exposed`.

Honor a user-selected service/model when available; verify its real graph/schema before execution. Otherwise report the capability gap. Do not install models, invent parameters or change services merely to hide a failed result. Model choice, prompt and optional supported conditioning are orchestration decisions; the Skill itself is no generation engine.

## 4. Inspect and make bounded corrections

Use [evaluation.md](references/evaluation.md): independent content/identity, visible lighting uplift, source-faithful color and clarity/coherence gates. Inspect full matched-scale images plus native detail crops, including faces, hands, emblems and tiny figures. A nicer face or stronger color cannot compensate for a critical content failure.

Initial candidate plus at most two targeted corrections. Always return to the original, changing one diagnosed axis: weak light relationship, drift, excess color or smear. Retain failed trials. If strict source fidelity is needed, explain the risk and let the user choose the separate pure-adjustment route; do not silently swap methods or chain redraws.

## 5. Deliver and label honestly

Deliver the result, full source-left/result-right comparison and optional center wipe using [review_artifact.py](scripts/review_artifact.py). Keep masters; comparisons are previews. Record `passed-on-this-image`, `qualified-preview`, `failed` or `unassessed`; distinguish assistant review from user approval. Prompt reproduction with hidden model/seed is approximate. Historical evidence: [validation.md](references/validation.md).

This is a still-image workflow. Batches require individual inspection; video requires a real temporal pipeline and contiguous-motion review. No always-on desktop/game processing or automatic reconstruction of true 3D light transport is claimed.
