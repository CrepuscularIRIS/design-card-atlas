# SD-NZ03 · 让近景立面模块与远景照片保持同一窗格身份
案例：[ neon-zenith ](../cases/neon-zenith.md) · 机制证据：`still_observed`

效果图用于理解来源作品，不自动验证本卡中的每个机制。

## 设计动作

距离变化时应减少细节，而不是把同一栋楼换成另一套窗户。

## 实现与参数

kit metadata→faceW/nb算colFit→共享bayOff/floorOff→每kit/LOD/cell批次；70m以内高模，位移6m更新可见cell；被相邻建筑盖住的面不放。

## 审美细节

近处空调/窗帘/房间的身份对应远处captured facade；这比只增加面数更能避免跳变。

## 适用条件

- 合法可拆分资产
- 一致UV/楼层坐标

## 相邻方案与区别

与全城impostor相比保留英雄建筑细节；与每距离随机换窗相比维持身份。

## 失败模式

- CC BY模型需保留作者与变更说明
- 切片格网与照片不一致产生跳变
- 性能系统不能替代建模质量

## Movie 裁决

- **verdict**：adapt
- **reason**：镜头拉远时可维持连续性。

## Frontend 裁决

- **verdict**：defer
- **reason**：先单建筑制作匹配远景图，再评估范围化系统。

## 最小对照

0→80m拉远固定曝光，逐窗身份不变且无明显双层表面；拍到近远错位即失败。

## 源码证据

- [Repos/neon-zenith/src/city/facadekit.js:1–47](https://github.com/billpwchan/neon-zenith/blob/27ad04ef04aa9e1e1366fccc63e15a379b999f01/src/city/facadekit.js#L1-L47)：模型切成bay×floor单元并加载匹配纹理
- [Repos/neon-zenith/src/city/facadekit.js:92–145](https://github.com/billpwchan/neon-zenith/blob/27ad04ef04aa9e1e1366fccc63e15a379b999f01/src/city/facadekit.js#L92-L145)：同bayOff/floorOff选cell，70m细LOD，移动6m重列

## 项目效果图

![neon-zenith · observed_still](../assets/previews/neon-zenith-a855ac555caa.jpg)

已view_image docs/media/market.jpg：黑色楼峡、横竖霓虹、暖路灯与湿地纵向反光；历史静帧不证明动态。

来源：[原作者/出处](https://github.com/billpwchan/neon-zenith/blob/27ad04ef04aa9e1e1366fccc63e15a379b999f01/docs/media/market.jpg) · observed_still。静帧观察；没有由此验证连续动画或性能。

## 归纳与练习

暂未归入新增专业视角；保留原机制边界。

[MP-09](../patterns/MP-09.md) / [MP-22](../patterns/MP-22.md)
