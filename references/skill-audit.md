# 图像 Skill 审查与方法取舍 — 2026-09-30

## 审查范围

本次完成 **15 个本地相关 Skill 入口，以及 7 个公开仓库内的 22 个入口筛查**；同名／同源重叠属于对照，不能作为独立证据累加。审查入口、相关执行和验收段落，按需查看条件引用；没有声称逐字审完每个仓库的所有代码和引用，也没有声称穷尽全网。UI、网站和 3D 入口用于边界筛查，未当成图片重绘执行路线。完整清单、日期、源码快照标识和内容 SHA-256 在 [source-inventory.json](source-inventory.json)。第三方原文未复制进发布包，也未执行下载的第三方代码。

“学习”在这里指比较流程并重写本项目指导，未训练或微调生成模型。本次改进目标是用户明确的整体效果：双档、明显光影、强环境氛围、保留角色与构图、清晰且色彩克制。

## 本地 Skill：吸收优点，避免误用

| Skill / 入口数 | 值得吸收 | 对本项目的限制或不合适的做法 | v3 的处理 |
|---|---|---|---|
| imagegen / 1 | 编辑目标与风格参考角色、无损保留原件、真实工具路线 | 生成成功并非保真；文字要求无法保证掩膜保护 | 图像角色契约、真实控制记录、实际输出复核 |
| comfyui-prompt-lab / 1 | 可见证据、模型语法适配、单变量实验、反例保留 | 隐藏 seed／模型时无法完成严格可复现实验 | 未暴露设置明确未知；整套提示改写按整套方案评估 |
| comfyui-local-operator / 1 | 节点兼容、实际结构引导、图有效／执行／画质分别验证 | 未安装模型或有效图不能靠提示词补出 | 仅显式选择该路线时检查真实运行环境 |
| image-enhancer / 1 | 根据用途考虑尺寸、格式和交付 | “提高分辨率／细节”表述缺乏具体操作及质量证据 | 单独记录实际像素；插值和新细节生成明确区分 |
| canvas-design / 1 | 焦点层级、构图节奏、材质与视觉一致性 | 自由创作、艺术宣言与长篇品质形容词容易扩大重绘范围 | 取焦点光影原则；保持原图布局及介质 |
| theme-factory、brand-guidelines / 2 | 一致的色彩规则和展示结构 | 固定主题／品牌配色会覆盖每张图的原有色彩 | 原图配色为权威，批次仅共享处理原则 |
| fal-ai-media / 1 | 发现真实模型／输入、队列、成本与输出记录 | 硬编码默认端点和通用数值可能失效 | 仅取能力检查；调用前查实际 schema，保留服务选择权 |
| adobe-retouch-portraits / 1 | 身份保护、局部编辑、可用预设检查 | 适用于特定 Adobe 能力；照片规则不能直接套动漫 | 按介质保护肤质／线条；实际局部路线才声称区域受保护 |
| adobe-batch-edit-photos / 1 | 先样张后批量、同组一致性、检查结果 | 自动色调／旋转可能改变原图；小预览不足以验细节 | 分组样张与逐图验收；保真默认保持框架／曝光意图 |
| adobe-create-social-variations / 1 | 比例交付、多种规格、部分成功追踪 | 社媒裁切／生成扩图不适合默认保构图 | 导出与生成分开；改比例需任务授权 |
| adobe-create-mockups / 1 | 真实素材引用、阶段检查 | 场景替换、设计改造属于另一任务 | 取输入角色与阶段检查，跳过场景替换 |
| adobe-design-from-template / 1 | 能力发现、预览与最终导出分别核实 | 模板主题不等于通用忠实重绘 | 取最终文件验证，不自动叠模板 |
| prompt-architect、prompt-optimizer / 2 | 目标、限制、结果格式清楚，删除模糊要求 | 长框架／连续追问／编码任务规则不直接适用于图像 | 一次简短编辑契约；仅关键缺项问用户 |

本地 Skill 是已安装的实际工作流样本，插件能力和具体服务可变；本审查不构成插件当前可用性或运行成功证明。

## 公开仓库：逐类取舍

