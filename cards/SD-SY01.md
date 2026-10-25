# SD-SY01 · 用稀有巨构与留空街区打断城市重复节奏
案例：[ synthcity ](../cases/synthcity.md) · 机制证据：`source_only`

效果图用于理解来源作品，不自动验证本卡中的每个机制。

## 设计动作

重复模块需要低频地标和空白作层级，不能以每栋不同代替整片城市的节奏。

## 实现与参数

区域noise→巨构6格间隔→普通区2×2细分→3族模型/广告；巨构避开玩家路径x±128；普通体高缩放.75–1.2。

## 审美细节

大量楼体不是均匀亮墙，typeNoise .33–.66去广告形成安静段；屋顶装置仅极少出现。

## 适用条件

- 可见城市横向节奏
- 地标不堵玩家轨道

## 相邻方案与区别

与Nexus单栋语法互补，本卡控制城市级分布；与纯随机多模型相比增加地标节奏。

## 失败模式

- 噪声阈值不是独立概率
- 烟/射灯仍Math.random
- 第三方模型/音乐权利另查

## Movie 裁决

- **verdict**：prototype
- **reason**：适合Ride背景建立近中远层级。

## Frontend 裁决

- **verdict**：adapt
- **reason**：复用布局策略与自有合法资产，不自动搬OBJ/音频。

## 最小对照

固定路线10秒对比均匀楼群/稀有地标，主地标能持续定位；遮住出口或地标重复过密即失败。

## 源码证据

- [Repos/synthcity/src/classes/GeneratorItem_CityBlock.js:24–65](https://github.com/jeffbeene/synthcity/blob/5a4ee0dd231ce06653a2a9776ed2e36137918d21/src/classes/GeneratorItem_CityBlock.js#L24-L65)：noise<.2且6格网点才放巨构，回避车路径；noise<.1留空
- [Repos/synthcity/src/classes/GeneratorItem_CityBlock.js:65–132](https://github.com/jeffbeene/synthcity/blob/5a4ee0dd231ce06653a2a9776ed2e36137918d21/src/classes/GeneratorItem_CityBlock.js#L65-L132)：2×2地块、模型家族、可选广告
- [Repos/synthcity/src/classes/GeneratorUtils.js:17–49](https://github.com/jeffbeene/synthcity/blob/5a4ee0dd231ce06653a2a9776ed2e36137918d21/src/classes/GeneratorUtils.js#L17-L49)：大楼稀有材质、四方向、noise重映射

## 项目效果图

![synthcity · author_repository_screenshot](../assets/previews/scene-synthcity-1.jpg)

实际查看：高角度密集夜城，蓝紫雾压远景，窗格/招牌粉青发光，光柱与高楼构成竖向节奏。

来源：本轮已观察的历史截图 · author_repository_screenshot。原仓README所用效果图的本地同名文件；历史静帧，不证明当前帧率、雨动或车辆控制。

![synthcity · author_repository_screenshot](../assets/previews/scene-synthcity-2.jpg)

实际查看：近中景大块深色交叉悬挑楼体，被蓝紫雾与白粉霓虹窗面包围，轮廓与高亮区分明。

来源：本轮已观察的历史截图 · author_repository_screenshot。原仓screenshots目录的历史渲染图；可观察体量与色彩，不能单凭此图认定所有几何可通行或动态稳定。

## 归纳与练习

暂未归入新增专业视角；保留原机制边界。

[MP-09](../patterns/MP-09.md)
