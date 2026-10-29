# 巨像越画框

分组：造型尺度 · 主维度：D 局部识别、C 果断裁切、G 近身透视、A 轮廓可读、I 压迫 · 情绪：压迫、敬畏

[![云上石像](shots/01.jpg)](shots/01.jpg)

云上石像 · 膝与手臂越出下方与画面左侧，脸与手势仍足以确认巨大人形。

| 参考 | 参考 |
|---|---|
| [![中式幻想 RPG · 雾中巨像](shots/02.jpg)](shots/02.jpg) | [![Unreal 云上神殿与巨龙](shots/03.jpg)](shots/03.jpg) |
| 中式幻想 RPG · 雾中巨像 · 两侧巨像的冠顶和身体被边框截断，中间水道仍能通行。 | Unreal 云上神殿与巨龙 · 巨龙头与长须挤入近景，廊柱和小人物提供另一个尺度。 |

## 一句话

只让巨物的一部分进入画面，同时留下熟悉轮廓，观众会主动补全框外的体量。

## 看哪里

1. **云上石像**：膝与手臂越出下方与画面左侧，脸与手势仍足以确认巨大人形。
2. **中式幻想 RPG · 雾中巨像**：两侧巨像的冠顶和身体被边框截断，中间水道仍能通行。
3. **Unreal 云上神殿与巨龙**：巨龙头与长须挤入近景，廊柱和小人物提供另一个尺度。

## 拆解

比例为原图目估区间，不是相机实参或场景米制测量；位置用归一化画幅描述。

- **D · 识别线索**：图1脸、肩、手仍构成人形，图3角、下颌与须提供龙的线索；不靠一块无从辨认的石皮。图1头部约在画面上1/3，膝部则压至底边。
- **C · 边界切断**：图1左侧手臂与下部膝腿越框，图2两侧像的上部/侧缘越框；图2两像之间的亮口约画宽16–22%（随所取高度变化）。不是把识别线全部切掉。
- **G · 近身关系**：图1近膝与脸有明显远近差，图3龙头近于廊柱；原作FOV未知，不从成片臆测镜头参数。迁移先用既有60°机位，不把广角本身当巨物。
- **A · 连续边缘**：图1浅像贴蓝天，图2深像贴灰雾；至少一侧长边在出框前连续可读，避免纯黑贴边成为黑条。
- **I · 人的标尺**：图2左前景船棚、图3廊柱与人物保留常见尺度；小物高度明显小于巨物局部。缺少参照时，这种裁切也可能只是小雕塑特写。

## 做法

完整形体与取景分开处理，留出真实框外体积供视差。原视频未取得源码，三条索引按不同缺口分别说明，不再复制同一“buildColossus+裁切”句式。Athenaion shot5 保留整个头盔，只能作为相机配置结构参考，不能证明本卡构图。

### 实现索引

路径相对 `~/Blog/`；citadel 栏相对 `~/Blog/citadel/`。源码默认值不是旧截图的已验证运行实参；建议迁移值仍需目标场景实看。`source: none` 不以邻接源冒充原作算法。

| 作品 | 源码 / 技术与边界 | 参数及性质 | 许可 / 复用 | citadel 已有实现 |
|---|---|---|---|---|
| 云上石像 | `none`；原作资产/源码未取得；邻接 Repos/athenaion/src/modules/statues.js:197-269 的 buildColossus(engine,variant,size,pedH,detail,opts) 可生成完整站立持盾像，依赖骨架、盾矛与材质模块，不是石佛。src/world/shots.js:24-25 的 shot5 明确保留整盔，不是裁切范例；只借完整形体与取景可分离的组织方式。 | 邻接模型 s=size/2.0（源码）；转译识别线=至少保留脸/手势一组（建议迁移值） | 原视频许可未明；邻接 MIT / reference | `lab/src/scenes/BlackCityAquarium/index.js:130-140` |
| 中式幻想 RPG · 雾中巨像 | `none`；原作源码未取得；邻接 Repos/athenaion/src/world/shots.js:24-42 提供 position/target/fov 相机预设结构，不提供图中的双侧巨像、河道或雾算法。两侧出框须独立验证；不能把 shot5 whole helmet 称为现成出框机位。 | 中部通道=保留约1/4画宽（建议迁移值）；镜头起点=citadel look-up FOV60°（建议迁移值） | 原视频许可未明；邻接 MIT / reference | `lab/src/scenes/BlackCityAquarium/index.js:130-140` |
| Unreal 云上神殿与巨龙 | `none`；原作龙资产/源码未取得；邻接 Repos/athenaion/src/modules/statues.js:197-269 仅提供组装完整巨物的层级方式，不生成龙头、须或动画。Citadel 已有右窗怪物的头、獠牙和框外躯干，不需要先重造一条龙；其长躯/触须可提供局部识别。 | 已有 citadel 躯干顶=y=5m（源码）；已有 citadel 躯干细分=seg80 / radial22（源码） | 原视频许可未明；邻接 MIT / reference | `lab/src/scenes/BlackCityAquarium/tank.js:288-322` |


## 迁移到博客

落点严格为 `black-city-2`（aquarium），不是 `black-city-1`（hall）。初始注册见 `src/game/places.js:452`；实际开放覆盖见 `src/game/placeBatches/b6-blackcity.js:48-49`。已有 `lab/src/scenes/BlackCityAquarium/tank.js:288-322` 的怪物躯干伸到y=5m、头/獠牙与触须跨过右窗，非新造工业立面。入口：`window.__rig.placeApi.goView("beast", true)`，对应 `index.js:133` position=[1.15,1.15,.85]、target=[2.15,1.65,-2.75]、FOV60°、DOF关闭；再与 `look-up`（position=[-.2,1.1,.5] target=[-.3,3.4,-3.5]）对照。建议只微调现有取景，保留獠牙/头部与窗框标尺、让躯干继续越上边；截图需等站内两次新draw，不直调api.render。已有怪物是复用对象，并不声称已经完成本卡验收。搭配 `card:scale-by-familiar-objects`、`card:backlight-reveals-silhouette`；与全物展示的俯瞰镜头冲突。Shrine无已核实巨像落点，删除该建议；title/atlas不动，人物前景不得被遮脸。

## 反例

浮岛把底座、树与外边界一次交代完，读起来像掌上模型；这在展示模型时是优点，却抵消本卡框外延伸。反例只针对观看关系，不评判整件作品。

[![水牛露营 · 浮岛](shots/04.jpg)](shots/04.jpg)

水牛露营 · 浮岛 · 从顶到底都看完的浮岛，让观众立刻知道模型边界。

[逐图来源与复现](SOURCE.md) · [返回视觉卡库](../../../README.md)
