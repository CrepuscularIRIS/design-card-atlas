# 镜面邻粗面

分组：材质 · 主维度：E 粗糙度对照、A 高光形状、C 接触边界、B 反射色、D 形体保存 · 情绪：清晰、触感

## 一句话

让会映出形状的面紧挨着哑光实体，观众靠高光形状读懂材质差异。

[![Falcon 9 · 海面降落](shots/05.jpg)](shots/05.jpg)
[Falcon 9 · 海面降落](https://github.com/noahsabaj/falcon9-blender/releases/tag/v1.0) · 海面续出船体、箱体的暗轮廓与左侧绿灯，船舷大面保留实体暗部。

| 参考 | 参考 |
|---|---|
| [![雷尼斯黑沙滩 · 海滩](shots/01.jpg)](shots/01.jpg) | [![Unreal 云上神殿与巨龙](shots/02.jpg)](shots/02.jpg) |
| [雷尼斯黑沙滩 · 海滩](https://github.com/Zp-Peter/kimi-k31pro-opus55-benchmark-showcase/blob/65e82c53b63f2fdd918617269c057d8e53af2c6f/opus/reynisfjara/index.html) · 干黑沙吸光，邻近湿沙出现宽银带，边界说明同一地面状态变化。 | [Unreal 云上神殿与巨龙](https://skillry.dev/ai-videos/kimi-k3-1/kimi-moonshot-068067-1) · 地面续出朱柱与人物反光，柱体本身仍以实体暗面为主。 |
## 看哪里

1. Falcon 9 · 海面降落：海面续出船体、箱体的暗轮廓与左侧绿灯，船舷大面保留实体暗部。
2. 雷尼斯黑沙滩 · 海滩：干黑沙吸光，邻近湿沙出现宽银带，边界说明同一地面状态变化。
3. Unreal 云上神殿与巨龙：地面续出朱柱与人物反光，柱体本身仍以实体暗面为主。

## 拆解

对roughness只作视觉判断；以下试验值不是原作参数。

- **E · 并置**：黑沙是同一视野里的干区与湿区；龙殿是柱体与地板；海上降落是船体与映出它的平静水面。必须把不同表面放在同一光环境下比较才有说服力。
- **A · 高光形状**：湿沙是宽而柔的银带，龙殿地板是拉长碎形，船下水面保留近似完整的暗反射。不是所有材质都用一样大的白点。
- **C · 边界**：海岸湿带从右下向远端收束，位置跟潮线一致；地板反射起于柱脚与人脚附近，不能与接触点错开。
- **B · 颜色**：地板主要借来朱金建筑颜色，湿沙借来冷灰天空，降落船左侧绿灯在水里有可指认的对应亮点。反光色应能找到来源。
- **D · 体积**：龙殿暗柱仍完整，船舷和上方细杆仍能认出。表面效果的职责是补充体积，不是替代可读形状。

## 做法

先确认反射来源和接触位置，再分配粗糙度。不要为了“高级材质”把地面、墙和道具都设成镜面。

- **迁移试验**：哑石roughness可从0.7–0.9试，局部湿面从0.15–0.35试；渲染器、法线和光源尺寸都会改变结果，最终以高光宽度验收。
- 试验先保留约10–25%画面有明显反射，其余实体允许安静；光学精确性与性能需要另测。

### 实现索引

以下是源码阅读索引，不把邻接技术源说成原作实现，也不把现有基础组件说成整卡已落地。`Repos/` 相对 `~/Blog/`；`citadel` 列相对 `~/Blog/citadel/`。参数逐项标明来源，未做本轮运行测量。

| 作品 | 源码（本地路径:行） | 技术与接入边界 | 参数（来源） | 许可 / 复用档 | Citadel 已有可复用入口 |
|---|---|---|---|---|---|
| Falcon 9 · 海面降落 | `Repos/falcon9-blender/film/envs.py:231-254` | Blender 海面以低粗糙度 Principled BSDF、IOR 和程序噪声 bump 保留船影；邻接船体材料 film/droneship.py:363-393 由钢、漆、锈、湿区混合 roughness。是离线节点配方，非 WebGL 可直接导入模块；Citadel 可复用镜像相机/水面反射与 dress/surfaces.js:5-46 的材料差异化，湿地板接收器仍待验证。 | ocean roughness / IOR=0.06 / 1.33（源码）；wave_scale / wave_bump=0.004 / 0.25（源码）；steel base roughness range=0.64–0.8（后续仍叠加斑驳和掩模）（源码） | 脚本 MIT（LICENSE:1-25）；生成 .blend、模型、渲染和音视频另属 CC BY-NC 4.0（LICENSE-ASSETS.md:1-18），不可当作 MIT 资产 / borrow | `src/world/worlds/planarWaterReflection.js` |
| 雷尼斯黑沙滩 · 海滩 | `Repos/kimi-k31pro-opus55-benchmark-showcase/opus/reynisfjara/src/world/beach.js:88-162` | 干沙/砾石的粗糙度与颜色随 dampness 改变，并用岸线深度掩模划出水膜；平面倒影另见 src/fx/reflection.js:1-109 的镜像相机、斜近裁面和反射 RT。Citadel planarWaterReflection.js:6-69 已有水平水面镜像路线，地面着色与湿区遮罩仍需适配；dress/surfaces.js:5-46 可做粗糙区。 | dry sand roughness=0.94（源码）；damp roughness target=0.4（源码）；reflection scale default=0.5（源码） | 未发现作品仓根 LICENSE，授权范围待验证；仅借手法，不复制代码/资产 / borrow | `src/world/worlds/planarWaterReflection.js` |
| Unreal 云上神殿与巨龙 | `none` | 原作反射算法待验证，不能凭画面断言 SSR 或光追；邻接技术源 Repos/kimi-k31pro-opus55-benchmark-showcase/opus/reynisfjara/src/fx/reflection.js:1-109 是可读的水平平面反射路线，仅借手法；Citadel 已有水面相机/RT，石地板材质与人物缺失反射需单独验收。 | 哑石 roughness=0.7–0.9（建议迁移值）；局部湿面 roughness=0.15–0.35（建议迁移值） | 原作源码及许可待验证；邻接黑沙滩未发现根 LICENSE，只借手法 / reference | `src/world/worlds/planarWaterReflection.js` |

本批面向 CompanyMeetingroom 局部地面与粗面并置提案。现成反射器仅支持水平水面及其 uniforms，不能直接挂到任意 PBR 石材；需适配接收器、湿区遮罩、反射成本和销毁生命周期。不会让屏幕空间 2D 人物进入 3D 倒影。

源码快照（2026-10-28 阅读；不是新增截图来源）：
- `falcon9-blender@c6a6349c0968870a7a864f8ba44d2182cafad60e`
- `kimi-k31pro-opus55-benchmark-showcase@65e82c53b63f2fdd918617269c057d8e53af2c6f`

已检索 `citadel/src` 及 `src/world/worlds/cardfx/`；本批未发现这些卡的同名预制模块。未来首次落地时才由执行者沉淀 `src/world/worlds/cardfx/mirror-beside-roughness.js`，此处不是已有文件承诺。

## 迁移到博客

BlackCityHall用一条湿地或局部磨亮石面与粗墙对照；Shrine雨后台阶只让踏面凹处积水，踢面保持哑。不是所有现有场景都要加镜面。

搭配水面续轮廓、侧光刻石；与全场亮纹、金缝描边冲突。若会面人物不参与3D反射，避免把明显镜面铺到其脚前让缺失变突出。

## 反例

玻璃杯图只展示透明棱面与投地焦散，不作为本卡镜面反射的正例。区分折射、焦散与映形，比把它们统称“亮材质”更有利于迁移。

[![玻璃概念边界对照](shots/03.jpg)](shots/03.jpg)


Cosmos画面的水几乎到处闪，亮形过多时观众只感到“很亮”，不易分清反射、发光和水底信息。这里需要的是邻接差异，而不是统一抛光。


[![Shader & Cosmos · 吸积盘](shots/04.png)](shots/04.png)
[Shader & Cosmos · 吸积盘](https://github.com/holooooo/webgl-seascape-video) · 满水面尖亮点与天空金环同样强，材质差异被统一的闪亮节奏盖过。

[逐图来源与复现](SOURCE.md) · [返回视觉卡库](../../../README.md)
