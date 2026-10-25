# SHOW-022 · 让指针痕迹具有可持续的流动记忆
案例：[ awesome-opus5.5-frontend-showcases ](../cases/awesome-opus5.5-frontend-showcases.md) · 机制证据：`source_only`

效果图用于理解来源作品，不自动验证本卡中的每个机制。

## 设计动作

一次划动继续卷曲、扩散并消退，产生可追踪因果；历史封面可见复杂卷曲色带，未验证动态稳定性。

## 实现与参数

step(dt)双FBO交换；黏性仅nu×dt>.002才迭代；速度与染料分别advect，decay=exp(-rate×dt)。

## 审美细节

一次划动继续卷曲、扩散并消退，产生可追踪因果；历史封面可见复杂卷曲色带，未验证动态稳定性。

## 适用条件

- 有非关键的交互画布
- 输入区域与页面滚动不冲突

## 相邻方案与区别

相对普通尾迹更有流体卷曲；如果只是提示点击，简短ripple更合适。

## 失败模式

- 全屏艳色遮挡内容
- 固定步长假设导致帧率相关
- 模拟昂贵且缺乏语义价值

## Movie 裁决

- **verdict**：reference
- **reason**：可离线录制为短片能量纹理，需控制构图。

## Frontend 裁决

- **verdict**：defer
- **reason**：当前阅读主线不应被全屏流体干扰。

## 最小对照

同轨迹在30/60/120Hz输入比较衰减形态；遮住按钮或手势抢滚动立即拒绝。

## 源码证据

- [Repos/awesome-opus5.5-frontend-showcases/repro/neon-fluid/index.html:1147–1207](https://github.com/OpenVGLab/awesome-opus5.5-frontend-showcases/blob/cac43b250f07b7b86f4709c61effc84269f46494/repro/neon-fluid/index.html#L1147-L1207)：ambient→curl/vorticity→viscosity→divergence→pressure迭代→gradientSubtract→velocity/dye advection，指数时间衰减

## 项目效果图

![awesome-opus5.5-frontend-showcases · historical_still_viewed](../assets/previews/awesome-opus5-5-frontend-showcases-bd3f08f61282.jpg)

已查看的来源静帧；不证明当前版本运行。

来源：[原作者/出处](https://github.com/OpenVGLab/awesome-opus5.5-frontend-showcases/blob/cac43b250f07b7b86f4709c61effc84269f46494/repro/_covers/neon-fluid.jpg) · historical_still_viewed。历史封面，不能证明当前运行/运动/交互

## 归纳与练习

暂未归入新增专业视角；保留原机制边界。

保留独立案例。