| 原始来源与入口数 | 吸收 | 修正或排除 |
|---|---|---|
| [OpenAI imagegen](https://github.com/openai/skills/blob/main/skills/.system/imagegen/SKILL.md) / 1 | 输入角色、保留原件、默认工具、显式 fallback | 不从示例模型／尺寸推断当前工具支持；输出仍需独立检查 |
| [Anthropic skills](https://github.com/anthropics/skills) / 3：canvas-design、brand-guidelines、theme-factory | 焦点层级、色彩体系、清晰展示 | 排除品牌强加配色、未经请求的布局重建与固定主题 |
| [Sancerio photo editing](https://github.com/Sancerio/codex-photo-editing-skills) / 4：editing、retouching、upscaling、delivery | 身份保护、原件与候选／母版／导出分离、哈希与文件验证 | 实际掩膜／合成才谈像素保护；插值不会恢复相机细节；不照搬第三方编辑脚本 |
| [fal-ai community](https://github.com/fal-ai-community/skills) / 11 | fal-prompting 的可见事实／单轴修正；character-design 的身份锚点；cinematography 的明确受光；workflow/genmedia 的 schema、节点和交付记录 | 不继承固定端点排名；cinematography 的换镜头／雨雾属于新增范围；网站 redesign 与 3D regenerate 仅筛查，排除出重绘路线 |
| [dancolta gen-images](https://github.com/dancolta/gen-images-skill) / 1 | 先读真实设计上下文、明确图像角色、逐素材提示 | 网站项目假设、框架工具和槽位策略不直接用于上传图片 |
| [teskor image reference fidelity](https://github.com/teskor-hub/chatgpt-imagegen-skill) / 1 | 参考图角色、身份与表情分别检查、失败留档、未知身体细节不猜测 | 人脸／身体替换不是本任务；作者实验不能当独立科研共识或通用成功率；“8K”与重复参考不是已证实权重 |
| [dnesdan imagegen UI prototype](https://github.com/dnesdan/Skills/blob/main/prototype-ui-with-imagegen/SKILL.md) / 1 | 冻结 brief、保留内容地图、生成与实现／验收分开 | UI 元素与原生代码路线不适用于角色画面；不引入默认多方案生成或不必要额外流程 |

fal 的 11 个入口为：fal-workflow、fal-regenerate-3d、fal-prompting、model-routing、genmedia、genmedia-workflow、cinematography、character-design、fal-models-catalog、fal-redesign、fal-recipes。当前上游结构与早期 fal 工具包装仓库不同，按实际入口清单审查，没有把旧名称当成现行 schema。

## 技术依据及推断边界

- [ControlNet 原论文](https://arxiv.org/abs/2302.05543)研究边缘、深度、姿态等空间条件。由此采用的流程建议是：严格结构任务优先检查**实际可用并提供的条件引导**。本 Skill 默认内置编辑没有提供这些条件，文字“锁定”不能冒充它们；论文也未保证我们这套提示词的身份保真。
- [Intrinsic Image Decomposition via Ordinal Shading](https://arxiv.org/abs/2311.12792)区分反射率与阴影估计，并展示重着色、重照明应用。我们据此采用“材质色与照明分开描述”的概念，尤其适合当前过饱和问题；本项目未运行该算法或恢复真实反射率。
- [InstructPix2Pix](https://arxiv.org/abs/2211.09800)提供指令式图像编辑研究背景，支持把任务写成具体变更指令；其结果不等于当前内置编辑器的质量证明。
- [Adobe Vibrance 文档](https://helpx.adobe.com/ie/photoshop/using/adjust-vibrance.html)说明真实色彩调整工具中的自然饱和度和饱和度处理。我们的提示词采用“原图色彩强度、肤色／中性色、局部色溢出”检查；没有把 Adobe 数值或保护效果虚构为生成工具参数。

以上是技术概念和工作流参考。没有找到可把社区应用同名旋钮数值直接迁移到所有生成模型的科学通用标定；本版本因此不给所谓权威的通用 DLSS5 科研参数。

## v3 最终改进

1. 将风格落在光源关系、接触阴影、材质响应和局部光晕上，删除用新场景／纹理逼出差距的做法。
2. 深度档提高光影幅度；色彩、内容和介质保护与正常档相同。
3. 逐图冻结输入角色与保留内容；照片／动漫／CG／海报分别适配。
4. 四项独立验收，颜色问题与清晰度问题单独记录。
5. 每次修正回原件，只改已诊断问题，最多两次；避免生成链条累积漂移。
6. 比较图自动化，但美学判断保持人工／助手实看；记录实际尺寸、哈希和控制项。
7. 照片、批次与视频路线条件化，静帧成功不会升级成全局实时或时间稳定承诺。

文档和工具链完整性已单独检查。视觉证据及缺口见 [validation-v3.md](validation-v3.md)，需求追踪见 [requirements.md](requirements.md)。这是完整执行版本，通用画质成功率仍需更广泛的真实输入验证。

## v4 method correction — 2026-09-30

Latest user request selects traditional Photoshop-style color/tonal layers and local masks, with minimal direct generative redraw. This supersedes v3's built-in generative default. The skill-creator practices retained are concise routing, real capabilities, executable helper validation and evidence separated from aesthetic approval.

Adopt Adobe adjustment layers and masked Curves/dodge-burn as the execution model. Keep Normal/Deep as intensity levels, source-chroma restraint and four-gate inspection. Generation is explicit opt-in; no missing-tool fallback to synthesis. Optional segmentation proposes selections only. PSD claims require an actual layered file; the local helper outputs JSON, masks and PNG steps. Broad example ellipses and RGB math are approximations, not calibrated Photoshop/PBR reconstruction.

Primary sources checked in this revision: [Adobe adjustment layers](https://helpx.adobe.com/au/photoshop/desktop/create-manage-layers/color-adjustment-fill-layers/work-with-adjustment-and-fill-layers.html), [Adobe masked Curves](https://www.adobe.com/learn/photoshop/web/lighten-darken-photos-with-curves). Prior local/public Skill inventory remains the dated v3 audit, not a new exhaustive internet survey.
