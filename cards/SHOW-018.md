# SHOW-018 · 只显示朝向观众的物件热点并同步键盘可达性
案例：[ awesome-opus5.5-frontend-showcases ](../cases/awesome-opus5.5-frontend-showcases.md) · 机制证据：`source_only`

效果图用于理解来源作品，不自动验证本卡中的每个机制。

## 设计动作

提示文字跟随实物而不是遮挡在背面；源码只是朝向近似，并非深度遮挡检测。封面是hero页，未观察360热点。

## 实现与参数

hotspot position/normal→worldMatrix/normalMatrix→dotToCam→project→DOM transform；位置右侧超过62%翻转标签方向。

## 审美细节

提示文字跟随实物而不是遮挡在背面；源码只是朝向近似，并非深度遮挡检测。封面是hero页，未观察360热点。

## 适用条件

- 物件表面法线有效
- 背面自遮挡可由朝向近似表达

## 相邻方案与区别

相对所有热点常显更清楚；复杂场景需深度查询或raycast补充。

## 失败模式

- 凹形物件正面仍被别物遮挡
- 旧焦点可能留在被隐藏按钮
- 当前固定视角只观看不能擅加标记

## Movie 裁决

- **verdict**：reference
- **reason**：镜头字幕定位可借用，但不需交互热点。

## Frontend 裁决

- **verdict**：adapt
- **reason**：适合独立物件inspect页，不能套到固定观赏视角。

## 最小对照

转到背面和被遮挡位置并Tab遍历；隐藏热点仍可聚焦或标签穿物即失败。

## 源码证据

- [Repos/awesome-opus5.5-frontend-showcases/repro/product-landing/js/viewer.js:77–110](https://github.com/OpenVGLab/awesome-opus5.5-frontend-showcases/blob/cac43b250f07b7b86f4709c61effc84269f46494/repro/product-landing/js/viewer.js#L77-L110)：热点世界位置投影，法线dot>0.12且explode<.5才显示，tabIndex同步
- [Repos/awesome-opus5.5-frontend-showcases/repro/product-landing/js/viewer.js:120–139](https://github.com/OpenVGLab/awesome-opus5.5-frontend-showcases/blob/cac43b250f07b7b86f4709c61effc84269f46494/repro/product-landing/js/viewer.js#L120-L139)：热点触发球坐标相机插值，theta最短角路径，默认900ms且减动1ms

## 项目效果图

![awesome-opus5.5-frontend-showcases · historical_still_viewed](../assets/previews/awesome-opus5-5-frontend-showcases-29822a37f8f4.jpg)

已查看的来源静帧；不证明当前版本运行。

来源：[原作者/出处](https://github.com/OpenVGLab/awesome-opus5.5-frontend-showcases/blob/cac43b250f07b7b86f4709c61effc84269f46494/repro/_covers/product-landing.jpg) · historical_still_viewed。历史封面，不能证明当前运行/运动/交互

## 归纳与练习

暂未归入新增专业视角；保留原机制边界。

[MP-20](../patterns/MP-20.md)
