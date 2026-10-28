# 风化依附形体

分组：材质 · 主维度：E 表面状态、D 破损层级、A 侧光、B 低饱和、I 时间痕迹 · 情绪：古老、遗迹

## 一句话

让磨损发生在边缘、接缝和暴露面，而不是给全部表面撒同一种噪点。

[![Athenaion · Grand staircase](shots/02.jpg)](shots/02.jpg)
[Athenaion · Grand staircase](https://github.com/Leonxlnx/athenaion) · 石阶的缺角、裂隙草和局部斑驳把规则台阶打散，但台阶轮廓仍连续。

| 参考 | 参考 |
|---|---|
| [![Athenaion · Fallen head](shots/01.jpg)](shots/01.jpg) | [![Athenaion · Ruined portico](shots/03.jpg)](shots/03.jpg) |
| [Athenaion · Fallen head](https://github.com/Leonxlnx/athenaion) · 斑驳与叶片沿残头像表面和边缘分布，受光大面仍然连续。 | [Athenaion · Ruined portico](https://github.com/Leonxlnx/athenaion) · 近柱断口与地面缝隙有局部草与小孔，未把每个完整面均匀染脏。 |
## 看哪里

1. Athenaion · Grand staircase：石阶的缺角、裂隙草和局部斑驳把规则台阶打散，但台阶轮廓仍连续。
2. Athenaion · Fallen head：斑驳与叶片沿残头像表面和边缘分布，受光大面仍然连续。
3. Athenaion · Ruined portico：近柱断口与地面缝隙有局部草与小孔，未把每个完整面均匀染脏。

## 拆解

本卡三图来自同一作者场景的不同机位，是一种材料处理的多尺度观察，不作为跨作品共识。数值为画面估计。

- **E · 状态分布**：巨像脸部的斑驳是不规则灰块，右侧叶片沿破损边缘覆盖；台阶草主要从缝里长出，没有随机悬浮在完整踏面中央。
- **D · 大中小破损**：门廊先读到缺失的整段柱，再读到地上直径约画宽1/6的柱鼓，最后看近柱针点状孔洞。破损有尺度层级，微孔不能替代大缺口。
- **A · 光的揭示**：低角度侧光把踏步边缘和柱鼓纹理照亮，凹陷保持暗；不能只靠黑色贴图假装所有孔洞。
- **B · 色域**：主体仍维持米灰、灰褐与苔绿三组低饱和色，斑点大多仅比底材暗一至两档；整体不会变成纯黑脏块。
- **I · 时间层**：完整神殿在远处，近处头像倒落、藤蔓覆盖，两种保存状态同框，暗示历史层次。是否仍被使用，需另加人物、灯火或维护活动，不能由完好的远殿单独断言。

## 做法

先区分完好结构与破坏结构，再分别放边缘崩损、积灰与裂隙植被。程序噪声应经过位置或形体遮罩，避免每个面长得一样。

- **可见做法的界限**：本轮不据截图断言作者具体使用了曲率、顶点色或某张贴图；可在[原作代码](https://github.com/Leonxlnx/athenaion/tree/9b8bd23b39c458a50fb1201037360047781c45b5/src)继续查对应材质。
- **迁移试验值**：先把大面积磨损限制在可见表面的10–20%，最深破损留在少数边角；粗糙度先试0.75–0.95。上述都是Blog试验范围，不是作者参数。

### 实现索引

2026-10-28 源码阅读补索引；不新增截图、不改上方视觉判断。上方“不能由截图推出/尚未审 shader”等界限指原视觉阶段，本节另列本批核过的源码。`Repos/` 相对 `~/Blog/`，Citadel 路径相对 `~/Blog/citadel/`。本批未运行这些源码测量参数，标为“源码”的值不得当作实测。

| 作品 | 源码（本地路径:行） | 技术与接入边界 | 参数（来源） | 许可 / 复用档 | Citadel 已有可复用入口 |
|---|---|---|---|---|---|
| Athenaion · Grand staircase | `Repos/athenaion/src/ruins/materials.js:131-158,207-215,284-317` | 已读到石材按 cav 凹腔、aux.y 边缘和法线朝向遮罩积垢、崩边与藻苔；不是由截图猜曲率。台阶具体几何属性生成链本批待验证，不把通用 shader 当 shot6 全链已核。先复用 Citadel lab/src/scenes/Shrine/decor.js:69-86 已按缝/阶鼻坐标布置苔与裂缝的路线，再决定是否移植材质。 | ruinStone default roughness=0.72（源码）；ruinStone default crust / edges=0.8 / 0.6（源码）；weathering area=可见面 10–20%（建议迁移值） | MIT；如移植需携带 core/materials.js、glsl/rng 依赖与 cav/aux 属性，保留声明 / integrate | `lab/src/scenes/Shrine/decor.js` |
| Athenaion · Fallen head | `Repos/athenaion/src/ruins/materials.js:165-187,299-307` | RN_HEAD 分支使用 cavity、aux.z 天空可见度和 aux.w 头发分类，让污迹按形体分布；默认 ensureCav 不能凭空生成真实凹腔。Repos/athenaion/src/core/materials.js:65-89 负责 shader hooks。Citadel lab/src/scenes/Shrine/decor.js:69-86 只可复用依附结构的 decal 思路，不具有该头像属性；迁移属性生成与兼容性待验证。 | required channels=cav; aux.y=edge, aux.z=sky, aux.w=hair（源码）；migration roughness=0.75–0.95（建议迁移值） | MIT；头像资产与属性生成需另核，未声称可只复制一段 GLSL / integrate | `lab/src/scenes/Shrine/decor.js` |
| Athenaion · Ruined portico | `Repos/athenaion/src/ruins/portico.js:292-329,345-386` | 固定种子生成地砖边缘崩损与 cavity；缺砖避开主通道，裂缝与草从接缝生长，再交给 ruinStoneMaterial；这是同项目 shot9 可核的几何路线，不代称 shot6 台阶源码。Citadel lab/src/scenes/Shrine/decor.js:81-86 的 ST 坐标阶鼻贴片可先复用到 corridor/door-305 边缝，坐标需按场景重算。 | wearW=0.035 + 0.07 * chipN²（源码）；citadel stair decal opacity=crack 0.35 / moss 0.3（源码）；weathering area=可见面 10–20%（建议迁移值） | MIT；移植保留声明，优先现成 Citadel decal，材质与几何链联动 / integrate | `lab/src/scenes/Shrine/decor.js` |

本卡为高频补索引项；队列仅在 self-residence-corridor-1 / door-305 存在合理边缝时试验，匹配表未直接命中。现代维护良好的墙面不应整面做旧；Shrine 现成 decal 是复用入口而非自动属性烘焙。

源码快照（本批读取，不是新增截图来源）：
- `athenaion@9b8bd23b39c458a50fb1201037360047781c45b5`

已检索 `citadel/src`（含 `src/world/worlds/`）与 `lab/src`；本批未发现 `src/world/worlds/cardfx/` 目录或本卡同名预制模块。以上入口只表示可复用部分；首次完整落地才由执行者沉淀 cardfx，不在此虚构文件。title / atlas locked，任何队列用途均不解除锁定。

## 迁移到博客

Shrine入口台阶可把草与磨损集中在边缘；BlackCityHall登记场景可让近处残构件与远处完整建筑形成时间对照。不要把所有地点都统一做旧，维护状态应服务各场景故事。

搭配侧光刻石、近框套远景；与全表面均匀污迹、强雾和过黑调色冲突。先确保400px缩图能看到大缺口，再决定微孔是否值得增加。

## 反例

Sponza偏暗机位中的表面差异被压没；即使再添加污渍和法线，小图也看不出时间痕迹。材料卡不能绕过照明和取景的问题。


[![Sponza · 本次偏暗机位](shots/04.png)](shots/04.png)
[Sponza · 本次偏暗机位](https://three-good-godrays.ameo.design/#sponza) · 暗部把石墙、柱脚的表面差异压没，不能据此读出风化位置。 仅评价本次画面。

[逐图来源与复现](SOURCE.md) · [返回视觉卡库](../../../README.md)
