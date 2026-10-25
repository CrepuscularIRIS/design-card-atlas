# SD-TW05 · 让环境声音跟随看见的事件阶段和空间位置
案例：[ tidewater ](../cases/tidewater.md) · 机制证据：`source_only`

效果图用于理解来源作品，不自动验证本卡中的每个机制。

## 设计动作

环境声的可信度来自声音与可见过程同源：浪崩、上冲、回流应在各自位置与时刻发生，而不是独立循环。

## 实现与参数

监听者移动>12米重建采样站，按波周期P与深度剖面推算breaking时间tc、上冲tw、回流tb；LOOK=.2秒预测调度，crash150米/wash70米/backwash60米内播放，last序号防重复；幅度影响音量和pitch，随机只加微扰。缺shore数据时回退fakeSurf。

## 审美细节

这是读过的源级声画耦合，不是已听过/验证同步的音效评价。Freesound42条录音CC0是CREDITS声明，本轮未逐个听取或追到远端源。

## 适用条件

- 有可信可见事件源
- 音频开启受用户控制
- 暂停/恢复有统一时钟

## 相邻方案与区别

与little-rain-cloud离线audio_log互补：本卡解决实时事件来源，后者解决记录与离线复现；不能把播放背景海浪当同步。

## 失败模式

- 本仓随机pitch不支持bit级重复音轨
- fakeSurf回退可能脱离视觉
- 只靠空间距离不能模拟遮挡和室内外声学

## Movie 裁决

- **verdict**：adapt
- **reason**：可用同源事件日志支持镜头声画同步。

## Frontend 裁决

- **verdict**：reference
- **reason**：仅在用户开启音频时使用；没有可见水过程就不必建浪声系统。

## 最小对照

录下画面事件时间与调度表，逐项比对开始时刻和位置；切场景、暂停、恢复不重复播放，离开声源衰减；视觉事件停止仍循环新撞击则失败。

## 源码证据

- [Repos/tidewater/src/audio/SoundScape.js:852–922](https://github.com/dgreenheck/tidewater/blob/4811ba48d795197de5621985f404e765c0b7c0ef/src/audio/SoundScape.js#L852-L922)：按shore相位预测crash/wash/backwash，提前.2秒调度并按距离裁剪

## 项目效果图

![tidewater · observed_still](../assets/previews/tidewater-85a2ca018d2a.jpg)

已view_image docs/screenshot.jpg：夕阳码头、近景木栏杆/绳索/灯具/钓竿、远近水色层次。仅为历史静帧，没有证明当前实时水体、声画同步或性能。

来源：[原作者/出处](https://github.com/dgreenheck/tidewater/blob/4811ba48d795197de5621985f404e765c0b7c0ef/docs/screenshot.jpg) · observed_still。静帧观察；没有由此验证连续动画或性能。

## 归纳与练习

暂未归入新增专业视角；保留原机制边界。

保留独立案例。
