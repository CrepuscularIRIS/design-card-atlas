# meshoptimizer
读JS简化器接口与C头语义；已有lodWorker明确使用LockBorder+ErrorAbsolute。新增价值是属性误差/顶点保护的后置检查，不是再建LOD。

## 案例档案

[来源仓库](https://github.com/zeux/meshoptimizer)
分析版本：`f0a684f11ead064e176775c9b796f82a55910e92`

模型归属未独立认证。

## 初始源码审计边界

未穷读C++求解器/编解码器/gltfpack，未跑简化。

以下保留初始源码审计的观察范围。后续新增静帧独立列于视觉材料，不追溯证明全部机制或运行状态。

## 机制与案例分析

### [SYS-007 · 把表面属性和接缝纳入减面保真目标](../cards/SYS-007.md)

simplifyWithAttributes 将属性向量、非负权重与顶点锁传入求解器；有助于表达外观保护目标，效果尚未测。

最需注意细金属杆的高光、字牌与模块边界；Prune可能删掉有叙事含义的小挂件。

**Movie：defer** · 镜头近景保留源模型优先
**前端：reference** · 已有LOD后续出现外观损伤才进入属性实验

失败条件：- 只看位置误差漏掉高光变形
- Prune删掉小配件
- 错误焊接打平法线或UV缝

## 项目效果与观察材料

尚无已观察的项目效果图；不以Logo、概念图或生成图代替。库/后端可能没有独立画面，详见来源审计。

## 复用边界

- **status**：observed
- **evidence**：LICENSE.md:1-21 MIT；输入模型权利另查。
- **reuse**：direct_with_notice

图片及第三方素材的权利单独保留；源代码许可证不自动授权媒体。
