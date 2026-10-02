# AI 修图师版：纯调整电影光感

调用名：`cinematic-ai-retoucher`。让 AI 像修图师一样分析光源、设计并执行曲线、局部蒙版、加深减淡和克制调色，处理原有像素。**这个 Skill 全程纯调整，生成式重绘放在独立的 AI 调度版。**

| 档位 | 目标 |
|---|---|
| Normal 正常档 | 清楚、克制地塑造受光与阴影 |
| Deep 深度档 | 更明显的焦点光、背光和空间层次，沿用原画线条与结构 |

色彩强度默认随原图，避免用饱和度或全图模糊制造“强效果”。AI 负责决策与执行；画面由传统调整工具或确定性运算处理。

## 安装与使用

把这个完整文件夹放进 `~/.codex/skills/`（Windows：`%USERPROFILE%\.codex\skills\`）。也可从仓库 `skills/cinematic-ai-retoucher` 单独复制。重新启动 Codex 后，附图调用：

```text
$cinematic-ai-retoucher 深度档，纯调整：用曲线、蒙版、加深减淡做明显光感，保留原图脸、线条和纹样。
```

优先使用宿主可用的原生修图工具与调整层；工具缺失会说明或给出可执行配方，避免换成生成式工具。原生 PSD 必须由实际编辑器保存。

备用本地脚本需要 Python 3.9+、NumPy 和 Pillow，返回 PNG、蒙版、逐步图、JSON 配方和记录。独立复算本包示例：

```bash
python scripts/apply_adjustments.py --source assets/v4-portrait-source.png --recipe references/v4-portrait-deep.json --output-dir portrait-deep-demo
```

使用新输出目录。单张 8-bit RGB/RGBA；16-bit/HDR 母版留在支持它的原生编辑器。脚本没有模型、图像重采样、修补或画面模糊，也没有伪称 PSD 或独立 EXE。

## 纯调整对比

**左原图、右深度档结果**。继承 v4 的单图两档证据；拆分后复算用于核对打包与输出一致性，未追加新的审美成功率。

![Deep 纯调整对比](assets/v4-portrait-deep-side-by-side.png)

[Normal 对比](assets/v4-portrait-normal-side-by-side.png) · [中线划像](assets/v4-portrait-deep-center-wipe.png) · [原图](assets/v4-portrait-source.png)

[执行入口](SKILL.md) · [调整方法与配方语法](references/adjustment-workflow.md) · [验收](references/evaluation.md) · [实测与限制](references/validation.md)

光感来自明暗／色彩关系调整，缺失纹理和真实三维光照没有由此重建。每张图单独设计蒙版与力度。自写文本／脚本使用 [MIT License](LICENSE)，示例权利见 [NOTICE.md](NOTICE.md)。
