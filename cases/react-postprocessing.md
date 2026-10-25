# react-postprocessing
实读SelectiveBloom、DOF和Autofocus，当前源码使用React19 use与R3F>=9.7，不可直接粘进本站React18/R3F8。项目已有后期，应迁机制而非替换库。

## 案例档案

[来源仓库](https://github.com/pmndrs/react-postprocessing)
分析版本：`3da552af77f5f6e150c1a0ba262c55fd570b6914`

模型归属未独立认证。

## 初始源码审计边界

未看本地bubbles静帧（不能据此声称视觉通过）；未穷尽几十effects/EffectComposer生命周期和测试；未跑。

以下保留初始源码审计的观察范围。后续新增静帧独立列于视觉材料，不追溯证明全部机制或运行状态。

## 机制与案例分析

### [REN-016 · 把发光资格绑定到对象身份](../cards/REN-016.md)

用局部霓虹或可交互道具作为强调源，避免每个白物件都发光；不能以发光替代照明。

用局部霓虹或可交互道具作为强调源，避免每个白物件都发光；不能以发光替代照明。

**Movie：adapt** · 指定镜头可稳定突出道具
**前端：reference** · 优先现有post.js强度/阈值，必要时才做mask

失败条件：- 遗漏灯或层号冲突导致对象消失/不亮
- effect重建频繁造成跳变
- 新源码React19不兼容本站18

### [REN-017 · 让焦点跟随语义目标并平滑过渡](../cards/REN-017.md)

对道具特写先清晰停留再转场；自由步行的识路/阅读应保清晰，不使用鼠标追焦扰动。

对道具特写先清晰停留再转场；自由步行的识路/阅读应保清晰，不使用鼠标追焦扰动。

**Movie：adapt** · 适合特写到全景的拉焦
**前端：reference** · 限于可取消的inspect镜头

失败条件：- 遮挡前景夺焦
- 深度异步过期结果回写
- 薄几何穿过模糊轮廓
- 全场步行持续浅景深降低可读性

## 项目效果与观察材料

![react-postprocessing · author_demo_screenshot](../assets/previews/lib-react-postprocessing-bubbles.jpg)

暗灰单色空间中的多个反射球体，中央大球边缘清晰，前后小球虚化，表面反射窗格。

来源：本轮已观察的历史截图 · author_demo_screenshot。仓内Bubbles演示封面，与README所列演示同名；只证明历史封面外观，不能据此确认某后期组件/配置生效。

## 复用边界

- **status**：observed
- **evidence**：LICENSE:1-21 MIT，保留版权许可。
- **reuse**：direct_with_notice

图片及第三方素材的权利单独保留；源代码许可证不自动授权媒体。
