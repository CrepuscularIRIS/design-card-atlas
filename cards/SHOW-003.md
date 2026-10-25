# SHOW-003 · 以窗内生活剪影区分建筑占用状态
案例：[ awesome-opus5.5-frontend-showcases ](../cases/awesome-opus5.5-frontend-showcases.md) · 机制证据：`source_only`

效果图用于理解来源作品，不自动验证本卡中的每个机制。

## 设计动作

不同窗口不是随机明暗矩形，而是用窗帘、植物、人物等内部遮挡暗示活动；静帧中的纸窗人物剪影与暖光可见。

## 实现与参数

WIN映射16种语义→windowAtlas()；暖光从(255,214,150)到(150,70,34)，seed81；plant26叶形、blinds11px节距。

## 审美细节

不同窗口不是随机明暗矩形，而是用窗帘、植物、人物等内部遮挡暗示活动；静帧中的纸窗人物剪影与暖光可见。

## 适用条件

- 窗存在性与亮暗随机应独立
- 近景有窗框和墙厚支撑

## 相邻方案与区别

相对parallax room mapping更轻；不适合可走近或进入的窗内空间。

## 失败模式

- 透明贴片近看无视差
- 所有窗同样亮使楼层身份丢失
- 图集边界渗色

## Movie 裁决

- **verdict**：prototype
- **reason**：固定中景窗可用剪影形成次叙事。

## Frontend 裁决

- **verdict**：adapt
- **reason**：远近分层，近窗必要时增加室内几何。

## 最小对照

保持几何与光照，比较统一亮窗/语义窗口；关闭bloom后仍应区分亮暗和窗框，无法区分则失败。

## 源码证据

- [Repos/awesome-opus5.5-frontend-showcases/repro/catwalk/js/textures.js:217–279](https://github.com/OpenVGLab/awesome-opus5.5-frontend-showcases/blob/cac43b250f07b7b86f4709c61effc84269f46494/repro/catwalk/js/textures.js#L217-L279)：4×4图集，暖亮/暗/纸屏/现代四行，窗帘植物百叶剪影；1024图集256单格

## 项目效果图

![awesome-opus5.5-frontend-showcases · historical_still_viewed](../assets/previews/awesome-opus5-5-frontend-showcases-d4e64693ab20.jpg)

已查看的来源静帧；不证明当前版本运行。

来源：[原作者/出处](https://github.com/OpenVGLab/awesome-opus5.5-frontend-showcases/blob/cac43b250f07b7b86f4709c61effc84269f46494/repro/_covers/catwalk.jpg) · historical_still_viewed。历史封面，不能证明当前运行/运动/交互

## 归纳与练习

暂未归入新增专业视角；保留原机制边界。

保留独立案例。
