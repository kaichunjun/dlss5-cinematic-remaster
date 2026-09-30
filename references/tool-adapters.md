# Tool and medium adapters

Select only the route genuinely needed for the request. These are capability checks, not a list of required installations.

## Traditional adjustments (default)

Use an available native image editor with reversible adjustment layers/masks. Read [adjustment-workflow.md](adjustment-workflow.md). Keep profile/bit depth, original geometry and source file; save the actual layered document plus a separate export. Verify that the chosen tool really returns editable layers. A flattened connector output must not be described as a PSD.

When native editing is unavailable, the packaged `apply_adjustments.py` is a local deterministic route: NumPy/Pillow, per-image curves/exposure/color operations and masks, PNG steps and a replayable recipe. See its real limits and schema in the workflow reference. Neither route needs an image-generation model.

For an Adobe connector, discover the actual schema and its required initialization/preview steps; honor its single-image versus batch routing. Supported brightness/contrast/exposure/HSL and one mask do not imply arbitrary Photoshop curves, blend modes or layered export. Stage local files only through supported upload paths. Manual masks remain the fallback for a fully traditional workflow.

## Generative editing (explicit opt-in only)

Only after a request for image synthesis, reconstruction, replacement content or a new image, use the available image editor and its actual instructions/schema. Inspect original targets and distinguish lighting references. Read [prompt-recipes.md](prompt-recipes.md); retain original-based bounded correction and four-gate review. Prompts do not lock geometry. Hidden seed, denoise, mask, checkpoint or output-size controls stay `not exposed`.

For an explicitly selected ComfyUI/img2img route, verify the running service, installed models/nodes and graph. Record actual checkpoint, seed, denoise and guidance only if available. A valid graph, completed execution and successful visual result are different states. Do not invoke generation merely because adjustment results look subtler.

## Medium-specific treatment

| Input | Preserve | Adapt the relight |
|---|---|---|
| Anime / line illustration | Face design, contour hierarchy, cel shapes and drawn motifs | Broad clean form shading; no pores, painted-smear conversion or real-person recasting |
| Graphic poster | Typography, symbols, flat intentional graphic shapes | Improve existing overlaps/highlights without converting decorative shapes into literal 3D objects |
| Game / CG | Character models, costumes, silhouettes and existing material language | More coherent apparent bounce/specular/contact response; no claim of actual depth/normal/PBR reconstruction |
| Photograph | Identity, expression, observable skin texture and real contacts | Plausible local light/color; no beautification or synthetic skin unless requested |
| Product / logo / document | Exact marks/text/geometry are usually critical | Prefer genuinely supported protected-region/deterministic edits; qualify full-frame redraw |

## New images, batches and video

An explicit new-image request authorizes generation for that scene. Label it as generation; avoid an unnecessary second generative pass. Subsequent grading defaults to adjustments unless synthesis is again requested.

For batches, group by medium/light conditions, make a representative sample for each group, retain a shared treatment contract and inspect individual identities. A new scene may need different light relationships; a fixed preset is not consistency proof. Sample review need not halt already authorized work, but hard failures require correction before propagating a treatment.

For video, prefer deterministic color grading with tracked/keyframed masks in a real video editor. The local helper is still-image-only. Validate a short representative segment before full-length processing; changing a mask per frame requires temporal review. An explicitly generative video job needs an actually available temporal model pipeline. Inspect contiguous motion, cuts, faces/occlusions, hair/text and light/color pumping; record dropped/duplicated frames, output fps, codec and audio continuity. Do not independently edit every frame with this still-image tool and claim temporal stability. Desktop/game realtime filtering belongs to a separate runtime request.
