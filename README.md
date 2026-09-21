# DLSS5 Cinematic Remaster

[中文说明](README.zh-CN.md)

**Structure-aware cinematic neural remastering for anime, game, and CG imagery.**

DLSS5 Cinematic Remaster is a reusable Codex skill and evaluation workflow for converting the visual goals associated with high-end neural rendering into controlled image-editing instructions. It improves material separation, lighting hierarchy, spatial depth, highlight roll-off, and local structure while protecting character identity, anatomy, costume geometry, camera, composition, palette, and the source art direction.

Unlike a generic “enhance,” sharpen, or style-transfer prompt, the workflow separates visual uplift from structural fidelity. Every output is checked for semantic drift and common reconstruction failures such as painterly smearing, waxy skin, universal gloss, bloom wash, halo sharpening, and invented detail.

The system provides two production modes:

- **Normal** — faithful cleanup, material separation, controlled highlights, and stable detail.
- **Deep** — stronger atmosphere, hero lighting, richer color separation, and cinematic depth while keeping faces, hands, costumes, and edges readable.

It can be used with natural-language image editors, Flux/SDXL/ComfyUI img2img pipelines, and neural-rendering tools that expose tone, structure, skin-protection, intensity, mask, or pass-count controls. The repository includes fixed prompt architecture, model adapters, parameter starting points, a repeatable QA rubric, and matched source/remaster comparisons.

![Source and Deep center-wipe comparison](assets/comparison-01-orange-deep.jpg)

*A center-wipe comparison built from the user's reference frame: source on the left, Deep on the right.*

## What it does

The skill inspects every input independently, chooses Normal or Deep, locks the visible structure, and rebuilds material response and lighting without turning the edit into a free redesign. Its core safeguards cover identity, pose, anatomy, costume geometry, camera, crop, scene layout, objects, palette, text, and the source's art direction.

| Mode | Best for | Visual behavior |
|---|---|---|
| Normal | portraits, clean anime art, UI or text-heavy frames, faithful restoration | moderate local contrast, controlled reflections, clear materials, open shadows, minimal drift |
| Deep | dramatic scenes, hero frames, strong atmosphere, “cinematic” or “maxed-out” requests | coherent key/fill/rim light, volumetric depth, deeper shadows, stronger complementary color separation |

Both modes reject broad denoising, waxy skin, watercolor smearing, universal gloss, halos, crushed blacks, clipped highlights, anatomy changes, and invented decoration.

### Comparison gallery

Every visual reference is presented as a matched center-wipe comparison. The left half is the supplied source and the right half is the remastered result.

#### Highlight control and cosmic depth

![Cosmic frame source and remaster](assets/comparison-02-cosmic.jpg)

#### Cool material depth

![Horned character source and remaster](assets/comparison-03-horned.jpg)

#### Atmospheric glow with readable structure

![Atmospheric frame source and remaster](assets/comparison-04-atmospheric.jpg)

#### Hero lighting and environmental scale

![Golden tree frame source and remaster](assets/comparison-05-hero-tree.jpg)

These comparisons define transferable image qualities rather than fixed characters or scenes. The workflow re-derives subjects, materials, palette, and light sources for every new input.

## Install

Clone the repository into the Codex skills directory:

```bash
git clone https://github.com/kaichunjun/dlss5-cinematic-remaster.git ~/.codex/skills/dlss5-cinematic-remaster
```

Restart Codex after installation if the skill does not appear immediately.

## Use

Attach an image and invoke the skill:

```text
$dlss5-cinematic-remaster Remaster this image. Choose the suitable mode yourself.
```

Or select a mode explicitly:

```text
$dlss5-cinematic-remaster Use Normal mode. Preserve the original composition and face.
```

```text
$dlss5-cinematic-remaster Use Deep mode. Make it atmospheric and powerful while keeping every edge readable.
```

Before generating, the skill states the selected mode. It asks only when the request is genuinely ambiguous and the choice would materially change the result.

## Runtime parameter mapping

For tools that expose Neural Rendering-style controls, these are starting points rather than universal presets:

| Mode | Style | NR intensity | Local tone | Local structure | Skin structure | Passes |
|---|---|---:|---:|---:|---:|---:|
| Normal | Natural / Cinematic | 0.55–0.75 | 0.30–0.45 | 0.70–0.90 | -0.7 to -0.3 | 1 |
| Deep | Cinematic | 0.80–1.00 | 0.45–0.65 | 0.80–1.00 | -0.5 to 0.0 | 1 |

Raise processing resolution before increasing local structure. Keep one pass by default; repeated reconstruction is a common cause of smeared hair, fabric, text, and background edges.

## Repository layout

```text
SKILL.md                    Core decision and execution workflow
agents/openai.yaml          Codex display metadata
references/prompt-recipes.md
references/evaluation.md    QA rubric and test record
assets/                     Matched center-wipe comparison gallery
```

## Scope

This project is an independent prompt and workflow skill. It is **not NVIDIA DLSS software**, does not contain NVIDIA binaries or models, and does not enable DLSS in unsupported games. The name describes the intended visual direction; actual output depends on the image editor or runtime used.

## License

MIT for the workflow, prompts, and documentation. See [LICENSE](LICENSE) and [NOTICE.md](NOTICE.md) for example-image rights.
