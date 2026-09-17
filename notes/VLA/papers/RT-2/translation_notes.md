# Translation notes — RT-2 (arXiv:2307.15818v1)

## 源文件与处理方式

- **源文件：** `raw/2307.15818v1.pdf`（arXiv:2307.15818v1 [cs.RO]，2023-07-28，26 页，A4，可选文本 PDF，pdfTeX 生成，未加密）。
- **文本提取：** Poppler `pdftotext -layout`（逐页，用于核对行序与空格）+ `pdfplumber`（用于段落边界、字号/粗体判定与图形对象包围盒）。
  段落边界由「行距 + 字号 + 粗体 + 首行缩进」共同判定，不采用单一空白行切分。
- **粗体判定：** 按行内字符的多数投票决定（`XCharter-Bold` 占比 > 60%），避免行内加粗术语（如 `RT-1`、`VC-1`）被误判为段首小标题；
  论文中真正的段首小标题（`Co-Fine-Tuning.`、`Output Constraint.`、`Baselines.`、`Open Source Language Table Benchmark.`、
  `Qualitative Evaluations.`、`Quantitative Evaluations.`）按加粗 run 的起始位置单独切分为新段落。
- **版面噪声过滤：** 每页页眉（“RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control”）、
  页码、页脚版权行（“© 2023 Google DeepMind. All rights reserved”）与通讯作者行，以及左侧旋转 90° 的 arXiv 页边标记
  （`arXiv:2307.15818v1 [cs.RO] 28 Jul 2023`）均被显式过滤，不进入正文区块。
- **图表提取：** 未整页截图。先用 `pdfplumber` 取图形对象包围盒，再用 300 dpi 渲染 + **像素墨迹分析**（`tight_bbox.py`）
  取可见内容的紧致包围盒，最后统一外扩 3 pt 作为安全边距；裁剪脚本为 `tmp/reader_rt2/crop_assets.py`（含全部 16 个裁剪框坐标）。

## 翻译原则与取舍

1. **段落级直译优先。** 保留原段落边界、证据链与限定语（`suggesting`、`seems to`、`we hypothesize` 等），不合并、不摘要化、
   不改写为要点列表。段落顺序与原文一致，唯一的顺序调整是：图与表按其**首次实质性提及处**插入（跨页图注仍标注其在 PDF 中的源页）。
2. **术语保真。** 专有名词一律保留英文原名（`RT-2`、`RT-2-PaLI-X`、`RT-2-PaLM-E`、`PaLI-X`、`PaLM-E`、`VLA`、`VLM`、
   `co-fine-tuning`、`Language-Table`、`MOO`、`VC-1`、`R3M`、`WebLI`、`token`、`rollout` 等），首次出现时给出中文说明；
   系统术语采用领域通行译法，见 `paper.md` 的术语表。
3. **公式与数值。** PDF 中的行内数学无法按线性文本可靠还原（下标、希腊字母、尖括号常被拆成独立文本块）。
   对这类位置，`**Original:**` 以行内形式重建：动作串写作 `Δpos_x Δpos_y Δpos_z Δrot_x Δrot_y Δrot_z`；
   附录 D 中的 `n × k`、`⟨ lang ⟩` 等沿用 PDF 中的数学斜体字符。所有数值、百分比、学习率、批大小与梯度步数按原样保留。
4. **跨页段落合并。** 论文有 7 处段落被分页截断，本稿按语义合并为单一区块，并在 `**Source:**` 中标注跨页范围。
   涉及区块见下方“跨页合并一览”。
5. **列表结构。** 4 节开头的四个研究问题、附录 A 的贡献分组、附录 C 的四条基线说明、附录 G 的四条失败类型，
   在原文中即为列表，本稿保留其列表形态（逐条编号或加 `-`），未改写为连续散文。
