# 骨架规整草木野

> 已撤出正式卡库：修订一次后复核仍 FAIL。此文件保留当时未闭环内容，不可作为 card:ordered-frame-wild-growth 实现索引引用；具体差距与重出条件见 [批次筛选表](../../cards-20261028-b3.csv)。

分组：造型尺度 · 主维度：D 规则与有机、C 密度分区、E 表面差、A 光下细节、I 生长感 · 情绪：生机、时间

## 一句话

把清楚的建筑骨架与不均匀生长的植物并置，让两种秩序互相说明。

[![Blender 机场室内雨林](shots/01.jpg)](shots/01.jpg)
[Blender 机场室内雨林](https://skillry.dev/ai-videos/kimi-k3-1/kimi-moonshot-068067-4) · 大网格天幕托住空间，下面林冠高低和疏密不一，水柱穿过两者。

| 参考 | 参考 |
|---|---|
| [![Athenaion · 水庭](shots/02.jpg)](shots/02.jpg) | [![Athenaion · Ruined portico](shots/03.jpg)](shots/03.jpg) |
| [Athenaion · 水庭](https://github.com/Leonxlnx/athenaion) · 圆亭和栏杆有确定边界，树冠与草簇越出边界但没有填平道路。 | [Athenaion · Ruined portico](https://github.com/Leonxlnx/athenaion) · 残柱与梁仍可读为规整构架，杂草沿地面与断口生长。 |
## 看哪里

1. Blender 机场室内雨林：大网格天幕托住空间，下面林冠高低和疏密不一，水柱穿过两者。
2. Athenaion · 水庭：圆亭和栏杆有确定边界，树冠与草簇越出边界但没有填平道路。
3. Athenaion · Ruined portico：残柱与梁仍可读为规整构架，杂草沿地面与断口生长。

## 拆解

各比例为画面估计，不是对植物实例数或多边形数的测量。

- **D · 两种秩序**：机场顶棚是重复网格，树冠是不同大小的不规则团块；规则骨架在上部约半幅，有机形体集中下半部，不混成同一种噪点。
- **C · 密度**：水庭让中间圆亭周边有水面呼吸，密植更多贴边；废墟中央开口仍然可读。植物的任务不是把所有空隙填满。
- **E · 反射/表面**：石柱大面与叶片小亮面尺度不同；顶棚构件比林冠线性、稳定。材质不同之外，形状频率也必须不同。
- **A · 细节主次**：机场天幕亮网格没有压成纯白，树冠暗处仍成大块；远草无需和近叶一样锐利。
- **I · 生长感**：废墟草簇沿断口和地面缝隙，暗示时间；机场雨林被有意容纳在建筑内，暗示人工维护。两者的叙事不能混写成“无人荒废”。

## 做法

先保证无植物灰模的结构清楚，再按区域分配植物密度。不要对每个网格格子放同样大小、同样方向的一棵树。

- **迁移试验**：选择三种冠幅与至少两档疏密区；主路和识别轮廓保留连续空隙。先审400px缩图是否还有树冠大形，再审近景叶片。
- 原作视频植被算法仍未知；下表已核实 Athenaion 残廊的 joints 采样与表面约束藤蔓，不把它冒充机场林冠算法。

### 实现索引

2026-10-28 已打开本地源码核对；当前 checkout 不等同旧成片版本。参数区分源码与建议迁移值，尚未在 Citadel 运行复刻。`citadel: none` 是尚未找到可复用实现，不是已落地声明。第三方路径相对 `~/Blog/`，Citadel 路径相对 `~/Blog/citadel/`。固定版本与许可见 [SOURCE.md](SOURCE.md)。

| 作品 | 源码 / 邻接与手法 | 参数及性质 | 许可 / 复用 | Citadel 可复用实现 |
|---|---|---|---|---|
| Blender 机场室内雨林 | `none`；原作源码未取得；邻接技术源 Repos/athenaion/src/ruins/grass.js:64-97；Repos/athenaion/src/ruins/portico.js:206-228（MIT）。沿缝隙生成成簇草、沿表面约束藤蔓，不提供机场林冠或天幕资产；大树需另配，待验证；不是原作实现证明，迁移待验证。 已查 Citadel src/world/places/foliage.js:15-44，它只做实例减量，不生成草木，不能作为生成器。 Citadel 已有局部草簇生成与缝隙/脚边聚簇，非林冠、藤蔓或森林生成器；见 citadel 索引。 | 主路留空=连续通道不放实例（建议迁移值） | 原作许可未明；邻接源许可见说明 / borrow | `lab/src/scenes/NeverlandRoom/moundDetail.js:28-56,81-96` |
| Athenaion · 水庭 | `none`；水庭画面源码归属尚未定位；邻接技术源 Repos/athenaion/src/ruins/grass.js:64-97、src/ruins/portico.js:206-228（MIT）仅证实残廊草缝/藤蔓，不提供水庭树冠或圆亭植被布局；完整植被迁移待验证。 Citadel 已有局部草簇生成与缝隙/脚边聚簇，非林冠、藤蔓或森林生成器；见 citadel 索引。 | density=2.2 簇/m（源码）；size=[0.06,0.2]m（源码）；藤蔓 steps=95（源码）；藤蔓 maxStems=170（源码） | MIT / borrow | `lab/src/scenes/NeverlandRoom/moundDetail.js:28-56,81-96` |
| Athenaion · Ruined portico | `Repos/athenaion/src/ruins/grass.js:64-97; Repos/athenaion/src/ruins/portico.js:206-228`；草从 joints/patch/crack 不均匀采样；藤蔓 inside 谓词留亮柱面。需要 grass.js 的 tuftMesh 与植物材质、portico.js 中表面SDF与地面高度；Citadel foliage.js 只减量，不是生成器。 Citadel 已有局部草簇生成与缝隙/脚边聚簇，非林冠、藤蔓或森林生成器；见 citadel 索引。 | density=2.2 簇/m（源码）；size=[0.06,0.2]m（源码）；藤蔓 steps=95（源码）；藤蔓 maxStems=170（源码） | MIT / integrate | `lab/src/scenes/NeverlandRoom/moundDetail.js:28-56,81-96` |

Citadel 草簇边界：`lab/src/scenes/NeverlandRoom/moundDetail.js:28-56,81-96` 的 `tuft()` 生成固定种子、11 叶片草簇，`addMoundDetail(mound, M)` 按缝隙/脚边 patches 聚簇。后者同时添加垫层、卵石和接触阴影，并依赖 core/kit、core/mats、SDF/contact；不是可直接调用的独立草木包。可拆用局部草簇，不提供大树林冠、藤蔓或整座森林。`src/world/places/foliage.js:15-44` 仍只是实例减量。

## 迁移到博客

Shrine庭院保留柱、檐、台阶的清楚边界，让草木在边缘和裂隙不均匀出现；Landfill（`landfill-1`）废墟边缘可沿断口布簇，Beach（`beach-1`）只在岸崖局部放草，均保留行走通道。atlas 已锁定，不在本批改动。

搭配阶台托举主殿、风化依附形体；与密集HUD、满屏粒子冲突，因为三者都增加高频信息。巨像脸旁的植物应减量。

## 反例

Kōyō-en这张入口图的平面叶簇呈密集、相似的条状重复，草地也细密均匀；缩小后自然层与木廊一样机械。它能支持园林框景讨论，但不作为植被品质目标。


[![Kōyō-en · 入口](shots/04.jpg)](shots/04.jpg)
[Kōyō-en · 入口](https://modelzengarden.com/garden/opus-5-5-claude-code) · 叶片与草地的重复纹理接近木廊节奏，缩图时自然层也变成规整花纹。

[逐图来源与复现](SOURCE.md) · [返回视觉卡库](../../../README.md)
