# 柱廊明暗节奏

分组：造型尺度 · 主维度：A 侧光、C 消失点、D 重复与尺度、E 石木对照、I 仪式感 · 情绪：庄严、神圣

## 一句话

用重复的柱身与暗腔给空间节拍，再用递减的间距把视线带向深处。

[![Blender cathedral interior](shots/01.jpg)](shots/01.jpg)
[Blender cathedral interior](https://x.com/k1rallik/status/2113693629713633435) · 柱束亮面与柱间暗腔成对重复，越靠尽端间距越紧，过道保留整段节奏的观看距离。

| 参考 | 参考 |
|---|---|
| [![Athenaion · Temple facade](shots/02.jpg)](shots/02.jpg) | [![Unreal 云上神殿与巨龙](shots/03.jpg)](shots/03.jpg) |
| [Athenaion · Temple facade](https://github.com/Leonxlnx/athenaion) · 柱身受光与柱间暗腔交替；侧立面把这组节奏延伸到深处。 | [Unreal 云上神殿与巨龙](https://skillry.dev/ai-videos/kimi-k3-1/kimi-moonshot-068067-1) · 右侧朱柱与柱间暗隙连续递进，弧形檐线把一根根柱的重复接成向远处收拢的节奏。 |
## 看哪里

1. Blender cathedral interior：柱束亮面与柱间暗腔成对重复，越靠尽端间距越紧，过道保留整段节奏的观看距离。
2. Athenaion · Temple facade：柱身受光与柱间暗腔交替；侧立面把这组节奏延伸到深处。
3. Unreal 云上神殿与巨龙：右侧朱柱与柱间暗隙连续递进，弧形檐线把一根根柱的重复接成向远处收拢的节奏。

## 拆解

比例与颜色为截图估计；相机和几何值另在做法中注明来源。

- **A · 明暗结构**：教堂左右近柱各占画面约15–20%宽，左柱有窄暖光带，右柱仍有可辨认的中间调。重复的不是一排同亮模型，而是受光面—背光面—柱间空隙。
- **C · 引导线**：教堂过道向(50%,79%)收束，尽端竖窗继续把视线抬高；龙殿右侧檐线从画面右上弯向左侧中远景，阵列因此有方向。
- **D · 三级节奏**：Athenaion有大柱、柱身凹槽、细金饰三层。近柱高度是小雕像的约4–5倍；小细节服务大柱的比例，不应覆盖柱间暗腔。
- **B · 色彩克制**：Athenaion以暖灰石 `#A69D83` 为大面，深蓝旗幅 `#202B3B` 与金边 `#AF8744` 只占局部；龙殿朱柱成大块，金色主要留在云光和柱脚。
- **E · 材质分工**：教堂石柱低反射，长椅顶边出现更窄更亮的木质高光。光带在不同材质上有不同宽度，空间因此不会像同一种塑料。

## 做法

先用没有纹理的柱、地、顶测试节奏。相机应能看到柱身侧面和柱间空隙；如果全正面排列变成栅栏，先换机位，再加装饰。

- **源码值**：Athenaion主殿前面8柱、侧面17柱、柱高10.4，见[柱阵列布局](https://github.com/Leonxlnx/athenaion/blob/9b8bd23b39c458a50fb1201037360047781c45b5/src/world/layout.js#L72-L83)。图中正立面机位FOV18.5°，是有意压缩透视的作者相机，不意味着所有柱廊都应使用长焦。
- **迁移起点**：Blog先用6–10个可见重复单元；相邻柱的投影空隙至少保留约柱宽的0.5倍；不要让近柱完全挡住远端入口。这些是构图试验起点，不是工程约束。
- 光源沿柱列侧上方布置，保持最靠近镜头的柱面有中间调，远端目标可比侧廊亮一档。

### 实现索引

以下是源码阅读索引，不把邻接技术源说成原作实现，也不把现有基础组件说成整卡已落地。`Repos/` 相对 `~/Blog/`；`citadel` 列相对 `~/Blog/citadel/`。参数逐项标明来源，未做本轮运行测量。

| 作品 | 源码（本地路径:行） | 技术与接入边界 | 参数（来源） | 许可 / 复用档 | Citadel 已有可复用入口 |
|---|---|---|---|---|---|
| Blender cathedral interior | `none` | 原作石柱建模与布光待验证；邻接技术源 Repos/athenaion/src/modules/temple.js:53-67 以柱阵和暗内腔产生亮柱/暗隙节奏，不提供哥特柱束资产。 | 可见重复单元=6–10（建议迁移值） | 原作品源码及许可待验证；仅参考画面。邻接 Athenaion 源码为 MIT，不代表原作授权 / reference | `none` |
| Athenaion · Temple facade | `Repos/athenaion/src/arch/temple.js:267-307` | peripteralTemple 本体通过 columnAxes 生成前后/两侧柱位并以 addInstance 发射柱体（src/arch/temple.js:267-307）；调用点 src/modules/temple.js:53-67 配置 darkCella 与内部减光以保留柱间暗腔；尺寸在 src/world/layout.js:73-81，压缩透视机位在 src/world/shots.js:23-28。 | columns=front 8 / side 17（源码）；columnHeight=10.4（源码）；darkCella=true（源码）；interiorDark=0.5（源码）；facade FOV=18.5°（源码） | MIT（LICENSE:1-21） / integrate | `none` |
| Unreal 云上神殿与巨龙 | `none` | 原作朱柱、曲檐和反射源码未定位；邻接技术源 Repos/athenaion/src/modules/temple.js:53-67 可生成带暗腔的柱列，曲檐与朱漆材料仍需另找已授权资产。 | 相邻柱投影空隙=至少约柱宽 0.5 倍（建议迁移值） | 原作品源码及许可待验证；仅参考画面。邻接 Athenaion 源码为 MIT，不代表原作授权 / reference | `none` |

本批面向 CompanyMeetingroom 的重复结构/暗腔提案；没有确认可直接复用的柱阵 cardfx，故 citadel=none。需先确认房间通路与遮挡，不强行把古典柱式搬进会议室。

源码快照（2026-10-28 阅读；不是新增截图来源）：
- `athenaion@9b8bd23b39c458a50fb1201037360047781c45b5`

已检索 `citadel/src` 及 `src/world/worlds/cardfx/`；本批未发现这些卡的同名预制模块。未来首次落地时才由执行者沉淀 `src/world/worlds/cardfx/colonnade-rhythm.js`，此处不是已有文件承诺。

## 迁移到博客

- **用在哪**：已登记地点BlackCityHall与Shrine入口；属于对应场景后续建模提案，不宣称它们已经拥有本图效果。
- **改什么**：先确立一条可行走或可注视的轴线，再用柱列定义两侧节奏。把金饰、灯具集中在入口与重复节点，避免每根柱都堆复杂雕花。
- **搭配**：配合仰视尺度、薄雾拉开远近、局部暖焦点。
- **冲突**：浓雾会吞掉最后几根柱，过强bloom会抹平凹槽；正面平均补光会让亮柱—暗腔节拍消失。

## 反例

Sponza本次机位的帘幕与墙柱压成大块近黑，柱间边界在小图里难分。它说明场景已有柱廊和雾光，也仍可能失去节奏；此处只评价这张截图，不评价项目能力。

[![Sponza · 本次偏暗机位](shots/04.png)](shots/04.png)

[Sponza · 本次偏暗机位](https://three-good-godrays.ameo.design/#sponza) · 帘幕与柱间暗区连成大块，重复柱与间隙难以交替辨认。 仅评价本次画面。

[逐图来源与复现](SOURCE.md) · [返回视觉卡库](../../../README.md)
