# concordia
实读EventResolution和SceneTracker；只产环境叙事状态裁决案例。模型生成的event不是几何或真实操作证据，不能代替本站日志。

## 案例档案

[来源仓库](https://github.com/google-deepmind/concordia)
分析版本：`239f0e8275a55b186b99e133e06432cd681ff2e3`

模型归属未独立认证。

## 初始源码审计边界

未读全部engine/prefabs/场景示例，未调用模型。

以下保留初始源码审计的观察范围。后续新增静帧独立列于视觉材料，不追溯证明全部机制或运行状态。

## 机制与案例分析

### [SYS-013 · 先裁决行动结果再让场景响应](../cards/SYS-013.md)

EventResolution以不同tag区分意图和事件；SceneTracker还显式列参与者，避免所有角色同时知道所有事。

本仓没有调色/建模；间接用于灯光、门、会面台词只响应真正成立的事件。

**Movie：reference** · 故事板可分意图和结果，渲染效果仍需镜头验证
**前端：reference** · 已有gmCheck，不上新的GM后端

失败条件：- 将模型event当真实执行成功
- active player缺失时fallback取别人建议
- 观察者范围由模型猜测出错

## 项目效果与观察材料

尚无已观察的项目效果图；不以Logo、概念图或生成图代替。库/后端可能没有独立画面，详见来源审计。

## 复用边界

- **status**：observed
- **evidence**：LICENSE:1-20 Apache-2.0，复用需保留许可和适用NOTICE；图像/第三方资产另查。
- **reuse**：conditional

图片及第三方素材的权利单独保留；源代码许可证不自动授权媒体。
