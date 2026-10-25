# SD-NX03 · 在窗格明暗中分配暖办公室与冷霓虹
案例：[ NexusCity ](../cases/NexusCity.md) · 机制证据：`source_only`

效果图用于理解来源作品，不自动验证本卡中的每个机制。

## 设计动作

窗格不是全亮噪声，暗窗提供视觉休息，少量暖窗给城市生活尺度。

## 实现与参数

256×512 Canvas→8列16行，pad6/8；60%默认亮窗，亮窗中40%暖#ffeed0、30%冷#78c6ff、30%青#00f0ff；按litRatio缓存。

## 审美细节

背景#0a0f1d、暗窗#121a2d；此文件画色纹理，并不证明窗会向室内投光。

## 适用条件

- 中远景窗矩阵
- 与日夜共享曝光管理

## 相邻方案与区别

catwalk窗内景增加深度，本卡仅提供廉价色块分布；选前者做近景。

## 失败模式

- Math.random导致重载不复现
- 仅litRatio缓存导致同类建筑纹理完全相同
- 复制色图为emissive不等于真实照明

## Movie 裁决

- **verdict**：reference
- **reason**：适合中远景，不足以表现近景房间。

## Frontend 裁决

- **verdict**：reference
- **reason**：Citadel已vendor catwalk/windows.js，先利用现有窗内景。

## 最小对照

同栋楼重载两次hash一致，再比较暗窗比例；颜色更热但玻璃失去分区判失败。

## 源码证据

- [Repos/NexusCity/src/core/ProceduralTextures.ts:74–122](https://github.com/vineetsharma96/NexusCity/blob/bc33737396179be841338eb09675239b5d1f82f0/src/core/ProceduralTextures.ts#L74-L122)：8×16窗格、默认litRatio=.6、三种亮窗色

## 项目效果图

![NexusCity · archived_local_screenshot](../assets/previews/scene-nexuscity-1.webp)

实际查看：夜街斑马线、中央NPC与交互提示，青色HUD/雷达、暗楼体和橙色树冠；画面整体很暗。

来源：本轮已观察的历史截图 · archived_local_screenshot。2026-09-27本地审阅项目快照中的Nexus City界面；未绑定当前Repos/NexusCity提交。静帧不证明当前运行、动画或模型质量。

## 归纳与练习

暂未归入新增专业视角；保留原机制边界。

保留独立案例。
