# Pixelle-Video 本地自托管模型资产与自媒体 IP 风格指南

本指南用于记录您本地已安装的 AI 绘图与视频模型资产，深入解析如何利用这些模型风格来打造您**专升本（升学备考）自媒体账号的独特个人 IP**，并提供专属 HTML 视频模板的调用指南，帮助您提升视频完播率与粉丝粘性。

---

## 📂 第一部分：已安装的本地模型资产清单

以下是您 Windows 本地已成功部署的全部模型资产及其对应的存放路径。文档中已清空所有临时下载链接，保持视觉规范的纯净。

### 🎨 1. FLUX.1 高画质生图模型（用于生成第一帧静态图）

| 序号 | 模型类型 | 文件名 (重命名后) | 存入文件夹 (ComfyUI 根目录下) | 资产用途与调用说明 |
| :--- | :--- | :--- | :--- | :--- |
| 1 | **大模型 (UNET)** | `flux1-dev.safetensors` | `ComfyUI\models\unet\` | FLUX 核心扩散大模型（fp8量化版，负责画面常识与骨架） |
| 2 | **画图 VAE** | `ae.safetensors` | `ComfyUI\models\vae\` | FLUX 专属 VAE 编码器，负责最终画面的高清还原 |
| 3 | **CLIP 文本1** | `clip_l.safetensors` | `ComfyUI\models\clip\` | 轻量级文本特征提取器，处理基础提示词 |
| 4 | **CLIP 文本2** | `t5xxl_fp8_e4m3fn.safetensors` | `ComfyUI\models\clip\` | T5 大型文本特征提取器，提供超强的提示词深度理解 |

### 🎬 2. Wan 2.1 高画质视频生成模型（用于将静图转为高动效视频）

| 序号 | 模型类型 | 文件名 (重命名后) | 存入文件夹 (ComfyUI 根目录下) | 资产用途与调用说明 |
| :--- | :--- | :--- | :--- | :--- |
| 5 | **视频大模型 (UNET)**| `WanT2V_MasterModel.safetensors` | `ComfyUI\models\unet\wan-fusionx\` | Wan 2.1 视频大模型（1.3B 轻量版，负责赋予画面动作与动效） |
| 6 | **视频 VAE** | `wan_2.1_vae.safetensors` | `ComfyUI\models\vae\` | 视频专属 VAE 编解码器 |
| 7 | **视频 CLIP** | `umt5_xxl_fp8_e4m3fn_scaled.safetensors`| `ComfyUI\models\clip\` | 视频专属 T5 量化文本编码器，处理复杂的视频动效指令 |

### 🎀 3. 专属风格化 LoRA 资产

| 序号 | 风格方案 | LoRA 文件名 | 存入文件夹 | 触发词 (Trigger Words) |
| :--- | :--- | :--- | :--- | :--- |
| 8 | **扁平矢量科普** | `flux1_dev_lora_vector_illustration.safetensors` | `ComfyUI\models\loras\` | `vector, vector illustration, flat illustration` |
| 9 | **Q版粘土盲盒** | `flux_claymation.safetensors` | `ComfyUI\models\loras\` | `Claymation` |
| 10 | **日系治愈动漫** | `flux_ghibli.safetensors` | `ComfyUI\models\loras\` | `Ghibli Art` |

---

## 🚀 第二部分：模型风格在专升本自媒体 IP 打造中的核心价值

对于面临巨大升学和备考压力的专科在校生（18-22岁群体），视频的**视觉调性**直接决定了他们对您的“第一印象信任感”和“情感粘性”。以下是这 4 种风格模型在您个人 IP 塑造上的深度赋能：

### 🎯 方案一：扁平矢量科普风 ➡️ 塑造【专业、硬核、高效的“提分学霸”IP】
*   **IP 打造帮助**：
    这种极简扁平的矢量画风（常用于回形针等科普视频）自带**“高智商、科学性、高可信度”**的视觉滤镜。对于专升本英语语法、高数公式这类枯燥的纯知识点复习视频，该画风可以让背景极其干净清爽，将学生的注意力 100% 聚焦在您打出的板书和干货文字上，大大提升完播率，建立起您作为**“提分干货博主”**的专业人设。

### 🧸 方案二：Q版粘土盲盒风 ➡️ 塑造【温和、接地气、陪伴式的“学长学姐”IP】
*   **IP 打造帮助**：
    20岁左右的大学生对“潮玩、盲盒、Q版3D人物”有着天然的偏爱。您可以用此风格生成一个专属的可爱3D粘土人物，作为您账号的**“虚拟代言人”**。当做备考建议或梳理备考日常时，背景上配着这个软萌的粘土小人或在书桌前拼搏、或在收到录取通知书时为之欢呼，能传递出极强的亲和力与减压感，极易收获年轻粉丝的喜爱。

### 🍃 方案三：日系治愈动漫风 ➡️ 塑造【懂情感共鸣、温暖陪伴的“深夜自习室”IP】
*   **IP 打造帮助**：
    专升本备考是一个充满孤独、焦虑的过程。选用类似吉卜力电影《侧耳倾听》或新海诚电影里的“午后洒满阳光的自修室”、“深夜台灯下的奋笔疾书”作为背景，会瞬间勾起考生的**情感共鸣与陪伴感**。在分享备战心态、学长姐经验、励志鸡汤时使用，极易触动考生心底的弦，从而引爆评论区的互动，获得**极高的评论率与收藏转发率**。

### 💻 方案四：科幻全息数据风 ➡️ 塑造【客观、官方、具备绝对权威的“报考政策专家”IP】
*   **IP 打造帮助**：
    在做“公办招生计划缩减”、“报考率对比”、“分数线变化”等重要政策解读时，必须彰显账号的**严肃度与绝对权威性**。通过 FLUX 原生大模型生成的科幻冷蓝色调、全息数码折线图与柱状图看板，会让画面充斥着“官方数据中心发布”的质感，直接拉满您作为**“专升本报考政策权威分析师”**的客观人设。

---

## 📈 第三部分：专升本视频风格搭配黄金公式与提示词范例

为了方便您在日常写完文案后秒出配套提示词，特为您梳理了这三种日常视频场景的无脑套用公式：

### 📊 公式一：纯知识点复习（高数定理/英语语法/专业课干货）➡️ **方案一：扁平矢量风**
*   **画面宗旨**：明亮、清爽、干净、突出文字板书。
*   **提示词公式**：`flat illustration, vector art, minimalist, vibrant gradient background, [画面主体], clean white lines`
*   **提示词范例**：`flat illustration, vector art, minimalist, vibrant warm yellow and orange gradient background, a neat study desk with an open textbook showing mathematics formula, a modern desk organizer, clean white lines`

### 🕯️ 公式二：励志鸡汤/备考日常心路历程/解压碎碎念 ➡️ **方案三：日系治愈动漫风**
*   **画面宗旨**：温暖、治愈、强光影、注重氛围和情绪传递。
*   **提示词公式**：`cozy anime style, Ghibli aesthetic, warm lighting, [画面主体], peaceful and emotional atmosphere`
*   **提示词范例**：`cozy anime style, Ghibli aesthetic, a warm desk lamp lighting up a college student writing in a notebook at night, soft shadows, steam rising from a hot mug, nostalgic and emotional study atmosphere`

### 📊 公式三：报考政策政策播报/录取名额变化/分数线趋势分析 ➡️ **方案四：科幻全息数据风**
*   **画面宗旨**：专业、客观、数码、高对比度科技图表。（**注意：无需加载任何 LoRA**）
*   **提示词公式**：`minimalist tech illustration, abstract digital hologram of growing charts and data, cyber blue grid background, professional data display`
*   **提示词范例**：`minimalist tech illustration, a glowing 3D holographic bar chart showing upward growth trend, neon blue and violet lines, clean digital grid background, high-tech information display`

---

## 🎥 第四部分：镜头动效与 Wan 2.1 运镜联动

在使用 **Wan 2.1** 视频模型时，通过合理的镜头提示词，可以让视频画面动起来得极其生动且自然：

*   **平滑侧移（横向缓缓平移镜头，最适合展示自习室或桌面的安静质感）**：
    > `camera panning left/right slowly, smooth motion`
*   **镜头微调/微微拉近（常用于情绪渲染，突出主角正在思考或努力）**：
    > `slow camera zoom in, focusing on the character's facial expression`