6. **参考文献。** 73 条书目条目保留英文原文（书目信息不译），序号为本阅读稿按原文顺序重排；条目文本由 PDF 文本层重建。
7. **图表转录。** 表 1、表 2、表 3、表 4、表 5、表 6 均在紧致裁剪图之外附一份 Markdown 转录，便于检索与复制数值；
   多层级表头（表 4/表 5/表 6 的分组列与 Easy/Hard 子列）在转录表中以列名展平表示，并在表下注明原表结构。

## 跨页合并一览

| 区块 | 合并的 PDF 页 | 说明 |
|---|---|---|
| S003 | p.1–p.2 | 引言第 1 段被分页截断（“However,” → “it is unclear…”） |
| S008 | p.3–p.4 | 相关工作（机器人学习中的泛化）段落跨页 |
| S013 | p.4–p.5 | 3.1 节段落跨页 |
| S015 | p.5–p.6 | 3.2 节段落跨页（“This requires” → “reserving 256 tokens…”） |
| S038 | p.8–p.9 | 4.2 节首段跨页 |
| S051 | p.11–p.12 | 结论段落跨页（“…inherited from” → “web-scale vision-language pretraining.”） |
| S063 | p.19–p.20 | 附录 B 机器人数据集段落跨页 |
| S072 | p.20–p.21 | 附录 D PaLI-X 架构段落跨页 |

## 已知不确定项与提取风险

