# SD-TW03 · 道具密度服从门口、路面和使用区的净空规则
案例：[ tidewater ](../cases/tidewater.md) · 机制证据：`source_only`

效果图用于理解来源作品，不自动验证本卡中的每个机制。

## 设计动作

有生活感的杂物需要出现得有理由，也需要有明确的不能出现区域；通路空白本身是设计。

## 实现与参数

stairs/stoop/porch/ladder/pierStep pad=.9，boardwalk/pier=.4，其余walkable=.3；门前沿朝向建立3.2米长、半径.9胶囊，spawn半径3.5；clear同时检查obs距离、terrain.pathDistance≥r+.25、occupancy.free。高脚屋允许地板下放物，柱仍是障碍。

## 审美细节

细节围绕墙边、海岸和植被的分布还需逐类查看；本轮已证实的是净空约束链，而非声称全部杂物都有正确叙事来源。静态截图不足验证通行。

## 适用条件

- 碰撞tag真实完整
- 道具footprint保守包含外伸部件
- 地面路径数据可靠

## 相邻方案与区别

与dungeon先图连通再栅格BFS相补：该卡防止后加装饰破坏通达性；单靠随机点最小间隔不够。

## 失败模式

- 二维footprint忽略垂直碰撞与头部净空
- 缩减高脚屋footprint须确认支柱仍注册
- 本仓数值基于自身尺度不可原样套

## Movie 裁决

- **verdict**：adapt
- **reason**：可让画面层次更密同时保住镜头通道。

## Frontend 裁决

- **verdict**：prototype
- **reason**：特别适合现有Place加细节前的layout/walkmask规则。

## 最小对照

固定seed批量摆道具，按人物半径膨胀后入口至交互点全部可达；任何道具中心合法但边缘伸进净空仍判失败。

## 源码证据

- [Repos/tidewater/src/world/debris/DebrisPlacement.js:1–195](https://github.com/dgreenheck/tidewater/blob/4811ba48d795197de5621985f404e765c0b7c0ef/src/world/debris/DebrisPlacement.js#L1-L195)：空间hash障碍和独立占用间隔结构
- [Repos/tidewater/src/world/debris/DebrisPlacement.js:240–327](https://github.com/dgreenheck/tidewater/blob/4811ba48d795197de5621985f404e765c0b7c0ef/src/world/debris/DebrisPlacement.js#L240-L327)：按语义tag扩展障碍，门前胶囊通道、出生区和clear三重过滤

## 项目效果图

![tidewater · observed_still](../assets/previews/tidewater-85a2ca018d2a.jpg)

已view_image docs/screenshot.jpg：夕阳码头、近景木栏杆/绳索/灯具/钓竿、远近水色层次。仅为历史静帧，没有证明当前实时水体、声画同步或性能。

来源：[原作者/出处](https://github.com/dgreenheck/tidewater/blob/4811ba48d795197de5621985f404e765c0b7c0ef/docs/screenshot.jpg) · observed_still。静帧观察；没有由此验证连续动画或性能。

## 归纳与练习

暂未归入新增专业视角；保留原机制边界。

[MP-10](../patterns/MP-10.md)
