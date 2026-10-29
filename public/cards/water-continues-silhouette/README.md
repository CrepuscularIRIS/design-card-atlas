# 水面续轮廓

分组：水与大气 · 主维度：F 反射连续性、C 水平分界、D 形体重复、B 反射色、E 波面 · 情绪：安静、延展

## 一句话

让岸上形体在水里接着存在，倒影为建筑增加第二个向下延伸的空间。

[![江南山谷 · 清晨河岸](shots/01.png)](shots/01.png)
[江南山谷 · 清晨河岸](https://github.com/holooooo/webgl-seascape-video/blob/915cb7c9a318e03bd2228bc232494b496ff2316c/episodes/04-jiangnan-voxel/interactive.html) · 桥洞与倒影接近闭合，两侧墙体沿岸线向下延伸。

| 参考 | 参考 |
|---|---|
| [![清明上河 · 雨中虹桥](shots/02.jpg)](shots/02.jpg) | [![Falcon 9 · 海面降落](shots/03.jpg)](shots/03.jpg) |
| [清明上河 · 雨中虹桥](https://silentfleetkk.github.io/qingming-bianjing/opus-5.5/qingming-bianjing.html) · 船身和桅杆被波纹打碎，仍能对回水上的对象。 | [Falcon 9 · 海面降落](https://github.com/noahsabaj/falcon9-blender/releases/tag/v1.0) · 船舷与右侧箱体在水中延成倒形，左侧绿灯也有对应亮点；水纹只轻微打散它们。 |
## 看哪里

1. 江南山谷 · 清晨河岸：桥洞与倒影接近闭合，两侧墙体沿岸线向下延伸。
2. 清明上河 · 雨中虹桥：船身和桅杆被波纹打碎，仍能对回水上的对象。
3. Falcon 9 · 海面降落：船舷与右侧箱体在水中延成倒形，左侧绿灯也有对应亮点；水纹只轻微打散它们。

## 拆解

下列为截图观察，反射实现与准确roughness不由画面断言。

- **F · 连续性**：江南拱桥下半圆由水补完；雨桥的暖窗倒影仍处在窗下方，虽碎但方向正确。反射不是随意铺一张漂亮波纹。
- **C · 分界**：江南水岸约在画高中线下方，桥洞与对称倒影围成中心入口；Falcon船体接水线位于画面下部，水中箱体倒形由这条边界向下延伸。
- **D · 形体**：先反射大的墙、桥、船，再出现窗和枝条。雨船长暗形比小白波点更能说明水面位置。
- **B · 色彩**：雨景船窗浅米色在水中变暗、变碎；冷灰水底仍占多数面积。倒影不应比源物体更饱和或无缘由更亮。
- **E · 波面**：Falcon船体的大形较稳，雨桥船边更破碎；两者都保留低频轮廓，近处波纹才承担细节。真实折射、屏幕反射范围须另验。

## 做法

先用没有小波纹的水面验证对象与倒影的空间对应，之后逐级加入法线扰动。斜看角度下更强的表面反射可以与近处透水区域共存。

- **迁移试验值**：构图先给水面25–40%画高；选一个桥洞、灯柱或门洞作反射标尺。波纹加入后，400px缩图仍应认出至少一个成对轮廓。
- 若使用屏幕空间反射，必须实看相机移动时是否突然断掉；截图本身不能证明离屏反射正确。

### 实现索引

路径相对 `~/Blog/`；citadel 栏相对 `~/Blog/citadel/`。源码默认值不是旧截图的已验证运行实参；建议迁移值仍需目标场景实看。`source: none` 不以邻接源冒充原作算法。

| 作品 | 源码 / 技术与边界 | 参数及性质 | 许可 / 复用 | citadel 已有实现 |
|---|---|---|---|---|
| 江南山谷 · 清晨河岸 | `Repos/webgl-seascape-video/episodes/04-jiangnan-voxel/interactive.html:1090-1221`；水平Reflector目标纹理经投影UV采样，噪声法线轻扰动，Fresnel随视角增反射；浅/深色与岸缘项混合。1222-1236的上游支流标NO_REFL，不属于此镜面路线。依赖Three Reflector、renderer/camera、TIME及雨量uniform；不是仅换一张水贴图。 | clipBias=.002（源码）；UV distortion=N.xz*.02*(.5+.5*uRipple)（源码）；Fresnel=.02+.98*(1-ndv)^5（源码）；浅/深色=#3d6a6a / #0d2430（源码） | 未发现LICENSE；只借手法 / borrow | `lab/src/core/reflect.js:53-101,112-164` |
| 清明上河 · 雨中虹桥 | `Repos/qingming-bianjing/opus-5.5/qingming-bianjing.html:1027-1104`；三频流动噪声+有限差分法线、雨圈扰动，再采样平面Reflector；保留大轮廓同时把边缘打碎。依赖uTime/uRain、场景层过滤与纹理矩阵；平面反射不负责水下吸收或几何波峰。 | 波频权重=.55/.3/.15（源码）；有限差分normal strength=.27（源码）；反射UV扰动=.032（源码）；反射mix上限=.74（源码）；clipBias=.002（源码） | 未发现LICENSE；只借手法 / borrow | `lab/src/core/reflect.js:53-101,112-164` |
| Falcon 9 · 海面降落 | `Repos/falcon9-blender/film/envs.py:231-282`；Blender Principled水面用低粗糙度与IOR反射环境/物体，Noise→Bump保留大形。以下是ocean()函数默认值，56s原成片的具体shot实参尚未逐一回放核对，不称截图实测值。依赖bpy/Cycles或原作渲染设置、sky_node与场景对象；材质逻辑可转译，不能把Python直接接入Three。 | rough default=.06（源码）；IOR=1.33（源码）；wave_scale default=.004（源码）；wave_bump default=.25（源码）；base color default=(.003,.010,.018)（源码） | 代码MIT；模型/成片/音乐CC BY-NC4.0，须署名noahsabaj/Claude Opus5.5 / integrate | `lab/src/core/reflect.js:53-101,112-164` |


Citadel 接法：`lab/src/core/reflect.js:84-101,112-164` 的 `reflectFloor({w,d,x,y,z,strength,blur,f0,tint,mask,size,...})` 已有镜像相机、裁切面与湿区mask，是**加法反射覆层**，底层还需独立水材质；不自带水深吸收、折射或几何波。雨圈仅扰动UV。`blur=0.5, smear=0, strength=0.5` 是建议迁移起点，不是既有场景实测值；先在灰模里找一个可配对轮廓。后续Beach1/2须在现有 `waterline` / `from-sea` 机位（`lab/src/scenes/Beach/index.js:118-120`）验证，而非改成巨型水庭。小尺寸Shrine basin也不能被描述成已存在的大水庭。

## 迁移到博客

Beach1/2已登记开放，其后续美术方案适合先做一个可读岸物与倒影组合；Shrine若加水庭，先让门柱或台阶反射成立，再添加漂浮花瓣。这里是新增方案，不表示已实现水庭。

搭配河道串景、镜面邻粗面；与强密集焦散、满水面白色高光冲突。反射负责形状，焦散只在浅水局部负责水底照明。

## 反例

Cosmos的水面高光与天体发光同时密集，虽然能读出水，却很难靠倒影延续主体。它适合躁动奇观，不适合本卡的安静空间延展。


[![Shader & Cosmos · 吸积盘](shots/04.png)](shots/04.png)
[Shader & Cosmos · 吸积盘](https://github.com/holooooo/webgl-seascape-video) · 亮点覆盖大部分水面，很难用稳定倒影读出上方形体。

[逐图来源与复现](SOURCE.md) · [返回视觉卡库](../../../README.md)
