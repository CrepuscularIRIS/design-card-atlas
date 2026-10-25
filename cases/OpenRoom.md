# OpenRoom
参考仓README现已称VibeApps。源码SHA02468154与本地vendor记载一致；Action已存在，桌面window host没有直接采用。

## 案例档案

[来源仓库](https://github.com/MiniMax-AI/OpenRoom)
分析版本：`02468154c4d99f8925916425bf444d672454fb3d`

模型归属未独立认证。

## 初始源码审计边界

实读Action与windowManager及本地VENDOR、action对应片段；未遍历全部手机应用、IndexedDB与Agent调度。

以下保留初始源码审计的观察范围。后续新增静帧独立列于视觉材料，不追溯证明全部机制或运行状态。

## 机制与案例分析

### [CN-007 · 让应用动作返回明确结果供角色读取](../cards/CN-007.md)

动作处理器向角色侧发送实际结果回执，使后续反馈有可检查依据；所引代码没有证明角色台词会等待回执，台词时序属于迁移验收目标。

剧情角色操作手机应用时，需要结果反馈而非只说自己已经操作。

**Movie：reference** · 可用于演示片脚本素材，不能代表实时操作完成
**前端：reference** · citadel已vendor同源机制；优先核对现有反馈不重复集成

失败条件：- 默认done可能掩盖未操作
- UI接到动作并不等于保存成功
- 同步handler抛异常时仅记录日志，无error回执；需单独补齐

### [CN-008 · 恢复同一窗口身份并统一焦点层级](../cards/CN-008.md)

恢复同一窗口身份并统一焦点层级。这是由该仓实现提炼的候选操作，跨项目效果待验证。

多应用避免重复副本，主操作窗口有确定前后关系。

**Movie：defer** · 对3D电影化环境打磨无直接帮助
**前端：reference** · Citadel phone已替换上游Shell/ChatPanel/AppWindow，不迁回桌面壳

失败条件：- 只抬z-index不等于DOM焦点
- 300px最小宽在小手机不适配

## 项目效果与观察材料

![OpenRoom · live_site_still](../assets/previews/live-openroom-desktop.png)

太空背景、左侧应用图标、底栏和黄色聊天输入共同组成桌面壳。

来源：[原作者/出处](https://www.openroom.ai/) · live_site_still。角色窗口持续Loading，已最小化以观察桌面；没有发送消息或验证角色行动回执。

## 复用边界

- **status**：observed
- **evidence**：LICENSE: MIT；NOTICE存在，复用需保留
- **reuse**：direct_with_notice

图片及第三方素材的权利单独保留；源代码许可证不自动授权媒体。
