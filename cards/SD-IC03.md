# SD-IC03 · 给悬空与架高结构补可追踪的受力和进入路径
案例：[ invisible-cities-opus-5.5 ](../cases/invisible-cities-opus-5.5.md) · 机制证据：`source_only`

效果图用于理解来源作品，不自动验证本卡中的每个机制。

## 设计动作

高质量细节优先回答结构为什么立得住、如何上去；锚点、斜撑和桥口比随机小物件更能解释尺度。

## 实现与参数

Octavia网半宽6.7/半深4.7、高11.8，中间按1.05下垂；锚链12分段、链环交替旋转，拉索向崖搜索地形达到锚固高度；桥板和扶绳同走sin(pi*t)*.3下垂曲线。Zenobia按平台四角放柱，在[.6,y*.5]和[y*.5,y-.1]补X撑。

## 审美细节

绳网麻色#d9c39a与深绳#a8875a，锚铁#3d3b3c；桥头绞盘小屋与灯窗给通行入口可读的落点。此为程序美术受力暗示，不是结构工程仿真。

## 适用条件

- 镜头能看到连接处
- 附属构件共享主结构坐标
- 结构目的清楚

## 相邻方案与区别

与随机屋顶设备相比，这些细节由主结构约束；与Tidewater使用痕迹互补，一个解释建成方式，一个解释使用历史。

## 失败模式

- 视觉可信不等于承载安全
- 微缩护栏高度不可照搬为真人米制
- 摇摆体与固定锚点分组后可能出现缝隙，须动态验收

## Movie 裁决

- **verdict**：prototype
- **reason**：先在选定中近景补少量有效连接点，能直接改善建模可信度。

## Frontend 裁决

- **verdict**：reference
- **reason**：可用设计检查表；源代码权利未明。

## 最小对照

固定近景/中景两镜头，隐藏装饰层仍能追踪支承路径；锚点不悬空、桥板扶手曲线一致，接头穿模或路径封闭判失败。

## 源码证据

- [Repos/invisible-cities-opus-5.5/src/cities/octavia.js:8–19](https://github.com/stared/invisible-cities-opus-5.5/blob/3c2d0cc6657d053d5c36802db359ce8bb3820aa1/src/cities/octavia.js#L8-L19)：悬网下垂曲面及静态/摇摆几何分组
- [Repos/invisible-cities-opus-5.5/src/cities/octavia.js:128–177](https://github.com/stared/invisible-cities-opus-5.5/blob/3c2d0cc6657d053d5c36802db359ce8bb3820aa1/src/cities/octavia.js#L128-L177)：崖锚链、拉索、桥板与护绳共用路径
- [Repos/invisible-cities-opus-5.5/src/cities/zenobia.js:52–77](https://github.com/stared/invisible-cities-opus-5.5/blob/3c2d0cc6657d053d5c36802db359ce8bb3820aa1/src/cities/zenobia.js#L52-L77)：柱角、双层X斜撑、铺板和护栏

## 项目效果图

![invisible-cities-opus-5.5 · live_site_still](../assets/previews/live-invisible-cities-atlas.png)

小型城市按类别列与序号行放在棋盘上；瓷金造型和标签共用空间位置，分类导航在下方。

来源：[原作者/出处](https://p.migdal.pl/invisible-cities-opus-5.5/) · live_site_still。本轮线上默认Atlas静帧，线上版本未绑定本地HEAD；不证明全部55城细节。

![invisible-cities-opus-5.5 · live_site_still](../assets/previews/live-invisible-cities-journey.png)

选择Journey后保留城市身份，发光线路把叙述顺序联结起来。

来源：[原作者/出处](https://p.migdal.pl/invisible-cities-opus-5.5/) · live_site_still。切换后的单帧，不据此认证完整过渡或输入中断。

## 归纳与练习

暂未归入新增专业视角；保留原机制边界。

[MP-10](../patterns/MP-10.md)
