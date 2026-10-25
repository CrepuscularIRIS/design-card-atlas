# SD-NX02 · 把镜头展示与交还控制拆成可跳过状态
案例：[ NexusCity ](../cases/NexusCity.md) · 机制证据：`source_only`

效果图用于理解来源作品，不自动验证本卡中的每个机制。

## 设计动作

展示段负责建立空间，独立交还段避免结束瞬间跳相机。

## 实现与参数

LOADING→CINEMATIC_INTRO→TRANSITION_TO_PLAYER→GAMEPLAY；段内smoothstep，交还2.2s五次ease；相机终点=玩家+(0,3.2,7.5)。

## 审美细节

位置和lookAt独立插值；原作先高空后地面，Citadel现定特写再拉远，应重排关键帧。

## 适用条件

- 有可选展示入口
- 相机归属单一

## 相邻方案与区别

与 FOG 的相机轨道插值是互补：本卡解决状态和控制权，不解决路径几何。

## 失败模式

- 线性空间插值无避障，smoothstep不保证不穿模
- 原作轨道缺减弱动态分支

## Movie 裁决

- **verdict**：adapt
- **reason**：可用状态结构，镜头顺序须重设计。

## Frontend 裁决

- **verdict**：prototype
- **reason**：跳过、打断、交还比强制长intro更有价值。

## 最小对照

在首/中/末帧跳过和移动打断，终点位置角度连续；穿墙、丢控制、重复intro任一即失败。

## 源码证据

- [Repos/NexusCity/src/cinematics/CinematicManager.ts:26–79](https://github.com/vineetsharma96/NexusCity/blob/bc33737396179be841338eb09675239b5d1f82f0/src/cinematics/CinematicManager.ts#L26-L79)：12.5秒四关键帧与2.2秒交还
- [Repos/NexusCity/src/cinematics/CinematicManager.ts:98–139](https://github.com/vineetsharma96/NexusCity/blob/bc33737396179be841338eb09675239b5d1f82f0/src/cinematics/CinematicManager.ts#L98-L139)：skip与vista退出共用过渡入口
- [Repos/NexusCity/src/cinematics/CinematicManager.ts:197–244](https://github.com/vineetsharma96/NexusCity/blob/bc33737396179be841338eb09675239b5d1f82f0/src/cinematics/CinematicManager.ts#L197-L244)：smoothstep位置目标插值，五次缓动交还

## 项目效果图

![NexusCity · archived_local_screenshot](../assets/previews/scene-nexuscity-1.webp)

实际查看：夜街斑马线、中央NPC与交互提示，青色HUD/雷达、暗楼体和橙色树冠；画面整体很暗。

来源：本轮已观察的历史截图 · archived_local_screenshot。2026-09-27本地审阅项目快照中的Nexus City界面；未绑定当前Repos/NexusCity提交。静帧不证明当前运行、动画或模型质量。

## 归纳与练习

[IF-06](../lenses/IF-06.md)

[MP-11](../patterns/MP-11.md)
