# SD-FO01 · 把色相与发光亮度分开调节
案例：[ folio-2025 ](../cases/folio-2025.md) · 机制证据：`still_observed`

效果图用于理解来源作品，不自动验证本卡中的每个机制。

## 设计动作

不同色相在相同RGB强度下不等亮，亮度归一可使色板调整不意外改变焦点。

## 实现与参数

createEmissive: color/luminance(color)*intensity；渐变先mix再可选归一，默认强度3；橙/蓝预设1.7。

## 审美细节

share-image静帧为低多边形暖地面、紫灰岩石、橙灯；本站仅提取控制方法，不照搬紫色背景。

## 适用条件

- 线性RGB处理
- 分母epsilon与强度上限

## 相邻方案与区别

与只改饱和度不同，控制的是亮度；与完整电影调色是局部材质层控制。

## 失败模式

- 原公式黑色除零
- 归一不等于人眼所有颜色感知完全相同
- TSL不可原样进r170

## Movie 裁决

- **verdict**：prototype
- **reason**：霓虹焦点与物件颜色能分别A/B。

## Frontend 裁决

- **verdict**：adapt
- **reason**：先对单标牌emissive应用，保留bloom阈值和曝光控制。

## 最小对照

同目标亮度青/红/黄切换，焦点面积保持接近；极暗色引起过曝或NaN即失败。

## 源码证据

- [Repos/folio-2025/sources/Game/Materials.js:100–153](https://github.com/brunosimon/folio-2025/blob/41046b57eeed8d156d9c3fd7fa259900baef7816/sources/Game/Materials.js#L100-L153)：luminance系数与base/luminance×intensity

## 项目效果图

![folio-2025 · observed_still](../assets/previews/folio-2025-bc0cef82ca68.png)

已view_image static/social/share-image.png：暖橙草地/灯、紫灰石、红车低多边形静帧；不是当前运行截图。

来源：[原作者/出处](https://github.com/brunosimon/folio-2025/blob/41046b57eeed8d156d9c3fd7fa259900baef7816/static/social/share-image.png) · observed_still。静帧观察；没有由此验证连续动画或性能。

## 归纳与练习

暂未归入新增专业视角；保留原机制边界。

[MP-02](../patterns/MP-02.md)
