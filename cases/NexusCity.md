# NexusCity
已实读体量生成、程序纹理、镜头状态机；旧vendor曾存在但已退役，README确定性宣传不覆盖Math.random纹理。

## 案例档案

[来源仓库](https://github.com/vineetsharma96/NexusCity)
分析版本：`bc33737396179be841338eb09675239b5d1f82f0`

模型归属未独立认证。

## 初始源码审计边界

未深读NPC、交通、流式chunk、雨云与全局光照；未运行。

以下保留初始源码审计的观察范围。后续新增静帧独立列于视觉材料，不追溯证明全部机制或运行状态。

## 机制与案例分析

### [SD-NX01 · 让体量变化、附属设备和灯带共享建筑语法](../cards/SD-NX01.md)

先建立可辨认轮廓，再让灯带解释结构，避免给相同盒子随机贴霓虹。

色板 #00f0ff/#00ffaa/#ffaa00/#ff0077，每栋选一 accent；退台灯位于檐口，悬挑灯位于肚底。

**Movie：prototype** · 适合作为窗外中景轮廓样机。
**前端：adapt** · 仅移植几何数据生成器，不引入整个开放世界。

失败条件：- 悬挑collisionBounds覆盖整块宽底空间，不能直接当可走碰撞
- 并非所有随机纹理都可复现

### [SD-NX02 · 把镜头展示与交还控制拆成可跳过状态](../cards/SD-NX02.md)

展示段负责建立空间，独立交还段避免结束瞬间跳相机。

位置和lookAt独立插值；原作先高空后地面，Citadel现定特写再拉远，应重排关键帧。

**Movie：adapt** · 可用状态结构，镜头顺序须重设计。
**前端：prototype** · 跳过、打断、交还比强制长intro更有价值。

失败条件：- 线性空间插值无避障，smoothstep不保证不穿模
- 原作轨道缺减弱动态分支

### [SD-NX03 · 在窗格明暗中分配暖办公室与冷霓虹](../cards/SD-NX03.md)

窗格不是全亮噪声，暗窗提供视觉休息，少量暖窗给城市生活尺度。

背景#0a0f1d、暗窗#121a2d；此文件画色纹理，并不证明窗会向室内投光。

**Movie：reference** · 适合中远景，不足以表现近景房间。
**前端：reference** · Citadel已vendor catwalk/windows.js，先利用现有窗内景。

失败条件：- Math.random导致重载不复现
- 仅litRatio缓存导致同类建筑纹理完全相同
- 复制色图为emissive不等于真实照明

## 项目效果与观察材料

![NexusCity · archived_local_screenshot](../assets/previews/scene-nexuscity-1.webp)

实际查看：夜街斑马线、中央NPC与交互提示，青色HUD/雷达、暗楼体和橙色树冠；画面整体很暗。

来源：本轮已观察的历史截图 · archived_local_screenshot。2026-09-27本地审阅项目快照中的Nexus City界面；未绑定当前Repos/NexusCity提交。静帧不证明当前运行、动画或模型质量。

## 复用边界

- **status**：observed
- **evidence**：LICENSE:1-21 为 MIT，保留版权与许可；本轮只对代码作此判读
- **reuse**：direct_with_notice

图片及第三方素材的权利单独保留；源代码许可证不自动授权媒体。
