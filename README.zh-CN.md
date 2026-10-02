# 电影光感双 Skill：AI 调度与 AI 修图师

[English](README.md)

同一个 GitHub 项目提供 **两个独立、可单独安装的 Skill**。两者都让 AI 先分析当前图片，并在正常档／深度档之间选择；执行方法明确分开。

| | [AI 调度版](skills/cinematic-ai-remaster) | [AI 修图师版](skills/cinematic-ai-retoucher) |
|---|---|---|
| 调用名 | `cinematic-ai-remaster` | `cinematic-ai-retoucher` |
| 执行方法 | AI 调度图像生成工具，做光影重绘 | AI 当修图师，用曲线、蒙版、加深减淡与调色 |
| 适用方向 | 更自由的材质／光影重构，接受生成变化 | 优先沿用原图脸、线条、纹样和构图 |
| 原图保持 | 提示词约束＋生成后检查；细节仍可能偏移 | 使用已有像素做调整；检查遮蔽、过曝和色彩 |
| 正常／深度 | 都有；差别在光影强度 | 都有；深度档也走纯调整 |
| 交付 | 图片、提示词、实际设置与评审 | 图片、真实调整层或蒙版／步骤／JSON 配方 |

DLSS5 为历史项目名及视觉灵感。这里提供给 AI 助手使用的工作流，没有 NVIDIA 模型／DLSS 运行时或实时游戏／桌面过滤器。

## 独立下载

- [AI 调度版 ZIP](https://github.com/kaichunjun/dlss5-cinematic-remaster/releases/download/v5.0.0/cinematic-ai-remaster-v5.0.0.zip)：生成式光影重绘。
- [AI 修图师版 ZIP](https://github.com/kaichunjun/dlss5-cinematic-remaster/releases/download/v5.0.0/cinematic-ai-retoucher-v5.0.0.zip)：传统纯调整。
- [发布页与 SHA-256 校验](https://github.com/kaichunjun/dlss5-cinematic-remaster/releases/tag/v5.0.0)。

## 分别安装与调用

分别下载对应 Skill 包，或从本仓库 `skills/` 复制所选的整个文件夹。无需同时安装两份。

- macOS／Linux：放进 `~/.codex/skills/`。
- Windows：放进 `%USERPROFILE%\.codex\skills\`。

重启 Codex 后附图调用：

```text
$cinematic-ai-remaster 深度档：用 AI 生成工具做明显光影重绘，保留人物构图，色彩克制。
```

```text
$cinematic-ai-retoucher 深度档，纯调整：用曲线、蒙版和加深减淡增强光感，保留原图线条与纹样。
```

AI 调度版需要宿主可用的生成工具。AI 修图师版优先用原生编辑器，另附 Python／NumPy／Pillow 备用计算工具；具体依赖、真实能力与使用方法见各自目录说明。

## 同题材、不同执行方式

下面是同一雨夜原件的两条历史路线，各自都为**左原图、右结果**。生成例为 Normal，纯调整例为 Deep，档位与日期不同；用于理解方法，不能当作同设置受控画质排名。拆分当天没有重新生成图片。

AI 调度版：生成式重绘，继承 2026-09-30 的 v3 结果。

![AI 调度生成对比](skills/cinematic-ai-remaster/assets/v3-portrait-side-by-side.png)

AI 修图师版：传统纯调整，继承 v4 结果，并核对拆分包复算。

![AI 修图师纯调整对比](skills/cinematic-ai-retoucher/assets/v4-portrait-deep-side-by-side.png)

[生成路线证据](skills/cinematic-ai-remaster/references/validation.md) · [纯调整路线证据](skills/cinematic-ai-retoucher/references/validation.md)

## 历史兼容与权利

根目录的 `dlss5-cinematic-remaster` 保留为旧 v4 入口，继续默认传统调整；新安装推荐上面的两个独立调用名。既有文件与实验记录保留。AI 调度版不会因效果弱而自动换成修图师路线，修图师版也会避免转成生成；改变方法时明确告知并遵循用户选择。

自写文本／脚本使用 [MIT License](LICENSE)，角色与第三方示例权利见 [NOTICE.md](NOTICE.md)。每条路线的证据与限制分开；文件格式检查无法证明所有题材的审美稳定性。
