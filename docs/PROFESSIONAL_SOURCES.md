# 专业视角的一手参考

这些资料支持诊断视角，不替代每个项目的源码与视觉证据。

## [Physically Based Rendering 4e — Transmittance](https://www.pbr-book.org/4ed/Volume_Scattering/Transmittance)

CINE-05：透射率表达沿路径因消光而保留的辐射比例；分段透射可相乘，光源到表面的介质衰减影响阴影。用于区分背景衰减、入射散射与整屏泛白。

边界：一手渲染教材；说明物理关系，不证明godrays/星云代码正确或画面美观。本轮已打开原文。

## [Physically Based Rendering 3e — Projective Camera Models](https://www.pbr-book.org/3ed-2018/Camera_Models/Projective_Camera_Models)

CINE-07/08：相机变换、投影、取景窗是不同参数；有限孔径使用lensRadius与focalDistance构造景深。支持把机位/FOV/对焦与镜头采样分开裁决。

边界：理想化投影与薄透镜模型，不替代真实镜头畸变、呼吸效应或实际电影摄影经验；不认证仓库实现。本轮已打开原文。

## [darktable user manual — AgX](https://darktable-org.github.io/dtdocs/en/module-reference/processing-modules/agx/)

CINE-04：区分场景参照与显示参照处理；通常仅启用一个tone mapper，先调中间调，再检查亮色向白的过渡与饱和度。用于检查过曝和重复映射。

边界：darktable官方实现文档，受Blender AgX启发；不能据此认为web-ocean的shader与其数学实现、色域或输出完全一致。本轮已打开原文。

## [Carbon Design System — Typography](https://www.carbondesignsystem.com/building-blocks/foundations/typography/overview)

IF-01、IF-02：以字号/字重/行高形成层级，区分任务型与表现型排版；连续正文采用中性色，动作色有明确职责。

边界：官方设计系统的角色分工参考，不是所有产品的字体与字号标准；不要求使用IBM Plex或蓝色，中文和本项目内容仍需独立验证。

## [W3C — Understanding SC 4.1.3 Status Messages](https://www.w3.org/WAI/WCAG22/Understanding/status-messages.html)

IF-05：状态消息需提供可程序识别的语义，让辅助技术获得状态而不强行转移焦点；单独播报变化数字可能缺少上下文。

边界：这是WCAG解释性资料；不是所有DOM变化都属于状态消息。引用不等于对这些仓库完成合规审核。

## [W3C — Understanding SC 2.3.3 Animation from Interactions](https://www.w3.org/WAI/WCAG22/Understanding/animation-from-interactions.html)

IF-07：用户触发的非必要运动应可关闭，系统减少运动偏好是实现途径之一；区别交互触发与自动开始的运动。

边界：SC 2.3.3为AAA层级，此页面为解释性资料；必要性与具体实现需分别判断，不等于光敏安全认证，也不涵盖所有音频问题。

## [web.dev — Rendering performance](https://web.dev/articles/rendering-performance)

IF-08：将浏览器绘制拆为JavaScript、样式、布局、绘制与合成；动画预算和离散操作响应应按任务分别检查。

边界：页面给的是一般浏览器工作原理与设备相关指导，不能替代本项目设备实测，也不证明用transform就必然无性能问题；本阶段不执行性能重构。
