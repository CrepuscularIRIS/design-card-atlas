# MOME-004 · 把地形跟随和净空约束做成平滑安全轨道，再叠加审美运镜
案例：[ map-of-middle-earth ](../cases/map-of-middle-earth.md) · 机制证据：`source_only`

效果图用于理解来源作品，不自动验证本卡中的每个机制。

## 设计动作

与Athenaion的参考构图小幅平移相比，本仓明确把跨山/跨水高度当作轨道输入。它是宏观地形安全机制，不是几何全碰撞保证，连续帧仍需抽检。

## 实现与参数

BAKE_HZ=96；目标地形13点圆盘半径.05D；安全采样中心+四轴点，半径.2+.02D，净空=.12+.015D（km）。±.6秒runningMax后σ=.3秒Gaussian。目标高度权重W=(4x(1-x))²在端点归零；姿态最终P.y+=dC。

## 审美细节

与Athenaion的参考构图小幅平移相比，本仓明确把跨山/跨水高度当作轨道输入。它是宏观地形安全机制，不是几何全碰撞保证，连续帧仍需抽检。

## 适用条件

- 有统一地形/水面高度查询
- 时间轴已固定可离线采样

## 相邻方案与区别

与单调Hermite或路径无过冲不同，这里实际查询环境高度；近楼/室内应另用扫掠体或几何碰撞检测。

## 失败模式

- 只测地形水面，不自动避开高楼、桥底、树和巨像
- 5点空间/96Hz时间采样可能漏窄尖峰
- 高斯平滑不构成严格净空数学证明
- 抬升相机可能破坏已审核构图

## Movie 裁决

- **verdict**：prototype
- **reason**：一段跨越地形的长镜头最适合验证，补足ATH-005的路径限制。

## Frontend 裁决

- **verdict**：adapt
- **reason**：适用于预设旅游镜头；不能替代自由相机实时碰撞。

## 最小对照

用山脊、桥梁、高楼三类障碍测首尾和中间帧；任何穿透/净空不足即失败，确认安全同时主角未被移出画面。

## 源码证据

- [Repos/map-of-middle-earth/src/tour/rig.ts:47–66](https://github.com/earthwalker17/map-of-middle-earth/blob/696e968e9d550327beda9e663ef5aec6961583c9/src/tour/rig.ts#L47-L66)：96Hz烘焙、净空余量与滤波常量
- [Repos/map-of-middle-earth/src/tour/rig.ts:495–551](https://github.com/earthwalker17/map-of-middle-earth/blob/696e968e9d550327beda9e663ef5aec6961583c9/src/tour/rig.ts#L495-L551)：主轨道按hold/move求解位置/变焦，细粗路径混合
- [Repos/map-of-middle-earth/src/tour/rig.ts:577–610](https://github.com/earthwalker17/map-of-middle-earth/blob/696e968e9d550327beda9e663ef5aec6961583c9/src/tour/rig.ts#L577-L610)：13点水面感知地形平均，平滑后在move中接入且端点回已审核高度
- [Repos/map-of-middle-earth/src/tour/rig.ts:618–687](https://github.com/earthwalker17/map-of-middle-earth/blob/696e968e9d550327beda9e663ef5aec6961583c9/src/tour/rig.ts#L618-L687)：高度上限作用量过滤、5点净空采样、运行最大值与高斯平滑后抬相机

## 项目效果图

![map-of-middle-earth · historical_still_viewed](../assets/previews/map-of-middle-earth-9732ef806c0e.jpg)

已查看的来源静帧；不证明当前版本运行。

来源：[原作者/出处](https://github.com/earthwalker17/map-of-middle-earth/blob/696e968e9d550327beda9e663ef5aec6961583c9/docs/images/lake-town.jpg) · historical_still_viewed。静帧观察；没有由此验证连续动画或性能。

![map-of-middle-earth · historical_still_viewed](../assets/previews/map-of-middle-earth-c4a392f4439d.jpg)

已查看的来源静帧；不证明当前版本运行。

来源：[原作者/出处](https://github.com/earthwalker17/map-of-middle-earth/blob/696e968e9d550327beda9e663ef5aec6961583c9/docs/images/mount-doom.jpg) · historical_still_viewed。静帧观察；没有由此验证连续动画或性能。

## 归纳与练习

[CINE-07](../lenses/CINE-07.md)

[MP-11](../patterns/MP-11.md)
