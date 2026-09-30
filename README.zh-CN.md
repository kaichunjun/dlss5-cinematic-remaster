# DLSS5 风格电影光影重绘 Skill

[English README](README.md)

用于动漫、游戏与 CG 图片的 **DLSS5 风格光影增强工作流**。v2 将编辑范围收窄到原图已有的光照、阴影和材质响应，分别检查人物／构图保真与可见效果。仓库提供提示词和执行规则，不含 DLSS 运行时或 NVIDIA 模型。

## 两个档位

- **Normal 正常档：**明显但克制的光影、层次和材质分离。
- **Deep 深度档：**明显的环境受光、更强且可读的阴影、局部轮廓光和高光。沿用原图光源与色彩；增强强度提高，内容保护规则相同。

生成前先判断档位并简短说明。生成后逐个检查脸、手、服装图案、小人物和布局，再检查光影差距。失败时从原图最多修正两次；仍未通过则明确报告问题。提示词本身无法保证像素级或几何级锁定。

## v2 本次实测

左侧原图，右侧新版。以下是暂定视觉样例，存在小细节重新描绘，不能作为完全保真证明。

![群像深度档中线对比](assets/v2-ensemble-center-wipe.png)

![海报正常档中线对比](assets/v2-poster-center-wipe.png)

2026-09-30 使用内置图片编辑器，对 **两张图执行三次**：群像 Deep 用同一提示词独立重复两次；橙金海报 Normal 一次。两次群像的光影方向相近，没有再次添加行星或重做宇宙背景；放大后脸部线条、服装和纹理细节仍有少量变化。结论是流程更受控，尚未获得通用稳定成功率。v2 的肖像与连续视频稳定性仍待测试。完整观察见 [验收与测试记录](references/evaluation.md)，[实测提示词](references/v2-test-prompts.json) 可复查。

## 安装与使用

```bash
git clone https://github.com/kaichunjun/dlss5-cinematic-remaster.git ~/.codex/skills/dlss5-cinematic-remaster
```

已有干净克隆可在该目录执行 `git pull --ff-only` 更新；保留本地自定义内容后再操作。如果安装后未显示，重启 Codex。附上图片并调用：

```text
$dlss5-cinematic-remaster 用深度档，光影和氛围要明显，保持当前图里的人物与构图。
```

也可指定正常档或让助手判断。每张图片重新分析，沿用的是光影处理方法，示例人物、背景和配色不会自动套进新图。内置图片编辑优先；可选 img2img 适配需要真实可用的模型设置与结构引导。

## 项目内容

- [SKILL.md](SKILL.md)：档位判断、执行步骤与有限重试。
- [提示词](references/prompt-recipes.md)：光影母模板及档位／修正模板。
- [验收记录](references/evaluation.md)：结构与效果两项检查、失败记录和当前证据。
- [运行时说明](references/runtime-controls.md)：针对明确运行时配置请求的历史经验参数，尚未构成权威或通用推荐。
- `assets/`：新版暂定样例及历史视觉参考；旧图属于 v1。

文档、提示词和工作流采用 MIT：[LICENSE](LICENSE)；[图片权利说明](NOTICE.md)。
