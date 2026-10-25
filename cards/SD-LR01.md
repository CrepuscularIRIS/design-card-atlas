# SD-LR01 · 一次落雨同时写入短期湿痕与长期生长记忆
案例：[ little-rain-cloud ](../cases/little-rain-cloud.md) · 机制证据：`still_observed`

效果图用于理解来源作品，不自动验证本卡中的每个机制。

## 设计动作

让行为改变环境的可见历史：湿润会消退，生长留下，回头看才读得出刚才做过什么。

## 实现与参数

雨滴碰到groundH→paintWet：R增amt*w*22、G增amt*max(0,1-d²/3.2)*9；同一次命中再以0.5概率spawnGrass。R每0.3s减2，G不衰减。注意真实因果是“落点事件→湿图”和“落点事件→植被”并行，代码没有读取湿度阈值来决定长草。

## 审美细节

暖沙上湿痕变深、绿线保留，生长边界比湿区窄；每次4株、出生时间错开≤0.4s。看过04-look-back静帧，绿色曲线在大尺度沙丘上成立，未看动画。

## 适用条件

- 世界坐标能稳定映射地面
- 痕迹区域在回望镜头中可见
- 明确长期状态是否需要存盘

## 相邻方案与区别

与racing-game轮痕同属动作留痕，但此处区分消退和永久改变；与纯贴花不同附带延迟几何生长。

## 失败模式

- 512米正方形域外不留痕
- 实例环形池会覆盖旧草而G仍保留
- 草密度以计数而非湿度控制，不能称生态模拟
- Math.random使重复录制不等同

## Movie 裁决

- **verdict**：prototype
- **reason**：一次行动→改变地表→回望读历史，适合完整短镜头结构。

## Frontend 裁决

- **verdict**：adapt
- **reason**：可收敛为一块可交互地表，非要求重建开放世界。

## 最小对照

固定落点与时刻，记录事件数、R/G值和草实例数；停雨后R变淡、G保留，回望镜头仍读出路径；越界写入、无事件长草、痕迹错位任一失败。

## 源码证据

- [Repos/little-rain-cloud/main.js:123–151](https://github.com/dososo/little-rain-cloud/blob/8180c1b1c98e993bad05e77eb596d472ce2910cd/main.js#L123-L151)：512×512湿度图，R湿润与G绿化采用不同半径与累积速率
- [Repos/little-rain-cloud/main.js:357–371](https://github.com/dososo/little-rain-cloud/blob/8180c1b1c98e993bad05e77eb596d472ce2910cd/main.js#L357-L371)：落点独立触发草实例，每格计数限制密度
- [Repos/little-rain-cloud/main.js:902–935](https://github.com/dososo/little-rain-cloud/blob/8180c1b1c98e993bad05e77eb596d472ce2910cd/main.js#L902-L935)：雨滴击地后分别调用paintWet与spawnGrass/Flower
- [Repos/little-rain-cloud/main.js:963–973](https://github.com/dososo/little-rain-cloud/blob/8180c1b1c98e993bad05e77eb596d472ce2910cd/main.js#L963-L973)：只衰减R，G保留；每3个dirty帧上传

## 项目效果图

![little-rain-cloud · observed_still](../assets/previews/little-rain-cloud-f483b6c2dde7.png)

已view_image shots/04-look-back.png：暖沙丘、白云、深湿痕与绿色曲线；它是历史静帧，只支持构图判断，不支持动画或当前运行验收。

来源：[原作者/出处](https://github.com/dososo/little-rain-cloud/blob/8180c1b1c98e993bad05e77eb596d472ce2910cd/shots/04-look-back.png) · observed_still。静帧观察；没有由此验证连续动画或性能。

## 归纳与练习

[CINE-06](../lenses/CINE-06.md)

[MP-06](../patterns/MP-06.md) / [MP-23](../patterns/MP-23.md)
