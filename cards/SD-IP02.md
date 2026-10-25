# SD-IP02 · 让空间入口与语义HTML共用内容和导航动作
案例：[ interactive-3d-portfolio ](../cases/interactive-3d-portfolio.md) · 机制证据：`still_observed`

效果图用于理解来源作品，不自动验证本卡中的每个机制。

## 设计动作

3D表现可以变化，但内容和可到达路径不应只存在画布内部。

## 实现与参数

useScene提供当前房间/teleportTo；useSiteConfig提供rooms；sr-only nav在走廊渲染入口，房内渲染返回及内容。

## 审美细节

与纸笔风格无关；这是前端内容可达性模式，不是美术画质机制。

## 适用条件

- 内容模型统一
- 动作可被DOM调用

## 相邻方案与区别

与只加aria-label不同，提供真正可执行的导航和内容。

## 失败模式

- 隐藏DOM不等于完整可访问
- 当前overlay部分介绍硬编码
- 源码未证实初始入场的可操作键盘入口

## Movie 裁决

- **verdict**：reject
- **reason**：不影响电影镜头画质。

## Frontend 裁决

- **verdict**：prototype
- **reason**：适用于3D环境中的博客内容入口。

## 最小对照

不用鼠标和WebGL拾取仍可读同一项目并返回；焦点丢失/内容版本分叉即失败。

## 源码证据

- [Repos/interactive-3d-portfolio/src/components/ui/ScreenReaderOverlay.jsx:12–27](https://github.com/Shaun520/interactive-3d-portfolio/blob/3f8e87827f09e1371c5a8829957b9a2e7cb1bc21/src/components/ui/ScreenReaderOverlay.jsx#L12-L27)：rooms配置同源与skip链接
- [Repos/interactive-3d-portfolio/src/components/ui/ScreenReaderOverlay.jsx:38–75](https://github.com/Shaun520/interactive-3d-portfolio/blob/3f8e87827f09e1371c5a8829957b9a2e7cb1bc21/src/components/ui/ScreenReaderOverlay.jsx#L38-L75)：HTML按钮调用teleportTo和requestExit
- [Repos/interactive-3d-portfolio/src/components/ui/ScreenReaderOverlay.jsx:102–125](https://github.com/Shaun520/interactive-3d-portfolio/blob/3f8e87827f09e1371c5a8829957b9a2e7cb1bc21/src/components/ui/ScreenReaderOverlay.jsx#L102-L125)：projects由同源内容生成

## 项目效果图

![interactive-3d-portfolio · observed_still](../assets/previews/interactive-3d-portfolio-1ae6478e3763.webp)

已view_image public/og-image.webp：白纸黑线走廊与人物；只观察历史封面，不证明绘制转场。

来源：[原作者/出处](https://github.com/Shaun520/interactive-3d-portfolio/blob/3f8e87827f09e1371c5a8829957b9a2e7cb1bc21/public/og-image.webp) · observed_still。静帧观察；没有由此验证连续动画或性能。

## 归纳与练习

[IF-03](../lenses/IF-03.md)

[MP-20](../patterns/MP-20.md)
