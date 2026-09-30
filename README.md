# DLSS5 Cinematic Remaster

[中文说明](README.zh-CN.md)

A reusable Codex skill for **DLSS5-inspired cinematic relighting** of anime, game and CG artwork. Version 2 narrows the edit to existing illumination, shading and material response, and checks structural fidelity separately from visible uplift. It contains no DLSS runtime or NVIDIA model.

## Modes

- **Normal:** clear, restrained lighting and material separation.
- **Deep:** conspicuous environmental light, stronger readable shadows and selective highlights, based on the original image's lights and palette. Deep raises lighting strength while retaining the same content constraints.

Before generation, the agent decides the mode from your request and states it. Faces, hands, costume designs, objects, crop and scene layout are inspected. A failed candidate returns to the original for at most two corrections; failure is reported if no result passes both fidelity and uplift checks. Text constraints alone cannot guarantee geometric or pixel-level fidelity.

## v2 examples and evidence

Source on the left, edited result on the right. These are provisional visual examples with small detail redraws, not perfect-fidelity demonstrations.

![Deep ensemble center wipe](assets/v2-ensemble-center-wipe.png)

![Normal graphic poster center wipe](assets/v2-poster-center-wipe.png)

On 2026-09-30, the built-in image editor was run **three times on two inputs**: the crowded ensemble twice with an identical Deep prompt, and the poster once in Normal. The ensemble's repeated lighting direction was consistent and no new planets/cosmic setting were introduced. Fine face lines and costume/texture details still varied. This supports a more constrained workflow, not a universal success guarantee. v2 portrait and temporal-video stability remain untested. See [evaluation and historical notes](references/evaluation.md) and [exact test prompts](references/v2-test-prompts.json).

## Install and use

```bash
git clone https://github.com/kaichunjun/dlss5-cinematic-remaster.git ~/.codex/skills/dlss5-cinematic-remaster
```

For an existing clean clone, update with `git pull --ff-only` from that directory. Preserve local customizations before updating. Restart Codex if the skill does not appear. Attach an image and use:

```text
$dlss5-cinematic-remaster Use Deep: clearly stronger lighting and atmosphere, preserve this image's characters and layout.
```

Or ask the agent to choose Normal/Deep. The source controls the scene; previous examples control only visual direction. Built-in editing is preferred where available. Optional controlled img2img adaptations require supported model/node settings and actual structural guidance, not simulated controls.

## Files

- [SKILL.md](SKILL.md): mode selection, edit workflow and bounded retries.
- [Prompt recipes](references/prompt-recipes.md): shared relighting core and mode/correction suffixes.
- [Evaluation](references/evaluation.md): two acceptance gates, failures and current evidence.
- [Runtime notes](references/runtime-controls.md): separate legacy empirical control notes for explicit runtime requests, not authoritative parameter recommendations.
- `assets/`: current previews and historical visual-direction references. Older comparisons are v1 examples.

Workflow/prompt text is MIT licensed; see [LICENSE](LICENSE) and [image rights](NOTICE.md).
