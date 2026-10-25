# SD-IP01 · 以同UV双版本贴图把素描逐步变为着色
案例：[ interactive-3d-portfolio ](../cases/interactive-3d-portfolio.md) · 机制证据：`still_observed`

效果图用于理解来源作品，不自动验证本卡中的每个机制。

## 设计动作

变化保留物体身份，观众能读到同一物件被赋色，而非整个画面简单交叉淡化。

## 实现与参数

onBeforeCompile改map_fragment；mask=(1-vMapUv.y)+noise(uv*15)*.15，threshold=uProgress*1.5，低于阈值替换paintedColor。

## 审美细节

源码注释称Standard但实际Basic；注释称blend但实际if硬切。已看og为黑白纸笔走廊，未看着色动画，不能宣传笔触平滑。

## 适用条件

- 两张图轮廓对应
- 无需真实受光

## 相邻方案与区别

与Folio世界径向discard不同，本卡保留对象并替换表面内容。

## 失败模式

- 不是PBR材质
- mask主要沿y而非真正对角线
- shader chunk版本兼容
- 未处理颜色转换路径需核对

## Movie 裁决

- **verdict**：adapt
- **reason**：适合回忆/文档局部揭示。

## Frontend 裁决

- **verdict**：reference
- **reason**：不应强套整个赛博城的纸笔风格。

## 最小对照

0/.25/.5/1四帧及动态比较，素描和着色轮廓完全对齐；色彩空间跳变或边界锯齿即失败。

## 源码证据

- [Repos/interactive-3d-portfolio/src/components/canvas/shaders/PaintRevealMaterial.jsx:14–47](https://github.com/Shaun520/interactive-3d-portfolio/blob/3f8e87827f09e1371c5a8829957b9a2e7cb1bc21/src/components/canvas/shaders/PaintRevealMaterial.jsx#L14-L47)：实际继承MeshBasicMaterial并缓存uProgress
- [Repos/interactive-3d-portfolio/src/components/canvas/shaders/PaintRevealMaterial.jsx:74–89](https://github.com/Shaun520/interactive-3d-portfolio/blob/3f8e87827f09e1371c5a8829957b9a2e7cb1bc21/src/components/canvas/shaders/PaintRevealMaterial.jsx#L74-L89)：噪声mask与阈值切换painted贴图

## 项目效果图

![interactive-3d-portfolio · observed_still](../assets/previews/interactive-3d-portfolio-1ae6478e3763.webp)

已view_image public/og-image.webp：白纸黑线走廊与人物；只观察历史封面，不证明绘制转场。

来源：[原作者/出处](https://github.com/Shaun520/interactive-3d-portfolio/blob/3f8e87827f09e1371c5a8829957b9a2e7cb1bc21/public/og-image.webp) · observed_still。静帧观察；没有由此验证连续动画或性能。

## 归纳与练习

暂未归入新增专业视角；保留原机制边界。

保留独立案例。
