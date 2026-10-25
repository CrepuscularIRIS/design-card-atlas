# instanced-mesh
实读每实例uniform与LOD选择；实例批处理可容纳局部差异，不必把重复元素做成完全相同。已看 public/banner.png 历史森林静帧，只见远近植被层次，不能据此证明LOD无跳变或性能。

## 案例档案

[来源仓库](https://github.com/agargaro/instanced-mesh)
分析版本：`56786de4651bf5d45d218d720bb09e95d765db93`

模型归属未独立认证。

## 初始源码审计边界

未读全部剔除/BVH/蒙皮与示例；banner未绑定具体场景源码，不能作uniform效果证据。

以下保留初始源码审计的观察范围。后续新增静帧独立列于视觉材料，不追溯证明全部机制或运行状态。

## 机制与案例分析

### [SYS-005 · 让重复构件共享结构但保留局部身份](../cards/SYS-005.md)

库的 per-instance uniform 数据纹理能将一组公共材质与局部参数分离；如何配色仍是项目设计决策。

例如仅少量窗亮、少量店招偏暖，与全体同时闪烁不同；固定seed和营业分区是迁移建议，库本身不生成这些规则。

**Movie：adapt** · 可给远景群体小幅相位差，拍摄前锁seed
**前端：reference** · 已有catwalk窗图集应优先延展，不默认新增库

失败条件：- 重排ID导致灯光花纹跳变
- 每窗独立颜色形成噪点
- 烘焙GLB未保存自定义uniform

### [SYS-006 · 让细节等级依据可见尺寸分配](../cards/SYS-006.md)

源码支持distance或screen-size metric及shadow专用列表；这允许把近景轮廓放在优先位置，但不保证切换平滑。

注意：本函数未基于上一等级保存真正双阈值状态，不能仅凭参数名宣称消除闪烁。

**Movie：defer** · 固定镜头可预选细节无需动态跳变
**前端：defer** · 性能优化后置，先复用现有LOD

失败条件：- 距离阈值附近来回跳
- 阴影形状和主体不一致
- 无状态hysteresis被误当平滑过渡

## 项目效果与观察材料

![instanced-mesh · author_showcase_banner](../assets/previews/historical-instanced-mesh.png)

作者横幅中可见层叠针叶林、草和远雾，叠有包名品牌。采用其可见场景作为展示，品牌文字不是机制证据。

来源：[原作者/出处](https://github.com/agargaro/instanced-mesh/blob/56786de4651b/public/banner.png) · author_showcase_banner。品牌覆盖较多，仅保留作者场景预览；不证明百万实例数量、裁剪、LOD或性能。

## 复用边界

- **status**：observed
- **evidence**：LICENSE:1-21 MIT，保留版权许可；示例资产单独核对。
- **reuse**：direct_with_notice

图片及第三方素材的权利单独保留；源代码许可证不自动授权媒体。
