# SD-FO02 · 让统一显现边界同步材质、镜头与输入解锁
案例：[ folio-2025 ](../cases/folio-2025.md) · 机制证据：`still_observed`

效果图用于理解来源作品，不自动验证本卡中的每个机制。

## 设计动作

空间显现、镜头和可操作状态由一个阶段推进，避免画面未出现用户已走出场。

## 实现与参数

load圆环收束→半径3.5 reveal，2s back.out→用户输入→半径30，2s back.in→置99999；镜头缩放和input filters同阶段切换。

## 审美细节

边缘厚.05、原色#e88eff/5.5；本站可改青白扫描，不直接借紫色主题。

## 适用条件

- 事件可跳过
- 全部相关材质可接入

## 相邻方案与区别

与屏幕fade不同保留空间顺序；与Nexus镜头交接互补。

## 失败模式

- 阴影/透明/自定义材质漏接
- 全局singleton耦合
- 弹性半径回摆可能重复闪现

## Movie 裁决

- **verdict**：adapt
- **reason**：适合局部装置重建/回忆显现。

## Frontend 裁决

- **verdict**：defer
- **reason**：不能再给Title加进入仪式；只作可选事件。

## 最小对照

各类材质同步出现；中途跳过后无残留遮罩，无输入锁死，阴影不提前暴露。

## 源码证据

- [Repos/folio-2025/sources/Game/Reveal.js:12–19](https://github.com/brunosimon/folio-2025/blob/41046b57eeed8d156d9c3fd7fa259900baef7816/sources/Game/Reveal.js#L12-L19)：共享中心/距离/厚度/发光uniform
- [Repos/folio-2025/sources/Game/Reveal.js:50–93](https://github.com/brunosimon/folio-2025/blob/41046b57eeed8d156d9c3fd7fa259900baef7816/sources/Game/Reveal.js#L50-L93)：0→3.5半径显现和镜头缩放
- [Repos/folio-2025/sources/Game/Reveal.js:149–195](https://github.com/brunosimon/folio-2025/blob/41046b57eeed8d156d9c3fd7fa259900baef7816/sources/Game/Reveal.js#L149-L195)：点击后半径30再99999及wandering输入解锁
- [Repos/folio-2025/sources/Game/Materials/MeshDefaultMaterial.js:7–18](https://github.com/brunosimon/folio-2025/blob/41046b57eeed8d156d9c3fd7fa259900baef7816/sources/Game/Materials/MeshDefaultMaterial.js#L7-L18)：世界xz到中心距离控制discard及边缘色

## 项目效果图

![folio-2025 · observed_still](../assets/previews/folio-2025-bc0cef82ca68.png)

已view_image static/social/share-image.png：暖橙草地/灯、紫灰石、红车低多边形静帧；不是当前运行截图。

来源：[原作者/出处](https://github.com/brunosimon/folio-2025/blob/41046b57eeed8d156d9c3fd7fa259900baef7816/static/social/share-image.png) · observed_still。静帧观察；没有由此验证连续动画或性能。

## 归纳与练习

暂未归入新增专业视角；保留原机制边界。

保留独立案例。
