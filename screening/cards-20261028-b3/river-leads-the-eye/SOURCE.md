# 河道串景 · 逐图来源

归档/观察日期：2026-10-25。图像版权归原作品权利人；媒体不随本库代码许可重新授权。模型归属只保留作者陈述。

## 01.jpg · 清明上河 · 黄昏全城

- 来源：https://silentfleetkk.github.io/qingming-bianjing/opus-5.5/qingming-bianjing.html
- 类型：浏览器实看后的原画面
- 机位/时间/步骤：Chrome打开Opus版→默认汴河全景→黄昏华灯初上→H隐藏界面，待变化稳定；2494×905原生视口。
- 尺寸：2494×905；原尺寸保存，未放大、改色或重绘。
- SHA256：`5fdbc04616d583ed57f24d71285249262edf8a6e70c8dbe8549529808bd0680e`
- [原片与操作详情](../../../public/references/opus-a/SOURCE.md)。

## 02.jpg · Sakura River Valley

- 来源：https://valley.mengto.here.now/
- 类型：浏览器实看后的原画面
- 机位/时间/步骤：作者在线版默认行船镜头；已观察连续行船与花瓣，近船左下/红桥右后/塔右上时截图；没有timecode，非完整路径验收。
- 尺寸：2494×905；原尺寸保存，未放大、改色或重绘。
- SHA256：`9187a701c104bef582a622d84664ba5d5f75d83110734a4d391e9e5a919c2099`
- [原片与操作详情](../../../public/references/local-collections/SOURCE.md)。

## 03.png · 江南山谷 · 清晨河岸

- 来源：https://github.com/holooooo/webgl-seascape-video/blob/915cb7c9a318e03bd2228bc232494b496ff2316c/episodes/04-jiangnan-voxel/interactive.html
- 类型：浏览器实看后的原画面
- 机位/时间/步骤：本地3079江南interactive.html；02河边低机位→清晨→隐藏界面；1920×1080。画质曾自适应降低。
- 尺寸：1920×1080；原尺寸保存，未放大、改色或重绘。
- SHA256：`4cc30085a77796e235e74957481ffc42f02f2cc70bf94f9127fc9b0de6a50ba3`
- [原片与操作详情](../../../public/references/light-water/SOURCE.md)。

## 04.png · Shader & Cosmos · 吸积盘

- 来源：https://github.com/holooooo/webgl-seascape-video
- 类型：浏览器实看后的原画面
- 机位/时间/步骤：本地3079/Repos/webgl-seascape-video/episodes/03-shader-cosmos/interactive.html；高画质、暂停、08吸积盘、隐藏界面；质量1.1、亮度1、曝光0.85，波相位未固定。
- 尺寸：1920×1080；原尺寸保存，未放大、改色或重绘。
- SHA256：`7aa4c416230909d14ddd2cfc4ebc7ca4759b67c4aa1db0c2a2b8e6c80fb04019`
- [原片与操作详情](../../../public/references/light-water/SOURCE.md)。

## 05.jpg · Poseidia · Sea Canal

- 日期：2026-10-25
- 原作：https://poseidia.vercel.app/
- 步骤/版本：Click to set sail→开场过门至Sea Canal→F照片模式→Hour09:04/Lens50°/Focus40m/Aperture Home→H隐藏；原2494×905，小船与水仍动。
- 尺寸：[2494, 905]
- SHA256：`94077f92fd9191ab85988c2dbe8eb27084d545c41f12d32f8eeb1fc779240b0c`
- 权利：原作者保留，未核实开放媒体许可，不移植原素材。
- [原全图、截图流程与限制](../../../public/references/opus-a/SOURCE.md)。

## 2026-10-28 实现索引核对

本轮不重拍既有视觉参考，仅新增读源码证据；图像来源与视频许可沿用上表。`source: none` 的作品仍无已确认原作源码，邻接实现不证明作品算法。Citadel 仅做只读检索，未改场景/预制模块。

- `Repos/qingming-bianjing`：读取版本 `d9d85a0a19e9e52daa028e37407637c3da211f31`；具体文件与行、参数、许可分工见 README 实现表。未见根 LICENSE，borrow；vendor 的 Three MIT 不授予整部作品许可。
- `Repos/webgl-seascape-video`：读取版本 `915cb7c9a318e03bd2228bc232494b496ff2316c`；具体文件与行、参数、许可分工见 README 实现表。未见根 LICENSE，borrow；当前模块化代码不等同归档915cb7c9的单文件成片版本。

参数的源码默认值不等于既有截图的已验证运行实参；建议迁移值均待目标场景验证。

禁建证据补充：`Repos/qingming-bianjing/opus-5.5/qingming-bianjing.html:1221-1231`，尤其 1229 的 `ri.d < ri.hw + 4`；809–829 本身只提供河道查询。无根 LICENSE，仍只借手法。
