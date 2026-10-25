# SD-NZ04 · 用建筑独立随机流维护体量与细节迭代的稳定性
案例：[ neon-zenith ](../cases/neon-zenith.md) · 机制证据：`still_observed`

效果图用于理解来源作品，不自动验证本卡中的每个机制。

## 设计动作

修改屋顶细节不应让商铺和灯牌换位置，否则无法做可归因A/B。

## 实现与参数

rngFor(seed,salt)使用seed整数异或salt；cornice、louvre、led、plant赋功能标签；退台高度>200/400决定2/3段；双塔gap至少9、桥高5–8。

## 审美细节

灯只强调冠顶和结构转折，外壳、百叶、设备层分材质身份。

## 适用条件

- 明确楼体/店铺/道具责任域

## 相邻方案与区别

比全局固定seed更强：全局seed遇到插入一次random仍会连锁改变后续布局。

## 失败模式

- 把独立流接回共享rng会重新耦合
- 过多家族缺统一尺度

## Movie 裁决

- **verdict**：adapt
- **reason**：可借结构而非量级

## Frontend 裁决

- **verdict**：prototype
- **reason**：可先以一个窗外塔测试，几何逻辑不依赖TSL材质。

## 最小对照

修改冠顶随机选择后，地块、入口、招牌坐标hash不变；轮廓必须通过主镜头检查。

## 源码证据

- [Repos/neon-zenith/src/city/massing.js:1–16](https://github.com/billpwchan/neon-zenith/blob/27ad04ef04aa9e1e1366fccc63e15a379b999f01/src/city/massing.js#L1-L16)：建筑seed独立rngFor
- [Repos/neon-zenith/src/city/massing.js:24–59](https://github.com/billpwchan/neon-zenith/blob/27ad04ef04aa9e1e1366fccc63e15a379b999f01/src/city/massing.js#L24-L59)：四冠顶家族与高塔天线
- [Repos/neon-zenith/src/city/massing.js:63–129](https://github.com/billpwchan/neon-zenith/blob/27ad04ef04aa9e1e1366fccc63e15a379b999f01/src/city/massing.js#L63-L129)：退台、错动、双塔语法

## 项目效果图

![neon-zenith · observed_still](../assets/previews/neon-zenith-a855ac555caa.jpg)

已view_image docs/media/market.jpg：黑色楼峡、横竖霓虹、暖路灯与湿地纵向反光；历史静帧不证明动态。

来源：[原作者/出处](https://github.com/billpwchan/neon-zenith/blob/27ad04ef04aa9e1e1366fccc63e15a379b999f01/docs/media/market.jpg) · observed_still。静帧观察；没有由此验证连续动画或性能。

## 归纳与练习

暂未归入新增专业视角；保留原机制边界。

[MP-08](../patterns/MP-08.md)
