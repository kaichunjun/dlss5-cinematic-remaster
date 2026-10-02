# AI 调度版：生成式电影光影重绘

调用名：`cinematic-ai-remaster`。让 AI 分析原图、组织提示词并调用可用的图像生成／编辑工具，得到正常档或深度档光影重绘结果。每张图片重新分析，参考图只提供指定的光感。

| 档位 | 目标 |
|---|---|
| Normal 正常档 | 清楚、克制的受光、阴影和材质增强 |
| Deep 深度档 | 更明显的环境氛围、明暗层次和局部光韵 |

两档均约束原图人物、构图与色彩强度，仍需实看生成结果：细线、脸和纹样可能改变。追求已有像素与线条保持时，选择独立的 **AI 修图师版**。

## 安装与使用

把这个完整文件夹放进 `~/.codex/skills/`（Windows：`%USERPROFILE%\.codex\skills\`）。也可从仓库 `skills/cinematic-ai-remaster` 单独复制。重新启动 Codex 后，附图调用：

```text
$cinematic-ai-remaster 深度档：调度图像生成工具，明显增强现有光影与环境氛围，保留人物构图，色彩克制。
```

需要宿主实际提供图像生成工具；Skill 文本本身没有模型。默认使用可用的内置编辑器；用户指定其他服务时，按其真实能力执行。输出图片、精确提示词／已暴露设置、评审和左右对比。可选比较工具需要 Python + FFmpeg/ffprobe。

## 历史生成对比

**左原图、右生成结果**。以下继承 2026-09-30 的实测，拆分当天没有重新生成。

Normal 雨夜：助手在该图上评审通过，仍有细线变化；用户批准待定。

![Normal 生成对比](assets/v3-portrait-side-by-side.png)

Deep 群像：光影更鲜明，细纹样重绘及输出分辨率降低，属于有条件预览。

![Deep 生成对比](assets/v3-ensemble-side-by-side.png)

[执行入口](SKILL.md) · [提示词配方](references/prompt-recipes.md) · [验收](references/evaluation.md) · [历史证据与限制](references/validation.md)

本包属于静态图像工作流，没有 DLSS 运行时、实时游戏或桌面渲染能力。自写文本／脚本使用 [MIT License](LICENSE)，示例权利见 [NOTICE.md](NOTICE.md)。
