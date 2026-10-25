# SD-CI01 · 把镜头和场景配置打包成可重访的评审状态
案例：[ 3dcitydb-web-map ](../cases/3dcitydb-web-map.md) · 机制证据：`source_only`

效果图用于理解来源作品，不自动验证本卡中的每个机制。

## 设计动作

多人比较画质需要同一视点与环境状态，分享场景状态比凭描述找镜头稳定。

## 实现与参数

generateLink记录静止时dayTime、shadows、terrainShadows，lat/lon6位、height3位、姿态2位，加layers；可以借概念形成Place评审preset。

## 审美细节

本仓主要GIS数据/选择界面，无电影化调色或建模方法；只提炼可复访评审工具。

## 适用条件

- 场景版本可识别
- 参数合法化
- 不含凭据

## 相邻方案与区别

与截图不同可回到场景；与录制动画不同只保存状态，不证明动态效果。

## 失败模式

- 原函数导出ion/Bing token不能照搬
- GIS经纬与本站局部米制坐标不通用
- 远端图层变化破坏可复现

## Movie 裁决

- **verdict**：reference
- **reason**：帮助锁定镜头验收，不直接提高画质。

## Frontend 裁决

- **verdict**：adapt
- **reason**：小型QA视点链接有用，完整Cesium迁移无必要。

## 最小对照

打开同一receipt两次，场景/相机/昼夜/曝光一致；漏载或状态随机变化即失败。

## 源码证据

- [Repos/3dcitydb-web-map/3dwebclient/utils/UrlController.js:99–143](https://github.com/3dcitydb/3dcitydb-web-map/blob/2e779d9e8a5b2acdcb52ae405839950d4d778f51/3dwebclient/utils/UrlController.js#L99-L143)：序列化相机/时间/阴影/图层到query，亦导出token
- [Repos/3dcitydb-web-map/3dwebclient/utils/UrlController.js:145–180](https://github.com/3dcitydb/3dcitydb-web-map/blob/2e779d9e8a5b2acdcb52ae405839950d4d778f51/3dwebclient/utils/UrlController.js#L145-L180)：经纬高和heading/pitch/roll及layer配置

## 项目效果图

![3dcitydb-web-map · author_repository_screenshot](../assets/previews/scene-3dcitydb-web-map-1.jpg)

实际查看：柏林贴图建筑与底图叠合，黄色高亮建筑、绿色选择框和右侧语义属性表同时出现。

来源：本轮已观察的历史截图 · author_repository_screenshot。README Demo 2历史截图，展示地理模型选择与语义数据；不是电影化建模质量样片。

![3dcitydb-web-map · author_repository_screenshot](../assets/previews/scene-3dcitydb-web-map-2.png)

实际查看：铁路、车站小屋、桥梁、隧道和植被落在三角地形上，带Cesium控件与比例尺。

来源：本轮已观察的历史截图 · author_repository_screenshot。README Demo 1的LoD3组合场景历史截图；不证明当前远端数据仍可访问。

## 归纳与练习

暂未归入新增专业视角；保留原机制边界。

[MP-07](../patterns/MP-07.md)
