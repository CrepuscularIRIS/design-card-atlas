# SD-OT04 · 用正反俯仰和线框检验资产，并给渲染失败保留真实预览
案例：[ offshore-tower ](../cases/offshore-tower.md) · 机制证据：`still_observed`

效果图用于理解来源作品，不自动验证本卡中的每个机制。

## 设计动作

单个漂亮正面不证明资产完整；查看入口应同时提供结构检查、相机复位和真实的载入失败状态。

## 实现与参数

离线生成reference/rear/left/right/above/below六张；网页另有detail视点。wireframe保存原mesh可见状态并独立切换，reset只动相机，reduce-motion直接复位，否则240ms cubic ease；WebGL/WebGPU启动失败继续显示本地poster并明确Static preview。

## 审美细节

六视图拼图已实际查看：背面窗组不同、上下平台、楼梯、吊臂与底部交叉撑均有几何；仍不能由小图确认每个窗口接缝。网页使用35°透视，离线为正交，因此两者并非像素等价验收。

## 适用条件

- 本地预览与当前资产版本绑定
- 用户能清楚区分静态与实时
- 视点覆盖资产弱面

## 相邻方案与区别

与3dcitydb状态链接互补，这里增加视角覆盖与错误状态；与美术hero镜头不同，它主动看背面/底面找缺陷。

## 失败模式

- README宣称浏览器测试通过属于作者报告，本轮未复现
- 离线与网页光照/投影不同不能逐像素比较
- 合批后线框很多不代表结构正确
- 源仓许可未知不能搬poster

## Movie 裁决

- **verdict**：adapt
- **reason**：作为镜头覆盖和资产检查清单，先确定各角度都有足够设计。

## Frontend 裁决

- **verdict**：adapt
- **reason**：采用有含义的静态fallback与独立线框/复位；不用本仓完整viewer替换本站。

## 最小对照

模拟GLB缺失和renderer初始化失败，预览仍可读且不谎报交互ready；切线框后reset不重置显示模式；各方向检查底部封口、背面遗漏与悬浮件。

## 源码证据

- [Repos/offshore-tower/Offshore_Tower_Generator.py:1450–1492](https://github.com/thebuggeddev/offshore-tower/blob/3a67f5ea7aec7955aaa7a576e8d772832add4afe/Offshore_Tower_Generator.py#L1450-L1492)：正交六视图离线渲染，底视隐藏地面
- [Repos/offshore-tower/app/src/scene.js:12–60](https://github.com/thebuggeddev/offshore-tower/blob/3a67f5ea7aec7955aaa7a576e8d772832add4afe/app/src/scene.js#L12-L60)：本地poster、进度、失败保留静图、ready状态
- [Repos/offshore-tower/app/src/scene.js:147–205](https://github.com/thebuggeddev/offshore-tower/blob/3a67f5ea7aec7955aaa7a576e8d772832add4afe/app/src/scene.js#L147-L205)：线框状态和相机复位分离，七个inspection视点
- [Repos/offshore-tower/app/src/scene.js:253–293](https://github.com/thebuggeddev/offshore-tower/blob/3a67f5ea7aec7955aaa7a576e8d772832add4afe/app/src/scene.js#L253-L293)：canvas说明、受限Orbit、状态变化请求渲染

## 项目效果图

![offshore-tower · observed_still](../assets/previews/offshore-tower-a3430d9d43f1.png)

已view_image Tower_Verification_Views.png六视图拼图：橙色收分塔、深骨架、多层维护平台、后侧窗组、底部交叉支撑、顶部天线与吊臂。历史离线渲染，不是当前网页截图或实时性能证据。

来源：[原作者/出处](https://github.com/thebuggeddev/offshore-tower/blob/3a67f5ea7aec7955aaa7a576e8d772832add4afe/Tower_Verification_Views.png) · observed_still。静帧观察；没有由此验证连续动画或性能。

## 归纳与练习

暂未归入新增专业视角；保留原机制边界。

[MP-21](../patterns/MP-21.md)
