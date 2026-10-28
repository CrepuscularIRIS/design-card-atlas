# 低彩分灰阶

分组：色彩 · 主维度：B 低饱和、A 明暗层级、C 大色块、E 表面差、F 远层 · 情绪：肃穆、清冷

## 一句话

减少色相竞争，让暗壁、灰天、亮水各占一个明度层，画面仍能有重量。

[![黑沙之境 · 海岸全景](shots/02.jpg)](shots/02.jpg)
[黑沙之境 · 海岸全景](https://github.com/Zp-Peter/kimi-k31pro-opus55-benchmark-showcase/blob/65e82c53b63f2fdd918617269c057d8e53af2c6f/kimi/iceland-black-sand/dist/index.html) · 灰天、灰海与黑柱壁分出层级，低彩并没有抹掉地理关系。

| 参考 | 参考 |
|---|---|
| [![雷尼斯黑沙滩 · 海滩](shots/01.jpg)](shots/01.jpg) | [![中式幻想 RPG · 雾中巨像](shots/03.jpg)](shots/03.jpg) |
| [雷尼斯黑沙滩 · 海滩](https://github.com/Zp-Peter/kimi-k31pro-opus55-benchmark-showcase/blob/65e82c53b63f2fdd918617269c057d8e53af2c6f/opus/reynisfjara/index.html) · 黑壁与干沙占大暗块，湿沙银带成为主要亮部。 | [中式幻想 RPG · 雾中巨像](https://skillry.dev/ai-videos/kimi-k3-1/crangerus-549203) · 灰绿近像与淡雾分层，最深的舟棚为全图定黑位。 |
## 看哪里

1. 黑沙之境 · 海岸全景：灰天、灰海与黑柱壁分出层级，低彩并没有抹掉地理关系。
2. 雷尼斯黑沙滩 · 海滩：黑壁与干沙占大暗块，湿沙银带成为主要亮部。
3. 中式幻想 RPG · 雾中巨像：灰绿近像与淡雾分层，最深的舟棚为全图定黑位。

## 拆解

色值与比例为目估，不等于原作调色参数。

- **B · 色相**：黑沙图主色近`#20272A`、中灰`#667275`、天光`#ADB7B6`；巨像稍偏灰绿。色相少，但不是简单一键去色。
- **A · 明度**：Opus海岸左壁和下部干沙组成大暗区，右侧水与湿带给亮层，远海为中灰。三层的大面积关系比小纹理更先被看见。
- **C · 面积**：海岸暗色约占半幅以上，亮天与湿带并不均分画面；巨像图中央亮口约1/4宽，两边暗块把它夹住。
- **E · 材质差**：黑沙哑光、湿沙带软反光、海面有小白浪；同一冷灰调里靠反射形状区别物质，不能把所有材质设成相同灰塑料。
- **F · 远近**：远礁比近柱壁浅，海平线反差弱；空气让远处进入中灰，而非增加另一种抢眼颜色。

## 做法

先排黑、灰、亮三个大块，再调色。保留表面原本的细微色差，不用全屏高对比滤镜代替照明。

- **迁移构图预算**：先试暗部50–65%、中调25–40%、高亮5–10%；面积是调整起点，不是硬性评分。亮水带最多承担一个主要视线方向。
- **校验**：400px预览中若壁、地、水黏在一起，优先调受光/粗糙度/机位，再提高饱和度。

### 实现索引

2026-10-28 源码阅读补索引；不新增截图、不改上方视觉判断。上方“不能由截图推出/尚未审 shader”等界限指原视觉阶段，本节另列本批核过的源码。`Repos/` 相对 `~/Blog/`，Citadel 路径相对 `~/Blog/citadel/`。本批未运行这些源码测量参数，标为“源码”的值不得当作实测。

| 作品 | 源码（本地路径:行） | 技术与接入边界 | 参数（来源） | 许可 / 复用档 | Citadel 已有可复用入口 |
|---|---|---|---|---|---|
| 黑沙之境 · 海岸全景 | `Repos/kimi-k31pro-opus55-benchmark-showcase/kimi/iceland-black-sand/src/iceland/atmosphere.js:76-85,181-213` | 冷灰天空、雾与有色填光分开设置，再与暗岩/亮水材质分工；不是全屏一键去色。Citadel lab/src/core/post.js:334-340 具 exposure/lift/gain/contrast/saturation，但应先在 platform-1 或 hospital-1 分配暗体、中灰背景、少量亮窗，再用 grade 收束；适配待验证。 | sky zenith / horizon=0x3f505b / 0xa3adae（源码）；fog color / density=0x8e9b9e / 0.0039（源码）；hemi intensity / sun intensity=1.55 / 1.65（源码）；dark / mid / bright area=50–65% / 25–40% / 5–10%（建议迁移值） | 未发现仓库根 LICENSE；作品代码授权待验证，只借手法，不复制代码/资产 / borrow | `lab/src/core/post.js` |
| 雷尼斯黑沙滩 · 海滩 | `Repos/kimi-k31pro-opus55-benchmark-showcase/opus/reynisfjara/src/config.js:41-50` | overcast 以近邻冷灰配置天空/云/雾并保留暗云层；Repos/kimi-k31pro-opus55-benchmark-showcase/opus/reynisfjara/src/world/beach.js:75-98 按真实岸线区分湿带/浪区，支持地、水的不同表面角色；这里不是仅降 saturation 就生成银带的承诺。Citadel lab/src/core/post.js:334-340 收尾，材质与受光仍须逐面组织。 | overcast zenith / horizon linear RGB=[0.6,0.63,0.68] / [0.7,0.72,0.75]（源码）；cloudDark linear RGB=[0.33,0.35,0.39]（源码）；overcast fogDensity / exposure=0.00042 / 1.0（源码） | 未发现仓库根 LICENSE；作品代码授权待验证，只借手法，不复制代码/资产 / borrow | `lab/src/core/post.js` |
| 中式幻想 RPG · 雾中巨像 | `none` | 原作源码未定位，许可待验证；邻接技术源 Repos/kimi-k31pro-opus55-benchmark-showcase/opus/reynisfjara/src/config.js:41-50：借近邻灰色天空与深浅雾层的分工，在 hospital-b 或 Platform 先排三档明度；不声称原片雾/材质参数或生成方式已知，grade 不能替代暗舟/灰像/亮背景的空间摆放；不是原作实现，画面一致性待验证。 | dark / mid / bright area=50–65% / 25–40% / 5–10%（建议迁移值） | 原作待验证；邻接源 未发现根 LICENSE，只借手法，原作资产不可据此复制 / reference | `lab/src/core/post.js` |

本卡为高频补索引项，非匹配表直接命中。队列可评估 hospital-1 / hospital-b 或 platform-1 的灰阶秩序；这里只给宿主与试验路线，不宣称已有场景缺陷或完成态。

源码快照（本批读取，不是新增截图来源）：
- `kimi-k31pro-opus55-benchmark-showcase@65e82c53b63f2fdd918617269c057d8e53af2c6f`

已检索 `citadel/src`（含 `src/world/worlds/`）与 `lab/src`；本批未发现 `src/world/worlds/cardfx/` 目录或本卡同名预制模块。以上入口只表示可复用部分；首次完整落地才由执行者沉淀 cardfx，不在此虚构文件。title / atlas locked，任何队列用途均不解除锁定。

## 迁移到博客

BlackCityHall登记场景可用深灰体块与冷灰天空组织门厅外观；Beach方案用湿沙亮带作引导。保持2D人物衣饰能从环境里分离，不把人物也染成灰。

搭配侧光刻石、镜面邻粗面；与每面墙同时上彩色霓虹冲突。如果必须加提示灯，限制为一处小面积点缀，不改变三层明度主体。

## 反例

Sponza说明低饱和不自动产生高级感：中间调丢失后，材质和纵深一起丢失。此对照针对本次取景和曝光，不评价项目全部能力。


[![Sponza · 本次偏暗机位](shots/04.png)](shots/04.png)
[Sponza · 本次偏暗机位](https://three-good-godrays.ameo.design/#sponza) · 几种表面都沉到同一暗值，低彩失去中间调就会只剩黑块。

[逐图来源与复现](SOURCE.md) · [返回视觉卡库](../../../README.md)
