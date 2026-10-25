# SHOW-016 · 让场景摆放、路径和活动区引用同一份米制布局
案例：[ awesome-opus5.5-frontend-showcases ](../cases/awesome-opus5.5-frontend-showcases.md) · 机制证据：`source_only`

效果图用于理解来源作品，不自动验证本卡中的每个机制。

## 设计动作

几何、脚下路径与交互区一致是空间设计本体。当前只读声明，未逐个跟踪所有消费者，不能声称所有碰撞都正确。

## 实现与参数

BUILDINGS {x,z,w,d,rot}；PATHS {w,pts}；围栏gate明确缺口；POND在(6,44),r9且PLACES引用同一POND。

## 审美细节

几何、脚下路径与交互区一致是空间设计本体。当前只读声明，未逐个跟踪所有消费者，不能声称所有碰撞都正确。

## 适用条件

- 所有消费者真正读同一布局
- 随机装饰固定seed

## 相邻方案与区别

相对先搭模型再补碰撞，提前统一空间契约。

## 失败模式

- 另一文件硬编码重复坐标
- 视觉门口有路但碰撞封住

## Movie 裁决

- **verdict**：adapt
- **reason**：分镜取景亦应引用布局中的地标。

## Frontend 裁决

- **verdict**：prototype
- **reason**：与当前逐场景layout SOP一致，优先核验执行情况。

## 最小对照

叠加建筑占地、道路、可走mask；每一出口必须连通，任何数据与画面偏移都失败。

## 源码证据

- [Repos/awesome-opus5.5-frontend-showcases/repro/farm-animals/js/layout.js:1–65](https://github.com/OpenVGLab/awesome-opus5.5-frontend-showcases/blob/cac43b250f07b7b86f4709c61effc84269f46494/repro/farm-animals/js/layout.js#L1-L65)：统一建筑宽深朝向、道路折线宽度、围栏门缺口
- [Repos/awesome-opus5.5-frontend-showcases/repro/farm-animals/js/layout.js:104–131](https://github.com/OpenVGLab/awesome-opus5.5-frontend-showcases/blob/cac43b250f07b7b86f4709c61effc84269f46494/repro/farm-animals/js/layout.js#L104-L131)：活动区和地点检测共享布局坐标；本段仅数据声明

## 项目效果图

![awesome-opus5.5-frontend-showcases · historical_still_viewed](../assets/previews/awesome-opus5-5-frontend-showcases-02d99c05fcab.jpg)

已查看的来源静帧；不证明当前版本运行。

来源：[原作者/出处](https://github.com/OpenVGLab/awesome-opus5.5-frontend-showcases/blob/cac43b250f07b7b86f4709c61effc84269f46494/repro/_covers/farm-animals.jpg) · historical_still_viewed。历史封面，不能证明当前运行/运动/交互

## 归纳与练习

暂未归入新增专业视角；保留原机制边界。

[MP-10](../patterns/MP-10.md)
