# SHOW-009 · 以支撑脚点采样把构筑物真正接到地面
案例：[ awesome-opus5.5-frontend-showcases ](../cases/awesome-opus5.5-frontend-showcases.md) · 机制证据：`source_only`

效果图用于理解来源作品，不自动验证本卡中的每个机制。

## 设计动作

连接关系比堆材质更决定模型可信度。须区别：最低点下沉适合石/植被，不能保证桌椅全脚不穿地；代码注释写3.6但循环为4.8。

## 实现与参数

groundMin取最低点用于下沉物件；tube沿路径s+=4.8，脚外偏1.25、顶偏.62，支撑胶囊终点gy−.2。

## 审美细节

连接关系比堆材质更决定模型可信度。须区别：最低点下沉适合石/植被，不能保证桌椅全脚不穿地；代码注释写3.6但循环为4.8。

## 适用条件

- 地形高度场可查询
- 构筑物支脚有单独长度自由度

## 相邻方案与区别

相对整个模型贴terrain中心，逐脚解决斜坡连接；仍不是结构力学验证。

## 失败模式

- 最低点策略让高侧埋入
- 不同的碰撞/渲染坐标造成假接地

## Movie 裁决

- **verdict**：prototype
- **reason**：桥柱/码头特写容易暴露悬空，优先补。

## Frontend 裁决

- **verdict**：adapt
- **reason**：接地后仍需walkmask和碰撞同步。

## 最小对照

四斜角低机位看脚点，记录脚底与地面差；超过约1cm可见空隙或明显穿地为失败。

## 源码证据

- [Repos/awesome-opus5.5-frontend-showcases/repro/pelagia/index.html:593–642](https://github.com/OpenVGLab/awesome-opus5.5-frontend-showcases/blob/cac43b250f07b7b86f4709c61effc84269f46494/repro/pelagia/index.html#L593-L642)：groundMin中心+6环采样；支撑脚用terrainH，入土.2，净空<.35不造支腿，实际循环间距4.8

## 项目效果图

![awesome-opus5.5-frontend-showcases · historical_still_viewed](../assets/previews/awesome-opus5-5-frontend-showcases-d74f1f9a2bf7.jpg)

已查看的来源静帧；不证明当前版本运行。

来源：[原作者/出处](https://github.com/OpenVGLab/awesome-opus5.5-frontend-showcases/blob/cac43b250f07b7b86f4709c61effc84269f46494/repro/_covers/pelagia.jpg) · historical_still_viewed。历史封面，不能证明当前运行/运动/交互

## 归纳与练习

暂未归入新增专业视角；保留原机制边界。

[MP-10](../patterns/MP-10.md)
