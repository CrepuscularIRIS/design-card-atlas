# LIVE-006 · 让加载标记沿场景视觉语言变化且对应真实进度
案例：[ opus55-live-demos ](../cases/opus55-live-demos.md) · 机制证据：`source_only`

效果图用于理解来源作品，不自动验证本卡中的每个机制。

## 设计动作

加载过程可以延续场景的墨圈与花瓣语言；进度环读取显式p，循环装饰不能冒充真实进度。源码未核对所有调用点，故不认证进度准确。

## 实现与参数

__load(p)→strokeDashoffset=1−clamp(p,.015,1)；track/pathLength1，加载圆圈笔刷filter displacement1.8；彗尾2.2s循环，容器淡出1.1s。

## 审美细节

加载过程可以延续场景的墨圈与花瓣语言；进度环读取显式p，循环装饰不能冒充真实进度。源码未核对所有调用点，故不认证进度准确。

## 适用条件

- 加载器提供实际进度
- 失败与重试另外可见
- 尊重减动

## 相邻方案与区别

相对通用spinner更有场景身份，但不能牺牲失败处理。

## 失败模式

- ARIA hidden整个加载区缺少状态告知
- 资产失败仍满圈
- 源代码/素材许可未知

## Movie 裁决

- **verdict**：reference
- **reason**：movie缓冲时可延续片头语言。

## Frontend 裁决

- **verdict**：adapt
- **reason**：仅为Places加载器，Title保持不动。

## 最小对照

模拟一资源失败和减动，观察完成比例、错误可达性与内容出现；假满进度或永久等待失败。

## 源码证据

- `Repos/opus55-live-demos/sakura-valley.html:20–33`：墨圈/彗尾/花瓣CSS，减动关闭动画（无上游永久链接）
- `Repos/opus55-live-demos/sakura-valley.html:46–57`：window.__load(p)映射strokeDashoffset；外部脚本入口scene-SV5IBQX7.js（无上游永久链接）

## 项目效果图

![opus55-live-demos · author_og_loading_state](../assets/previews/scene-opus55-live-demos-1.jpg)

实际查看：暗绿黑背景中央是一段暖色墨圈弧线、少量花瓣与细环；没有山谷/水面/树木。

来源：[原作者/出处](https://here.now/og/vowful-prism-y87r.jpg) · author_og_loading_state。仅对应Sakura Valley的加载标记卡LIVE-006。官方OG截在加载态，严禁当作已加载山谷效果图或fog-over-the-gate画面。

## 归纳与练习

暂未归入新增专业视角；保留原机制边界。

[MP-15](../patterns/MP-15.md)
