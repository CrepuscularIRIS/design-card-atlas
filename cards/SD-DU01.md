# SD-DU01 · 先给空间路径语义，再用栅格连通性复核几何落地
案例：[ threejs-procedural-dungeon ](../cases/threejs-procedural-dungeon.md) · 机制证据：`still_observed`

效果图用于理解来源作品，不自动验证本卡中的每个机制。

## 设计动作

图连通不代表雕刻后的走廊可走；规划层与实际占用层需要分别验证。

## 实现与参数

Delaunay→MST→只加长度<mean*2.2的候选环；最大房Boss，最远叶入口；BFS depth→角色；最后reach===floorTotal确认栅格连通。 部分火盆、柱、墓碑另行调用nearDoor排除门口，不覆盖所有装饰。

## 审美细节

历史俯视图有主厅、细廊和灯点层次；格网连通不代表带人物半径可通过，也没包含后加装饰阻挡。

## 适用条件

- 已有米制layout
- 真实障碍纳入walkmask

## 相邻方案与区别

与只做空间图不同增加栅格证据；与现有walkmask互补而非替代。

## 失败模式

- 原BFS发生在装饰前
- 方格点连通不代表连续人物体积
- 主题类型不能生搬成博客战斗内容

## Movie 裁决

- **verdict**：reference
- **reason**：可规划镜头的压缩→释放节奏。

## Frontend 裁决

- **verdict**：adapt
- **reason**：适合场景layout审查，不要把现成Place改随机地牢。

## 最小对照

同一布局用人物半径膨胀障碍再BFS；入口到交互点不可达即失败，即使图层MST连通。

## 源码证据

- [Repos/threejs-procedural-dungeon/src/main.js:238–285](https://github.com/majidmanzarpour/threejs-procedural-dungeon/blob/0a2aa0980028cbbc77af6642b4232b45713dc5de/src/main.js#L238-L285)：MST加短环并剪环保留至少3叶节点
- [Repos/threejs-procedural-dungeon/src/main.js:287–331](https://github.com/majidmanzarpour/threejs-procedural-dungeon/blob/0a2aa0980028cbbc77af6642b4232b45713dc5de/src/main.js#L287-L331)：按深度给入口/Boss/宝物/精英赋语义
- [Repos/threejs-procedural-dungeon/src/main.js:522–550](https://github.com/majidmanzarpour/threejs-procedural-dungeon/blob/0a2aa0980028cbbc77af6642b4232b45713dc5de/src/main.js#L522-L550)：实际floor栅格BFS；定义nearDoor查询，尚非所有道具均调用
- [Repos/threejs-procedural-dungeon/src/main.js:561–581](https://github.com/majidmanzarpour/threejs-procedural-dungeon/blob/0a2aa0980028cbbc77af6642b4232b45713dc5de/src/main.js#L561-L581)：部分火盆、柱、墓碑调用nearDoor排除门口；不能泛称全部装饰

## 项目效果图

![threejs-procedural-dungeon · observed_still](../assets/previews/threejs-procedural-dungeon-256d06c9a586.jpg)

已view_image docs/preview.jpg：暖色俯视地牢、点灯与主厅；截图HUD帧率不能视为当前实测。

来源：[原作者/出处](https://github.com/majidmanzarpour/threejs-procedural-dungeon/blob/0a2aa0980028cbbc77af6642b4232b45713dc5de/docs/preview.jpg) · observed_still。静帧观察；没有由此验证连续动画或性能。

## 归纳与练习

暂未归入新增专业视角；保留原机制边界。

[MP-10](../patterns/MP-10.md)
