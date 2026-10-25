# mesh2motion-app
实读AnimationPlayer与导出清理。实际看了readme.png历史静帧：模型占主视口、右侧动作网格、底部时间轴；未播放动画。

## 案例档案

[来源仓库](https://github.com/Mesh2Motion/mesh2motion-app)
分析版本：`653a9698f5f315523072f1c3ff3496100401317b`

模型归属未独立认证。

## 初始源码审计边界

未读自动绑定、蒙皮权重、retarget/道具全链；历史截图不证明绑定或运动质量。

以下保留初始源码审计的观察范围。后续新增静帧独立列于视觉材料，不追溯证明全部机制或运行状态。

## 机制与案例分析

### [CN-018 · 拖动时间轴时临时暂停并恢复用户原先播放意图](../cards/CN-018.md)

拖动时间轴时临时暂停并恢复用户原先播放意图。这是由该仓实现提炼的候选操作，跨项目效果待验证。

源历史readme.png已实际查看：左大模型+右动作缩略网格，底部明确Run和时间轴，适合审片工具操作。

**Movie：adapt** · 适合作为movie审查播放器的交互参考
**前端：reference** · 只建议内部预览，不给访客增加编辑器

失败条件：- 此片段仅mousedown/up未见pointercancel，会有拖出后不恢复风险
- 固定30fps标签不能假称原动画采样率

### [CN-019 · 导出前清除失去目标的动画轨并保证时间严格递增](../cards/CN-019.md)

导出前清除失去目标的动画轨并保证时间严格递增。这是由该仓实现提炼的候选操作，跨项目效果待验证。

资产在编辑器里能动不代表导出后绑定完整；这是交付完整性机制，不是美术风格。

**Movie：reference** · 离线镜头使用导出动画前有价值
**前端：defer** · 本轮2D角色和静态场景无需新骨骼管线

失败条件：- 静默删轨可能掩盖错误删骨
- 去重可能改变极密运动，需要比较关键姿态

## 项目效果与观察材料

![mesh2motion-app · historical_still_viewed](../assets/previews/mesh2motion-app-65a78a4bde4a.png)

历史静帧实际查看：左侧模型主视口、右侧动画缩略列表、底部Run时间轴；不能验证真实运动或绑定质量。

来源：[原作者/出处](https://github.com/Mesh2Motion/mesh2motion-app/blob/653a9698f5f315523072f1c3ff3496100401317b/readme.png) · historical_still_viewed。静帧观察；没有由此验证连续动画或性能。

## 复用边界

- **status**：observed
- **evidence**：LICENSE-MIT.MD: 所有代码MIT；LICENSE-CC0.MD: 3D模型、blend、rig、动画CC0
- **reuse**：direct_with_notice

图片及第三方素材的权利单独保留；源代码许可证不自动授权媒体。
