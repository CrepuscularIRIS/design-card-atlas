# inkjs
与ink同主机制的浏览器实现。本轮提取可读宽度、段落节奏与选择DOM更新，避免重复计作独立叙事理论。

## 案例档案

[来源仓库](https://github.com/y-lohse/inkjs)
分析版本：`6b1153410ab1c4bcfd9ef04eb2f0107f36be7778`

模型归属未独立认证。

## 初始源码审计边界

实读serverless模板JS/CSS和Story推进/选择；未读compiler、所有示例和端到端浏览器行为。

以下保留初始源码审计的观察范围。后续新增静帧独立列于视觉材料，不追溯证明全部机制或运行状态。

## 机制与案例分析

### [CN-023 · 把段落与选择依次揭示并尊重减弱动态](../cards/CN-023.md)

把段落与选择依次揭示并尊重减弱动态。这是由该仓实现提炼的候选操作，跨项目效果待验证。

视觉节奏是段落级，不是强迫逐字等候；600px/1.7em仅为模板阅读参考。

**Movie：reference** · 用于字幕分段草拟，影片应时间轴锁定
**前端：adapt** · 适合2D会面/阅读卡的低运动呈现

失败条件：- 模板innerHTML直接写叙事文本，不可直接装载不可信模型HTML
- 自动滚动时长300+3*dist可能长到失控

## 项目效果与观察材料

![inkjs · live_site_still](../assets/previews/live-inkjs.png)

内置故事以极简文本和编号选择呈现，页面保留加载故事入口；这是叙事运行时的基础输出形态。

来源：[原作者/出处](http://yannick-lohse.fr/inkjs/) · live_site_still。已打开内置样例的首个节点；未验证状态恢复、分支全集或无障碍流程。

## 复用边界

- **status**：observed
- **evidence**：LICENSE.md: MIT，inkle及inkjs contributors
- **reuse**：direct_with_notice

图片及第三方素材的权利单独保留；源代码许可证不自动授权媒体。
