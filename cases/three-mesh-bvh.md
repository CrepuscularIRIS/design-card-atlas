# three-mesh-bvh
实读通用shapecast与characterMovement胶囊推离；Citadel collision.js已有直接改造且只做横向推离/floorY定高。

## 案例档案

[来源仓库](https://github.com/gkjohnson/three-mesh-bvh)
分析版本：`1d7a4249d4ac6d6500fe16eda482a2b8cf7be521`

模型归属未独立认证。

## 初始源码审计边界

未读GPU/WebGPU BVH、动画重建与所有示例；未跑碰撞。

以下保留初始源码审计的观察范围。后续新增静帧独立列于视觉材料，不追溯证明全部机制或运行状态。

## 机制与案例分析

### [SYS-009 · 让观众靠近细节时仍保有实体边界](../cards/SYS-009.md)

单纯视觉精细而可穿透会破坏空间可信度；源码可给接近桌边/栏杆时一致的边界反馈。

保住接近栏杆、桌角的尺度感；雾、glow、反射卡不能误作实体。

**Movie：reference** · 运镜可借碰撞查询，但不能把人物胶囊直接当相机视锥
**前端：adapt** · 已集成，继续校准新增细节的实体分类

失败条件：- glow卡造成空气墙
- 烘焙后碰撞仍用旧几何
- 高速步进越过薄面

## 项目效果与观察材料

![three-mesh-bvh · author_demo_screenshot](../assets/previews/lib-three-mesh-bvh-screenshot.png)

深灰底上的洋红纽结，白色细线从多个白点射向中心；属于几何查询示例的可见输出。

来源：本轮已观察的历史截图 · author_demo_screenshot。技术示例静帧，不是高质量场景美术或BVH加速性能证明；线段命中正确性未运行核验。

## 复用边界

- **status**：observed
- **evidence**：LICENSE:1-21 MIT，保留版权许可；示例资产单独核对。
- **reuse**：direct_with_notice

图片及第三方素材的权利单独保留；源代码许可证不自动授权媒体。
