# Prompt recipes

## Fixed mother prompt

Use this as the stable core. Replace bracketed fields only when an input requires it.

```text
Apply a controlled 3D-guided cinematic neural remaster to the supplied image.

STRUCTURE LOCK — preserve exactly: [identity, facial proportions, expression, pose, body proportions, hairstyle silhouette, costume geometry and symbols, camera, crop, perspective, scene layout, object count, existing light-source positions, and source palette]. Do not redesign, replace, add, remove, or move anything.

MATERIAL RECONSTRUCTION — separate the existing materials through physically plausible response: natural skin subsurface scattering; fine hair-light transmission; readable fabric weave and folds; differentiated leather roughness; metal micro-scratches and edge variation; coherent glass, foliage, water, and wet-surface behavior where already present. Add micro-detail only when supported by the visible surface; never invent decoration.

LIGHT TRANSPORT — preserve every original light direction and color while improving soft global-illumination bounce, ambient occlusion, contact shadows, reflections, transmission, and highlight rolloff. Keep shadows readable and highlights controlled.

ART DIRECTION — retain the source's anime, game, or CG identity. Improve dimensionality and tactility without converting the subject into a different person, live-action casting, or a different franchise. Use a restrained filmic grade and preserve the dominant palette.

PROTECT — face identity, eyes, hands, anatomy, silhouette, costume design, symbols, text, and composition.

AVOID — waxy or plastic skin, beauty-filter face, excessive pores, universal wet gloss, greasy materials, oversharpening, halos, bloom wash, crushed blacks, oversaturation, random engraved detail, new accessories, anatomy change, face replacement, costume redesign, new objects, missing objects, text corruption, and watermark.
```

## Strength suffixes

Append exactly one.

### Normal — balanced texture-preserving cinematic

```text
Strength: balanced texture-preserving cinematic. Keep the source's own palette, light colors, atmosphere, and art direction. Clearly improve physically coherent material separation, dimensionality, contact shadows, bounced light, transmission, reflections, and smooth highlight rolloff while preserving mid-frequency information supported by this image: hair locks, facial linework, fabric folds, surface relief, object boundaries, intentional brushwork, particles, and background contours. Recover readable tonal separation from clipped highlights without dimming genuine light sources or effects. Maintain small natural luminance variation and restrained fine grain so surfaces do not merge into broad painted patches. Prefer clean local separation over aggressive denoising. No watercolor blending, texture melting, edge soup, waxy smoothing, universal gloss, clarity halos, or compensating oversharpening.
```

Use this when the mode decision selects Normal. Replace the protected-detail examples with features actually visible in that image; do not carry characters, materials, colors, lighting, objects, or scenery from previous jobs. Start from the original source rather than an already processed frame whenever possible.

### Deep — atmospheric cinematic

```text
Strength: deep atmospheric cinematic. Preserve the source identity, geometry, composition, palette, light-source positions and art direction, then intensify the frame into a powerful hero image. Build a coherent key/fill/rim/environment hierarchy from light already supported by the scene. Add controlled volumetric atmosphere, localized haze, bounced color, deeper contact shadows, ambient occlusion, foreground/background separation, selective specular accents and smooth highlight bloom. Reproduce the characteristic low-frequency relighting seen in actual DLSS 5 Neural Rendering output: broad warm translucent light wrap, cool environmental spill, gently lifted shadow color, and soft diffusion around bright transitions. Counterbalance that diffusion by retaining local tonal separation and every supported mid-frequency edge; do not imitate the runtime's gray veil or texture smear. Shape contrast locally around the subject and use restrained complementary color separation to strengthen visual focus. Make existing materials denser and more tactile through plausible roughness and reflection. Protect all mid-frequency structure: face, eyes, hair locks, hands, linework, fabric folds, seams, object edges, particles, brush direction and background contours. Keep bright light cores with colored gradients and readable surrounding detail. One clean reconstruction pass; high processing resolution. No broad denoising, global fog blanket, watercolor blending, texture melt, plastic smoothing, universal gloss, halo sharpening, crushed blacks, clipped highlights, excessive bloom, oversaturation, new light-source objects or scene redesign.
```

