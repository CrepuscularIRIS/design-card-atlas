# SD-DD01 · 用开口房壳与正交构图保持室内小物件可读
案例：[ csc35-diorama-day ](../cases/csc35-diorama-day.md) · 机制证据：`source_only`

效果图用于理解来源作品，不自动验证本卡中的每个机制。

## 设计动作

低复杂度房间靠清晰的层次、尺度和留空形成可读场景，正交投影减少近远大小变化，但必须主动处理墙遮挡。

## 实现与参数

OrthographicCamera初位(13,13,16)，target(0,1,0)，zoom .7–2.5、polar .35–π/2.12、禁pan；房壳11×11地面与后/左两面墙高4.4，前/右开放。材质按色缓存、roughness .9。resize横屏固定高度15.2，竖屏固定宽15.2，不裁短边。

## 审美细节

背景#eee8e1、地板#eadfd3、墙#f2e9e1/#eee1d8、沙发#91a497、accent#d8755d贯穿抱枕/书/UI；植物深浅绿提供小范围对比。未找到本地截图，不把配色数值当实际画面验收。

## 适用条件

- 场景范围小且边界明确
- 视角围绕可见开口设计
- 视口与HUD占位共同评估

## 相邻方案与区别

与Invisible Cities剖面同属主动让出观察面；这里是常态开放房壳，前者用共享布局表达两种状态。

## 失败模式

- 源码未限制azimuth，绕到后墙仍会遮挡
- 无自动bounds fit，15.2是本场景常数
- 所有roughness .9不能支撑写实材质差异
- 正交能缩小距离感也会削弱电影推镜深度

## Movie 裁决

- **verdict**：reference
- **reason**：适合单室微缩展示，透视叙事镜头不一定适用。

## Frontend 裁决

- **verdict**：adapt
- **reason**：作为一个小型互动房间的构图草案，不替代当前写实Place。

## 最小对照

横竖屏和zoom两端检查家具、入口、交互目标都入安全区；旋转到后侧时墙遮挡应有明确处理，否则锁方位。贴近墙的道具被完全挡住即失败。

## 源码证据

- [Repos/csc35-diorama-day/index.html:200–265](https://github.com/agent-marsha/csc35-diorama-day/blob/aa88c6276e2d57f16e855245780bb83bea662721/index.html#L200-L265)：正交相机、受限极角、共享粗糙材质、两面墙开放房壳
- [Repos/csc35-diorama-day/index.html:276–302](https://github.com/agent-marsha/csc35-diorama-day/blob/aa88c6276e2d57f16e855245780bb83bea662721/index.html#L276-L302)：沙发靠垫、桌腿/杯书等少量功能性层次
- [Repos/csc35-diorama-day/index.html:657–675](https://github.com/agent-marsha/csc35-diorama-day/blob/aa88c6276e2d57f16e855245780bb83bea662721/index.html#L657-L675)：横竖屏都保持短边view=15.2的正交范围

## 项目效果图

![csc35-diorama-day · local_head_still](../assets/previews/live-csc35-diorama-day.png)

奶油色正交房间，低饱和绿沙发和陶土色地毯划分活动区；四个人物占据前部，需求面板留在右侧。

来源：[原作者/出处](https://github.com/agent-marsha/csc35-diorama-day) · local_head_still。本轮本地HEAD页面打开并开始后截图；未验证家具动作、寻路、持续状态与性能。

## 归纳与练习

暂未归入新增专业视角；保留原机制边界。

[MP-11](../patterns/MP-11.md)
