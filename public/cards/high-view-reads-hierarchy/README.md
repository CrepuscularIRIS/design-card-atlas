# 俯瞰读层级

分组：镜头运动 · 主维度：G 高视点、C 布局与通路、D 高低层级、F 远景衰减、H 标注空间 · 情绪：开阔、统观

## 一句话

把相机抬到能读懂地形与通路的位置，同时保留近景遮挡，避免把世界拍成桌面模型。

[![清明上河 · 黄昏全城](shots/02.jpg)](shots/02.jpg)
[清明上河 · 黄昏全城](https://silentfleetkk.github.io/qingming-bianjing/opus-5.5/qingming-bianjing.html) · 河与街区关系被一次读懂，桥成为岸区之间的连接点。

| 参考 | 参考 |
|---|---|
| [![Athenaion · Panorama](shots/01.jpg)](shots/01.jpg) | [![江南山谷 · 蓝调全景](shots/03.png)](shots/03.png) |
| [Athenaion · Panorama](https://github.com/Leonxlnx/athenaion) · 高处斜看仍有近殿遮挡，城市由高殿、低居与远山组成。 | [江南山谷 · 蓝调全景](https://github.com/holooooo/webgl-seascape-video/blob/915cb7c9a318e03bd2228bc232494b496ff2316c/episodes/04-jiangnan-voxel/interactive.html) · 山脊围住水与村落，视点够高能看布局，又未露出世界底盘。 |
## 看哪里

1. 清明上河 · 黄昏全城：河与街区关系被一次读懂，桥成为岸区之间的连接点。
2. Athenaion · Panorama：高处斜看仍有近殿遮挡，城市由高殿、低居与远山组成。
3. 江南山谷 · 蓝调全景：山脊围住水与村落，视点够高能看布局，又未露出世界底盘。

## 拆解

本卡分析静态高视点，不据三张静帧编造升降镜头的速度或缓动。

- **G · 视点**：看得见屋顶与水面，所以能读区域连接；Athenaion仍从一侧高处看，不是完全垂直正投影。近殿保留立面高度。
- **C · 布局**：汴河斜切街区，宽度沿远近缩小；山谷水道被两岸建筑夹住。主要通道约占宽1/5–1/3，密集建筑不能封死它。
- **D · 层级**：Athenaion高殿、低城、山脉不等高，山谷近岸、谷地与山顶也分级。若所有建筑同高，抬高相机只会看见一片重复格子。
- **F · 延续**：远山与远城向浅色衰减，框外仍可延伸；没有把整个世界的圆形底座交代完。
- **H · 信息位置**：总览适合少量地点标记，但应沿空水面/天空或空隙放置；不让每个屋顶都顶一条常驻标签。参考原图不证明已实现这种UI。

## 做法

先选择能说明通路的高视点，再保留一个近景大体块作为观看位置。总览不是把相机无限拉远。

- **原作机位**：江南[CAMERAS](https://github.com/holooooo/webgl-seascape-video/blob/915cb7c9a318e03bd2228bc232494b496ff2316c/episodes/04-jiangnan-voxel/interactive.html#L3615-L3618)给出全景与高处机位；本卡所用截图的实际操作仍以SOURCE为准，不以代码存在替代实看。
- **迁移试验**：画面至少保留一个近实体、一个通路、一个远地标；标记先只显示当前目标，避免总览变成仪表盘。

### 实现索引

以下是源码阅读索引，不把邻接技术源说成原作实现，也不把现有基础组件说成整卡已落地。`Repos/` 相对 `~/Blog/`；`citadel` 列相对 `~/Blog/citadel/`。参数逐项标明来源，未做本轮运行测量。

| 作品 | 源码（本地路径:行） | 技术与接入边界 | 参数（来源） | 许可 / 复用档 | Citadel 已有可复用入口 |
|---|---|---|---|---|---|
| 清明上河 · 黄昏全城 | `Repos/qingming-bianjing/opus-5.5/qingming-bianjing.html:2500-2524` | VIEWS.overview 在横竖屏分别设置斜俯瞰 position/target/FOV，bw 将桥局部平面坐标转世界坐标；不可把 bw 参数直接当 xyz。Citadel place.js:529-546 已有 named views/goView，可复用接口但必须为 street-1 重选场景机位；atlas/title locked, not changed。 | landscape overview=pos=bw(80,66,34), target=bw(-24,-58,4)（源码）；portrait overview=pos=bw(64,80,46), target=bw(-6,-42,3)（源码）；overview FOV=42°（源码） | 未发现作品仓根 LICENSE，授权范围待验证；仅借手法，不复制代码/资产 / borrow | `src/world/worlds/place.js` |
| Athenaion · Panorama | `Repos/athenaion/src/world/shots.js:5-10` | 作者透视相机在侧上方保留近殿遮挡并读到低城；布局 src/world/layout.js:37-110 决定高低关系，相机参数不是缩比地形的替代品。可把 preset 结构映射到 Citadel place.js:529-546 的 views/goView，不直接复制米制坐标。 | position=[108,66,30]（源码）；target=[15.1,61.5,-6.7]（源码）；FOV=40°（源码） | MIT（LICENSE:1-21） / integrate | `src/world/worlds/place.js` |
| 江南山谷 · 蓝调全景 | `Repos/webgl-seascape-video/episodes/04-jiangnan-voxel/interactive.html:3612-3623` | SHOTS 提供山谷全景和山坡俯瞰两档透视相机，用河道和山脊保留布局方向；具体截图操作仍以原 SOURCE 为准，不把预设存在当成截图机位实测。Citadel place.js:529-546 可承接目标场景的具名机位。 | valley panorama=pos=[32,15,128], target=[-6,5,22], FOV=52°（源码）；hillside overview=pos=[80,42,52], target=[-10,3,-14], FOV=50°（源码） | 未发现作品仓根 LICENSE，授权范围待验证；仅借手法，不复制代码/资产 / borrow | `src/world/worlds/place.js` |

队列落点优先 street-1 的场景总览机位。car-1 是车内场景，不直接套飞行/俯瞰镜头；是否有合适车外可见布局待验证。本批只索引 place.js 的 views/goView；atlas/title locked, not changed。

源码快照（2026-10-28 阅读；不是新增截图来源）：
- `athenaion@9b8bd23b39c458a50fb1201037360047781c45b5`
- `webgl-seascape-video@915cb7c9a318e03bd2228bc232494b496ff2316c`
- `qingming-bianjing@d9d85a0a19e9e52daa028e37407637c3da211f31`

已检索 `citadel/src` 及 `src/world/worlds/cardfx/`；本批未发现这些卡的同名预制模块。未来首次落地时才由执行者沉淀 `src/world/worlds/cardfx/high-view-reads-hierarchy.js`，此处不是已有文件承诺。

## 迁移到博客

以 street-1 场景总览机位为主目标：复用现有 named views/goView，从侧上方读清街道、入口与远地标的连接关系，保留近景实体并让街区延伸到框外；具体 position/target/FOV 按现有街道尺度重选，不照抄参考坐标。car-1 是车内场景，不直接套用俯瞰镜头。

atlas/title：locked, not changed；仅保留历史参考，不列入本批修改目标。

搭配河道串景、雾层分远近；与巨像越画框的近身目标分属两级镜头。可顺序使用，不能要求同一帧同时读清全城布局与巨像脸部纹理。

## 反例

浮岛全轮廓、底盘和树冠全被看见，空间被压成可搬走的物件。要保留巨构感，至少让世界在一个方向上继续到框外。


[![水牛露营 · 浮岛](shots/04.jpg)](shots/04.jpg)
[水牛露营 · 浮岛](https://github.com/Zp-Peter/kimi-k31pro-opus55-benchmark-showcase/blob/65e82c53b63f2fdd918617269c057d8e53af2c6f/opus/buffalo/02-camp.html) · 完整岛底与等比例小树让俯视变成手办展示，缺少框外世界。

[逐图来源与复现](SOURCE.md) · [返回视觉卡库](../../../README.md)
