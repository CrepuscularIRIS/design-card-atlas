# 金饰点亮哑面 · 逐图来源

归档/观察日期：2026-10-25。图像版权归原作品权利人；媒体不随本库代码许可重新授权。模型归属只保留作者陈述。

## 01.jpg · Athenaion · Temple facade

- 来源：https://github.com/Leonxlnx/athenaion
- 类型：作者实际3D渲染成片，已逐张查看
- 机位/时间/步骤：作者最终独立静帧，1920×1080逐字节保存；机位pos=[75,62,66]，target=[32.73,74.2,-24.23]，FOV18.5°。原作9b8bd23。非本轮运行截图。
- 尺寸：1920×1080；原尺寸保存，未放大、改色或重绘。
- SHA256：`ead68e2bb4abea8a3db98b8de172ed974d4141a38e7e2071fa50ca9b9ea8c094`
- [原片与操作详情](../../references/strong-scenes/SOURCE.md)。

## 02.jpg · 悟空 · 金箍与棍端

- 来源：https://skillry.dev/ai-videos/kimi-k3-1/oddjolt-160428
- 类型：浏览器实看后的原画面
- 机位/时间/步骤：浏览器实看17.117s人物近景与30.293s末帧；已观察原片17.117s原尺寸抽帧，1920×1080；非完整动作验收。
- 尺寸：1920×1080；原尺寸保存，未放大、改色或重绘。
- SHA256：`b9254eb9fe9c20f5a6cfa03b98263495016d6538eda0b8119013a2a19dadd50f`
- [原片与操作详情](../../references/kimi-videos-tail/SOURCE.md)。

## 03.jpg · Athenaion · Grand staircase

- 来源：https://github.com/Leonxlnx/athenaion
- 类型：作者实际3D渲染成片，已逐张查看
- 机位/时间/步骤：作者独立静帧，1920×1080逐字节保存；机位pos=[24,26.8,50]，target=[-11.3,60.2,-37.4]，FOV42°。原作9b8bd23。与图01为同一作品的不同机位，非本轮运行截图。
- 尺寸：1920×1080；原尺寸保存，未放大、改色或重绘。
- SHA256：`b93171ce243cedd165f4c0c66d766dc739a60f82236dfff2f3f1c600cdece602`
- [原片与操作详情](../../references/strong-scenes/SOURCE.md)。

## 04.jpg · Kintsugi · 发光裂缝

- 来源：https://github.com/OpenVGLab/awesome-opus5.5-frontend-showcases/blob/cac43b250f07b7b86f4709c61effc84269f46494/repro/imaginary-planets/index.html
- 类型：浏览器实看后的原画面
- 机位/时间/步骤：本地3079/repro/imaginary-planets/index.html→Kintsugi第02行星→近景；实际整视口2494×905，默认自转相位未固定。
- 尺寸：2494×905；原尺寸保存，未放大、改色或重绘。
- SHA256：`1ae11817a64d53274c0e45cfef5c4ff647c41104c111c629126dc542832e2ea9`
- [原片与操作详情](../../references/local-collections/SOURCE.md)。

## 2026-10-28 实现索引核对

本轮不重拍既有视觉参考，仅新增读源码证据；图像来源与视频许可沿用上表。`source: none` 的作品仍无已确认原作源码，邻接实现不证明作品算法。Citadel 仅做只读检索，未改场景/预制模块。

- `Repos/athenaion`：读取版本 `9b8bd23b39c458a50fb1201037360047781c45b5`；具体文件与行、参数、许可分工见 README 实现表。根 LICENSE：MIT（Leon Lin, 2026）。

参数的源码默认值不等于既有截图的已验证运行实参；建议迁移值均待目标场景验证。

实际赋材质核对：盾牌 `Repos/athenaion/src/modules/statues.js:260-263` 调用 `src/sculpt/statueMaterial.js:1-44,133-164,180-194`；纹理 G 不是仅颜色贴图，它参与金箔/青铜颜色、粗糙度、金属度遮罩。因此不采纳“贴图即非金属”的推断，但撤回 generic metal.js 是盾牌实际实现的旧引文。阶梯盆体 `src/props/brazier.js:266-275` 调用 `src/props/metals.js:45-69` 的 bronzeMaterial，rough=0.24。generic materials/metal.js 仅保留为悟空的邻接源。
