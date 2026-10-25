# SHOW-004 · 以分层雾化轮廓补足窗外城市纵深
案例：[ awesome-opus5.5-frontend-showcases ](../cases/awesome-opus5.5-frontend-showcases.md) · 机制证据：`source_only`

效果图用于理解来源作品，不自动验证本卡中的每个机制。

## 设计动作

远层更受雾染，近层更深；少量亮窗跨层保留城市生活感。源封面视野主要为近景，远层效果未单独观察。

## 实现与参数

defs三层→PlaneGeometry(900,512×scale)；轮廓混入uHaze，lum>.25保留uWin=1.6的亮窗贡献。

## 审美细节

远层更受雾染，近层更深；少量亮窗跨层保留城市生活感。源封面视野主要为近景，远层效果未单独观察。

## 适用条件

- 视角范围受限
- 场景有明确地平线

## 相邻方案与区别

与完整远景城市相比成本低，但只承担背景轮廓。

## 失败模式

- 自由绕行会看见纸片
- 透明排序和窗框遮挡冲突
- 层间移动视差不符合真实尺度

## Movie 裁决

- **verdict**：prototype
- **reason**：适合室内向窗外的限定电影机位。

## Frontend 裁决

- **verdict**：adapt
- **reason**：自由移动需要360度围合或限制可见角度。

## 最小对照

横向移动2米与转头60度比较一层/三层；若边缘暴露或天空跟随建筑移动，判失败。

## 源码证据

- [Repos/awesome-opus5.5-frontend-showcases/repro/catwalk/js/sky.js:125–165](https://github.com/OpenVGLab/awesome-opus5.5-frontend-showcases/blob/cac43b250f07b7b86f4709c61effc84269f46494/repro/catwalk/js/sky.js#L125-L165)：三张天际线位于z=-230/-135/-72，haze=.72/.5/.28，亮窗单独衰减

## 项目效果图

![awesome-opus5.5-frontend-showcases · historical_still_viewed](../assets/previews/awesome-opus5-5-frontend-showcases-d4e64693ab20.jpg)

已查看的来源静帧；不证明当前版本运行。

来源：[原作者/出处](https://github.com/OpenVGLab/awesome-opus5.5-frontend-showcases/blob/cac43b250f07b7b86f4709c61effc84269f46494/repro/_covers/catwalk.jpg) · historical_still_viewed。历史封面，不能证明当前运行/运动/交互

## 归纳与练习

暂未归入新增专业视角；保留原机制边界。

[MP-09](../patterns/MP-09.md)
