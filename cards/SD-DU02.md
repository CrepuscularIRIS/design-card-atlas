# SD-DU02 · 让粒子发射位置解释主题而不均匀撒满画面
案例：[ threejs-procedural-dungeon ](../cases/threejs-procedural-dungeon.md) · 机制证据：`still_observed`

效果图用于理解来源作品，不自动验证本卡中的每个机制。

## 设计动作

主题差异应同时改变材质、光色、物理来源和密度。

## 实现与参数

TH统一配置；kind1熔岩/火焰→embers，kind4苔藓/根→spores，kind0光柱→dust；n=min(spec.n,max(40,sources*6))；关键灯后余预算按分散覆盖选择。

## 审美细节

ancient暖火#ffa640配冷环境#2e3a52；frost蓝冰/冷白；verdant青绿根和孢子。

## 适用条件

- 明确源物件
- 能标出安全可走域

## 相邻方案与区别

与全屏噪点不同有空间来源；与LightPool轮换预算互补。

## 失败模式

- 无源时源码回退全floor随机点
- 12灯是本仓配置非本站性能结论
- 固定样本可能遗漏关键近景灯

## Movie 裁决

- **verdict**：adapt
- **reason**：主题来源适合镜头可读性

## Frontend 裁决

- **verdict**：prototype
- **reason**：先给单Place已有motes绑定真正光柱/通风口。

## 最小对照

粒子开/关A/B，读者能指出来源且交互物不被遮；远离源仍均匀满屏则失败。

## 源码证据

- [Repos/threejs-procedural-dungeon/src/main.js:55–118](https://github.com/majidmanzarpour/threejs-procedural-dungeon/blob/0a2aa0980028cbbc77af6642b4232b45713dc5de/src/main.js#L55-L118)：五主题绑定fog/palette/liquid/props/particles
- [Repos/threejs-procedural-dungeon/src/main.js:1795–1845](https://github.com/majidmanzarpour/threejs-procedural-dungeon/blob/0a2aa0980028cbbc77af6642b4232b45713dc5de/src/main.js#L1795-L1845)：火星来自池/火炬，孢子来自苔藓/根，尘来自光柱
- [Repos/threejs-procedural-dungeon/src/main.js:1855–1884](https://github.com/majidmanzarpour/threejs-procedural-dungeon/blob/0a2aa0980028cbbc77af6642b4232b45713dc5de/src/main.js#L1855-L1884)：关键房间优先、火炬最远点采样12灯预算

## 项目效果图

![threejs-procedural-dungeon · observed_still](../assets/previews/threejs-procedural-dungeon-256d06c9a586.jpg)

已view_image docs/preview.jpg：暖色俯视地牢、点灯与主厅；截图HUD帧率不能视为当前实测。

来源：[原作者/出处](https://github.com/majidmanzarpour/threejs-procedural-dungeon/blob/0a2aa0980028cbbc77af6642b4232b45713dc5de/docs/preview.jpg) · observed_still。静帧观察；没有由此验证连续动画或性能。

## 归纳与练习

暂未归入新增专业视角；保留原机制边界。

保留独立案例。
