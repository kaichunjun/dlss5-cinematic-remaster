# DLSS5 风格电影光影重绘 Skill · v3

[English](README.md)

用于现有动漫、游戏、CG 和照片的双档光影增强工作流。目标是**效果明显、环境光统一、阴影有层次、材质可读，同时保持角色与构图、克制色彩、避免涂抹**。每张图重新分析，继承处理方法，示例的角色、场景和配色不会自动套入新图。

这是提供给 AI 助手执行的 Skill，包含提示词、工具适配与验收方法；没有 DLSS 运行时／NVIDIA 模型，也不是 Windows 实时过滤软件。

## 正常档与深度档

| 档位 | 目标 |
|---|---|
| Normal 正常档 | 清楚而克制地增强形体阴影、材质区分与高光过渡 |
| Deep 深度档 | 明显加强已有环境受光、明暗关系、接触阴影和局部光韵，形成更有气场的画面 |

先判断档位，再简短说明；明确指定优先。深度档提高光影强度，保真规则和原图色彩强度与正常档相同。当前默认尤其保护肤色、中性色和未受光背景，避免把强氛围做成高饱和滤镜。

## v3 改进

本次审查 15 个本地相关 Skill，并筛查 7 个公开仓库的 22 个入口；存在同源重叠，范围和取舍完整列于 [审查报告](references/skill-audit.md)，没有声称穷尽全网。

- 原件／风格参考角色明确；逐图建立保留内容表，照片、动漫、CG、海报分别适配。
- 将内容与身份、可见光影差距、色彩、清晰度与受光一致性分成四项独立检查。
- 每次修正回到原件，只针对一个问题，初次结果后最多两次修正；保留失败与用户反馈。
- 真实工具设置按能力使用；文字要求不会被当成掩膜、结构控制或实际 PBR 重建。
- 比较与文件证据可自动生成，视觉结论仍基于实看；静帧、批量、视频与实时运行边界分别说明。

完整需求逐条追踪见 [requirements.md](references/requirements.md)。

## 新版对比图

**左原图，右结果；中线划分为展示预览。** 完整双图和原生细节检查才用于验收。

Deep 群像：原有羊皮纸与人物受光更鲜明，色彩相较 v2 收敛。细小线条／纹样仍有重绘，属于有条件预览。

![Deep 群像中线对比](assets/v3-ensemble-center-wipe.png)

[查看完整左右对比](assets/v3-ensemble-side-by-side.png)

Normal 雨夜单人图：沿已有灯笼方向增强发缘、服装阴影与金属高光。助手视觉检查通过；用户确认待定。

![Normal 雨夜中线对比](assets/v3-portrait-center-wipe.png)

[查看完整左右对比](assets/v3-portrait-side-by-side.png)

v3 新增两次执行、两个输入；结合 v2 为五次执行、三个独立输入。精细纹样保持仍有限，底层模型版本／seed 未暴露；当前没有通用稳定成功率。真实照片与连续视频尚无 v3 实测。见 [实测记录](references/validation-v3.md) 和 [精确提示词](references/v3-test-prompts.json)。

## 安装与调用

macOS／Linux，安装至 Codex Skill 目录：

```bash
git clone https://github.com/kaichunjun/dlss5-cinematic-remaster.git ~/.codex/skills/dlss5-cinematic-remaster
```

Windows PowerShell：

```powershell
git clone https://github.com/kaichunjun/dlss5-cinematic-remaster.git "$env:USERPROFILE\.codex\skills\dlss5-cinematic-remaster"
```

已有干净克隆可在该目录执行 `git pull --ff-only`；更新前保留本地自定义内容。也可把仓库文件夹放进 Skill 目录。安装后若未出现，重启 Codex。附图调用：

```text
$dlss5-cinematic-remaster 用深度档：光影与环境氛围明显，保留原图人物和构图，色彩克制。
```

可改成“正常档”，或让助手判断。执行需要宿主提供图片编辑工具；仓库文本本身没有生成引擎。内置编辑默认使用，无需本 Skill 单独配置模型密钥。可选外部路线按实际工具能力和任务授权使用。

## 文件导航

- [SKILL.md](SKILL.md)：自包含执行入口与双档选择。
- [prompt-recipes.md](references/prompt-recipes.md)：母模板、档位及四类问题修正。
- [tool-adapters.md](references/tool-adapters.md)：介质、真实工具、批次与视频适配。
- [evaluation.md](references/evaluation.md)：四项验收、交付方法与历史反例。
- [review_artifact.py](scripts/review_artifact.py)：需要 Python 3.9+、FFmpeg／ffprobe 的可选比较与元数据工具；不会自动评判画质。
- [skill-audit.md](references/skill-audit.md)、[source-inventory.json](references/source-inventory.json)：吸收／排除的依据、来源与源码哈希。
- [validation-v3.md](references/validation-v3.md)：真实生成记录及能力缺口。
- [runtime-controls.md](references/runtime-controls.md)：隔离的历史社区应用经验笔记，仅供明确运行时请求参考，非通用权威参数。

本项目自写文档、提示词和脚本使用 [MIT License](LICENSE)。游戏／角色示例及第三方资料权利归原权利人；见 [NOTICE.md](NOTICE.md)。
