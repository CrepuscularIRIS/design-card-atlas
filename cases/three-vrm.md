# three-vrm
查看了three-vrm.png历史宣传静帧：高对比黄色背景、右侧半身卡通角色、细轮廓。它不能证明当前运行或任一shader参数效果。源码实读表情混合与MToon片段。

## 案例档案

[来源仓库](https://github.com/pixiv/three-vrm)
分析版本：`68c7d6b1f73b79568f81139be62831968bff7876`

模型归属未独立认证。

## 初始源码审计边界

未读加载器、springbone、完整shader分支/全部资产；历史banner不是当前运行验证。

以下保留初始源码审计的观察范围。后续新增静帧独立列于视觉材料，不追溯证明全部机制或运行状态。

## 机制与案例分析

### [CN-016 · 在每帧先清除旧绑定再按冲突通道分配表情权重](../cards/CN-016.md)

在每帧先清除旧绑定再按冲突通道分配表情权重。这是由该仓实现提炼的候选操作，跨项目效果待验证。

和Amica的应用层互斥可归并为表情控制权主卡，但这里是底层权重清理，不是时间延迟。

**Movie：reference** · 适合动画技术理解；不改变hIE只用2D边界
**前端：defer** · 当前静态立绘不需VRM引擎

失败条件：- 旁路直接写blendshape会绕过仲裁
- 2D整张图没有连续权重接口

### [CN-017 · 分开控制明暗分界、轮廓光和描边的光照响应](../cards/CN-017.md)

分开控制明暗分界、轮廓光和描边的光照响应。这是由该仓实现提炼的候选操作，跨项目效果待验证。

硬边阴影、边缘可读性和受光一致性分别调整；并不等于把整场景换成卡通材质。

**Movie：reference** · 可指导风格化道具小样，不建议直接改人物
**前端：reference** · 只有某个道具需要toon表现时再评估

失败条件：- 强rim让暗侧违背场景光源
- 描边与现有后期outline双重加粗

## 项目效果与观察材料

![three-vrm · historical_still_viewed](../assets/previews/three-vrm-4baa6f58cda1.png)

历史宣传图实际查看：黄色背景、右侧半身卡通人物、细轮廓；不证明任何shader参数效果或当前运行。

来源：[原作者/出处](https://github.com/pixiv/three-vrm/blob/68c7d6b1f73b79568f81139be62831968bff7876/three-vrm.png) · historical_still_viewed。静帧观察；没有由此验证连续动画或性能。

## 复用边界

- **status**：observed
- **evidence**：LICENSE: MIT；角色模型/纹理资产不由代码许可自动覆盖
- **reuse**：conditional

图片及第三方素材的权利单独保留；源代码许可证不自动授权媒体。
