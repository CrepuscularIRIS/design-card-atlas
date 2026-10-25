# SD-DD03 · 让窗色、环境光和局部灯共享昼夜状态而保留开关权
案例：[ csc35-diorama-day ](../cases/csc35-diorama-day.md) · 机制证据：`source_only`

效果图用于理解来源作品，不自动验证本卡中的每个机制。

## 设计动作

昼夜过渡需要可见的参照物一起变化，同时保持用户关灯具有持续效力；否则环境变化和交互状态互相覆盖。

## 实现与参数

daylight=.5+.5*cos(elapsed*.035)，周期约179.5s；sun .5+1.3d、hemi .75+.6d，背景从#bfc5d2→#eee8e1、窗#77869e→#b8d1d5。灯强度lampOn ? .25+(1-d)*.75 : 0；用户关闭后不会被昼夜自动开启。日/黄昏/夜标签阈值.72/.35。

## 审美细节

冷蓝窗与背景退入夜色、暖#ffd9ac点光相对增强。太阳位置和颜色不随daylight移动，窗口roughness1是实色面，所以不能称天文太阳或真实窗外景观。

## 适用条件

- 已有统一环境参数
- 用户开关有持久语义
- 曝光策略不同时抵消光强差

## 相邻方案与区别

与neon共享空间发光场不同，此处共享时间状态；两者可以组合，但不应混成一个“全局光照”主张。

## 失败模式

- 太阳方向不变，只是风格化状态混合
- 低帧率dt截断会使周期落后真实时间
- 没有reduce-motion/用户暂停时间入口
- 灯罩改色不是emissive，暗处可能与亮灯不一致

## Movie 裁决

- **verdict**：adapt
- **reason**：可作为材质/光强统一状态原型，录制时直接锁daylight。

## Frontend 裁决

- **verdict**：adapt
- **reason**：适合已有昼夜系统中明确用户开关与环境状态的组合。

## 最小对照

d=0/.5/1下分别开/关灯，关闭始终无局部点光，窗色和环境不过冲；暂停/切回状态一致。夜间物件失去可读性或开关被周期覆盖判失败。

## 源码证据

- [Repos/csc35-diorama-day/index.html:304–323](https://github.com/agent-marsha/csc35-diorama-day/blob/aa88c6276e2d57f16e855245780bb83bea662721/index.html#L304-L323)：灯到达开关更新lampOn及灯罩色
- [Repos/csc35-diorama-day/index.html:345–361](https://github.com/agent-marsha/csc35-diorama-day/blob/aa88c6276e2d57f16e855245780bb83bea662721/index.html#L345-L361)：窗口是实体颜色面而非真实透射窗
- [Repos/csc35-diorama-day/index.html:642–655](https://github.com/agent-marsha/csc35-diorama-day/blob/aa88c6276e2d57f16e855245780bb83bea662721/index.html#L642-L655)：统一daylight参数驱动环境、窗面和灯强度
- [Repos/csc35-diorama-day/index.html:690–701](https://github.com/agent-marsha/csc35-diorama-day/blob/aa88c6276e2d57f16e855245780bb83bea662721/index.html#L690-L701)：仅started累计时间，dt上限.05

## 项目效果图

![csc35-diorama-day · local_head_still](../assets/previews/live-csc35-diorama-day.png)

奶油色正交房间，低饱和绿沙发和陶土色地毯划分活动区；四个人物占据前部，需求面板留在右侧。

来源：[原作者/出处](https://github.com/agent-marsha/csc35-diorama-day) · local_head_still。本轮本地HEAD页面打开并开始后截图；未验证家具动作、寻路、持续状态与性能。

## 归纳与练习

暂未归入新增专业视角；保留原机制边界。

[MP-01](../patterns/MP-01.md)
