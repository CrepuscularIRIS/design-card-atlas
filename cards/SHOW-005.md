# SHOW-005 · 用楼层节律与稀疏亮窗给简单楼体可读尺度
案例：[ awesome-opus5.5-frontend-showcases ](../cases/awesome-opus5.5-frontend-showcases.md) · 机制证据：`source_only`

效果图用于理解来源作品，不自动验证本卡中的每个机制。

## 设计动作

建筑轮廓可简单，楼层/窗口节律提供尺度参照；历史封面可见条带和稀疏窗。

## 实现与参数

TOWER_VERT→vLocal/vH/vSeed→TOWER_FRAG；窗口side屏蔽屋顶，winA/B两色，边缘灯带仅占9单位周期的.025。

## 审美细节

建筑轮廓可简单，楼层/窗口节律提供尺度参照；历史封面可见条带和稀疏窗。

## 适用条件

- 用作中远景
- instance缩放/世界尺寸解释一致

## 相邻方案与区别

比逐窗建模轻，但不能代替近景入口/窗洞/屋顶设备。

## 失败模式

- 近看表面无深度
- 重复统一盒体会像阵列
- 频繁呼吸亮度削弱真实城市感

## Movie 裁决

- **verdict**：adapt
- **reason**：背景移动镜头有效，主楼仍需轮廓独特。

## Frontend 裁决

- **verdict**：adapt
- **reason**：只用于不可抵达背景楼。

## 最小对照

固定楼群，比较无窗格/规则全亮/稀疏双色；远看尺度不清或近景全是盒子则拒绝。

## 源码证据

- [Repos/awesome-opus5.5-frontend-showcases/repro/warp-shooter/src/env.js:122–155](https://github.com/OpenVGLab/awesome-opus5.5-frontend-showcases/blob/cac43b250f07b7b86f4709c61effc84269f46494/repro/warp-shooter/src/env.js#L122-L155)：实例矩阵产生局部世界尺寸，1.7×1.25窗格，hash>.74点亮，9单位灯带

## 项目效果图

![awesome-opus5.5-frontend-showcases · historical_still_viewed](../assets/previews/awesome-opus5-5-frontend-showcases-3656ae17e6b9.jpg)

已查看的来源静帧；不证明当前版本运行。

来源：[原作者/出处](https://github.com/OpenVGLab/awesome-opus5.5-frontend-showcases/blob/cac43b250f07b7b86f4709c61effc84269f46494/repro/_covers/warp-shooter.jpg) · historical_still_viewed。历史封面，不能证明当前运行/运动/交互

## 归纳与练习

暂未归入新增专业视角；保留原机制边界。

[MP-09](../patterns/MP-09.md)
