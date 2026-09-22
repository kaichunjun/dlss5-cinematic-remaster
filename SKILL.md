---
name: dlss5-cinematic-remaster
description: Structure-aware cinematic neural remastering for anime, game, CG, image, or video frames. Translate DLSS-5-inspired visual goals into controlled material, lighting, depth, highlight, and local-structure improvements while preserving identity, geometry, composition, palette, and art direction. Choose a restrained Normal mode or high-atmosphere Deep mode, enforce anti-smear and semantic-protection gates, map the intent to compatible rendering controls, and verify results with matched comparisons; do not present a prompt-based imitation as the actual DLSS 5 runtime.
---

# DLSS5-inspired cinematic remaster

Create the visual effect through **anchored reconstruction**, not a free redesign. The input frame controls identity, geometry, pose, composition, objects, palette, and light direction. The transformation may improve material response, light transport, contact shadows, micro-detail, and filmic grading.

Use the matched source/remaster pairs in `assets/comparison-*.jpg` as the persistent **quality-direction references** supplied by the user. Read them as transferable behaviors—cool material depth, controlled highlights, atmospheric glow, strong hero lighting, and preserved mid-frequency detail. Never copy their characters, objects, scenery, palette, or composition into a new image.

Use `assets/reference-actual-dlss5-nr-portrait.jpg` as the user-supplied **actual-runtime effect reference**. Its useful signature is low-frequency warm/cool light transport, lifted environmental illumination, colored highlight diffusion, and coherent atmosphere. Preserve that behavior while correcting its gray veil, softened material boundaries, and hair-detail smear. It is a visual-direction reference rather than proof for an arbitrary new render.

## Six-layer visual model

1. **Structure lock:** preserve face identity and proportions, pose, silhouette, costume geometry, camera, crop, perspective, scene layout, and object count.
2. **Material separation:** distinguish skin, hair, cloth, leather, metal, glass, foliage, and wet surfaces through plausible roughness, specular response, absorption, wear, and microtexture.
3. **Light transport:** add restrained skin subsurface scattering, hair or foliage transmission, contact shadows, ambient occlusion, bounced global illumination, and coherent reflections while preserving existing light sources.
4. **Local structure:** reveal weave, seams, scratches, rain beads, folds, and surface relief without inventing patterns or changing geometry.
5. **Filmic tone:** use controlled highlight rolloff, open shadow detail, coherent local contrast, and a restrained grade that preserves the source palette.
6. **Semantic protection:** protect the face, hands, costume symbols, text, and defining anime shape language from beautification, replacement, or realism drift.

## Decide the mode first

Before writing the edit prompt, answer internally: **Normal or Deep?** Decide from the user's words, the image's visual capacity, and the intended use. State the selected mode briefly before generating. Ask the user only when their intent is genuinely ambiguous and the mode would materially change the result.

- Choose **Normal** for faithful cleanup, identity-sensitive portraits, clean line art, UI/text-heavy images, already-complex compositions, weak sources, or when the user asks for natural, restrained, clean, or faithful results.
- Choose **Deep** when the user asks for strong atmosphere, cinematic impact, heroic presence, dramatic lighting, “很帅”, “拉满”, “大片感”, or when the frame has enough structural information to support stronger depth and lighting without losing readability.
- If evidence is mixed, use **Normal**. Deep is an intentional creative increase, not a default excuse to overprocess.

## Mode 1 — Normal

Apply **Balanced texture-preserving cinematic**:

- clearly improve material separation, dimensionality, contact shadows, bounced light, transmission, reflections, and highlight rolloff;
- protect mid-frequency structure such as hair locks, linework, fabric folds, surface relief, object edges, intentional brushwork, particles, and background contours;
- preserve the source palette and art direction rather than imposing a fixed cool, warm, fantasy, realistic, cosmic, wet, or metallic look;
- recover readable information from clipped highlights while retaining the brightness and color of real light sources and effects;
- keep natural fine variation without waxy smoothing, watercolor blending, or compensating oversharpening.

## Mode 2 — Deep

Apply **Deep atmospheric cinematic**. Preserve the same structure and art direction, then create a stronger hero-frame impression through relationships already supported by the image:

- establish a readable key, fill, rim, and environmental-light hierarchy without inventing visible light-source objects;
- deepen spatial layers with controlled volumetric atmosphere, local haze, bounced color, contact shadows, ambient occlusion, and foreground/background separation;
- strengthen light rhythm through localized glow, smooth highlight bloom, shadow shaping, and specular accents while keeping bright cores and edge gradients readable;
- increase tonal contrast and complementary color separation around the subject, not uniformly across the whole frame;
- make materials feel denser and more tactile while protecting the face, hair, hands, linework, fabric folds, edges, particles, and intentional brushwork;
- keep one clean reconstruction pass and high processing resolution. Reject broad denoising, global fog, texture melt, halo sharpening, black crush, and bloom that erases anatomy or costume detail.

Deep should feel more atmospheric, powerful, and visually cool than Normal. It must remain crisp enough to inspect at matched scale.

Read [references/prompt-recipes.md](references/prompt-recipes.md) for the fixed mother prompt, strength variants, model adapters, and parameter starting points. Read [references/evaluation.md](references/evaluation.md) when judging an output or recording an experiment.

## Workflow

1. Inspect each new input independently and list its observable structure locks, materials, light sources, palette, intentional stylization, and capture overlays. Do not reuse scene nouns or material assumptions from earlier images.
2. Build the prompt from the fixed visual logic plus the current image's actual content. Describe material and lighting behaviors, not vague quality words or a previous image's subject.
3. Make the Normal-versus-Deep decision before drafting the prompt. Use exactly one mode recipe for the first pass.
4. For image editing, repeat all invariants in the edit prompt. For Flux/SD/ComfyUI, combine low-denoise img2img with structural conditioning rather than relying on prose alone.
5. Generate or process one frame. Compare it side by side with the source at matched scale.
6. Score identity/geometry preservation separately from visual uplift. Tool success is not aesthetic success.
7. If structure drifts, reduce transformation strength before adding more negative words. If the result is merely sharper, strengthen material separation and light transport rather than generic detail adjectives.
8. If the result smears, preserve mid-frequency texture before adding sharpening: lower reconstruction or denoise strength, keep one pass, raise processing resolution, protect linework and material boundaries, and retain natural fine grain. Sharpen only after clean reconstruction.
9. Save the source, complete prompt, target model, settings, result path, observed differences, failure conditions, and user feedback. A result becomes user-approved only after explicit feedback.

## Actual DLSS 5 controls versus text prompts

DLSS 5 Neural Rendering does not accept natural-language prompts. When the target is Visual Enhancer, NeuralScreen, a game injector, or a related runtime, translate the intended look into style, intensity, local tone, local structure, skin structure, mask, and pass count. Treat the values in the recipes as starting points and verify with a comparison wipe.

When the target is a generative image model, state that the result is a DLSS-5-inspired imitation. Preserve the visual logic above, but expect lower determinism and greater identity drift than an engine-guided renderer.

## Stopping rules

- Reject a result that replaces the face, changes anatomy or pose, redesigns clothing, adds objects, moves the camera, or invents decorative textures.
- Reject universal gloss, waxy skin, crushed blacks, bloom wash, excessive pores, halos, or oversharpening.
- Reject denoising smear: merged hair clumps, melted fabric folds, softened armor seams, muddy runes, watercolor-like background edges, or texture that changes between adjacent frames.
- Do not call a prompt validated from a single attractive image. Record it as `tested-on-this-setup`; user approval and repeated results are separate upgrades.
