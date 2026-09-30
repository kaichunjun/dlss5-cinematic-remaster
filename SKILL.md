---
name: dlss5-cinematic-remaster
description: Relight anime, game and CG images with Normal or Deep cinematic enhancement, preserving the supplied artwork and checking visible uplift separately from identity and layout drift. Use for DLSS5-inspired image edits; actual runtime configuration is a separate optional reference.
---

# DLSS5-inspired cinematic remaster — v2

Create **clearly visible lighting and material-response changes on the existing artwork**. The reusable look is dimensional illumination, environmental light wrap, readable shadows, selective glow and distinct materials without smear. Do not impose a fixed palette or recreate the scene. This is a prompt-based image-edit workflow, not the DLSS runtime.

## Decide the mode first

Ask yourself **Normal or Deep?** State the choice briefly. Respect an explicit user selection. Infer Deep for “明显”, “深度”, “帅”, “氛围强”, or “拉满”; infer Normal for faithful cleanup or restrained edits. Ask the user only when the choice cannot be inferred and materially changes the result. Complex compositions require tighter structural protection in either mode, rather than an automatic downgrade of the user's requested intensity.

- **Normal:** clearly improved material separation, local shading and highlight rolloff; restrained atmosphere.
- **Deep:** conspicuous light/shadow hierarchy and environmental illumination; stronger source-supported rim light, bounce, contact shadows and spatial separation. It must look stronger at fit-to-screen size while preserving character and object design.

Deep raises **lighting amplitude**, not creative freedom. “拉满” never silently permits a new setting, new celestial bodies, denser particle fields, replacement fireworks, costume changes or face redesign.

## Execute with two independent acceptance gates

1. Inspect the original source with the image tool. Record visible subject count (including small background subjects), identity features, pose, crop, object layout, text/overlays, palette, actual light evidence and existing materials. Keep overlay handling unchanged unless the user requests a change. Infer appearance only, not hidden depth, normals or missing textures.
2. Read [prompt-recipes.md](references/prompt-recipes.md). Use its **relighting-only core** and one mode suffix. Fill the scene fields using only this image. Apply no example-scene nouns from a previous job. Supply this job's original source as the edit target; style-reference images are optional and never structural targets.
3. Use the built-in image editor when available. Do not claim that prompt instructions are masks, geometry locks or actual PBR reconstruction. If the tool has no denoise/mask/seed control, do not invent those settings or switch tools silently. Structural conditioning may improve control on an explicitly selected pipeline but must be checked on output.
4. Produce one candidate. Save the exact prompt, available tool settings, source/output paths and tool identity. Compare complete source/output views at the same display scale, then inspect every face, hands, costume symbols and small subjects at 100%. A center wipe alone hides cross-half changes and is insufficient for acceptance.
5. Apply the structure and uplift gates from [evaluation.md](references/evaluation.md). Structure failures cannot be offset by good lighting. Weak uplift cannot pass solely because structure is retained. Avoid precise numeric scores without supporting observations.
6. **At most two corrections after the first candidate.** Always return to the original source. For drift, narrow the editable area/operation or reduce its amplitude; for weak uplift, raise only one source-supported lighting relationship (e.g. lit side versus shadow side), keeping the same palette and objects. For smear, reduce diffusion/reconstruction demand; added sharpening is not a repair. Never chain generated frames or compensate with a longer list of cinematic adjectives.
7. Deliver a passing candidate with a matched comparison and a brief description of the actual changes. If no candidate passes both gates, label the best preview with its remaining issue and report that this attempt failed; preserve the source. Do not quietly deliver a redesigned or nearly identical frame as success.

## Reliability and references

Bundled older comparisons are visual-direction references, not a success-rate study. The user-labeled runtime portrait is a lighting reference with unverified processing provenance. See [evaluation.md](references/evaluation.md) for current test evidence.

Call the workflow **v2 with acceptance gates**. Call a result `passed-on-this-image` only after inspection. Calling a model/mode stable requires repeated passes on varied images, including portraits and crowded compositions; report sample counts, failures, model and date. Neither a document validator nor a single attractive image establishes stability. Video requires temporal validation beyond single-frame results.

For an explicit request about a NeuralScreen/Visual Enhancer runtime, read [runtime-controls.md](references/runtime-controls.md); do not conflate community labels or empirical knobs with verified DLSS behavior.
