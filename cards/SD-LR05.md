# SD-LR05 · 用同一模拟时间驱动画面帧和离线声轨事件
案例：[ little-rain-cloud ](../cases/little-rain-cloud.md) · 机制证据：`source_only`

效果图用于理解来源作品，不自动验证本卡中的每个机制。

## 设计动作

电影样机需要可定位的动作时间线；截帧与声音事件共享模拟时钟，才便于评审同一镜头。

## 实现与参数

director从4.4s行走、9.2s奔跑、12.3s召回、18.6s阵风、21.2s入夜、24.2s回望，27.2s片尾。record以目标fps生成时刻，页面内部固定1/60推进；声音记录雨量/镜头距离/夜值/风和chime事件，供另脚本混音。

## 审美细节

每一步是在证明一种操作后的视觉结果，不是无输入随机游览；源码没有让Math.random固定，因而“固定时间步”不等于“完全确定性回放”。

## 适用条件

- 可暂停rAF并单步模拟
- 资产加载完成可查询
- 随机源和模拟状态可重置

## 相邻方案与区别

3dcitydb视点链接仅存静态状态；本卡补时间与事件，仍需种子和资源锁定才可复现。

## 失败模式

- 目标时间被1/60离散步长向前取整
- 原工具硬编码Mac路径、9333端口与Metal
- 字体等待仅800ms且外部Google字体，不符合本站本地资产方向
- 截图成功不能证明实时性能

## Movie 裁决

- **verdict**：adapt
- **reason**：可借事件时间线与声音日志接口；本轮没有录制成片。

## Frontend 裁决

- **verdict**：reference
- **reason**：仅开发评审工具，不进入常规浏览流程。

## 最小对照

固定seed、资产版本与时刻，重复导出各关键帧和事件表；相机/对象/声响事件时间一致，漏音、跨帧重复触发或未ready就截屏判失败。

## 源码证据

- [Repos/little-rain-cloud/main.js:1016–1051](https://github.com/dososo/little-rain-cloud/blob/8180c1b1c98e993bad05e77eb596d472ce2910cd/main.js#L1016-L1051)：字幕/输入/召回/风/昼夜/回望均由director时间轴触发
- [Repos/little-rain-cloud/main.js:1052–1077](https://github.com/dososo/little-rain-cloud/blob/8180c1b1c98e993bad05e77eb596d472ce2910cd/main.js#L1052-L1077)：记录声音采样；__renderAt按1/60步进到目标时间
- [Repos/little-rain-cloud/tools/record.mjs:45–67](https://github.com/dososo/little-rain-cloud/blob/8180c1b1c98e993bad05e77eb596d472ce2910cd/tools/record.mjs#L45-L67)：等ready、逐帧调用__renderAt(f/fps)、保存JPEG与audio_log

## 项目效果图

![little-rain-cloud · observed_still](../assets/previews/little-rain-cloud-f483b6c2dde7.png)

已view_image shots/04-look-back.png：暖沙丘、白云、深湿痕与绿色曲线；它是历史静帧，只支持构图判断，不支持动画或当前运行验收。

来源：[原作者/出处](https://github.com/dososo/little-rain-cloud/blob/8180c1b1c98e993bad05e77eb596d472ce2910cd/shots/04-look-back.png) · observed_still。静帧观察；没有由此验证连续动画或性能。

## 归纳与练习

[CINE-06](../lenses/CINE-06.md)

[MP-19](../patterns/MP-19.md)
