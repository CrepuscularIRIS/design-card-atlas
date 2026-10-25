# 黑沙与银水的海岸

给 **Beach1/2 后续美术方案、BlackCityHall 外部材质研究** 的配方：黑壁、灰天、银色湿带构成三块主关系。用于已有登记地点的后续造景，不重建已退役的海上入场路线。

## 参考情绪板

| 远景构图 | 近壁材质 |
|---|---|
| [![雷尼斯海岸](../cards/low-chroma-value-steps/shots/01.jpg)](../cards/low-chroma-value-steps/shots/01.jpg) | [![玄武岩柱](../cards/staged-camera-approach/shots/02.jpg)](../cards/staged-camera-approach/shots/02.jpg) |
| [Opus标注版本](https://github.com/Zp-Peter/kimi-k31pro-opus55-benchmark-showcase)：湿带串起近远，非模型排名 | 同作近柱镜位；不要把远景纹理硬放大充当近壁 |
| [![Kimi黑沙全景](../cards/low-chroma-value-steps/shots/02.jpg)](../cards/low-chroma-value-steps/shots/02.jpg) | [![船体与海面](../cards/mirror-beside-roughness/shots/05.jpg)](../cards/mirror-beside-roughness/shots/05.jpg) |
| 同合集另一独立实现，借大色块与标题留白 | Falcon 9图只借哑船与海面反射对照；[原作](https://github.com/noahsabaj/falcon9-blender/releases/tag/v1.0)，不迁移火箭题材 |

所有图为实看画面，来源详见卡内SOURCE。材料辅图不代表场景题材必须混搭。

## 维度分工

| 维度 | 负责卡 | 在此组合中的试验决定 |
|---|---|---|
| A 光影 | [低彩分灰阶](../cards/low-chroma-value-steps/README.md)内的明暗结构 | 阴天漫射；湿带反射天空成为局部亮处，不另设无来源聚光照地。 |
| B 色彩 | [低彩分灰阶](../cards/low-chroma-value-steps/README.md) | 主黑灰`#20272A`、辅灰青`#748184`、少量浪白`#BAC6C5`。UI白也控制面积，不加第二套霓虹色。 |
| C 构图 | [斜向配重](../cards/diagonal-mass-balance/README.md) | 暗壁占左侧约40–50%，右侧海与湿带抵住重量；岸线连到一个远礁。 |
| D 造型 | [柱廊明暗节奏](../cards/colonnade-rhythm/README.md)的自然转译 | 玄武岩竖柱高低参差，粗崖、细柱、近碎石三级；不是完美等高的人造柱阵。 |
| E 表面 | [镜面邻粗面](../cards/mirror-beside-roughness/README.md) | 干沙/崖面先试roughness0.8，湿带约0.2起调；以反光宽度和潮线连贯性判断。 |
| F 水与雾 | [水面续轮廓](../cards/water-continues-silhouette/README.md)、[雾层分远近](../cards/fog-separates-depth/README.md) | 海浪只保留几条近岸白边，远海反差降低；不是全海面星光闪点。 |
| G 镜头 | [分级机位靠近](../cards/staged-camera-approach/README.md) | 海岸全景→近柱细节是两级信息；每一级有自己可读的地面与主体，不为拉近而穿入几何。 |
| H UI | [巨字随景退场](../cards/type-yields-to-scene/README.md) | 标题只在远景负空间，进入近壁/会面后退场。保留地点名即可，不搬参考的控制面板。 |

## 组合检查

1. **光源**：银湿带来自灰天反射，浪白来自表面，不让海面无端发蓝光；若出现夜灯，需另立夜景方案，不能借暖灯补救当前灰度。
2. **色彩**：黑灰主、灰青辅、浪白点缀，没有紫雾。角色着色是否与灰岸分离另看。
3. **明暗**：暗壁/干沙50–65%，中灰天海25–40%，亮带与浪5–10%；保留崖面中调，不能压成完全黑的剪影。
4. **尺度**：近碎石、中柱壁、远礁。还需放一件熟悉尺寸的沿岸物或角色参照，否则地质结构可能读成小岩石。
5. **冲突**：密集焦散会破坏阴天沉静；全镜面水会让海浪像玻璃板；低彩不等于低反差；标题和湿带不能同时占据主要视觉入口。

## 先验证什么

做一个灰模崖体、一个湿干边界和一个远礁就开始看400px截图；若没有主次，不添噪声贴图。近柱机位要另验接触阴影与断面，远景中好看的材质不保证近处也成立。
