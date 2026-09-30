# v2 relighting recipes

The first version overloaded reconstruction, fine texture, atmospheric effects and cinematic world-building. v2 narrows the operation to **lighting, shading and existing material response**, and evaluates fidelity and uplift separately.

## Shared core

Fill only observable fields. Omit unsupported materials and light relationships. Keep the prompt concise; do not invent a depth map, rendering buffer or numeric tool knob.

```text
Use case: lighting-weather / image relighting.
Edit target: the supplied original artwork. Edit this image; do not reinterpret it as a new scene.
Mode: [Normal or Deep].
Keep: [visible subjects, defining identity features, expressions, poses, costume motifs, object counts including small distant subjects, crop, camera, background layout, text/overlays]. Preserve original silhouettes and drawn feature positions as closely as the editor allows.
Current light evidence: [bright regions / luminous objects / lit-side direction already visible].
Current palette and style: [observed palette and medium].
Change only illumination, shading, existing highlights and material response. Retain the original edges, shapes and texture vocabulary. Keep faces in the original anime design: no casting, beautification, added pores, anatomy or expression change. Preserve hand gestures, jewelry, emblems, clothing panels and background subjects.
Make existing surfaces respond differently to the same scene light: [two or three supported material distinctions]. Add no new decorative texture or invisible-surface detail.
[One mode suffix below.]
Keep bright cores and clean edge gradients. Do not smooth hair locks, costume linework or fine ornaments into painted patches. Avoid a global haze/gray veil, uniform glow, clipping, black crush or sharpening halos. Do not add, remove or rearrange scene content, particles, light-source objects or background decoration. Maintain the source aspect ratio and framing; add no text or watermark.
```

## Normal suffix

```text
Normal: a clear but restrained relight. Improve separation between existing illuminated and shaded surfaces, soften harsh highlight clipping and deepen small contact shadows where surfaces meet. Preserve the original palette and lighting character. The improvement should be visible side by side, with no dramatic restaging or change in drawn detail.
```

## Deep suffix

```text
Deep: an unmistakable cinematic RELIGHT, with the same artwork and exact scene content. Build a stronger difference between existing lit and shaded surfaces. Intensify source-supported environmental bounce onto subject-facing surfaces, shape deeper readable contact shadows at existing overlaps, and make existing rim/specular highlights more deliberate. Use the source's own light colors for color separation. Localize glow to already-luminous regions, leaving faces, eyes, hair strands, hands, ornaments and clothing borders sharply readable. Create stronger dimensionality through shading relationships, not added scenery, new texture, increased particle count, extra fog or global saturation. The difference should be obvious at fit-to-screen size and remain coherent at 100%.
```

## Correction: fidelity failed

Return to the original. Keep the selected mode, but limit the operation to one existing light relationship:

```text
Edit the original image again. The previous attempt changed [specific feature]. Preserve that feature exactly as drawn. Limit this correction to [existing lit-versus-shadow relationship] on [existing surface]. Preserve all remaining scene content and texture; no new objects or structural edits. Keep the resulting lighting change clearly visible without restaging the image.
```

If the available editor repeatedly changes identity/layout, mark the attempt unsuccessful. Switching to a mask/conditioning pipeline requires an actually available, user-selected workflow. Do not claim prompt text can guarantee pixel-level preservation.

## Correction: uplift too weak

Return to the original; raise only one supported relationship:

```text
Keep the image's original structure, palette and contents. Make [named source-supported light relationship] substantially stronger: brighter but unclipped light-facing surfaces and deeper readable shadows on the opposing/occluded surfaces. Preserve all faces, linework, costume patterns, objects and background. Keep glow local. Do not compensate by adding detail, changing color palette, increasing particle density or redesigning scenery.
```

## Optional controlled img2img adapter

For an explicitly selected Flux/SD/ComfyUI workflow, consult the installed model/node documentation for valid denoise, conditioning and seed controls. Use the original as img2img input, source-derived edge/depth guidance and protected masks when supported. Select the lowest transformation strength that passes uplift; maintain the same seed for paired comparisons. These controls improve repeatability but do not by themselves prove identity preservation. No fixed denoise range transfers reliably across all models/nodes.
