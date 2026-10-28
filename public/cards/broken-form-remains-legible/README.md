# 残损仍识原形

分组：材质 · 主维度：E 断口与磨损、D 可辨认残体、C 完整与破损对照、A 凹凸光影、I 时间 · 情绪：沧桑、失落

## 一句话

保留足以辨认的原形，再用缺失、断口和散件说明它经历过什么。

[![Ozymandias · 孤立残像](shots/03.png)](shots/03.png)
[Ozymandias · 孤立残像](https://www.echohive.ai/posts/ozymandias/animation.html) · 残腿、底座、散石分别留着完整纪念物的线索。

| 参考 | 参考 |
|---|---|
| [![Athenaion · Fallen head](shots/01.jpg)](shots/01.jpg) | [![Athenaion · Ruined portico](shots/02.jpg)](shots/02.jpg) |
| [Athenaion · Fallen head](https://github.com/Leonxlnx/athenaion) · 落地巨像保留鼻梁、眼与发束，断裂不是均匀污渍。 | [Athenaion · Ruined portico](https://github.com/Leonxlnx/athenaion) · 柱头和残梁还说明这里原有廊架，断掉的部分由观众补全。 |
## 看哪里

1. Ozymandias · 孤立残像：残腿、底座、散石分别留着完整纪念物的线索。
2. Athenaion · Fallen head：落地巨像保留鼻梁、眼与发束，断裂不是均匀污渍。
3. Athenaion · Ruined portico：柱头和残梁还说明这里原有廊架，断掉的部分由观众补全。

## 拆解

图像比例为目估；本卡关注几何缺失，与“风化依附形体”的表面分布分开。

- **D · 识别**：Athenaion巨头像的眼鼻口仍连续，Ozymandias腿与基座关系明确；看不出原物的碎石只能说明石堆，不能说明纪念物坍塌。
- **E · 断口**：残廊上部不连续，头像落地后改变朝向；大缺失先读到，微斑驳后读到。平均撒同样小的破洞不会产生同样叙事。
- **C · 对照**：落地头像后仍有完整高殿，近破远整把两种时间放进一幅图；残像在空沙地上则借缺失的周边表达孤立。
- **A · 光影**：巨像眼窝与断边有宽暗部，受光颊面仍连续；纹理不能把裂纹画成无视光向的纯黑线。
- **I · 时间**：废墟草木、倾倒方向与散件关系共同暗示过程；没有考古证据时只说画面暗示，不编造作品设定或真实历史。

## 做法

先建完整原形并定义“哪里断了”，再做断口、落地接触与小碎片。让碎件大小集中在一两类，并沿可信范围分布。

- **迁移试验**：约保留主体60–80%的识别线索，再移走一处关键完整性；不是破坏比例越大越好。使用灰模确认破损后仍认得物体。
- 此处不提供未检查的破碎算法，也不把静帧等同可交互物理破坏。

### 实现索引

2026-10-28 已打开本地源码核对；当前 checkout 不等同旧成片版本。参数区分源码与建议迁移值，尚未在 Citadel 运行复刻。`citadel: none` 是尚未找到可复用实现，不是已落地声明。第三方路径相对 `~/Blog/`，Citadel 路径相对 `~/Blog/citadel/`。固定版本与许可见 [SOURCE.md](SOURCE.md)。

| 作品 | 源码 / 邻接与手法 | 参数及性质 | 许可 / 复用 | Citadel 可复用实现 |
|---|---|---|---|---|
| Ozymandias · 孤立残像 | `none`；原作源码未取得；邻接技术源 Repos/athenaion/src/ruins/portico.js:29-49,168-176,340-375（MIT）。以完整柱鼓保留沟槽、顶部局部破断、碎件另置；只迁移几何残损，不声称重现原作腿像；不是原作实现证明，迁移待验证。 | 识别线索保留=60–80%（建议迁移值） | 原作许可未明；邻接源许可见说明 / borrow | `none` |
| Athenaion · Fallen head | `Repos/athenaion/src/sculpt/head.js:210-229,498-523; Repos/athenaion/src/ruins/headpose.js:11-34`；sculpt/head.js 的 CHIPS/CRACKS 和 detail>0 分支用噪声断颈平面、局部球减法与有限裂面生成残损；headpose.js 仅用眼锚、面/冠轴、anchorDepth 与各向异性放置头像。两者职责分开；保留 sculpt/head.js 与 bake/head.js 几何管线，非损坏贴图。 | anchorDepth=4.42（源码）；aniso=[1.15,1,0.85]（源码）；断颈粗糙振幅=0.035 fbm + 0.012 noise（源码）；裂面宽=0.005 / 0.0016（源码） | MIT / integrate | `none` |
| Athenaion · Ruined portico | `Repos/athenaion/src/ruins/portico.js:29-49,168-176,340-375`；保留柱身/柱头与残梁，SDF柱鼓局部 breakTop、石板缺失和分裂；接触高度由 floor9 求解 | 最后柱鼓 breakTop=0.25（源码）；flutes=24（源码）；裂板条件概率=0.38（源码） | MIT / integrate | `none` |

## 迁移到博客

Shrine旧庭院可放一处残碑/倒像与仍在使用的主门对照；BlackCityHall若增加历史层，选择一处旧构件，不把所有立柱同时破坏。均为新提案。

搭配风化依附形体、留空放大孤立物；与整齐镜面金属的全新工业目标要分区，避免一个场景既处处崭新又处处荒废而没有原因。

## 反例

黑沙柱壁的规则完整竖柱本身很有力量，但均匀表面噪声无法承担“曾经倒塌”的叙事。它作为对照说明完整阵列与结构性残损是两种不同语言。


[![雷尼斯黑沙滩 · 柱壁](shots/04.jpg)](shots/04.jpg)
[雷尼斯黑沙滩 · 柱壁](https://github.com/Zp-Peter/kimi-k31pro-opus55-benchmark-showcase/blob/65e82c53b63f2fdd918617269c057d8e53af2c6f/opus/reynisfjara/index.html) · 完整等距柱列是秩序参考；若只均匀贴噪点，不能讲出局部破损事件。

[逐图来源与复现](SOURCE.md) · [返回视觉卡库](../../../README.md)
