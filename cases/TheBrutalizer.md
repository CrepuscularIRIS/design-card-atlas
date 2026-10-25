# TheBrutalizer
入口链确认使用Building.jsx；实见参数尺寸/随机性缺陷，不能把仓名当质量背书。

## 案例档案

[来源仓库](https://github.com/KrishGaur1354/TheBrutalizer)
分析版本：`ec8708101d5debb8cd61d2a6bbdee75edde91b91`

模型归属未独立认证。

## 初始源码审计边界

未深读车辆/分享/物理全链；buildingGenerator工具仅部分读；不声称整仓均有问题。

以下保留初始源码审计的观察范围。后续新增静帧独立列于视觉材料，不追溯证明全部机制或运行状态。

## 机制与案例分析

### [SD-BR01 · 从按层退台提取轮廓，但把窗面绑定真实楼层尺寸](../cards/SD-BR01.md)

参数建筑要让开口、楼层和附属体共享尺寸来源；该仓同时提供可借轮廓与明确反例。

built.jpg历史图可见灰色主量、黑色窗孔、层间凹口和绿树；仅能说明静态构图，不证明生成器无错位。

**Movie：reference** · 保留块体节奏，不直接当hero建筑资产。
**前端：defer** · 许可和错位问题清理后再考虑集成。

失败条件：- 未seed的Math.random让扩展和门不稳定
- retreat层窗仍在原表面
- utils生成器不是当前Building实现

### [SD-BR02 · 把低成本混凝土噪声限制为底材，而不冒充完整PBR](../cards/SD-BR02.md)

微色差能破除纯色，但不能让同一颜色纹理同时承担所有物理通道。

历史图整体灰度接近，细纹不足以说明真实混凝土尺度。

**Movie：reference** · 可供远景廉价底材。
**前端：reject** · 不作为当前PBR升级方案，现有pbr管线更适合。

失败条件：- 颜色亮度耦合roughness
- 关mipmap可能远处闪烁
- 无seed

## 项目效果与观察材料

![TheBrutalizer · observed_still](../assets/previews/TheBrutalizer-d1d734604634.jpg)

已view_image built.jpg：灰塔/黑窗/绿树历史静帧；未运行动画。

来源：[原作者/出处](https://github.com/KrishGaur1354/TheBrutalizer/blob/ec8708101d5debb8cd61d2a6bbdee75edde91b91/built.jpg) · observed_still。静帧观察；没有由此验证连续动画或性能。

## 复用边界

- **status**：unknown
- **evidence**：README.md License节与package.json声明ISC，未见根LICENSE；与本项目CLAUDE.md MIT叙述冲突
- **reuse**：idea_only

图片及第三方素材的权利单独保留；源代码许可证不自动授权媒体。
