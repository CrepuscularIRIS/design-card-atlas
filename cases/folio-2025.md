# folio-2025
已读材质、显现与输入入口局部；可借色彩与同步机制，不整套迁TSL，不移植车辆形象。

## 案例档案

[来源仓库](https://github.com/brunosimon/folio-2025)
分析版本：`41046b57eeed8d156d9c3fd7fa259900baef7816`

模型归属未独立认证。

## 初始源码审计边界

未读完整世界模块、赛车物理、任务、互动点后半逻辑及二进制模型。

以下保留初始源码审计的观察范围。后续新增静帧独立列于视觉材料，不追溯证明全部机制或运行状态。

## 机制与案例分析

### [SD-FO01 · 把色相与发光亮度分开调节](../cards/SD-FO01.md)

不同色相在相同RGB强度下不等亮，亮度归一可使色板调整不意外改变焦点。

share-image静帧为低多边形暖地面、紫灰岩石、橙灯；本站仅提取控制方法，不照搬紫色背景。

**Movie：prototype** · 霓虹焦点与物件颜色能分别A/B。
**前端：adapt** · 先对单标牌emissive应用，保留bloom阈值和曝光控制。

失败条件：- 原公式黑色除零
- 归一不等于人眼所有颜色感知完全相同
- TSL不可原样进r170

### [SD-FO02 · 让统一显现边界同步材质、镜头与输入解锁](../cards/SD-FO02.md)

空间显现、镜头和可操作状态由一个阶段推进，避免画面未出现用户已走出场。

边缘厚.05、原色#e88eff/5.5；本站可改青白扫描，不直接借紫色主题。

**Movie：adapt** · 适合局部装置重建/回忆显现。
**前端：defer** · 不能再给Title加进入仪式；只作可选事件。

失败条件：- 阴影/透明/自定义材质漏接
- 全局singleton耦合
- 弹性半径回摆可能重复闪现

### [SD-FO03 · 给风格化暗面保留地面反色和统一阴影色](../cards/SD-FO03.md)

暗面也参与色彩构图，但补色应有朝向/高度约束。

有色阴影适合低多边形风格；不是物理GI，地面反色仅按朝向高度。

**Movie：reference** · 可借暗部配色，不替换全部PBR。
**前端：defer** · 现有bake场景不可叠加同类暗部色造成双重处理。

失败条件：- 会覆盖真实PBR能量关系
- 直接叠加造成双重染色

## 项目效果与观察材料

![folio-2025 · observed_still](../assets/previews/folio-2025-bc0cef82ca68.png)

已view_image static/social/share-image.png：暖橙草地/灯、紫灰石、红车低多边形静帧；不是当前运行截图。

来源：[原作者/出处](https://github.com/brunosimon/folio-2025/blob/41046b57eeed8d156d9c3fd7fa259900baef7816/static/social/share-image.png) · observed_still。静帧观察；没有由此验证连续动画或性能。

## 复用边界

- **status**：observed
- **evidence**：license.md MIT ©2025 Bruno Simon；音效/商业品牌等资产未逐项核权
- **reuse**：conditional

图片及第三方素材的权利单独保留；源代码许可证不自动授权媒体。
