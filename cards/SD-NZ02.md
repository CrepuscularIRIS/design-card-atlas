# SD-NZ02 · 让雨条相对相机运动并在屋檐处停止
案例：[ neon-zenith ](../cases/neon-zenith.md) · 机制证据：`still_observed`

效果图用于理解来源作品，不自动验证本卡中的每个机制。

## 设计动作

雨的可信度来自运动相对关系和遮蔽，不是单纯提高数量。

## 实现与参数

hash(index,time)世界锚定→相机盒wrap→高度图剔除→vel-camVel*.85，长度|relV|*.034 clamp(.25,3.5)；宽度max(base,dist*.0011)，alpha按base/w衰减。

## 审美细节

远近两层盒26/110m；雨到街面变彩，进雨棚消失；源参数很重，不建议按原数量照搬。

## 适用条件

- 有高度图/简化屋顶mask
- 相机速度稳定

## 相邻方案与区别

与SV相机盒循环互补：本卡增加遮雨和曝光长度，不只循环复用。

## 失败模式

- 单层heightmap不表达桥下多层空间
- TSL移植成本
- 过量additive雨变亮噪声

## Movie 裁决

- **verdict**：prototype
- **reason**：可验证进屋檐、加速镜头中雨的变化。

## Frontend 裁决

- **verdict**：adapt
- **reason**：从已有place雨系统补遮蔽/相对运动即可。

## 最小对照

静止/前进/横移及进雨棚四段，雨不可粘镜头、穿顶；近远亮度不能骤变。

## 源码证据

- [Repos/neon-zenith/src/atmos/rain.js:18–65](https://github.com/billpwchan/neon-zenith/blob/27ad04ef04aa9e1e1366fccc63e15a379b999f01/src/atmos/rain.js#L18-L65)：world anchored wrap、heightmap遮雨、相对速度长度、像素宽度守恒
- [Repos/neon-zenith/src/atmos/rain.js:130–144](https://github.com/billpwchan/neon-zenith/blob/27ad04ef04aa9e1e1366fccc63e15a379b999f01/src/atmos/rain.js#L130-L144)：近14000远22000及2600溅水配置

## 项目效果图

![neon-zenith · observed_still](../assets/previews/neon-zenith-a855ac555caa.jpg)

已view_image docs/media/market.jpg：黑色楼峡、横竖霓虹、暖路灯与湿地纵向反光；历史静帧不证明动态。

来源：[原作者/出处](https://github.com/billpwchan/neon-zenith/blob/27ad04ef04aa9e1e1366fccc63e15a379b999f01/docs/media/market.jpg) · observed_still。静帧观察；没有由此验证连续动画或性能。

## 归纳与练习

暂未归入新增专业视角；保留原机制边界。

[MP-06](../patterns/MP-06.md)
