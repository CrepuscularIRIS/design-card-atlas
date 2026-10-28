# 逆光露轮廓

分组：光影 · 主维度：A 逆光、B 色温、C 亮暗重心、D 剪影、F 明亮大气 · 情绪：敬畏、压迫

## 一句话

把亮背景放在需要读懂的外轮廓后面，让暗主体以形状而不是满身高光成立。

[![清明上河 · 黄昏虹桥](shots/02.jpg)](shots/02.jpg)
[清明上河 · 黄昏虹桥](https://silentfleetkk.github.io/qingming-bianjing/opus-5.5/qingming-bianjing.html) · 亮天空从桥栏、人物与拱洞后透出，桥本身保持暗形。

| 参考 | 参考 |
|---|---|
| [![Unreal 云上神殿与巨龙](shots/01.jpg)](shots/01.jpg) | [![中式幻想 RPG · 雾中巨像](shots/03.jpg)](shots/03.jpg) |
| [Unreal 云上神殿与巨龙](https://skillry.dev/ai-videos/kimi-k3-1/kimi-moonshot-068067-1) · 看下方人物与右侧檐线：暖云是它们的亮背景；龙鬃白高光不是本卡目标。 | [中式幻想 RPG · 雾中巨像](https://skillry.dev/ai-videos/kimi-k3-1/crangerus-549203) · 两侧合掌轮廓由中央淡雾开口衬出，暗像不必全身发亮。 |

<a href="shots/05.jpg"><img src="shots/05.jpg" width="420" alt="长风 · 草原风起"></a>
[长风 · 草原风起](https://jbang2004.github.io/long-wind/) · 看太阳下方三个中景人形与右侧树干：亮雾把暗轮廓分出来；草穗亮边属于另一层，近角色面部不是建模范本。
## 看哪里

1. 清明上河 · 黄昏虹桥：亮天空从桥栏、人物与拱洞后透出，桥本身保持暗形。
2. Unreal 云上神殿与巨龙：看下方人物与右侧檐线：暖云是它们的亮背景；龙鬃白高光不是本卡目标。
3. 中式幻想 RPG · 雾中巨像：两侧合掌轮廓由中央淡雾开口衬出，暗像不必全身发亮。
4. 长风 · 草原风起：看太阳下方三个中景人形与右侧树干：亮雾把暗轮廓分出来；草穗亮边属于另一层，近角色面部不是建模范本。

## 拆解

以下比例为画面估计，不代表材质或光源测量。

- **A · 背光位置**：龙殿最亮云层在中央偏左，朱柱与人物前侧暗；虹桥的亮天空透过栏杆和拱洞，桥面不需要整体提亮。
- **D · 剪影可读**：巨像画面两侧肩、手与冠顶被裁出框，中央浅灰开口约占宽25%；观众仍可由合掌轮廓辨认巨像。关掉表面花纹，形状也成立。
- **C · 正负形**：虹桥的实心暗桥与透亮桥洞互相定义；巨龙下颌和云层之间保留一条清楚边界，人物放在最简单的亮地面前。
- **B · 色温**：龙殿暖云约`#D8AE62`对朱褐暗体，巨像灰绿对近白雾，说明本语言不依赖固定橙蓝配色。
- **F · 空气角色**：巨像后的亮雾降低远景对比，却没有覆盖近舟的外轮廓；雾在主体后面承担背景板，而不是全屏白纱。

## 做法

先在最终相机里摆暗主体与亮背景，确认轮廓有没有相互黏连，再加局部填充。光源或发亮天空不必在画面里直接露出圆形太阳。

- **迁移试验值**：近景暗主体先占约45–65%面积，主要亮开口约15–30%；保留窄的中间调识别材质。数字是构图预算，非曝光公式。
- 江南实例的[天空、太阳与雾状态](https://github.com/holooooo/webgl-seascape-video/blob/915cb7c9a318e03bd2228bc232494b496ff2316c/episodes/04-jiangnan-voxel/interactive.html#L3465-L3500)可作为分开控制背景与主体照明的实现线索；不宣称其参数能复现龙殿。

### 实现索引

2026-10-28 源码阅读补索引；不新增截图、不改上方视觉判断。上方“不能由截图推出/尚未审 shader”等界限指原视觉阶段，本节另列本批核过的源码。`Repos/` 相对 `~/Blog/`，Citadel 路径相对 `~/Blog/citadel/`。本批未运行这些源码测量参数，标为“源码”的值不得当作实测。

| 作品 | 源码（本地路径:行） | 技术与接入边界 | 参数（来源） | 许可 / 复用档 | Citadel 已有可复用入口 |
|---|---|---|---|---|---|
| 清明上河 · 黄昏虹桥 | `Repos/qingming-bianjing/opus-5.5/qingming-bianjing.html:2385-2388,2405-2418` | dusk 将亮地平线、低太阳与半球补光分控；applyAtm 同时更新天空、雾、sun/hemi 和曝光。先在最终机位把桥栏/拱洞放在亮天前，再压住正面填光，不是轮廓描边 shader。Citadel lab/src/scenes/Shrine/index.js:73-89 已有主光/半球光/补光；还须按 street-1 或 platform-1 机位重排亮背景，不能只转太阳。 | dusk sun elevation / azimuth=6.5° / 252°（源码）；dusk sun intensity / hemi intensity=2.4 / 0.7（源码）；dusk horizon / zenith=#efb07a / #4d6290（源码）；bright opening=画面 15–30%（建议迁移值） | README 声明项目许可待定；不能以依赖 Three.js 的许可替代作品许可，只借手法 / borrow | `lab/src/scenes/Shrine/index.js` |
| Unreal 云上神殿与巨龙 | `none` | 原作源码未定位，许可待验证；邻接技术源 Repos/qingming-bianjing/opus-5.5/qingming-bianjing.html:2385-2388,2405-2418：借亮天空/雾背景与暗主体照明分控；在 street-1 门廊或 platform-1 窗侧先构图，再限制正面补光；不提供龙、巨像或草原资产，亦不把草穗亮边当主体描边；不是原作实现，画面一致性待验证。 | dark subject / bright opening=约 45–65% / 15–30% 画面预算（建议迁移值） | 原作待验证；邻接源 项目许可待定，仅借手法，原作资产不可据此复制 / reference | `lab/src/scenes/Shrine/index.js` |
| 中式幻想 RPG · 雾中巨像 | `none` | 原作源码未定位，许可待验证；邻接技术源 Repos/qingming-bianjing/opus-5.5/qingming-bianjing.html:2385-2388,2405-2418：借亮天空/雾背景与暗主体照明分控；在 street-1 门廊或 platform-1 窗侧先构图，再限制正面补光；不提供龙、巨像或草原资产，亦不把草穗亮边当主体描边；不是原作实现，画面一致性待验证。 | dark subject / bright opening=约 45–65% / 15–30% 画面预算（建议迁移值） | 原作待验证；邻接源 项目许可待定，仅借手法，原作资产不可据此复制 / reference | `lab/src/scenes/Shrine/index.js` |
| 长风 · 草原风起 | `none` | 原作源码未定位，许可待验证；邻接技术源 Repos/qingming-bianjing/opus-5.5/qingming-bianjing.html:2385-2388,2405-2418：借亮天空/雾背景与暗主体照明分控；在 street-1 门廊或 platform-1 窗侧先构图，再限制正面补光；不提供龙、巨像或草原资产，亦不把草穗亮边当主体描边；不是原作实现，画面一致性待验证。 | dark subject / bright opening=约 45–65% / 15–30% 画面预算（建议迁移值） | 原作待验证；邻接源 项目许可待定，仅借手法，原作资产不可据此复制 / reference | `lab/src/scenes/Shrine/index.js` |

队列优先 platform-1 窗侧与 street-1 门廊。匹配表 Beyond Horizon/EDOLUS 行命中本卡并指向 Metro/Platform，但这些邻接源码不是两部视频的原作源；场景适配仍待验证。

源码快照（本批读取，不是新增截图来源）：
- `qingming-bianjing@d9d85a0a19e9e52daa028e37407637c3da211f31`

已检索 `citadel/src`（含 `src/world/worlds/`）与 `lab/src`；本批未发现 `src/world/worlds/cardfx/` 目录或本卡同名预制模块。以上入口只表示可复用部分；首次完整落地才由执行者沉淀 cardfx，不在此虚构文件。title / atlas locked，任何队列用途均不解除锁定。

## 迁移到博客

street-1门廊或platform-1窗侧可把暗建筑放到亮天前；Shrine会面背景可把门、像或檐角放到亮雾前。title / atlas locked，本卡不改这两个场景。先保留人物与建筑的边界，避免用黑色剪影完全吃掉会面对象。

搭配熟悉物标定巨构、前景框景；与全场强bloom、每条边都描光冲突。轮廓已有足够反差时，不再额外加宽光边。

## 反例

吸积盘图把左太阳、金环和大量水纹同时推亮，黑核虽清楚，视线却不断被周围亮点打断。背光的目的应是说明主体，而不是制造尽可能多的亮像素。


[![Shader & Cosmos · 吸积盘](shots/04.png)](shots/04.png)
[Shader & Cosmos · 吸积盘](https://github.com/holooooo/webgl-seascape-video) · 太阳、环带与满水面亮点同时抢高光，不作为主参考。

[逐图来源与复现](SOURCE.md) · [返回视觉卡库](../../../README.md)
