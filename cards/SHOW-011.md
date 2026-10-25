# SHOW-011 · 把柔性权重与空间相位结合成有根的风动
案例：[ awesome-opus5.5-frontend-showcases ](../cases/awesome-opus5.5-frontend-showcases.md) · 机制证据：`source_only`

效果图用于理解来源作品，不自动验证本卡中的每个机制。

## 设计动作

同风场但不同空间相位让植被形成连贯阵风，根部不整体漂移。静帧只能观察树形，不能验证风动。

## 实现与参数

uWind→ph=t(1.1+1.9wind)+dot(ip,.13,.11)；gust=.55+.45sin(...)；flex×sway/sc，加y向flutter并按|sway|下垂。

## 审美细节

同风场但不同空间相位让植被形成连贯阵风，根部不整体漂移。静帧只能观察树形，不能验证风动。

## 适用条件

- 顶点有aFlex
- 实例轴与尺度正确
- 烘焙保留属性

## 相邻方案与区别

相对整体摇摆，局部权重能保根；复杂树枝仍需层级骨骼或更细模式。

## 失败模式

- 全顶点相同权重导致根浮起
- shadow material未同步顶点动画会出现影子脱节

## Movie 裁决

- **verdict**：adapt
- **reason**：远近树丛可给静止机位持续微动。

## Frontend 裁决

- **verdict**：adapt
- **reason**：适用于植物/布条，不应用到hIE立绘。

## 最小对照

固定树根标记，风0/.5/1录影；根漂、影不动或不同缩放树幅度失真即失败。

## 源码证据

- [Repos/awesome-opus5.5-frontend-showcases/repro/prehistoric-island/index.html:433–455](https://github.com/OpenVGLab/awesome-opus5.5-frontend-showcases/blob/cac43b250f07b7b86f4709c61effc84269f46494/repro/prehistoric-island/index.html#L433-L455)：aFlex限制根部，世界风投影到实例局部轴，除实例缩放，gust由位置和时间变化

## 项目效果图

![awesome-opus5.5-frontend-showcases · historical_still_viewed](../assets/previews/awesome-opus5-5-frontend-showcases-88fec099399a.jpg)

已查看的来源静帧；不证明当前版本运行。

来源：[原作者/出处](https://github.com/OpenVGLab/awesome-opus5.5-frontend-showcases/blob/cac43b250f07b7b86f4709c61effc84269f46494/repro/_covers/prehistoric-island.jpg) · historical_still_viewed。历史封面，不能证明当前运行/运动/交互

## 归纳与练习

暂未归入新增专业视角；保留原机制边界。

保留独立案例。
