# synthcity
已读街区分配、模型选择辅助和锐化shader；可借城市节奏，不能将全部外部素材视为MIT。

## 案例档案

[来源仓库](https://github.com/jeffbeene/synthcity)
分析版本：`5a4ee0dd231ce06653a2a9776ed2e36137918d21`

模型归属未独立认证。

## 初始源码审计边界

未读取巨大index运行时、全部OBJ、交通/自动驾驶与资产管理；无本地场景图被观察。

以下保留初始源码审计的观察范围。后续新增静帧独立列于视觉材料，不追溯证明全部机制或运行状态。

## 机制与案例分析

### [SD-SY01 · 用稀有巨构与留空街区打断城市重复节奏](../cards/SD-SY01.md)

重复模块需要低频地标和空白作层级，不能以每栋不同代替整片城市的节奏。

大量楼体不是均匀亮墙，typeNoise .33–.66去广告形成安静段；屋顶装置仅极少出现。

**Movie：prototype** · 适合Ride背景建立近中远层级。
**前端：adapt** · 复用布局策略与自有合法资产，不自动搬OBJ/音频。

失败条件：- 噪声阈值不是独立概率
- 烟/射灯仍Math.random
- 第三方模型/音乐权利另查

### [SD-SY02 · 拒绝用强锐化替代材质细节](../cards/SD-SY02.md)

高频增强不能补不存在的几何/贴图，会放大霓虹边界噪声。

此实现只有屏幕锐化；没有材质法线或几何细节。

**Movie：defer** · 仅后期诊断，不优先用于打磨。
**前端：reject** · 不作为前端画质默认提升。

失败条件：- 光晕与负值
- 不能恢复缺失资产

## 项目效果与观察材料

![synthcity · author_repository_screenshot](../assets/previews/scene-synthcity-1.jpg)

实际查看：高角度密集夜城，蓝紫雾压远景，窗格/招牌粉青发光，光柱与高楼构成竖向节奏。

来源：本轮已观察的历史截图 · author_repository_screenshot。原仓README所用效果图的本地同名文件；历史静帧，不证明当前帧率、雨动或车辆控制。

![synthcity · author_repository_screenshot](../assets/previews/scene-synthcity-2.jpg)

实际查看：近中景大块深色交叉悬挑楼体，被蓝紫雾与白粉霓虹窗面包围，轮廓与高亮区分明。

来源：本轮已观察的历史截图 · author_repository_screenshot。原仓screenshots目录的历史渲染图；可观察体量与色彩，不能单凭此图认定所有几何可通行或动态稳定。

## 复用边界

- **status**：observed
- **evidence**：LICENSE代码MIT；README Credits另列Sketchfab模型、Freesound声音、Uppbeat音乐，未逐资产核权利
- **reuse**：conditional

图片及第三方素材的权利单独保留；源代码许可证不自动授权媒体。