*   **微风/暖光闪烁等细节动效（画面最稳健，不易产生杂波或崩坏）**：
    > `the wind blowing, hair gently swaying, subtle facial movement, warm desk lamp lights flickering softly`

---

## 🖥️ 第五部分：专升本专属 HTML 视频帧渲染模板调用指南

为了让您的视频在图片之外，文字、板书、品牌签名等也达到千万级大 V 的高阶质感，项目已在 `templates/1080x1920/`（竖屏格式）中为您内置了两个顶级设计的 HTML 渲染模板。

### 📕 1. 考点知识卡片模板：`image_zsb_knowledge.html`

*   **视觉优势**：
    深沉极光暗墨绿背景搭配金色拉丝拉花相框与磨砂玻璃文字卡片，极度彰显学术沉淀感与知识含金量，与**方案一（扁平矢量 LoRA）**是天然绝配。
*   **适用视频场景**：
    高数公式推导、英语词汇速记、专业课必背考点、每日打卡学习等。
*   **文案脚本对应的 HTML 变量参数**：
    *   `{{countdown}}` ➡️ 顶部左侧徽章（如：*江西专升本 • 核心考点* / *备考倒计时 30 天*）
    *   `{{category}}` ➡️ 顶部右侧学科徽章（如：*高等数学* / *公共英语*）
    *   `{{title}}` ➡️ 本帧考点核心标题
    *   `{{text}}` ➡️ 详细考点正文解析内容
    *   `{{image}}` ➡️ 本帧对应的 AI 生成高清图片（由 FLUX 自动生成）
    *   `{{author}}` ➡️ 您的自媒体品牌名字（默认已设为：*壹格专升本*）

