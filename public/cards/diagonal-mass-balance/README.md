# 斜向配重

分组：构图重心 · 主维度：C 不对称平衡、D 体量主次、A 亮暗配重、G 透视方向、F 空场 · 情绪：张力、延伸

## 一句话

把重体块压向一侧，用斜向地面或水带把另一侧的空场接回来。

[![Athenaion · Panorama](shots/01.jpg)](shots/01.jpg)
[Athenaion · Panorama](https://github.com/Leonxlnx/athenaion) · 右侧大殿与左侧低城不等重，山谷与天空补出呼吸。

| 参考 | 参考 |
|---|---|
| [![Unreal 云上神殿与巨龙](shots/02.jpg)](shots/02.jpg) | [![雷尼斯黑沙滩 · 海滩](shots/03.jpg)](shots/03.jpg) |
| [Unreal 云上神殿与巨龙](https://skillry.dev/ai-videos/kimi-k3-1/kimi-moonshot-068067-1) · 巨龙压左、柱廊弯向右远处，小人物落在两种尺度交界。 | [雷尼斯黑沙滩 · 海滩](https://github.com/Zp-Peter/kimi-k31pro-opus55-benchmark-showcase/blob/65e82c53b63f2fdd918617269c057d8e53af2c6f/opus/reynisfjara/index.html) · 左黑壁的重量由右侧海面亮带抵住，斜岸线把两侧接在一起。 |
## 看哪里

1. Athenaion · Panorama：右侧大殿与左侧低城不等重，山谷与天空补出呼吸。
2. Unreal 云上神殿与巨龙：巨龙压左、柱廊弯向右远处，小人物落在两种尺度交界。
3. 雷尼斯黑沙滩 · 海滩：左黑壁的重量由右侧海面亮带抵住，斜岸线把两侧接在一起。

## 拆解

比例和位置为截图估计，不反推相机矩阵。

- **C · 重块**：Athenaion右殿约占半幅，左城更碎、更低；海岸左壁黑重，右海浅亮。两侧不按物件数量平分，而按面积和亮度配重。
- **G · 方向**：龙殿地面与柱列斜向右方收束；黑沙湿带从右下弯到远方。斜线不是画面装饰，它接着可行走或可观看的空间。
- **D · 主次**：巨龙、柱群、人物至少三级形体。主块可以出框，次块必须保留识别边界，否则不对称会变成杂乱。
- **A · 明暗**：右海虽物体少，较亮且面积大，足以平衡左壁；龙殿明亮云口也在暗龙旁形成配重。并非只有一个同样大的实体才能平衡大物。
- **F · 空场**：天空与水的低细节面占约1/3–1/2，让密集建筑有呼吸。细纹不能填平这块差异。

## 做法

在相机预览上先把场景概括成两三块灰形，检查主块偏左或偏右是否仍有承托。再沿真实地形放斜向线，不临时画一束无来源的斜光来补构图。

- **迁移试验**：主重块先占宽40–60%，另一侧用连续低细节亮面补平衡；人物所在区避免同时是最密纹理区。
- Athenaion固定机位可参照[shots.js](https://github.com/Leonxlnx/athenaion/blob/9b8bd23b39c458a50fb1201037360047781c45b5/src/world/shots.js)，数值应按Blog场景单位重新定。

### 实现索引

2026-10-28 源码阅读补索引；不新增截图、不改上方视觉判断。上方“不能由截图推出/尚未审 shader”等界限指原视觉阶段，本节另列本批核过的源码。`Repos/` 相对 `~/Blog/`，Citadel 路径相对 `~/Blog/citadel/`。本批未运行这些源码测量参数，标为“源码”的值不得当作实测。

| 作品 | 源码（本地路径:行） | 技术与接入边界 | 参数（来源） | 许可 / 复用档 | Citadel 已有可复用入口 |
|---|---|---|---|---|---|
| Athenaion · Panorama | `Repos/athenaion/src/world/layout.js:70-96; Repos/athenaion/src/world/shots.js:8-9` | 主殿与巨像真实分布配合偏轴 shot1；不是相机 roll 倾斜屏幕。主殿中心/尺寸和镜头共同构成重块。Citadel src/world/worlds/place.js:535-546 可以复用机位，但仍需在 platform-1 或 luxury-house-1 用现有墙/柱和窗外空场重新投影检验。 | temple center / stylobate=[20,66,-64] / [70,31]（源码）；shot1 pos / target / FOV=[108,66,30] / [15.1,61.5,-6.7] / 40°（源码）；main mass width=画宽 40–60%（建议迁移值） | MIT；构图可参考，代码移植保留声明，坐标不可跨尺度照搬 / integrate | `src/world/worlds/place.js` |
| 雷尼斯黑沙滩 · 海滩 | `Repos/kimi-k31pro-opus55-benchmark-showcase/opus/reynisfjara/src/config.js:4-36; Repos/kimi-k31pro-opus55-benchmark-showcase/opus/reynisfjara/src/world/beach.js:75-98` | cliff 折线/远礁分布加 beach 偏轴机位，使岸线与湿带连接重岩壁和低细节海面。相机预设 y 是相对地面高度，由 main.js:257-264 求最终坐标。迁移到街角/外廊需已有斜向地面边界，不是加一束无来源斜光；src/world/worlds/place.js 只提供机位宿主。 | beach preset pos / target / FOV=[6,1.8,-15] / [230,12,34] / 46°，y 为局部地面偏移（源码）；main mass width=画宽 40–60%（建议迁移值） | 未发现仓库根 LICENSE；作品代码授权待验证，只借手法，不复制代码/资产 / borrow | `src/world/worlds/place.js` |
| Unreal 云上神殿与巨龙 | `none` | 原作源码未定位，许可待验证；邻接技术源 Repos/athenaion/src/world/layout.js:70-96; Repos/athenaion/src/world/shots.js:8-9：借偏轴实体重块与低细节空场配重，适用于 luxury-house-1 窗侧或 Platform 柱廊；没有龙模型/云海实现，不把原视频解释为该代码产物；不是原作实现，画面一致性待验证。 | main mass width / quiet field=40–60% / 约 1/3–1/2 画面（建议迁移值） | 原作待验证；邻接源 MIT，原作资产不可据此复制 / reference | `src/world/worlds/place.js` |

本卡为高频补索引项，未找到匹配表直接命中；队列可评估 luxury-house-1 窗侧或 platform-1，具体镜头与角色覆盖后的平衡待验证。

源码快照（本批读取，不是新增截图来源）：
- `athenaion@9b8bd23b39c458a50fb1201037360047781c45b5`
- `kimi-k31pro-opus55-benchmark-showcase@65e82c53b63f2fdd918617269c057d8e53af2c6f`

已检索 `citadel/src`（含 `src/world/worlds/`）与 `lab/src`；本批未发现 `src/world/worlds/cardfx/` 目录或本卡同名预制模块。以上入口只表示可复用部分；首次完整落地才由执行者沉淀 cardfx，不在此虚构文件。title / atlas locked，任何队列用途均不解除锁定。

## 迁移到博客

luxury-house-1窗侧或platform-1柱廊让重体偏一侧，另一侧保留窗外低细节空场；BlackCityHall外廊让墙体与远处空场形成斜向对话。title / atlas locked，本卡不改这两个场景。进入会面视图时重新检查角色覆盖后的配重，不照搬空镜构图。

搭配留空放大孤立物、近框套远景；与严格正面中轴构图需二选一作为主结构，不能一边要求对称庄严、一边把焦点都挤到角落。

## 反例

露营浮岛把完整底座悬在右侧，左侧大字负责商业阅读。移植这套平衡会让Citadel像一件可购买的小模型，而不是观众身处的场所。


[![水牛露营 · 浮岛](shots/04.jpg)](shots/04.jpg)
[水牛露营 · 浮岛](https://github.com/Zp-Peter/kimi-k31pro-opus55-benchmark-showcase/blob/65e82c53b63f2fdd918617269c057d8e53af2c6f/opus/buffalo/02-camp.html) · 孤立浮岛与左侧广告文本是产品陈列平衡，不是人在巨构旁边的空间张力。

[逐图来源与复现](SOURCE.md) · [返回视觉卡库](../../../README.md)
