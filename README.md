# Cinematic tonal grading and local light shaping · v4

[简体中文](README.zh-CN.md)

A reusable **traditional adjustment-first** Skill for illustrations, game images, CG and photos. The assistant analyzes the source and designs curves, local masks, dodge/burn and restrained color layers. Existing faces, lines, motifs and layout remain the source geometry. Each image gets its own treatment rather than inheriting example subjects or coordinates.

The legacy identifier is `dlss5-cinematic-remaster`. DLSS5 denotes visual inspiration; no NVIDIA model/runtime or always-on desktop/game filter is bundled.

| Mode | Target |
|---|---|
| Normal | Clear, restrained form shading, material separation and highlight hierarchy |
| Deep | More obvious focal light, backlit shade, local environment response and spatial separation |

Both modes default to traditional pixel adjustments and source-strength color. Deep does not authorize saturation boosts, whole-image blur or synthesis. Generative reconstruction is **explicit opt-in only**; unavailable adjustment tools are reported, not silently replaced with a model.

## Current example

Traditional adjustment of the same rain-night source. **Source left, Deep result right**: brighter existing facial illumination and a darker backlit sleeve; original hair, expression, motifs and alley retained. Preview scaling is for presentation only.

![Deep traditional-adjustment full pair](assets/v4-portrait-deep-side-by-side.png)

[Center wipe](assets/v4-portrait-deep-center-wipe.png) · [Native result](assets/v4-portrait-deep-result.png) · [Normal full pair](assets/v4-portrait-normal-side-by-side.png)

One source, two mode variants and one Deep replay. Fourteen computational checks passed; assistant visual review passed on this image, user aesthetic approval is pending. No universal success rate is claimed. [v4 validation](references/validation-v4.md) distinguishes computation, visual judgment and limits. [v3 tests](references/validation-v3.md) are historical generative evidence, not validation of this default route.

## Install and use

macOS/Linux:

```bash
git clone https://github.com/kaichunjun/dlss5-cinematic-remaster.git ~/.codex/skills/dlss5-cinematic-remaster
```

Windows PowerShell:

```powershell
git clone https://github.com/kaichunjun/dlss5-cinematic-remaster.git "$env:USERPROFILE\.codex\skills\dlss5-cinematic-remaster"
```

Or copy the folder into your Skill directory. A clean existing clone can `git pull --ff-only`; preserve local customizations. Restart Codex if discovery needs refreshing. Attach your image:

```text
$dlss5-cinematic-remaster Deep, traditional adjustments only: visible light shaping with curves and local masks, retain original faces/lines/motifs and restrained source color.
```

Prefer real reversible adjustment layers in an available native editor. Label flattened connector output honestly. The optional local fallback requires Python 3.9+, NumPy and Pillow:

```bash
python scripts/apply_adjustments.py --source your-source.png --recipe your-image.json --output-dir grade-new
```

The assistant designs the recipe for that input. The [portrait recipe](references/v4-portrait-deep.json) is example-specific, not a universal preset. Output includes PNG result, masks, numbered layer steps and replayable JSON; **not a PSD or standalone EXE**. Single 8-bit RGB/RGBA inputs only; use a suitable native editor for 16-bit/HDR masters. A new output directory protects existing files.

## Resources

- [SKILL.md](SKILL.md): mode decision, source analysis, default method and review.
- [adjustment-workflow.md](references/adjustment-workflow.md): Photoshop layer guidance, local schema and exact computational limits.
- [apply_adjustments.py](scripts/apply_adjustments.py): deterministic processing; no synthesis, geometric resampling, inpainting or artwork blur.
- [tool-adapters.md](references/tool-adapters.md): native/connector capabilities, batches/video and opt-in synthesis.
- [requirements.md](references/requirements.md), [evaluation.md](references/evaluation.md): complete brief and four independent gates.
- [review_artifact.py](scripts/review_artifact.py): Python + FFmpeg/ffprobe comparison/native-crop helper; it never grades aesthetics.
- [skill-audit.md](references/skill-audit.md): previous source review and this method revision. [Legacy prompts](references/prompt-recipes.md) apply only to explicit generation.

This shapes apparent light through existing pixel relationships; it does not reconstruct missing texture or true 3D light transport. Masks and strength require image-specific judgment. Own text/scripts: [MIT License](LICENSE); underlying sample/character rights: [NOTICE.md](NOTICE.md).
