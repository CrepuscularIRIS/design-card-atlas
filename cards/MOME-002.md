# MOME-002 · 让同一发光事件同时改变灯体、受光面、空气和水面
案例：[ map-of-middle-earth ](../cases/map-of-middle-earth.md) · 机制证据：`still_observed`

效果图用于理解来源作品，不自动验证本卡中的每个机制。

## 设计动作

mount-doom历史图有暖岩浆与烟底红光、冷灰远山，灯体与环境颜色相互解释。代码把控制通道统一，减少只有发光贴片没有邻近受光的漂浮感；静图不能确认事件切换正确。

## 实现与参数

night=smoothstep(.2,.7,night)+.4*twilight；dusk=.25+.75*max(night,golden)；事件beacons/morgul-beam共享槽。受光E=c/(1+(d/r0)^2)，WRAP=.3，reach处平滑归零；halo cap=.12对数压缩。最多8个spill，preview4（不是物理完整多光源）。

## 审美细节

mount-doom历史图有暖岩浆与烟底红光、冷灰远山，灯体与环境颜色相互解释。代码把控制通道统一，减少只有发光贴片没有邻近受光的漂浮感；静图不能确认事件切换正确。

## 适用条件

- 表面材质能接收共同灯数据
- 事件和昼夜状态有统一来源

## 相邻方案与区别

区别于全屏bloom：bloom只扩散亮像素，不能提供与位置/法线一致的邻近受光。可先用现有点光源完成此关系，再考虑本仓TSL实现。

## 失败模式

- 该spill没有真实遮挡阴影，会穿墙漏光
- 灯数筛选是近似，英雄光应单独核对
- CPU/GPU公式后续改动可能漂移

## Movie 裁决

- **verdict**：prototype
- **reason**：在一处信号灯/火源检验环境反馈即可。

## Frontend 裁决

- **verdict**：adapt
- **reason**：需保留自由走动时的遮挡与选光稳定性，不搬整套WebGPU渲染器。

## 最小对照

保持相机曝光固定，仅切换事件0/1：灯体、墙面、雾和水是否同步；背墙被照亮、灯灭而水面光斑不灭即失败。

## 源码证据

- [Repos/map-of-middle-earth/src/materials/gates.ts:9–35](https://github.com/earthwalker17/map-of-middle-earth/blob/696e968e9d550327beda9e663ef5aec6961583c9/src/materials/gates.ts#L9-L35)：统一night/nightDim/dusk/always/event语义
- [Repos/map-of-middle-earth/src/materials/gates.ts:73–115](https://github.com/earthwalker17/map-of-middle-earth/blob/696e968e9d550327beda9e663ef5aec6961583c9/src/materials/gates.ts#L73-L115)：TSL gate与CPU mirror使用相同阈值和事件槽
- [Repos/map-of-middle-earth/src/emission/spillSources.ts:289–337](https://github.com/earthwalker17/map-of-middle-earth/blob/696e968e9d550327beda9e663ef5aec6961583c9/src/emission/spillSources.ts#L289-L337)：选择受光源时调用gateCPU并上传光位/强度/halo/glint
- [Repos/map-of-middle-earth/src/emission/spill.ts:61–86](https://github.com/earthwalker17/map-of-middle-earth/blob/696e968e9d550327beda9e663ef5aec6961583c9/src/emission/spill.ts#L61-L86)：有限核心衰减与柔和终止窗计算表面受光
- [Repos/map-of-middle-earth/src/emission/spill.ts:96–128](https://github.com/earthwalker17/map-of-middle-earth/blob/696e968e9d550327beda9e663ef5aec6961583c9/src/emission/spill.ts#L96-L128)：射线空气散射采用对数压缩防止平顶光盘
- [Repos/map-of-middle-earth/src/materials/families.ts:610–644](https://github.com/earthwalker17/map-of-middle-earth/blob/696e968e9d550327beda9e663ef5aec6961583c9/src/materials/families.ts#L610-L644)：建筑材质和发光覆盖层显式接受spill
- [Repos/map-of-middle-earth/src/water/waterMaterial.ts:446–453](https://github.com/earthwalker17/map-of-middle-earth/blob/696e968e9d550327beda9e663ef5aec6961583c9/src/water/waterMaterial.ts#L446-L453)：水面同时接受GGX光斑和漫射受光

## 项目效果图

![map-of-middle-earth · historical_still_viewed](../assets/previews/map-of-middle-earth-9732ef806c0e.jpg)

已查看的来源静帧；不证明当前版本运行。

来源：[原作者/出处](https://github.com/earthwalker17/map-of-middle-earth/blob/696e968e9d550327beda9e663ef5aec6961583c9/docs/images/lake-town.jpg) · historical_still_viewed。静帧观察；没有由此验证连续动画或性能。

![map-of-middle-earth · historical_still_viewed](../assets/previews/map-of-middle-earth-c4a392f4439d.jpg)

已查看的来源静帧；不证明当前版本运行。

来源：[原作者/出处](https://github.com/earthwalker17/map-of-middle-earth/blob/696e968e9d550327beda9e663ef5aec6961583c9/docs/images/mount-doom.jpg) · historical_still_viewed。静帧观察；没有由此验证连续动画或性能。

## 归纳与练习

[CINE-04](../lenses/CINE-04.md)

[MP-03](../patterns/MP-03.md)
