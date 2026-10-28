# 残损仍识原形 · 逐图来源

归档/观察日期：2026-10-25。图像版权归原作品权利人；媒体不随本库代码许可重新授权。模型归属只保留作者陈述。

## 01.jpg · Athenaion · Fallen head

- 来源：https://github.com/Leonxlnx/athenaion
- 类型：已逐张查看的作者3D最终成片
- 机位/时间/步骤：作者最终独立渲染静帧；pos=[134.4,54,145]，target=[83.2,47.4,59.5]，FOV34.7°；原始版本9b8bd23，非本轮runtime。
- 尺寸：1920×1080；原尺寸保存，未放大、改色或重绘。
- SHA256：`a8e8af5e304280d5a904ca4e259b760858b8306bb25a79bed1a339b6f217fbf1`
- [原片与操作详情](../../references/strong-scenes/SOURCE.md)。

## 02.jpg · Athenaion · Ruined portico

- 来源：https://github.com/Leonxlnx/athenaion
- 类型：已逐张查看的作者3D最终成片
- 机位/时间/步骤：作者最终独立渲染静帧；pos=[151.56,57.8,139.41]，target=[83.16,60,66.41]，FOV36.5°；非本轮runtime。
- 尺寸：1920×1080；原尺寸保存，未放大、改色或重绘。
- SHA256：`68d7bf692af8428ee7b94584a6b76ba5eb348275fe648ef93022b9c94c479462`
- [原片与操作详情](../../references/strong-scenes/SOURCE.md)。

## 03.png · Ozymandias · 孤立残像

- 来源：https://www.echohive.ai/posts/ozymandias/animation.html
- 类型：实际浏览器截图的标注裁切，原全图保留
- 机位/时间/步骤：Enter the desert→Pause→slider110s；原2494×905保留于references/opus-a，裁切(0,65,2494,815)去播放器，得2494×750；无放大，长影末端被裁。
- 尺寸：2494×750；原尺寸保存，未放大、改色或重绘。
- SHA256：`8ee1ed7a8db7413a986022b910e756b00dd607e6b033ec55f6607b8ddf3fbeaf`
- [原片与操作详情](../../references/opus-a/SOURCE.md)。

## 04.jpg · 雷尼斯黑沙滩 · 柱壁

- 来源：https://github.com/Zp-Peter/kimi-k31pro-opus55-benchmark-showcase/blob/65e82c53b63f2fdd918617269c057d8e53af2c6f/opus/reynisfjara/index.html
- 类型：本轮实际观察后截取
- 机位/时间/步骤：从机位1按2，实际观察过渡后正面柱壁；未计时。
- 尺寸：2494×905；原尺寸保存，未放大、改色或重绘。
- SHA256：`c7c976ed7b3813183603be85d8743dfe58cdb66fa8e10382a9e0fd455c8e2827`
- [原片与操作详情](../../references/local-collections/SOURCE.md)。

- 本地复现入口：http://localhost:3079/Repos/kimi-k31pro-opus55-benchmark-showcase/opus/reynisfjara/index.html

## 2026-10-28 实现索引核对

本轮不重拍既有视觉参考，仅新增读源码证据；图像来源与视频许可沿用上表。`source: none` 的作品仍无已确认原作源码，邻接实现不证明作品算法。Citadel 仅做只读检索，未改场景/预制模块。

- `Repos/athenaion`：读取版本 `9b8bd23b39c458a50fb1201037360047781c45b5`；具体文件与行、参数、许可分工见 README 实现表。根 LICENSE：MIT（Leon Lin, 2026）。

参数的源码默认值不等于既有截图的已验证运行实参；建议迁移值均待目标场景验证。
