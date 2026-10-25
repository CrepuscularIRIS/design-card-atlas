# SD-DD02 · 把选中、走向、到达和物件响应连成可读动作链
案例：[ csc35-diorama-day ](../cases/csc35-diorama-day.md) · 机制证据：`source_only`

效果图用于理解来源作品，不自动验证本卡中的每个机制。

## 设计动作

点击物件后的反馈要有阶段：对象被选中、意图已接受、移动进行、到达后才执行；不让视觉动作和业务状态各说各话。

## 实现与参数

选中同时设置ring与人物卡；sendTo复制prop.target并按index轻微分开，到达阈值.065后调用onArrive。步速1.5*(.55+.45*energy/100)，摆臂/腿phase+=9dt；点击灯只在arrive切换lampOn。raycast仅在pointer位移≤6px时发生。原实现直线移动，没有绕桌/墙的寻路或碰撞。

## 审美细节

可借的是可读的操作状态与目标点；沙发“relax”仍是站在沙发前的小幅姿态，没有完整坐下接触。四个程序人物的发型/服色区别只是案例，不建议本站hIE改3D。

## 适用条件

- 物件有可达approach point
- 交互能中断与重定向
- 选择反馈同时覆盖空间与UI

## 相邻方案与区别

与立即点亮按钮相比增加空间过程；与完整行为树不同，这是小型显式状态链。Town/Places已有移动系统应复用其通达性，而非重写直走。

## 失败模式

- 原直线运动穿越家具，不能直接迁移
- index横向偏移不保证多人避碰
- 动作姿势长期停留，未定义完成/退出事件
- 6px阈值不完整处理多指/取消指针

## Movie 裁决

- **verdict**：reference
- **reason**：状态链可帮助组织可理解的短镜头，动作本身未观察。

## Frontend 裁决

- **verdict**：adapt
- **reason**：可把同样逻辑用于2D hIE与现有物件交互，保留本站walkmask。

## 最小对照

点灯后移动中改点桌子：旧灯不得提前切换；拖相机不触发命令；目标点可达且不会穿桌。相同prop多人到达还需占位策略，否则判部分完成。

## 源码证据

- [Repos/csc35-diorama-day/index.html:268–274](https://github.com/agent-marsha/csc35-diorama-day/blob/aa88c6276e2d57f16e855245780bb83bea662721/index.html#L268-L274)：prop独立登记目标位置
- [Repos/csc35-diorama-day/index.html:499–547](https://github.com/agent-marsha/csc35-diorama-day/blob/aa88c6276e2d57f16e855245780bb83bea662721/index.html#L499-L547)：地面ring与DOM选中同步，sendTo与arrive分阶段
- [Repos/csc35-diorama-day/index.html:549–614](https://github.com/agent-marsha/csc35-diorama-day/blob/aa88c6276e2d57f16e855245780bb83bea662721/index.html#L549-L614)：移动/动作状态、需要值与姿态/UI更新
- [Repos/csc35-diorama-day/index.html:616–639](https://github.com/agent-marsha/csc35-diorama-day/blob/aa88c6276e2d57f16e855245780bb83bea662721/index.html#L616-L639)：6像素拖动阈值后raycast拾取

## 项目效果图

![csc35-diorama-day · local_head_still](../assets/previews/live-csc35-diorama-day.png)

奶油色正交房间，低饱和绿沙发和陶土色地毯划分活动区；四个人物占据前部，需求面板留在右侧。

来源：[原作者/出处](https://github.com/agent-marsha/csc35-diorama-day) · local_head_still。本轮本地HEAD页面打开并开始后截图；未验证家具动作、寻路、持续状态与性能。

## 归纳与练习

暂未归入新增专业视角；保留原机制边界。

[MP-16](../patterns/MP-16.md)
