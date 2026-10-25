# racing-game
实读相机类型、尾焰、刹车痕迹三个模块；README称CC0资产但本轮未核每个源资产。

## 案例档案

[来源仓库](https://github.com/pmndrs/racing-game)
分析版本：`7816a5d954b75e6ad853ae4e4f0cbbd628072643`

模型归属未独立认证。

## 初始源码审计边界

未读车身物理、轮胎接触/地形和完整音效链；Blender源模型未打开。

以下保留初始源码审计的观察范围。后续新增静帧独立列于视觉材料，不追溯证明全部机制或运行状态。

## 机制与案例分析

### [SD-RA01 · 让加速与刹车留下不同空间尺度的动作证据](../cards/SD-RA01.md)

加速短命尾焰说明当前状态，刹车地面痕迹保存刚发生的动作，两种时间尺度让运动有重量。

尾焰青#5ecfff、opacity .5；轮痕黑opacity .5且depthWrite=false；thumbnail只见暖峡谷低模赛道，未观察动作效果。

**Movie：reference** · 可借动作因果，但车内镜头通常看不到尾焰。
**前端：adapt** · 作为Ride第三人称或环境车辆小范围反馈。

失败条件：- 原skid位置直接用轮中心可能悬浮
- 每帧落痕密度依赖fps
- 环形index普通变量重渲可能重置
- 透明boost depthWrite=true可能遮挡

## 项目效果与观察材料

![racing-game · observed_still](../assets/previews/racing-game-44088d796a27.webp)

已view_image thumbnail.webp：橙色多面岩地形、浅隧道、深道路清晰分层；运动尚未观察。

来源：[原作者/出处](https://github.com/pmndrs/racing-game/blob/7816a5d954b75e6ad853ae4e4f0cbbd628072643/thumbnail.webp) · observed_still。静帧观察；没有由此验证连续动画或性能。

## 复用边界

- **status**：observed
- **evidence**：LICENSE.md代码MIT；README:9声称CC0 assets，未逐项独立核验
- **reuse**：conditional

图片及第三方素材的权利单独保留；源代码许可证不自动授权媒体。
