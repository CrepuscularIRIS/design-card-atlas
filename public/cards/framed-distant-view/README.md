# 近框套远景

分组：构图重心 · 主维度：C 画中框、D 近远尺度、A 局部反差、E 前景材质、I 观察位置 · 情绪：窥见、敬畏

## 一句话

用有厚度的近景边界围住远处目标，让观众先拥有一个站立的位置。

[![Athenaion · Ruined portico](shots/01.jpg)](shots/01.jpg)
[Athenaion · Ruined portico](https://github.com/Leonxlnx/athenaion) · 近柱与残梁组成不完整的窗，远殿仍然是窗内最清晰的结构。

| 参考 | 参考 |
|---|---|
| [![中式幻想 RPG · 雾中巨像](shots/02.jpg)](shots/02.jpg) | [![Athenaion · 水庭](shots/03.jpg)](shots/03.jpg) |
| [中式幻想 RPG · 雾中巨像](https://skillry.dev/ai-videos/kimi-k3-1/crangerus-549203) · 两侧巨像与底座夹出中央远岩、水道的开口，近舟压住左下前景。 | [Athenaion · 水庭](https://github.com/Leonxlnx/athenaion) · 上角枝叶与右侧近雕像、柱座围出不规则开口，圆亭和阶台后的主殿保留完整轮廓；框不必四边封闭。 |
## 看哪里

1. Athenaion · Ruined portico：近柱与残梁组成不完整的窗，远殿仍然是窗内最清晰的结构。
2. 中式幻想 RPG · 雾中巨像：两侧巨像与底座夹出中央远岩、水道的开口，近舟压住左下前景。
3. Athenaion · 水庭：上角枝叶与右侧近雕像、柱座围出不规则开口，圆亭和阶台后的主殿保留完整轮廓；框不必四边封闭。

## 拆解

数值是截图估计。

- **C · 框的开口**：Athenaion两侧近柱与上方残梁占约左右各15–25%，中央留下不规则开口；框不是等宽装饰边框，远殿落在右侧开口中。
- **D · 尺度**：近柱的一个柱头几乎与远殿立面同高；水路图近船顶棚宽约半幅，后方巨像仍延伸出上边界，两种尺度在一个镜头里并存。
- **A · 明暗**：近舟顶棚接近黑，背后的雾接近浅灰；水庭上角枝叶暗于天空和后殿，但右侧石像也可受光，框不必全黑。
- **E · 厚度**：废墟残梁能看到下表面，水庭右侧石座有顶面与侧面，枝叶前后交叠。只画一圈平面线条不会产生相同的空间位置感。
- **I · 叙事**：破柱像一个遗址内的眺望点，船棚让观众与乘客共享视点，水庭枝叶与石岸让观众站在花园边看高殿。框景同时交代“我在哪里”。

## 做法

只选择一组前景框，不把四边都封死。前景的纹理频率可以比远景高，但明亮文字或彩灯不应压过框内目标。

- **源码相机**：Athenaion通过[shot9](https://github.com/Leonxlnx/athenaion/blob/9b8bd23b39c458a50fb1201037360047781c45b5/src/world/shots.js)的36.5° FOV取景于废墟柱廊；真正的框来自几何遮挡，而非屏幕后处理边框。
- **迁移试验值**：近框总遮挡先试20–35%，主目标至少保留完整的一个识别轮廓；不要让细枝与人物脸相交。

### 实现索引

2026-10-28 源码阅读补索引；不新增截图、不改上方视觉判断。上方“不能由截图推出/尚未审 shader”等界限指原视觉阶段，本节另列本批核过的源码。`Repos/` 相对 `~/Blog/`，Citadel 路径相对 `~/Blog/citadel/`。本批未运行这些源码测量参数，标为“源码”的值不得当作实测。

| 作品 | 源码（本地路径:行） | 技术与接入边界 | 参数（来源） | 许可 / 复用档 | Citadel 已有可复用入口 |
|---|---|---|---|---|---|
| Athenaion · Ruined portico | `Repos/athenaion/src/ruins/portico.js:83-97,168-205` | 将近柱按 shot9 像素射线落到实体平面，残梁与左前景柱形成真实遮挡；Repos/athenaion/src/world/shots.js:41-42 固定观察机位。迁移到 street-1 门廊/Platform 窗边：保留近框厚度，重定目标与 FOV；src/world/worlds/place.js:535-546 仅承接机位，框的几何需用场景现有构件摆放，尚无同名 cardfx。 | shot9 FOV / near=36.5° / 0.3（源码）；architrave fragment length / D=6.6 / 0.95，原场景单位（源码）；near frame total occlusion=20–35%（建议迁移值） | MIT；portico 依赖 ARCH 构件与相机投影工具，保留声明并按依赖移植 / integrate | `src/world/worlds/place.js` |
| Athenaion · 水庭 | `Repos/athenaion/src/sets/shot2.js:168-210` | 实体墩柱、出框檐梁及沿檐藤蔓组成非闭合框；Repos/athenaion/src/world/shots.js:12-13 提供 shot2。只迁移几何框住远目标的做法，不复制到屏幕空间，不把机位插值当自动框景。src/world/worlds/place.js:535-546 可复用取景接口，场景摆位待验证。 | shot2 FOV=28.5°（源码）；pier width=1.16，原场景单位（源码）；near frame total occlusion=20–35%（建议迁移值） | MIT；几何/藤蔓生成器需连同依赖审查，不是单文件即插即用 / integrate | `src/world/worlds/place.js` |
| 中式幻想 RPG · 雾中巨像 | `none` | 原作源码未定位，许可待验证；邻接技术源 Repos/athenaion/src/ruins/portico.js:168-205; Repos/athenaion/src/world/shots.js:41-42：用近处实体框遮挡远目标的邻接路线；可用 street-1 门廊而非从零重造巨像；保持会面人物的屏幕空间，录像中的水道/像资产不在此源内；不是原作实现，画面一致性待验证。 | near frame total occlusion=20–35%（建议迁移值） | 原作待验证；邻接源 MIT，原作资产不可据此复制 / reference | `src/world/worlds/place.js` |

队列候选为 street-1 门廊、platform-1 窗景；匹配表 Twilight Canyon / Pluto Colony 分别提供 Street / Metro-Platform 的候选映射，仍须按表确认，不等于本批已实施。

源码快照（本批读取，不是新增截图来源）：
- `athenaion@9b8bd23b39c458a50fb1201037360047781c45b5`

已检索 `citadel/src`（含 `src/world/worlds/`）与 `lab/src`；本批未发现 `src/world/worlds/cardfx/` 目录或本卡同名预制模块。以上入口只表示可复用部分；首次完整落地才由执行者沉淀 cardfx，不在此虚构文件。title / atlas locked，任何队列用途均不解除锁定。

## 迁移到博客

street-1可从门廊后望远处目标，platform-1可用实体窗框；Shrine入口用檐和柱，Alley2用门洞。title / atlas locked，本卡不改这两个场景。只调整3D环境的取景，保持屏幕人物层的阅读空间。

搭配雾层分远近、侧光刻石；与满屏HUD和大标题叠压冲突。标题如果需要留左侧，就让框在右侧更厚，别挤占同一块位置。

## 反例

Sponza暗帘与墙体遮挡过多且缺乏中间调，观众很难分清框内到底要看哪一处。框景需要开口和目标同时成立，遮挡本身不是纵深。


[![Sponza · 本次偏暗机位](shots/04.png)](shots/04.png)
[Sponza · 本次偏暗机位](https://three-good-godrays.ameo.design/#sponza) · 暗帘堵住拱间开口，框内没有清楚目标。 仅评价本次画面。

[逐图来源与复现](SOURCE.md) · [返回视觉卡库](../../../README.md)
