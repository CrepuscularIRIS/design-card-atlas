# SD-MO01 · 用同一压力状态联动空间压缩和发光核心
案例：[ The-Monolith ](../cases/The-Monolith.md) · 机制证据：`source_only`

效果图用于理解来源作品，不自动验证本卡中的每个机制。

## 设计动作

让反馈发生在空间、体量与亮度三个通道，可把抽象压力变成可感知的环境事件。

## 实现与参数

volume→outwardForce=volume*.2；墙距clamp(20-fatigue+force,7,20)，fatigue每帧+.001；核心baseScale=.3+.7*compressionRatio，声强额外*.03。

## 审美细节

四面500²灰线网+1500白色点+黑雾0.02；设计重点是围合与呼吸，不是黑洞模拟。

## 适用条件

- 可选短事件
- dt归一化
- 亮度上限

## 相邻方案与区别

不同于黑洞引力/透镜：这里只是线框空间反馈；相比仅bloom脉冲，空间位置也变化。

## 失败模式

- 当前逐帧fatigue与旋转依赖刷新率
- 持续疲劳最终压到下限
- 闪烁强度随机
- 无LICENSE，不能拷代码

## Movie 裁决

- **verdict**：adapt
- **reason**：可改为场景事件时间线，脱离麦克风输入。

## Frontend 裁决

- **verdict**：reference
- **reason**：主动声音入口有权限门槛，不能强制用于博客进入。

## 最小对照

用固定时间轨道测试30/60/120fps，墙距和亮度应一致；不能造成阅读闪烁或持续强制压迫。

## 源码证据

- [Repos/The-Monolith/main.js:70–105](https://github.com/val00813/The-Monolith/blob/f931b85ada56598d1f1f4c3d3202588ccb6d7261/main.js#L70-L105)：麦克风FFT256采样
- [Repos/The-Monolith/main.js:112–175](https://github.com/val00813/The-Monolith/blob/f931b85ada56598d1f1f4c3d3202588ccb6d7261/main.js#L112-L175)：噪声门限15、音量平滑.1、墙体平滑.05、粒子尺度与bloom联动

## 项目效果图

![The-Monolith · archived_local_screenshot](../assets/previews/scene-the-monolith-1.webp)

实际查看：黑色空间里白色发光点团和多层细线格网，文字提示点击开始并允许麦克风。

来源：本轮已观察的历史截图 · archived_local_screenshot。历史项目快照，明确处于点击/麦克风启动前待机态；不是音频响应已运行或各阶段完整效果证据。

## 归纳与练习

暂未归入新增专业视角；保留原机制边界。

保留独立案例。
