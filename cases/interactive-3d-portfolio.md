# interactive-3d-portfolio
已读揭示shader、滚轮相机和读屏层；明确源码注释与实际Basic/hard-step实现的差异。

## 案例档案

[来源仓库](https://github.com/Shaun520/interactive-3d-portfolio)
分析版本：`3f8e87827f09e1371c5a8829957b9a2e7cb1bc21`

模型归属未独立认证。

## 初始源码审计边界

未深读无限走廊/传送状态机/房间组件；全局wheel preventDefault方案不建议搬进本站阅读界面。

以下保留初始源码审计的观察范围。后续新增静帧独立列于视觉材料，不追溯证明全部机制或运行状态。

## 机制与案例分析

### [SD-IP01 · 以同UV双版本贴图把素描逐步变为着色](../cards/SD-IP01.md)

变化保留物体身份，观众能读到同一物件被赋色，而非整个画面简单交叉淡化。

源码注释称Standard但实际Basic；注释称blend但实际if硬切。已看og为黑白纸笔走廊，未看着色动画，不能宣传笔触平滑。

**Movie：adapt** · 适合回忆/文档局部揭示。
**前端：reference** · 不应强套整个赛博城的纸笔风格。

失败条件：- 不是PBR材质
- mask主要沿y而非真正对角线
- shader chunk版本兼容
- 未处理颜色转换路径需核对

### [SD-IP02 · 让空间入口与语义HTML共用内容和导航动作](../cards/SD-IP02.md)

3D表现可以变化，但内容和可到达路径不应只存在画布内部。

与纸笔风格无关；这是前端内容可达性模式，不是美术画质机制。

**Movie：reject** · 不影响电影镜头画质。
**前端：prototype** · 适用于3D环境中的博客内容入口。

失败条件：- 隐藏DOM不等于完整可访问
- 当前overlay部分介绍硬编码
- 源码未证实初始入场的可操作键盘入口

## 项目效果与观察材料

![interactive-3d-portfolio · observed_still](../assets/previews/interactive-3d-portfolio-1ae6478e3763.webp)

已view_image public/og-image.webp：白纸黑线走廊与人物；只观察历史封面，不证明绘制转场。

来源：[原作者/出处](https://github.com/Shaun520/interactive-3d-portfolio/blob/3f8e87827f09e1371c5a8829957b9a2e7cb1bc21/public/og-image.webp) · observed_still。静帧观察；没有由此验证连续动画或性能。

## 复用边界

- **status**：observed
- **evidence**：LICENSE:1-21 为 MIT，保留版权与许可；本轮只对代码作此判读
- **reuse**：direct_with_notice

图片及第三方素材的权利单独保留；源代码许可证不自动授权媒体。
