# SD-NZ01 · 让招牌、地面、雨雾共享同一发光分布
案例：[ neon-zenith ](../cases/neon-zenith.md) · 机制证据：`still_observed`

效果图用于理解来源作品，不自动验证本卡中的每个机制。

## 设计动作

把环境的颜色出处固定到场景光源位置，减少只在屏幕上添加独立彩雾的脱节。

## 实现与参数

lamps/shopfronts/signs→Canvas lighter合成，extent1750；店铺半径5.5，灯13；招牌高度fall=1/(1+(y/9)^2)；生成near与far，雨色=基础雨色(.42,.46,.56)*.22 + lm*(2.4*exp(-(p.y-max(cover,0))/26)+.25) + 闪电色(.7,.8,1)*U.flash*1.6；地面同时用near/far，雾用far。

## 审美细节

钠灯#ffae55、LED#cfe2ff，商店含暖白/冷白；market.jpg历史静帧中招牌与湿地彩色竖向反光一致，但未证实每种动态采样。

## 适用条件

- 场景平面高度结构较简单
- 发光体位置可读
- 线性色彩空间一致

## 相邻方案与区别

不同于LightPool动态灯预算；这是艺术化空间色场，不是物理GI。

## 失败模式

- 2D光图没有遮挡与垂向结构
- bake加光图可能重复照明
- TSL版本不可直接兼容

## Movie 裁决

- **verdict**：prototype
- **reason**：固定夜街镜头可直接比较光色因果一致性。

## Frontend 裁决

- **verdict**：adapt
- **reason**：移植世界坐标光图及采样逻辑，不能整包TSL搬进r170。

## 最小对照

关掉某一招牌时，对应位置雨雾色也消失；灰墙不应无条件变彩，房间不能隔墙漏光。

## 源码证据

- [Repos/neon-zenith/src/city/lightmap.js:6–81](https://github.com/billpwchan/neon-zenith/blob/27ad04ef04aa9e1e1366fccc63e15a379b999f01/src/city/lightmap.js#L6-L81)：2048街面光图及256模糊远场图
- [Repos/neon-zenith/src/atmos/rain.js:56–59](https://github.com/billpwchan/neon-zenith/blob/27ad04ef04aa9e1e1366fccc63e15a379b999f01/src/atmos/rain.js#L56-L59)：雨色采样街面光图并按离地高度衰减
- [Repos/neon-zenith/src/city/ground.js:85–92](https://github.com/billpwchan/neon-zenith/blob/27ad04ef04aa9e1e1366fccc63e15a379b999f01/src/city/ground.js#L85-L92)：地面近场光图与高空far色场共同驱动emissive
- [Repos/neon-zenith/src/atmos/fog.js:50–60](https://github.com/billpwchan/neon-zenith/blob/27ad04ef04aa9e1e1366fccc63e15a379b999f01/src/atmos/fog.js#L50-L60)：雾haze/cloud颜色均读取lightmap.far

## 项目效果图

![neon-zenith · observed_still](../assets/previews/neon-zenith-a855ac555caa.jpg)

已view_image docs/media/market.jpg：黑色楼峡、横竖霓虹、暖路灯与湿地纵向反光；历史静帧不证明动态。

来源：[原作者/出处](https://github.com/billpwchan/neon-zenith/blob/27ad04ef04aa9e1e1366fccc63e15a379b999f01/docs/media/market.jpg) · observed_still。静帧观察；没有由此验证连续动画或性能。

## 归纳与练习

暂未归入新增专业视角；保留原机制边界。

[MP-03](../patterns/MP-03.md)
