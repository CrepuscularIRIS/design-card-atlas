# 3DTilesRendererJS
地理瓦片渲染库，本轮只提取fade连续性案例，不宣称提供高质量场景设计。

## 案例档案

[来源仓库](https://github.com/NASA-AMMOS/3DTilesRendererJS)
分析版本：`eb6ea84c74fa38ad3c8151aeba877520289485f2`

模型归属未独立认证。

## 初始源码审计边界

未读core加载/缓存完整逻辑、Cesium/Google示例资产、Babylon/R3F适配；未运行瓦片LOD。

以下保留初始源码审计的观察范围。后续新增静帧独立列于视觉材料，不追溯证明全部机制或运行状态。

## 机制与案例分析

### [SD-TI01 · 在LOD交接时保留旧几何直到抖动淡出结束](../cards/SD-TI01.md)

减少大块pop-in需要把可见性转换和资源回收分开，不只是插值opacity。

这是连续性处理，不产生新的建筑细节；抖动颗粒在小字号/细栏杆附近可能更明显。

**Movie：defer** · 固定hero镜头不应以LOD抖动作为首要美术改进。
**前端：reference** · 只有实证存在LOD跳变才提取局部机制。

失败条件：- shader chunk兼容问题
- Bayer pattern本身可见
- 性能优化后置

## 项目效果与观察材料

![3DTilesRendererJS · author_demo_banner](../assets/previews/scene-3dtilesrendererjs-1.png)

实际查看：火星地形的摄影纹理和岩石细节上叠加白色瓦片边界，底部为项目标题。

来源：本轮已观察的历史截图 · author_demo_banner。原作者README渲染展示横幅，确有地形效果；带标题的静态展示，不是本轮运行截图，也不能证明LOD淡出动画。

![3DTilesRendererJS · author_demo_banner](../assets/previews/scene-3dtilesrendererjs-2.png)

实际查看：同块地形以平面分区、等高线和灰度细节三种表示并列，能比较轮廓和表面信息层。

来源：本轮已观察的历史截图 · author_demo_banner。原仓展示横幅，包含真实地形可视化效果与项目字样；不是单个现场运行状态。

## 复用边界

- **status**：observed
- **evidence**：LICENSE Apache2.0；shader注明一段Bayer参考Shadertoy，具体外部数据供应商权利独立
- **reuse**：conditional

图片及第三方素材的权利单独保留；源代码许可证不自动授权媒体。
