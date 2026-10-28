# 侧光刻石

分组：光影 · 主维度：A 主光与阴影、C 重心、D 凹凸层级、E 粗糙表面 · 情绪：庄严、厚重

## 一句话

让侧来的光同时照见凸面、留下凹槽，石材的体量才不会被花纹替代。

[![Athenaion · Fallen head](shots/01.jpg)](shots/01.jpg)
[Athenaion · Fallen head](https://github.com/Leonxlnx/athenaion) · 巨像眼窝、发束和鼻梁由侧光分成清楚的凸面与凹面。

| 参考 | 参考 |
|---|---|
| [![Blender cathedral interior](shots/02.jpg)](shots/02.jpg) | [![Athenaion · Temple facade](shots/03.jpg)](shots/03.jpg) |
| [Blender cathedral interior](https://x.com/k1rallik/status/2113693629713633435) · 左侧柱身窄亮面与凹槽暗带相邻，柱头花饰在受光边与背光凹处之间显出起伏。 | [Athenaion · Temple facade](https://github.com/Leonxlnx/athenaion) · 柱身受光与柱间暗腔交替；侧立面把这组节奏延伸到深处。 |
## 看哪里

1. Athenaion · Fallen head：巨像眼窝、发束和鼻梁由侧光分成清楚的凸面与凹面。
2. Blender cathedral interior：左侧柱身窄亮面与凹槽暗带相邻，柱头花饰在受光边与背光凹处之间显出起伏。
3. Athenaion · Temple facade：柱身受光与柱间暗腔交替；侧立面把这组节奏延伸到深处。

## 拆解

数值和颜色为截图估计，物理光强未知。

- **A · 光向**：巨像鼻梁和左侧额面亮，眼窝与鼻底暗；主光来自画面左上。眼窝阴影约占面部高度的1/8，方向与发束凹槽一致。
- **D · 层级**：Athenaion先读出大柱圆面，再读出柱沟，最后才看见金饰。凹槽宽远小于柱身，约1:10；不能让表面噪点与大体块同等醒目。
- **E · 表面**：巨像颊部是连续哑光中间调，上面叠不规则灰斑；反射不形成玻璃般锐白点。教堂石柱与木椅的高光宽度不同。
- **C · 重心**：残头像占图右侧约40%宽，眼窝的高局部反差留在这个区域；左侧神殿是次级明亮结构。细节并未平均覆盖全图。
- **B · 色彩**：暖灰石约`#B8AE95`、深槽约`#5F5A4C`，用同色系明度塑体；天空冷蓝只作为环境衬托。

## 做法

先在无纹理模型上检查侧光。如果柱沟和石阶在灰模里看不清，先改光向或几何，而不是叠一张更脏的贴图。

- **源码线索**：Athenaion的[各机位光照设置](https://github.com/Leonxlnx/athenaion/blob/9b8bd23b39c458a50fb1201037360047781c45b5/src/world/looks.js#L55-L82)区分柱廊侧光与废墟略逆光；不是一套正面补光覆盖全部镜头。
- **迁移试验值**：主光先从相机侧方约35–65°试起；石材粗糙度可先试0.7–0.9，再按实际渲染调整。这些是Blog试验值，非图像反推原作参数。
- 预览缩图应保留三个层次：暗槽、中灰柱面、少量受光凸缘。不要只剩黑与白。

### 实现索引

2026-10-28 源码阅读补索引；不新增截图、不改上方视觉判断。上方“不能由截图推出/尚未审 shader”等界限指原视觉阶段，本节另列本批核过的源码。`Repos/` 相对 `~/Blog/`，Citadel 路径相对 `~/Blog/citadel/`。本批未运行这些源码测量参数，标为“源码”的值不得当作实测。

| 作品 | 源码（本地路径:行） | 技术与接入边界 | 参数（来源） | 许可 / 复用档 | Citadel 已有可复用入口 |
|---|---|---|---|---|---|
| Athenaion · Fallen head | `Repos/athenaion/src/world/looks.js:14-21,70-72` | sunRel 按相机 heading 设置日光方位；shot8 用左后斜光让鼻梁、发束与眼窝分面。Repos/athenaion/src/core/engine.js:152-181 将 look 真正应用到相机、太阳与 grade。Citadel lab/src/scenes/Shrine/index.js:73-89 可调主光与 fill，lab/src/scenes/Shrine/matlib.js:15-21 可调石材；灰模先读出凹凸，再加纹理，现成灯并不等于整卡已落地。 | shot8 relative azimuth / elevation=-140° / 40°（源码）；shot8 sun RGB=[1.0,0.87,0.70]（源码）；stone roughness=0.7–0.9（建议迁移值） | MIT；保留 Athenaion 版权声明；材质/资产另核许可 / integrate | `lab/src/scenes/Shrine/index.js` |
| Athenaion · Temple facade | `Repos/athenaion/src/world/looks.js:62-67` | shot5 主光位于相机左后侧，并设独立曝光/对比；配合真实柱沟和柱间遮挡产生明暗节奏，不是花纹贴图。执行路径 Repos/athenaion/src/core/engine.js:171-181。Citadel lab/src/scenes/Shrine/index.js:73-89 调光，lab/src/core/post.js:334-340 只作最后校准；不能照搬原作曝光。 | shot5 relative azimuth / elevation=-110° / 28°（源码）；shot5 exposure / contrast / saturation=0.46 / 1.8 / 0.82（源码）；camera-side light starting range=35–65°，非原作 shot5/8 光角（建议迁移值） | MIT；保留版权声明 / integrate | `lab/src/scenes/Shrine/index.js` |
| Blender cathedral interior | `none` | 原作源码未定位，许可待验证；邻接技术源 Repos/athenaion/src/world/looks.js:62-76; Repos/athenaion/src/core/engine.js:171-181：借相机相对侧光、低正面补光和实体柱沟；Shrine/BlackCityHall 先校灰模，不提供教堂模型，也不假定视频使用 Three.js；不是原作实现，画面一致性待验证。 | stone roughness=0.7–0.9（建议迁移值） | 原作待验证；邻接源 MIT，原作资产不可据此复制 / reference | `lab/src/scenes/Shrine/index.js` |

本卡属用户指定高频补索引项；未在匹配表找到该卡对队列的直接命中。可先评估 luxury-house-1 / hospital-1 的实体柱/墙，但不能把 Shrine 现有灯配置当这些场景已经落地。

源码快照（本批读取，不是新增截图来源）：
- `athenaion@9b8bd23b39c458a50fb1201037360047781c45b5`

已检索 `citadel/src`（含 `src/world/worlds/`）与 `lab/src`；本批未发现 `src/world/worlds/cardfx/` 目录或本卡同名预制模块。以上入口只表示可复用部分；首次完整落地才由执行者沉淀 cardfx，不在此虚构文件。title / atlas locked，任何队列用途均不解除锁定。

## 迁移到博客

Shrine台阶与登记的BlackCityHall柱面先选一侧主光，再添加低对比磨损。用在会面镜头时避免让最亮石面落在2D人物脸后。

搭配柱廊明暗节奏和局部风化；与正面平均补光、覆盖全柱的强发光冲突。当前是修改建议，未声称已检查这些Blog场景的具体缺陷。

## 反例

Sponza本次截图压暗了中间调：即使存在复杂柱体，缩图只读成大块黑影。增加纹理细节无法补回已经丢失的面转折。


[![Sponza · 本次偏暗机位](shots/04.png)](shots/04.png)
[Sponza · 本次偏暗机位](https://three-good-godrays.ameo.design/#sponza) · 柱面和凹槽同陷暗值，石体转折缺少可读中间调。 仅评价本次画面。

[逐图来源与复现](SOURCE.md) · [返回视觉卡库](../../../README.md)
