# detect-gpu
分类来自 renderer 匹配与已有 benchmark，不是当前场景帧率实测；已核对 Citadel 的本地表和 timing 回退。该仓不提供配色、几何或灯光设计。

## 案例档案

[来源仓库](https://github.com/pmndrs/detect-gpu)
分析版本：`628b7c0aefbcf24714cd550e6f3c2dc279b67adc`

模型归属未独立认证。

## 初始源码审计边界

未读所有 GPU 表与 Apple 去混淆路径，未做设备检测实测。

以下保留初始源码审计的观察范围。后续新增静帧独立列于视觉材料，不追溯证明全部机制或运行状态。

## 机制与案例分析

### [SYS-001 · 区分检测未知与低性能，避免误删视觉主次](../cards/SYS-001.md)

源码将 BENCHMARK_FETCH_FAILED 与 FALLBACK 单独返回，使应用有机会保留未知状态；保留主光属于本项目迁移推论。

无审美产物；用于避免低档误砍主光导致材质和空间关系失读。不能把库里的 fps 当本场景 fps。

**Movie：defer** · 离线镜头不应受访客硬件分档改变画面
**前端：reference** · 现有 quality 管线已有同类分流；适合补保真验收

失败条件：- 新 GPU 查不到表却被等同弱 GPU
- 关闭阴影导致光穿墙
- 低档丢掉导视光

## 项目效果与观察材料

尚无已观察的项目效果图；不以Logo、概念图或生成图代替。库/后端可能没有独立画面，详见来源审计。

## 复用边界

- **status**：observed
- **evidence**：LICENSE:1-21 MIT，保留版权许可；benchmark 数据来源和停更提示见 README:16。
- **reuse**：direct_with_notice

图片及第三方素材的权利单独保留；源代码许可证不自动授权媒体。
