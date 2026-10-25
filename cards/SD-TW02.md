# SD-TW02 · 让铺板缺陷按使用历史分布，并受远景可读性约束
案例：[ tidewater ](../cases/tidewater.md) · 机制证据：`still_observed`

效果图用于理解来源作品，不自动验证本卡中的每个机制。

## 设计动作

“旧”应由新旧替换、磨耗路径和少量破损共同表达，不能把所有构件随机扭坏。

## 实现与参数

plank先以.6%/1.2%概率缺失，7%用newer分支；newer风化.25–.45、旧.55–1，宽.198–.206对pitch .215，yOff0–.014并偶有追加，端点±约.06；旧板5%切成两块带.022左右裂缝。walk参数把通行中心线交给木材shader；下面碰撞仍整片连续。

## 审美细节

源码注释说明曾因缝过宽产生远处亚像素暗线，现收窄板缝。截图可见重复铺板、栏杆和暖光，但截图不能证明动态抗闪烁解决。

## 适用条件

- 材质与几何使用同一老化状态
- 维护通行碰撞意图
- 近远镜头都检查

## 相邻方案与区别

与均匀noise粗糙度不同包含替换历史；与Octavia连接结构互补，先造得合理再用得合理。

## 失败模式

- 源码缺板但collider仍连续，不能宣称真实破洞
- 高频缝和斜纹仍可能闪烁
- 每块完全随机破损会失去维护历史感

## Movie 裁决

- **verdict**：prototype
- **reason**：优先选择镜头前景能解释磨耗的地板/栈道。

## Frontend 裁决

- **verdict**：adapt
- **reason**：小范围低幅度变化，并保留可走面与交互稳定。

## 最小对照

锁seed，以近景和慢速远景推进对比：新旧板可辨、通行线合理、远景不闪；过度破碎、穿插、窄缝摩尔纹加重则退回。

## 源码证据

- [Repos/tidewater/src/world/Pier.js:225–275](https://github.com/dgreenheck/tidewater/blob/4811ba48d795197de5621985f404e765c0b7c0ef/src/world/Pier.js#L225-L275)：旧木板7%新换、轻微翘曲、5%旧板裂开、稀少缺板及连续deck collider

## 项目效果图

![tidewater · observed_still](../assets/previews/tidewater-85a2ca018d2a.jpg)

已view_image docs/screenshot.jpg：夕阳码头、近景木栏杆/绳索/灯具/钓竿、远近水色层次。仅为历史静帧，没有证明当前实时水体、声画同步或性能。

来源：[原作者/出处](https://github.com/dgreenheck/tidewater/blob/4811ba48d795197de5621985f404e765c0b7c0ef/docs/screenshot.jpg) · observed_still。静帧观察；没有由此验证连续动画或性能。

## 归纳与练习

暂未归入新增专业视角；保留原机制边界。

[MP-05](../patterns/MP-05.md)