### 📢 2. 政策速递大屏模板：`static_zsb_consult.html`

*   **视觉优势**：
    玫瑰红与极光橙的动感红润流光背景，配上巨大的磨砂玻璃通栏卡片。正文中的核心重点和数字会自动带有**黄色下划线高亮显示**，极富官方速报与头条的即时可信度。
*   **适用视频场景**：
    报考政策突发播报、招生名额变化对比、公办民办分数线对比长文、备考指南等字数较多的视频。
*   **文案脚本对应的 HTML 变量参数**：
    *   `{{badge}}` ➡️ 顶部亮眼小标题徽章（如：*政策速递* / *报考必看*）
    *   `{{title}}` ➡️ 本次播报的加粗大标题
    *   `{{text}}` ➡️ 详细的报考政策解读长文
    *   `{{slogan}}` ➡️ 底部签名小口号（默认已设为：*祝您再上一格 • 一站式上岸*）
    *   `{{author}}` ➡️ 您的自媒体品牌名字（默认已设为：*壹格专升本*）

---

## ⚙️ 第六部分：一键备份与后续维护提醒

1.  **多端共享模型**：
    如果您以后需要在别的 ComfyUI 整合包中使用这套模型，或者希望节省 Windows 硬盘空间，可以编辑 `ComfyUI/extra_model_paths.yaml`，指定您其他 Stable Diffusion/WebUI 软件所在的根目录，即可自动共享模型。
2.  **IP 改变快速恢复**：
    项目内的 `config.yaml` 已经将本地 Windows ComfyUI 的连接地址（如 `192.168.101.19:8188`）记录。当您的路由器重启、Windows 本地 IP 改变时，只需要编辑 `config.yaml` 中的 `comfyui_url` 即可秒速恢复连接！
