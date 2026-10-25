# SD-IC04 · 用共享布局和剖面让两种状态可以直接对照
案例：[ invisible-cities-opus-5.5 ](../cases/invisible-cities-opus-5.5.md) · 机制证据：`source_only`

效果图用于理解来源作品，不自动验证本卡中的每个机制。

## 设计动作

当场景要表达时间、命运或状态对照，保持位置身份比同时更改模型与颜色更容易读懂。

## 实现与参数

先生成最多30个不冲突lots，同一city(b,y0,dead)调用构建两套；上城暖粉墙/红屋顶，下城骨白/赭色。剖线dotN=CUT3.6，live略去线外对象，stairs和cut附近留净空；活动位置来自共享scenes。

## 审美细节

对照靠位置、屋形和活动对应，窗从约每3格一亮变成暗洞；前侧剖开而非把地下完全封在地形里。没有源图，本轮不判断上下层实际遮挡效果。

## 适用条件

- 状态差异是叙事中心
- 对象有对应关系
- 剖面与镜头共同设计

## 相邻方案与区别

与全屏溶解相比保留并列对象对应；与纯换色相比加入窗光和活动差异，但仍共享布局。

## 失败模式

- 上下堆叠会增加遮挡
- 本仓上层主动删剖线外对象，不是完整复制
- 不适用于必须保持真实建筑封闭外观的常态场景

## Movie 裁决

- **verdict**：reference
- **reason**：适合一次性的剖面或状态对照镜头。

## Frontend 裁决

- **verdict**：adapt
- **reason**：可为昼夜/材质方案比较保留相机和布局，不引入双城世界观。

## 最小对照

固定实体ID、相机和位置，比对两状态投影；变化只来自计划中的材质/灯/部件，剖面不能暴露错误背面或遮住比较对象。

## 源码证据

- [Repos/invisible-cities-opus-5.5/src/cities/eusapia.js:13–50](https://github.com/stared/invisible-cities-opus-5.5/blob/3c2d0cc6657d053d5c36802db359ce8bb3820aa1/src/cities/eusapia.js#L13-L50)：前向剖面、楼梯通道和共享lots排布
- [Repos/invisible-cities-opus-5.5/src/cities/eusapia.js:52–80](https://github.com/stared/invisible-cities-opus-5.5/blob/3c2d0cc6657d053d5c36802db359ce8bb3820aa1/src/cities/eusapia.js#L52-L80)：相同lots上下生成并替换墙、屋顶、窗光
- [Repos/invisible-cities-opus-5.5/src/cities/eusapia.js:94–110](https://github.com/stared/invisible-cities-opus-5.5/blob/3c2d0cc6657d053d5c36802db359ce8bb3820aa1/src/cities/eusapia.js#L94-L110)：同场景活动在对应位置重复

## 项目效果图

![invisible-cities-opus-5.5 · live_site_still](../assets/previews/live-invisible-cities-atlas.png)

小型城市按类别列与序号行放在棋盘上；瓷金造型和标签共用空间位置，分类导航在下方。

来源：[原作者/出处](https://p.migdal.pl/invisible-cities-opus-5.5/) · live_site_still。本轮线上默认Atlas静帧，线上版本未绑定本地HEAD；不证明全部55城细节。

![invisible-cities-opus-5.5 · live_site_still](../assets/previews/live-invisible-cities-journey.png)

选择Journey后保留城市身份，发光线路把叙述顺序联结起来。

来源：[原作者/出处](https://p.migdal.pl/invisible-cities-opus-5.5/) · live_site_still。切换后的单帧，不据此认证完整过渡或输入中断。

## 归纳与练习

暂未归入新增专业视角；保留原机制边界。

[MP-07](../patterns/MP-07.md)
