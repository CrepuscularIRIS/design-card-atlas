# SHOW-015 · 按深度插入雾幕与前景物，控制二维海景遮挡
案例：[ awesome-opus5.5-frontend-showcases ](../cases/awesome-opus5.5-frontend-showcases.md) · 机制证据：`source_only`

效果图用于理解来源作品，不自动验证本卡中的每个机制。

## 设计动作

二维也可通过一致遮挡序建立纵深，雾不应作为最后一层均匀白色蒙版。封面可见远云、岛、海面、前景波纹的层次。

## 实现与参数

island→drawSky/clouds→depth inserts→drawSea(L,t,inserts)→drawSheen→beam→近雾→rain/snow；fog veil与bank有不同层深。

## 审美细节

二维也可通过一致遮挡序建立纵深，雾不应作为最后一层均匀白色蒙版。封面可见远云、岛、海面、前景波纹的层次。

## 适用条件

- 相机为受控2D变换
- 每层有明确深度

## 相邻方案与区别

相对单层后期雾，可控制前后遮挡，但不是真体积散射。

## 失败模式

- 自由3D移动会失去正确交叉
- 全屏近雾影响前景UI

## Movie 裁决

- **verdict**：prototype
- **reason**：适用于2D序章/海报动图。

## Frontend 裁决

- **verdict**：reference
- **reason**：仅用于手机内展示或背景视频，不能替代3D Places雾。

## 最小对照

固定色板比较末层白雾/深度插入；去掉纹理后仍应读出前后关系，否则机制不足。

## 源码证据

- [Repos/awesome-opus5.5-frontend-showcases/repro/xhs-free-short/js/film.js:141–169](https://github.com/OpenVGLab/awesome-opus5.5-frontend-showcases/blob/cac43b250f07b7b86f4709c61effc84269f46494/repro/xhs-free-short/js/film.js#L141-L169)：island按d=.262/.3/.372插入岛/堤/危险物，雾位于.28/.34，海后绘制beam/近雾/雨雪

## 项目效果图

![awesome-opus5.5-frontend-showcases · historical_still_viewed](../assets/previews/awesome-opus5-5-frontend-showcases-c6da1cbf3e3b.jpg)

已查看的来源静帧；不证明当前版本运行。

来源：[原作者/出处](https://github.com/OpenVGLab/awesome-opus5.5-frontend-showcases/blob/cac43b250f07b7b86f4709c61effc84269f46494/repro/_covers/xhs-free-short.jpg) · historical_still_viewed。历史封面，不能证明当前运行/运动/交互

## 归纳与练习

暂未归入新增专业视角；保留原机制边界。

保留独立案例。
