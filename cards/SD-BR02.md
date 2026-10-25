# SD-BR02 · 把低成本混凝土噪声限制为底材，而不冒充完整PBR
案例：[ TheBrutalizer ](../cases/TheBrutalizer.md) · 机制证据：`still_observed`

效果图用于理解来源作品，不自动验证本卡中的每个机制。

## 设计动作

微色差能破除纯色，但不能让同一颜色纹理同时承担所有物理通道。

## 实现与参数

128² Canvas填底色，5000点±10灰度变化；map与roughnessMap复用，默认roughness=.8/metalness=.2，关闭mipmap。

## 审美细节

历史图整体灰度接近，细纹不足以说明真实混凝土尺度。

## 适用条件

- 远景
- 无需可辨识材质纹理

## 相邻方案与区别

与真实粗糙度/法线贴图不同，它仅是色噪声；不应列为高质量材质资产。

## 失败模式

- 颜色亮度耦合roughness
- 关mipmap可能远处闪烁
- 无seed

## Movie 裁决

- **verdict**：reference
- **reason**：可供远景廉价底材。

## Frontend 裁决

- **verdict**：reject
- **reason**：不作为当前PBR升级方案，现有pbr管线更适合。

## 最小对照

侧光、近远距离比较：纹理无方向/尺度细节或远处闪烁则弃用。

## 源码证据

- [Repos/TheBrutalizer/src/utils/textureLoader.js:4–47](https://github.com/KrishGaur1354/TheBrutalizer/blob/ec8708101d5debb8cd61d2a6bbdee75edde91b91/src/utils/textureLoader.js#L4-L47)：128纹理5000噪点、color map同时作roughnessMap

## 项目效果图

![TheBrutalizer · observed_still](../assets/previews/TheBrutalizer-d1d734604634.jpg)

已view_image built.jpg：灰塔/黑窗/绿树历史静帧；未运行动画。

来源：[原作者/出处](https://github.com/KrishGaur1354/TheBrutalizer/blob/ec8708101d5debb8cd61d2a6bbdee75edde91b91/built.jpg) · observed_still。静帧观察；没有由此验证连续动画或性能。

## 归纳与练习

暂未归入新增专业视角；保留原机制边界。

[MP-05](../patterns/MP-05.md)