| 位置 | 问题 | 处理方式 |
|---|---|---|
| p.6 动作串公式（S016） | 下标字符（`x y z`）在 PDF 文本层被拆成独立文本块，与主行分离 | 按行内公式重建为 `Δpos_x … Δrot_z`，并在区块下加说明；该区块的字符级覆盖率为 0（已标注） |
| p.9 图 5 与表 1 的图注 | 该页顶部为双栏排布，两条图注在文本层被合并为一个文本块 | 按栏位 x 坐标拆分为两条图注，并恢复被分栏吞掉的 `|` 分隔符；表 1 图注中的 `Ser-manet` 连字断字已复原为 `Sermanet` |
| p.7 图 3、p.10 图 6 的子图注 | 两栏子图注在文本层合并成一行 | 未强行拆分，而是把子图注**保留在图像裁剪内**（面板标识属于与图不可分割的部分），正文中不重复 |
| p.11 图 7、p.23 图 9、p.25 图 10 | 图形对象包围盒包含不可见的透明占位区域（图 9 的占位框位于 y 305.7–368.6，而可见内容从 y 391.1 开始，其上方实际是正文与项目符号列表） | 一律以**像素墨迹包围盒**为准确定裁剪框，并用 `check_crops.py` 反查框内是否混入 ≥9.5 pt 的正文行 |
| p.2 图 1 背景矩形 | 该页存在一个横向超出页宽（x 22.8–642.9）的填充矩形对象，属于版式残留 | 裁剪框按可见内容（x 65.8–529.7）确定，未包含该残留对象 |
| 全篇行内数学 | PDF 使用 `txsys` / `CharterMathMI` / `CharterMathRM` 字体，部分符号（∈、∼、×、上下标）提取后与正文粘连 | 相关位置以 Unicode 数学字符或行内形式重建；不改变数学含义 |
| p.13–p.18 参考文献 | 条目被 `pdfplumber` 按行切块，续行缩进不一；个别 URL/DOI 前后残留换行 | 按空白块与缩进重建为 73 条，已修补连字断字；仍可能残留个别空格差异，不影响检索 |
| p.19 附录 A | 贡献分组的加粗角色名与续行被拆成 3 个文本块（如 “Training and Evaluations (…, evalu-” + “ating models …”） | 逐组合并并复原连字断字（`evalu-` + `ating` → `evaluating`），重建为 6 个分组 |
| p.20 附录 C | 四条基线说明在文本层被合并成一个大块，且模型名在加粗 run 与正文中重复出现（“RT-1 : Robotics Transformer 1 …”） | 按 `• RT-1 / VC-1 / R3M / MOO` 标记切分为四条，并规范化冒号前的空格 |
| 正文固有笔误 | 见下方“原文笔误清单” | 逐处加注，不擅自改动原文语义 |

## 原文笔误清单（照录，不做静默修正）

| 位置 | 原文 | 说明 |
|---|---|---|
| S036（p.8） | “qualitative real-world out-of-distribution behaviors behaviors in Figure 5” | `behaviors` 重复 |
| S040（p.9） | “We' split the emergent capabilities” | 应为 `We split`，撇号多余 |
| S078（p.21） | “quantiative evalution” | 应为 `quantitative evaluation` |
| 表 3 图注（p.22） | “quantitative emergent evalutions” | 应为 `evaluations` |
| 表 2 图注（p.26） | “A visualization of these scenarios if shown in Figure 3” | 应为 `is shown` |
| S063（p.19） | 七种技能列举了 8 项（含 “Pick Object ” 与 “Pick Object from Receptacle…”） | 原文如此，未做增删 |
| S040（p.9） | “the smaller PaLM-E-based model has an edge on tasks that involve math reasoning” 与表 5 的 Math 列（25 vs 35）一致 | 已核对，非笔误 |
| 表 4（p.23） | “RT-2-PaLM-E-12B 1 (ours)” 上标 1 | 脚注正文见本稿 S091（位于 p.24） |

## 覆盖度自检（对照 skill 的 Output Contract）

- `paper.md` 含 **69** 组 `**Original:** …` + `**中文:** …` 配对（对应 97 个源区块中的全部正文类区块；其余 28 个为章节标题区块，单独以
  `## 标题 ｜ 中文标题` 形式给出）。无未翻译的实质性正文段落。
- 覆盖 p.1–p.26 全部页面：p.1–p.12 正文与结论，p.13–p.18 参考文献（单一锚点 `R001`），p.19–p.26 附录 A–I。
  纯图页（p.22 上半、p.25、p.26）与其图/表区块一一对应，无遗漏正文内容。
- **10 张图 + 6 张表**全部有 `assets/*.png` 紧致裁剪图、原图注、中文图注与阅读提示；`assets/` 中 16 个文件全部被 `paper.md` 引用，无孤立文件。
- 表 1–表 6 均附 Markdown 转录；`source_map.json` 为合法 JSON，包含 `paper / blocks / figures / tables / reference_section` 五部分，
  区块 ID 与 `paper.md` 锚点一一对应（97 个区块 + 16 个图表锚点）。
- 页面索引覆盖 p.1–p.26，含跨页区块的双页登记与“本页含 Fig./Table”提示。

## 未纳入本阅读稿的内容

- **补充视频与项目网站内容**（robotics-transformer2.github.io 上的执行视频、`robotics-transformer2` 项目页）不在 PDF 内，未纳入。
- **RT-2 未开源代码**（论文未提供代码仓库链接，仅在致谢与贡献中提及内部基础设施），未做代码级核验。
- 本阅读稿为**离线阅读稿**，未生成 `reader.html`（浏览器预览版）——如需，可在此基础上追加。

## 构建产物（可复现）

构建脚本与中间产物位于 `tmp/reader_rt2/`：

- `inspect_layout.py` / `geometry.py` / `build_blocks.py` / `block_index.txt` — 版面对象、字号与段落结构重建
- `tight_bbox.py` / `ink_profile.py` / `check_crops.py` / `border_check.py` — 墨迹包围盒测定与裁剪校验
- `crop_assets.py` — 16 个图表裁剪（含坐标表）
- `make_source_blocks.py` / `source_blocks.json` — 正文区块与结构修正（分段、跨页合并、附录重建）
- `make_captions.py` / `captions.json` — 图注提取（含 p.9 双栏图注拆分）
- `build_refs.py` / `references.md` — 参考文献重建
- `zh_01.json`–`zh_05.json` / `zh_captions.py` — 中文译文（正文分片与图表注）
- `build_reader.py` — 组装 `paper.md`、页面索引与 `source_map.json`
- `verify_reader.py` — 逐区块回查原文（字符 n-gram 覆盖率）与锚点/资源一致性检查
