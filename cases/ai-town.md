# ai-town
实读Player/Character渲染和服务器历史时间缓冲；真正可迁移的是把等待状态变成可读反馈，以及缓冲后插值。不是新增多智能体后端的理由。

## 案例档案

[来源仓库](https://github.com/a16z-infra/ai-town)
分析版本：`8e05997f2409275669c8344b84a51692e83f3f33`

模型归属未独立认证。

## 初始源码审计边界

未读全部Convex事务、LLM提示、地图编辑器；远程README截图未查看。

以下保留初始源码审计的观察范围。后续新增静帧独立列于视觉材料，不追溯证明全部机制或运行状态。

## 机制与案例分析

### [SYS-010 · 让等待、发言和活动各有明确视觉状态](../cards/SYS-010.md)

源码把后端等待暴露为可理解的角色状态，避免静止画面被误认为卡死。

原作像素人物仅作案例；本站用2D会面立绘/手机状态，不复制3D人物或满屏气泡。

**Movie：reference** · 编排镜头可以用状态暗示场景活动，但避免UI压画面
**前端：adapt** · 适合现有手机/会面等待体验

失败条件：- 请求已失败气泡仍转
- 思考与发言同时出现
- 所有角色头顶常驻噪声

### [SYS-011 · 用已发生的状态缓冲保持运动连续](../cards/SYS-011.md)

HistoricalTimeManager只在已收到区间内选择时间，可减轻分批状态导致的瞬移；未实测流畅性。

关注动作连续与转向不抽搐；此处会带延迟，不能用于直接操纵的游走相机。

**Movie：reference** · 适合回放，不必为预录镜头引入网络状态
**前端：defer** · 本站主要本地游走，无需新增远端群体同步

失败条件：- 时间倒退
- 慢缓冲让提示与画面错位
- 将1.5s延迟用于玩家输入

## 项目效果与观察材料

![ai-town · author_demo_screenshot](../assets/previews/lib-ai-town-author-screenshot.png)

左侧像素草地、交叉土路、菜地与多个人物，右侧羊皮纸色聊天栏显示Lucky/Kurt对话和时间戳。

来源：[原作者/出处](https://github.com/a16z-infra/ai-town/assets/3489963/a4c91f17-23ed-47ec-8c4e-9f9a8505057d) · author_demo_screenshot。README明确历史应用截图；含品牌页眉但主要区域是实际场景与聊天界面，不证明现有后端对话质量或实时运行。

## 复用边界

- **status**：observed
- **evidence**：LICENSE:1-21 MIT；README:49-56列多个第三方tilesheet/UI作者，资产不能笼统按MIT搬。
- **reuse**：conditional

图片及第三方素材的权利单独保留；源代码许可证不自动授权媒体。
