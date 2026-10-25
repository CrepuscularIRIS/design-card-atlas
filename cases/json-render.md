# json-render
该仓同时有React与Remotion渲染器，直接对应前端卡与movie卡的不同契约。已发现motion单位注释/实现差异、types音轨不代表Renderer处理、坏clip静默空白风险。

## 案例档案

[来源仓库](https://github.com/vercel-labs/json-render)
分析版本：`72568f990e5502c4d3115691facb8ca928a5c9fc`

模型归属未独立认证。

## 初始源码审计边界

实读React registry/错误边界/串行动作，Remotion Renderer/ClipWrapper/hooks/types/schema；未深读所有standard组件、其他渲染器、AI provider或导出服务；未运行。

以下保留初始源码审计的观察范围。后续新增静帧独立列于视觉材料，不追溯证明全部机制或运行状态。

## 机制与案例分析

### [CN-026 · 把主画面与叠加说明分轨并按帧明确镜头寿命](../cards/CN-026.md)

把主画面与叠加说明分轨并按帧明确镜头寿命。这是由该仓实现提炼的候选操作，跨项目效果待验证。

可把场景shot、对比标签和字幕分层，不让解释文字跟随3D镜头抖动；这是视频卡的有用组织单位。

**Movie：prototype** · 适合离线设计卡A/B短片模板原型，不是直接重做场景
**前端：reference** · 前端取组件表和状态模型，不照搬定长片段

失败条件：- Renderer片段未处理audio/tracks.enabled，不能以types存在当完整音轨支持
- 未知组件和出错clip静默null会使影片缺段

### [CN-027 · 把进出场转场与片段内部动作分别计算再组合](../cards/CN-027.md)

把进出场转场与片段内部动作分别计算再组合。这是由该仓实现提炼的候选操作，跨项目效果待验证。

让镜头内部轻运动与切换过渡可独立调节；发现types称x/y像素但Wrapper用百分比，必须先统一单位。

**Movie：adapt** · 适合movie卡原型，先修单位约定
**前端：reference** · 可借运动层组合，不强制用Remotion播放页面

失败条件：- 位移单位不一致导致偏离预期
- 双重淡入使画面过暗、双scale导致过冲

### [CN-028 · 让生成界面只组合已注册组件并局部隔离坏片段](../cards/CN-028.md)

让生成界面只组合已注册组件并局部隔离坏片段。这是由该仓实现提炼的候选操作，跨项目效果待验证。

以受控设计积木限制模型输出，保留一致排版/按钮语义；局部错误隔离不能替代显式缺块标记。

**Movie：adapt** · 与CN-026共用clip registry，错误片段不能进成片
**前端：adapt** · 适合设计卡检索器的受控卡型

失败条件：- null隐藏错误导致看似完成但信息缺失
- 默认AI prompt并非强执行权限边界

## 项目效果与观察材料

![json-render · live_site_still](../assets/previews/live-json-render.png)

页面预设示例渲染出营收数字、折线图与两条进度；文字层级和图表占比集中于一张窄卡。

来源：[原作者/出处](https://json-render.dev/) · live_site_still。公开站默认UI演示，未发送生成请求；不证明Remotion影片、流式协议或导出实现。

## 复用边界

- **status**：observed
- **evidence**：LICENSE: Apache-2.0；保留许可、改动声明和适用NOTICE，Remotion依赖许可另查
- **reuse**：conditional

图片及第三方素材的权利单独保留；源代码许可证不自动授权媒体。