Deep is judged on two axes at once: stronger atmosphere and preserved readability. If atmosphere rises while hair, fabric, face, hands, text, or silhouette become less readable, the pass fails. Reduce NR/denoise or localized bloom before reducing material depth.

## Compact reusable prompt

```text
DLSS-5-inspired cinematic PBR remaster of the supplied frame; absolute identity, geometry, pose, costume, camera, composition and object lock; preserve anime facial proportions and source palette; reconstruct only material response and light transport: restrained skin subsurface scattering, fine hair transmission, differentiated cloth/leather/metal roughness, supported microtexture, deeper contact shadows, ambient occlusion, bounced global illumination, coherent reflections, controlled highlight rolloff and open shadows; no redesign, face replacement, anatomy change, new objects, invented patterns, waxy skin, universal gloss, oversharpening, halos, crushed blacks, oversaturation or watermark.
```

## Model adapters

### GPT Image or similar natural-language editor

- Provide the source as the edit target.
- Choose Normal or Deep first, then use the mother prompt plus exactly that mode suffix.
- Repeat the complete Structure Lock and Protect clauses on every iteration.
- Change one variable per iteration. Move between Normal and Deep only after re-evaluating structure preservation and the user's requested intensity.

### Flux, SDXL, or ComfyUI img2img

- Start with denoise `0.20-0.35`; reduce it when face, costume, or layout drifts.
- Use Depth plus Normal or Canny/Lineart conditioning when geometry matters.
- Keep a fixed seed and compare at least two seeds before attributing an effect to a phrase.
- Add an identity reference for important faces. Use inpainting or semantic masks to protect faces, hands, symbols, and text.
- Negative prompt core: `waxy skin, plastic face, altered identity, anatomy change, costume redesign, new objects, missing objects, random texture, universal gloss, oversharpened, halo, bloom wash, crushed blacks, oversaturated, watermark`.

### Actual DLSS 5 tools

These values are starting points, not universal presets.

| Mode | Style | NR intensity | Local tone | Local structure | Skin structure | Passes |
|---|---|---:|---:|---:|---:|---:|
| Normal | Natural or Cinematic | 0.55-0.75 | 0.30-0.45 | 0.70-0.90 | -0.7 to -0.3 | 1 |
| Deep | Cinematic | 0.80-1.00 | 0.45-0.65 | 0.80-1.00 | -0.5 to 0.0 | 1 |

Use face/skin protection and tone preservation when available. Raise the network processing resolution before raising Local structure. Keep Deep at one pass; if hair, fabric, face, hands, linework, text, particles, or background edges begin to merge, reduce NR intensity and localized glow first. A second pass compounds smear and is outside the default Normal/Deep workflow.

## Visual direction references and tested scenes

The bundled center-wipe comparisons record target qualities taken from the user's supplied frames: cool material depth, controlled highlights, atmospheric glow, strong hero lighting, and preserved mid-frequency detail. Treat them as visual behaviors, never as scene nouns or a fixed palette. See `assets/comparison-*.jpg`.

The primary matched comparison uses an orange-gold anime poster. Deep strengthens supported light rhythm, color separation, spatial layering, and the hero-frame impression. See `assets/comparison-01-orange-deep.jpg` and [evaluation.md](evaluation.md).

Four additional source/remaster pairs test portability across different characters, compositions, palettes, materials, highlight problems, and atmospheric depth. See `assets/comparison-02-cosmic.jpg` through `assets/comparison-05-hero-tree.jpg`.

`assets/reference-actual-dlss5-nr-portrait.jpg` is a user-supplied Visual Enhancer DLSS 5 Neural Rendering output reference. It anchors the runtime-specific effect signature: broad warm hair transmission, cyan environmental spill, lifted low-frequency illumination, smooth highlight diffusion, muted background contrast, and a soft atmospheric veil. Treat these as transferable light-transport behaviors. Deep should preserve their atmosphere while recovering local contrast, hair-lock separation, facial linework, metal edges, and crystal boundaries that the runtime reference softens.
