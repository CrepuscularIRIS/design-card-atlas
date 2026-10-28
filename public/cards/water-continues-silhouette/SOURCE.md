# 水面续轮廓 · 逐图来源

归档/观察日期：2026-10-25。图像版权归原作品权利人；媒体不随本库代码许可重新授权。模型归属只保留作者陈述。

## 01.png · 江南山谷 · 清晨河岸

- 来源：https://github.com/holooooo/webgl-seascape-video/blob/915cb7c9a318e03bd2228bc232494b496ff2316c/episodes/04-jiangnan-voxel/interactive.html
- 类型：浏览器实看后的原画面
- 机位/时间/步骤：本地3079江南interactive.html；02河边低机位→清晨→隐藏界面；1920×1080。画质曾自适应降低。
- 尺寸：1920×1080；原尺寸保存，未放大、改色或重绘。
- SHA256：`4cc30085a77796e235e74957481ffc42f02f2cc70bf94f9127fc9b0de6a50ba3`
- [原片与操作详情](../../references/light-water/SOURCE.md)。

## 02.jpg · 清明上河 · 雨中虹桥

- 来源：https://silentfleetkk.github.io/qingming-bianjing/opus-5.5/qingming-bianjing.html
- 类型：浏览器实看后的原画面
- 机位/时间/步骤：虹桥河岸→清明时节雨纷纷→隐藏界面；待雨线出现。2494×905原生。
- 尺寸：2494×905；原尺寸保存，未放大、改色或重绘。
- SHA256：`7ecd1b00cadbf84d5907156ed454640eb4f355712d17a734f7801f4ab9e467a6`
- [原片与操作详情](../../references/opus-a/SOURCE.md)。

## 03.jpg · Falcon 9 · 海面降落

- 来源：https://github.com/noahsabaj/falcon9-blender/releases/tag/v1.0
- 类型：作者3D电影单帧；noahsabaj，CC BY-NC 4.0
- 机位/时间/步骤：作者v1.0成片56.000s原尺寸帧；已实际查看，非本轮本地Blender运行。
- 尺寸：1920×1080；原尺寸保存，未放大、改色或重绘。
- SHA256：`12cf6f1fa7c36888dd6932d3eb0733683d3b1bc5e82967b36daa9f9d0d5aed1e`
- [原片与操作详情](../../references/opus-d/SOURCE.md)。

## 04.png · Shader & Cosmos · 吸积盘

- 来源：https://github.com/holooooo/webgl-seascape-video
- 类型：浏览器实看后的原画面
- 机位/时间/步骤：本地3079/Repos/webgl-seascape-video/episodes/03-shader-cosmos/interactive.html；高画质、暂停、08吸积盘、隐藏界面；质量1.1、亮度1、曝光0.85，波相位未固定。
- 尺寸：1920×1080；原尺寸保存，未放大、改色或重绘。
- SHA256：`7aa4c416230909d14ddd2cfc4ebc7ca4759b67c4aa1db0c2a2b8e6c80fb04019`
- [原片与操作详情](../../references/light-water/SOURCE.md)。

## 2026-10-28 实现索引核对

本轮不重拍既有视觉参考，仅新增读源码证据；图像来源与视频许可沿用上表。`source: none` 的作品仍无已确认原作源码，邻接实现不证明作品算法。Citadel 仅做只读检索，未改场景/预制模块。

- `Repos/falcon9-blender`：读取版本 `c6a6349c0968870a7a864f8ba44d2182cafad60e`；具体文件与行、参数、许可分工见 README 实现表。LICENSE 仅授予 Python/脚本 MIT；LICENSE-ASSETS.md 对模型/渲染/成片为 CC BY-NC 4.0，不混用。
- `Repos/qingming-bianjing`：读取版本 `d9d85a0a19e9e52daa028e37407637c3da211f31`；具体文件与行、参数、许可分工见 README 实现表。未见根 LICENSE，borrow；vendor 的 Three MIT 不授予整部作品许可。
- `Repos/webgl-seascape-video`：读取版本 `915cb7c9a318e03bd2228bc232494b496ff2316c`；具体文件与行、参数、许可分工见 README 实现表。未见根 LICENSE，borrow；当前模块化代码不等同归档915cb7c9的单文件成片版本。

参数的源码默认值不等于既有截图的已验证运行实参；建议迁移值均待目标场景验证。

Citadel 复用补充：`src/world/worlds/atlasWater.js:6-25,38-62`（材质、梯度波、Fresnel 与反射采样），需 shoreColor 与反射 uniform；`planarWaterReflection.js` 调用为 render(camera,width,height)。索引现有实现不改变锁定 atlas。Falcon 项整体仍按 borrow，避免将源码 MIT 扩张为成片/模型可自由集成。
