# SD-TW04 · 把地面反弹光限制在朝向、距离和日照共同允许的区域
案例：[ tidewater ](../cases/tidewater.md) · 机制证据：`source_only`

效果图用于理解来源作品，不自动验证本卡中的每个机制。

## 设计动作

暗面需要来自环境的有色补光，但不应通过抬高全局环境光把接触与体积一起抹平。

## 实现与参数

groundBounceMap储地表反射依据与高度，接收侧view=sat(-Ny*.5+.5)，手动双线性采样；fade排除地表上方反向贡献并随高度变化，低太阳时背向面selfShade最多降.6，再乘sunColor/cloud/strength/SURROUND .6，最后/π。water与NO_GROUND_BOUNCE直接跳过。

## 审美细节

沙、岩、植被和海面颜色参与环境差异；底面接收更多，侧面也有补光。它是高度场近似，不是完整光线追踪或多次GI。截图不足隔离该项贡献。

## 适用条件

- 地表高度与反射颜色可查询
- 已有直接光与曝光稳定
- 能避免与烘焙GI双算

## 相邻方案与区别

与全局HemisphereLight不同保留位置颜色；与完整bake相比可响应部分状态但缺完整可见性。

## 失败模式

- 高度场忽略桥下多层表面和墙体遮挡
- 近似selfShade不是物体真实遮挡
- 动态地表/天光变化需刷新依据
- WebGPU代码不能直接塞进Three材质

## Movie 裁决

- **verdict**：adapt
- **reason**：可用于棚底、窗台和脚边暗面，但应先固定灯光做A/B。

## Frontend 裁决

- **verdict**：reference
- **reason**：本站优先已有bake/局部补光，确实缺少地面色传递才加此近似。

## 最小对照

地面白/暖/绿三色、太阳高低两态对比；只有合理接收面着色，接触阴影不消失；室内隔墙穿光、角色漂浮或暗部全染色即失败。

## 源码证据

- [Repos/tidewater/src/materials/GroundBounce.js:9–100](https://github.com/dgreenheck/tidewater/blob/4811ba48d795197de5621985f404e765c0b7c0ef/src/materials/GroundBounce.js#L9-L100)：512²地形颜色/高度反弹图，按日照和地形阴影烘入
- [Repos/tidewater/src/materials/GroundBounce.js:156–187](https://github.com/dgreenheck/tidewater/blob/4811ba48d795197de5621985f404e765c0b7c0ef/src/materials/GroundBounce.js#L156-L187)：按法线朝向、地表高度、太阳背向和云影衰减hookBounce

## 项目效果图

![tidewater · observed_still](../assets/previews/tidewater-85a2ca018d2a.jpg)

已view_image docs/screenshot.jpg：夕阳码头、近景木栏杆/绳索/灯具/钓竿、远近水色层次。仅为历史静帧，没有证明当前实时水体、声画同步或性能。

来源：[原作者/出处](https://github.com/dgreenheck/tidewater/blob/4811ba48d795197de5621985f404e765c0b7c0ef/docs/screenshot.jpg) · observed_still。静帧观察；没有由此验证连续动画或性能。

## 归纳与练习

暂未归入新增专业视角；保留原机制边界。

[MP-03](../patterns/MP-03.md)
