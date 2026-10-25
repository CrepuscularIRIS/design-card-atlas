# SHOW-021 · 让切换面板保留共同高度，降低阅读位置跳动
案例：[ awesome-opus5.5-frontend-showcases ](../cases/awesome-opus5.5-frontend-showcases.md) · 机制证据：`source_only`

效果图用于理解来源作品，不自动验证本卡中的每个机制。

## 设计动作

页面切换时FAQ不被不同内容长度来回推移；封面可见代码/预览并排与FAQ。高度稳定不是始终最佳：手机长内容会留巨大空白。

## 实现与参数

panels display:grid→panel grid-area1/1；非活动visibility:hidden，当前opacity1/transform none；.32s/.38s动画。

## 审美细节

页面切换时FAQ不被不同内容长度来回推移；封面可见代码/预览并排与FAQ。高度稳定不是始终最佳：手机长内容会留巨大空白。

## 适用条件

- 面板内容长度接近
- 隐藏项从交互与辅助树正确移出

## 相邻方案与区别

相对动态height动画，逻辑简单稳定；长文采用自然高度更适合。

## 失败模式

- 最高面板过长造成空白
- radio交互不等于完整ARIA tab模式
- 源码紫色强调不直接套项目

## Movie 裁决

- **verdict**：defer
- **reason**：没有movie用途。

## Frontend 裁决

- **verdict**：adapt
- **reason**：适合手机短设置/项目小面板，需响应式与键盘测试。

## 最小对照

交替最短/最长内容并在360px宽测试；焦点丢失、滚动跳跃或大空白即失败。

## 源码证据

- [Repos/awesome-opus5.5-frontend-showcases/repro/tabs-accordion/index.html:352–409](https://github.com/OpenVGLab/awesome-opus5.5-frontend-showcases/blob/cac43b250f07b7b86f4709c61effc84269f46494/repro/tabs-accordion/index.html#L352-L409)：radio checked控制状态；面板同grid-area取最高高度，visibility隐藏非当前项；8px淡入
- [Repos/awesome-opus5.5-frontend-showcases/repro/tabs-accordion/index.html:1264–1295](https://github.com/OpenVGLab/awesome-opus5.5-frontend-showcases/blob/cac43b250f07b7b86f4709c61effc84269f46494/repro/tabs-accordion/index.html#L1264-L1295)：details name=faq原生互斥展开

## 项目效果图

![awesome-opus5.5-frontend-showcases · historical_still_viewed](../assets/previews/awesome-opus5-5-frontend-showcases-57b5094393ca.jpg)

已查看的来源静帧；不证明当前版本运行。

来源：[原作者/出处](https://github.com/OpenVGLab/awesome-opus5.5-frontend-showcases/blob/cac43b250f07b7b86f4709c61effc84269f46494/repro/_covers/tabs-accordion.jpg) · historical_still_viewed。历史封面，不能证明当前运行/运动/交互

## 归纳与练习

暂未归入新增专业视角；保留原机制边界。

[MP-13](../patterns/MP-13.md)
