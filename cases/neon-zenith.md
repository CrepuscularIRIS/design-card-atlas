# neon-zenith
高价值街景案例：共享光场、遮雨、近远立面连续、建筑语法与品牌招牌五条机制；不是要求迁WebGPU。

## 案例档案

[来源仓库](https://github.com/billpwchan/neon-zenith)
分析版本：`27ad04ef04aa9e1e1366fccc63e15a379b999f01`

模型归属未独立认证。

## 初始源码审计边界

未深读全楼面shader、Blender烘焙脚本、光图完整消费者、clouds、vehicle及游戏任务；无运行验证。

以下保留初始源码审计的观察范围。后续新增静帧独立列于视觉材料，不追溯证明全部机制或运行状态。

## 机制与案例分析

### [SD-NZ01 · 让招牌、地面、雨雾共享同一发光分布](../cards/SD-NZ01.md)

把环境的颜色出处固定到场景光源位置，减少只在屏幕上添加独立彩雾的脱节。

钠灯#ffae55、LED#cfe2ff，商店含暖白/冷白；market.jpg历史静帧中招牌与湿地彩色竖向反光一致，但未证实每种动态采样。

**Movie：prototype** · 固定夜街镜头可直接比较光色因果一致性。
**前端：adapt** · 移植世界坐标光图及采样逻辑，不能整包TSL搬进r170。

失败条件：- 2D光图没有遮挡与垂向结构
- bake加光图可能重复照明
- TSL版本不可直接兼容

### [SD-NZ02 · 让雨条相对相机运动并在屋檐处停止](../cards/SD-NZ02.md)

雨的可信度来自运动相对关系和遮蔽，不是单纯提高数量。

远近两层盒26/110m；雨到街面变彩，进雨棚消失；源参数很重，不建议按原数量照搬。

**Movie：prototype** · 可验证进屋檐、加速镜头中雨的变化。
**前端：adapt** · 从已有place雨系统补遮蔽/相对运动即可。

失败条件：- 单层heightmap不表达桥下多层空间
- TSL移植成本
- 过量additive雨变亮噪声

### [SD-NZ03 · 让近景立面模块与远景照片保持同一窗格身份](../cards/SD-NZ03.md)

距离变化时应减少细节，而不是把同一栋楼换成另一套窗户。

近处空调/窗帘/房间的身份对应远处captured facade；这比只增加面数更能避免跳变。

**Movie：adapt** · 镜头拉远时可维持连续性。
**前端：defer** · 先单建筑制作匹配远景图，再评估范围化系统。

失败条件：- CC BY模型需保留作者与变更说明
- 切片格网与照片不一致产生跳变
- 性能系统不能替代建模质量

### [SD-NZ04 · 用建筑独立随机流维护体量与细节迭代的稳定性](../cards/SD-NZ04.md)

修改屋顶细节不应让商铺和灯牌换位置，否则无法做可归因A/B。

灯只强调冠顶和结构转折，外壳、百叶、设备层分材质身份。

**Movie：adapt** · 可借结构而非量级
**前端：prototype** · 可先以一个窗外塔测试，几何逻辑不依赖TSL材质。

失败条件：- 把独立流接回共享rng会重新耦合
- 过多家族缺统一尺度

### [SD-NZ05 · 以行业身份组织招牌配色和横竖版式](../cards/SD-NZ05.md)

让街道广告成为世界叙事，而不是无内容的彩色矩形。

招牌主体大字、次级英文、最小服务说明三层；可用黑红/深蓝金/白绿，不复制大面积紫渐变。

**Movie：prototype** · 中近景有语义招牌可提供尺度和生活感。
**前端：adapt** · 供手机品牌卡或场景标牌，但文字需可读而非只装饰。

失败条件：- 原源码部分广告紫渐变不符合本站约束
- 未检查完整atlas装配和动态wipe实现
- 压字过度损害可读性

## 项目效果与观察材料

![neon-zenith · observed_still](../assets/previews/neon-zenith-a855ac555caa.jpg)

已view_image docs/media/market.jpg：黑色楼峡、横竖霓虹、暖路灯与湿地纵向反光；历史静帧不证明动态。

来源：[原作者/出处](https://github.com/billpwchan/neon-zenith/blob/27ad04ef04aa9e1e1366fccc63e15a379b999f01/docs/media/market.jpg) · observed_still。静帧观察；没有由此验证连续动画或性能。

## 复用边界

- **status**：observed
- **evidence**：LICENSE代码MIT；CREDITS.md列模型CC BY4.0、PolyHaven/ambientCG CC0、字体OFL，必须按资产保留来源
- **reuse**：conditional

图片及第三方素材的权利单独保留；源代码许可证不自动授权媒体。
