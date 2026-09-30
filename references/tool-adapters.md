# Tool and medium adapters

Select only the route genuinely needed for the request. These are capability checks, not a list of required installations.

## Built-in image editing (default)

Inspect local inputs first. Use the current built-in schema and imagegen instructions; supply the original target and label optional references. Preserve original alpha unless a background change is requested. Save separately and inspect the returned file. The schema used in this release exposed a prompt, input-image references and transparency; it did **not** expose seed, denoise, protected-region masks, ControlNet strength, model checkpoint or requested pixel dimensions. Do not invent those controls. Unknown underlying version stays unknown.

One call per requested asset/variant. A failed job is an execution failure; check existing returned artifacts before repeating an uncertain call. A successful job still needs visual assessment.

## Explicit ComfyUI / img2img / other model route

Discover the running server, installed compatible models/nodes and their actual schemas. Record checkpoint/version, graph, text encoder, dimensions, sampler/steps/CFG/seed and denoise only if available. Start from the original source, not an accumulated redraw. Derive edge/depth/pose guidance from the source when supported and actually supplied. Review masks: where the tool protects original pixels, verify the composite rather than merely describing it as protected.

Hold available seed/settings constant for a paired test; vary one meaningful factor. Fixed seed alone does not ensure identical output across changed graphs/backends/versions. Pick the lowest transformation strength that still meets the requested uplift on that image; no universal denoise/CFG recommendation is bundled. A valid graph, installed model, completed execution and acceptable image are four different states.

## Explicit photo-editor / color-only route

For a user-selected editor, reversible curves, tonal masks and local color adjustments can change existing pixels while retaining geometry. Check the application's supported operation first. Treat generated light and subsequent grading as separate stages. Preserve original/master/grade/export separately. Exact geometry says nothing about whether the relighting looks convincing.

If the user requests only saturation correction and an actual deterministic color operation is authorized/available, avoid rerendering an already acceptable structure. Otherwise use the image-edit tool with named regional color goals and inspect redraw risk. Never map Photoshop saturation values onto a generative prompt as actual tool settings.

## Medium-specific treatment

| Input | Preserve | Adapt the relight |
|---|---|---|
| Anime / line illustration | Face design, contour hierarchy, cel shapes and drawn motifs | Broad clean form shading; no pores, painted-smear conversion or real-person recasting |
| Graphic poster | Typography, symbols, flat intentional graphic shapes | Improve existing overlaps/highlights without converting decorative shapes into literal 3D objects |
| Game / CG | Character models, costumes, silhouettes and existing material language | More coherent apparent bounce/specular/contact response; no claim of actual depth/normal/PBR reconstruction |
| Photograph | Identity, expression, observable skin texture and real contacts | Plausible local light/color; no beautification or synthetic skin unless requested |
| Product / logo / document | Exact marks/text/geometry are usually critical | Prefer genuinely supported protected-region/deterministic edits; qualify full-frame redraw |

## New images, batches and video

For a new-image request, first specify/create the requested scene, then use the Normal/Deep lighting principles. Label it generation, not a faithful edit of a nonexistent original. Avoid a second generation pass by default; it increases drift and cost without guaranteed improvement.

For batches, group by medium/light conditions, make a representative sample for each group, retain a shared treatment contract and inspect individual identities. A new scene may need different light relationships; a fixed preset is not consistency proof. Sample review need not halt already authorized work, but hard failures require correction before propagating a treatment.

For video, use an actually available temporal pipeline on a short representative segment before full-length processing. Inspect contiguous motion, cuts, faces/occlusions, hair/text and light/color pumping; record dropped/duplicated frames, output fps, codec and audio continuity. Do not independently edit every frame with this still-image tool and claim temporal stability. Desktop/game realtime filtering belongs to a separate runtime request.
