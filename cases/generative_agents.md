# generative_agents
实读perceive与retrieve；该仓是空间事件/记忆仿真，非3D材质来源。检查cover历史拼图，确认场所与局部对话的展示，不推断当前动态质量。

## 案例档案

[来源仓库](https://github.com/joonspk-research/generative_agents)
分析版本：`fe05a71d3e4ed7d10bf68aa4eda6dd995ec070f4`

模型归属未独立认证。

## 初始源码审计边界

未深读plan/reflect/execute、Django回放、素材来源；未运行模型。

以下保留初始源码审计的观察范围。后续新增静帧独立列于视觉材料，不追溯证明全部机制或运行状态。

## 机制与案例分析

### [SYS-012 · 把事件知识限制在角色所在空间与注意范围](../cards/SYS-012.md)

perceive不是全城广播；arena边界、距离顺序与att_bandwidth限制角色知道什么，有利于会面台词与空间一致。

历史cover.png可见分房间活动、地点放大与短对话；图片只支持该展示组织方式，不证明运行时行为。

**Movie：reference** · 可借局部知情编排旁白与环境线索
**前端：reference** · dayPlan/memoryRecall已有思路移植，优先核对一致性

失败条件：- 同屋不同隔墙仍被arena误作可见
- 重复事件挤占注意带宽
- 台词宣称未发生的访客行为

## 项目效果与观察材料

![generative_agents · author_scene_screenshot_montage](../assets/previews/lib-generative_agents-cover.png)

像素小镇总图，五个放大框展示咖啡馆、公园、学校、办公室和晨间活动，角色有局部气泡。

来源：本轮已观察的历史截图 · author_scene_screenshot_montage。作者以实际场景截图做的说明拼图，保留框线和说明；不是系统架构图，但也不是单帧完整运行画面，不验证自主行为或对话真实性。

## 复用边界

- **status**：observed
- **evidence**：LICENSE:1-20 Apache-2.0，复用需保留许可和适用NOTICE；图像/第三方资产另查。
- **reuse**：conditional

图片及第三方素材的权利单独保留；源代码许可证不自动授权媒体。
