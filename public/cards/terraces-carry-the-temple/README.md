# 阶台托举主殿

分组：造型尺度 · 主维度：D 层台与主殿、C 路径层级、A 面转折、G 视点、I 仪式感 · 情绪：庄严、攀登

## 一句话

用宽台、细阶和最高处主殿组成逐级上升的体量，庄严感来自可读的攀登关系。

[![Athenaion · 水庭](shots/03.jpg)](shots/03.jpg)
[Athenaion · 水庭](https://github.com/Leonxlnx/athenaion) · 水庭、环廊、中央高台再到后殿，让高度关系拥有前景起点。

| 参考 | 参考 |
|---|---|
| [![Athenaion · Grand staircase](shots/01.jpg)](shots/01.jpg) | [![Athenaion · Panorama](shots/02.jpg)](shots/02.jpg) |
| [Athenaion · Grand staircase](https://github.com/Leonxlnx/athenaion) · 近阶宽面一路抬向高处主殿，平台停顿打断机械等距。 | [Athenaion · Panorama](https://github.com/Leonxlnx/athenaion) · 城镇低层台阶为高处主殿提供基底，民居与巨像不是同一高度。 |
## 看哪里

1. Athenaion · 水庭：水庭、环廊、中央高台再到后殿，让高度关系拥有前景起点。
2. Athenaion · Grand staircase：近阶宽面一路抬向高处主殿，平台停顿打断机械等距。
3. Athenaion · Panorama：城镇低层台阶为高处主殿提供基底，民居与巨像不是同一高度。

## 拆解

本卡三张正例来自Athenaion同一作品的三个机位；不计作三个独立来源。比例为图像估计。

- **D · 三级体块**：阶梯图先读到下部宽梯、中部平台、右上主殿；小台阶数量虽多，大块只保持三四级。细级重复不能替代宽平台。
- **C · 路径**：阶梯边线由下部向右上收束，平台的水平转折让视线停一下再上升；水庭视图用前方低水面说明第一层高度。
- **A · 转折**：踏面亮、踢面暗，宽平台受光面积更大。若所有阶面一样亮，级差就会退成条纹贴图。
- **G · 视点**：楼梯机位FOV42°、水庭28.5°来自原作shots.js；一张靠近读步级，一张退远读整体。这些数值不应不经场景尺度换算地复制。
- **I · 节奏**：最终主殿放在层台之上而非第一步旁边，使“到达”有预期。下部草、裂角只作小尺度细节，不抢主路。

## 做法

先画主殿的高度和能通达它的三段大关系，再细分台阶。步级宽高还应满足实际角色与相机通行，不为构图做成无法站立的陡坡。

- **源码机位**：[Athenaion shots](https://github.com/Leonxlnx/athenaion/blob/9b8bd23b39c458a50fb1201037360047781c45b5/src/world/shots.js)。原作高质量静帧不等同本轮runtime表现。
- **迁移试验**：宽平台与连续细阶交替；先用约3级大平台读懂上升关系，再补小步级。数量是层级起点，不是强制规格。

### 实现索引

以下是源码阅读索引，不把邻接技术源说成原作实现，也不把现有基础组件说成整卡已落地。`Repos/` 相对 `~/Blog/`；`citadel` 列相对 `~/Blog/citadel/`。参数逐项标明来源，未做本轮运行测量。

| 作品 | 源码（本地路径:行） | 技术与接入边界 | 参数（来源） | 许可 / 复用档 | Citadel 已有可复用入口 |
|---|---|---|---|---|---|
| Athenaion · 水庭 / Grand staircase / Panorama（同一作品三机位） | `Repos/athenaion/src/acropolis/stair.js:41-129` | planStair 按地形层台拆分梯段/休息平台，buildStair 实际发射阶梯、平台及承台；米制配置在 src/world/layout.js:37-68,100-110，主殿中心在:73-81，机位在 src/world/shots.js:5-10（全景）、11-14（水庭）、27-30（大阶梯）。需结合地形 levels 和建造依赖迁移，不能把台阶纹理当层台。 | acropolis top=54（源码）；terrace drops=12 / 12 / 11 / 10（源码）；riser / tread=0.23 / 0.33（源码）；landing / midLanding=7 / 2.8（源码）；flightRise=8.5（源码）；stair widths=12 / 14 / 16 / 18 / 21（源码） | MIT（LICENSE:1-21） / integrate | `none` |

本批面向 CompanyMeetingroom 的基座/入口高差关系提案，不是给房间塞整座神殿；没有确认对应 cardfx，citadel=none。碰撞、可通行坡度与现有空间容积需先验证。

源码快照（2026-10-28 阅读；不是新增截图来源）：
- `athenaion@9b8bd23b39c458a50fb1201037360047781c45b5`

已检索 `citadel/src` 及 `src/world/worlds/cardfx/`；本批未发现这些卡的同名预制模块。未来首次落地时才由执行者沉淀 `src/world/worlds/cardfx/terraces-carry-the-temple.js`，此处不是已有文件承诺。

## 迁移到博客

Shrine入口可先明确水/地面、第一平台、主门三个高度；BlackCityHall给厚门厅一个足够宽的基座。人物仍在2D层呈现，背景透视与角色脚部的接地位置需单独验收。

搭配侧光刻石、风化依附形体；与全场浓雾冲突时保留至少近段踏面，否则只剩漂浮主殿。与巨像尺度卡配合时，别让每一级台阶都夸张得像另一座建筑。

## 反例

露营浮岛的薄盘底座适合展示商品集合，但不建立逐级攀登的身体经验。照搬完整底盘会让阶台像包装底托。


[![水牛露营 · 浮岛](shots/04.jpg)](shots/04.jpg)
[水牛露营 · 浮岛](https://github.com/Zp-Peter/kimi-k31pro-opus55-benchmark-showcase/blob/65e82c53b63f2fdd918617269c057d8e53af2c6f/opus/buffalo/02-camp.html) · 浮岛只有一层薄底座，主物像摆在托盘上，无法讲述攀登。

[逐图来源与复现](SOURCE.md) · [返回视觉卡库](../../../README.md)
