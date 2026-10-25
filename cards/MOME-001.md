# MOME-001 · 用连续地块、交通留白和分区偏转组织聚落，避免散落玩具盒
案例：[ map-of-middle-earth ](../cases/map-of-middle-earth.md) · 机制证据：`still_observed`

效果图用于理解来源作品，不自动验证本卡中的每个机制。

## 设计动作

实际lake-town.jpg能看到薄甲板下桩、密集屋脊和成片城镇轮廓；大面积背光仍压暗细部，不能仅凭高密度称其已达电影品质。把主街/水道与广场作为负空间，随机性局限在街区内部。

## 实现与参数

主水道宽.195（代码单位km），码头高.075厚.012；轮廓半轴1.7/1.3，110格边缘扰动*.075。regionYaw=±(5+5*rand)。fits检查五点、步道WALK=.016和预留广场。屋面0x4a5358等冷板岩、墙面0x67645d等灰褐、灯0xf0a54a。

## 审美细节

实际lake-town.jpg能看到薄甲板下桩、密集屋脊和成片城镇轮廓；大面积背光仍压暗细部，不能仅凭高密度称其已达电影品质。把主街/水道与广场作为负空间，随机性局限在街区内部。

## 适用条件

- 有主观看方向和交通语义
- 建筑足迹可参与布局检查

## 相邻方案与区别

与每栋随机旋转不同，区内有共同街向；与整块平台不同，边缘桩和薄板让结构可读。

## 失败模式

- 五点足迹检测可能漏细窄通道或凹边交叉
- 以英雄机位分配灯窗会让背面显空
- 本仓建筑人为约9倍展示尺度，不能搬成真实城市尺寸

## Movie 裁决

- **verdict**：prototype
- **reason**：一段街区即可测试轮廓与通道的可读性。

## Frontend 裁决

- **verdict**：adapt
- **reason**：需补完整足迹/可走空间检查与多方向照明。

## 最小对照

固定视点比较散点版与分区版，再看反向视点；主通道消失、步道被挤占或变成多块漂浮积木即失败。

## 源码证据

- [Repos/map-of-middle-earth/src/landmarks/lake-town/layout.ts:20–33](https://github.com/earthwalker17/map-of-middle-earth/blob/696e968e9d550327beda9e663ef5aec6961583c9/src/landmarks/lake-town/layout.ts#L20-L33)：统一城镇坐标、码头高度、主次水道宽度
- [Repos/map-of-middle-earth/src/landmarks/lake-town/layout.ts:49–122](https://github.com/earthwalker17/map-of-middle-earth/blob/696e968e9d550327beda9e663ef5aec6961583c9/src/landmarks/lake-town/layout.ts#L49-L122)：椭圆轮廓叠加低频变化、离散边缘与港湾缺口，再扣除水道
- [Repos/map-of-middle-earth/src/landmarks/lake-town/layout.ts:125–149](https://github.com/earthwalker17/map-of-middle-earth/blob/696e968e9d550327beda9e663ef5aec6961583c9/src/landmarks/lake-town/layout.ts#L125-L149)：街区旋转5–10度并预留市场与主宅
- [Repos/map-of-middle-earth/src/landmarks/lake-town/index.ts:18–90](https://github.com/earthwalker17/map-of-middle-earth/blob/696e968e9d550327beda9e663ef5aec6961583c9/src/landmarks/lake-town/index.ts#L18-L90)：暗冷木材配色、薄甲板和水下桩；不再用深裙边围住漂浮平台
- [Repos/map-of-middle-earth/src/landmarks/lake-town/index.ts:181–258](https://github.com/earthwalker17/map-of-middle-earth/blob/696e968e9d550327beda9e663ef5aec6961583c9/src/landmarks/lake-town/index.ts#L181-L258)：建筑中心与四角检查、临水正立面、分区背靠背排列、按区域分配层高

## 项目效果图

![map-of-middle-earth · historical_still_viewed](../assets/previews/map-of-middle-earth-9732ef806c0e.jpg)

已查看的来源静帧；不证明当前版本运行。

来源：[原作者/出处](https://github.com/earthwalker17/map-of-middle-earth/blob/696e968e9d550327beda9e663ef5aec6961583c9/docs/images/lake-town.jpg) · historical_still_viewed。静帧观察；没有由此验证连续动画或性能。

![map-of-middle-earth · historical_still_viewed](../assets/previews/map-of-middle-earth-c4a392f4439d.jpg)

已查看的来源静帧；不证明当前版本运行。

来源：[原作者/出处](https://github.com/earthwalker17/map-of-middle-earth/blob/696e968e9d550327beda9e663ef5aec6961583c9/docs/images/mount-doom.jpg) · historical_still_viewed。静帧观察；没有由此验证连续动画或性能。

## 归纳与练习

[CINE-01](../lenses/CINE-01.md) / [CINE-02](../lenses/CINE-02.md)

[MP-09](../patterns/MP-09.md)
