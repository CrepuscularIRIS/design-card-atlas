# 骨架规整草木野 · 逐图来源

2026-10-28 重新浏览归档原图后编辑。图片原尺寸复制，未放大、改色、生成或重绘；图像版权归原作者，不随代码许可重授权。静帧不宣称本轮运行原作引擎。

## 01.jpg · Blender 机场室内雨林

- 角色：reference。
- 来源：https://skillry.dev/ai-videos/kimi-k3-1/kimi-moonshot-068067-4
- [归档原图](../../references/kimi-videos/019-airport-rainforest-13.773.jpg)；尺寸 1920×1080。
- 类型：本轮实际观察后截取。
- 机位 / 时间 / 观察范围：浏览器看9.63s编辑器与13.77s成片；仅取13.773s，1920×1080原尺寸。
- SHA256：`1e4f9c1b57b66a2ffdf5d2c64ae6449480bac88cc56231182791142817b67f4a`。

## 02.jpg · Athenaion · 水庭

- 角色：reference。
- 来源：https://github.com/Leonxlnx/athenaion
- [归档原图](../../references/strong-scenes/athenaion-author-shot2.jpg)；尺寸 1920×1080。
- 类型：已逐张查看的作者3D最终成片。
- 机位 / 时间 / 观察范围：作者独立3D成片；pos=[-19,7,227] target=[-13.6,14.8,127.4] FOV28.5°，版本9b8bd23；非本轮runtime。
- SHA256：`b7ab6ee8013af83524b6d49a5c3e8f971026f7f298f88c978626690be3236c73`。

## 03.jpg · Athenaion · Ruined portico

- 角色：reference。
- 来源：https://github.com/Leonxlnx/athenaion
- [归档原图](../../references/strong-scenes/athenaion-author-shot9.jpg)；尺寸 1920×1080。
- 类型：已逐张查看的作者3D最终成片。
- 机位 / 时间 / 观察范围：作者最终独立渲染静帧；pos=[151.56,57.8,139.41]，target=[83.16,60,66.41]，FOV36.5°；非本轮runtime。
- SHA256：`68d7bf692af8428ee7b94584a6b76ba5eb348275fe648ef93022b9c94c479462`。

## 04.jpg · Blender cathedral interior · 仅骨架对照

- 角色：counterexample；对照只有建筑骨架而没有草木的画面，不是教堂质量评价。
- 来源：https://x.com/k1rallik/status/2113693629713633435
- [归档原图](../../references/opus-c-guide/kimi-63-18s.jpg)；1920×1080，未裁切、未放大、未调色。
- 观察：此前浏览器观看成片，pageAssets保存已观察原片，18.000s原尺寸抽帧；编辑器时刻已排除。2026-10-28本轮重新实看该归档，不声称重跑Blender。
- SHA256：`289adc79e887de9f19f3d8f8b4bbf7ff7e95c0e63c0d77e339247139a915d1b5`。
- 详细原片、模型陈述和操作记录：[来源笔记](../../references/opus-c-guide/SOURCE.md)。媒体归原作者，许可未明，仅作参考。
- 原Kōyō-en图含esc提示与鼠标指针，已从本卡移除；原稿仍可在ff13e7d及b3筛选档案追溯。

历史两席FAIL保留于 screening/cards-20261028-b3.csv 与对应目录，本次为重出编辑稿，尚不宣称通过新的双席核卡。旧图未重拍，capture字段保留原观察时间；本轮只重新浏览这些已归档画面。

## 实现来源版本与许可

本轮只读核对，未修改第三方仓或 citadel；尚未新增 cardfx 模块。下面是读源码的固定版本，不意味着所有旧媒体都由该版本实测生成。

- `athenaion`：`9b8bd23b39c458a50fb1201037360047781c45b5`；[固定版本](https://github.com/Leonxlnx/athenaion/tree/9b8bd23b39c458a50fb1201037360047781c45b5)；MIT，Leon Lin 2026。

- citadel 只读版本：`498bb2fb07a78754f8cd6df113d720f220546a8c`。README 的具体路径与行已读；这是可复用代码索引，不是移植完成声明。

## 已读实现的永久行链接

- [`Repos/athenaion/src/modules/vegetation.js:27-35`](https://github.com/Leonxlnx/athenaion/blob/9b8bd23b39c458a50fb1201037360047781c45b5/src/modules/vegetation.js#L27-L35)
- [`Repos/athenaion/src/vegetation/scatter.js:266-307`](https://github.com/Leonxlnx/athenaion/blob/9b8bd23b39c458a50fb1201037360047781c45b5/src/vegetation/scatter.js#L266-L307)
- [`Repos/athenaion/src/modules/flora.js:640-678`](https://github.com/Leonxlnx/athenaion/blob/9b8bd23b39c458a50fb1201037360047781c45b5/src/modules/flora.js#L640-L678)
- [`Repos/athenaion/src/ruins/grass.js:8-98`](https://github.com/Leonxlnx/athenaion/blob/9b8bd23b39c458a50fb1201037360047781c45b5/src/ruins/grass.js#L8-L98)
- [`Repos/athenaion/src/ruins/portico.js:185-244`](https://github.com/Leonxlnx/athenaion/blob/9b8bd23b39c458a50fb1201037360047781c45b5/src/ruins/portico.js#L185-L244)
- [`Repos/athenaion/src/ruins/ivy.js:112-192`](https://github.com/Leonxlnx/athenaion/blob/9b8bd23b39c458a50fb1201037360047781c45b5/src/ruins/ivy.js#L112-L192)

- [`Repos/athenaion/src/ruins/ivy.js:196-252`](https://github.com/Leonxlnx/athenaion/blob/9b8bd23b39c458a50fb1201037360047781c45b5/src/ruins/ivy.js#L196-L252)
- [`Repos/athenaion/src/vegetation/library.js:9-53`](https://github.com/Leonxlnx/athenaion/blob/9b8bd23b39c458a50fb1201037360047781c45b5/src/vegetation/library.js#L9-L53)

本次改稿另只读核对citadel当前版本 `3938c44eb11418fcc9462d3b41e1989c42cfdd2c` 的Shrine结构、canopy与机位：`structures.js:155-183`、`canopy.js:18-67,97-130`、`index.js:161-186,255-257`。没有改场景代码或完成新视觉验收；b4原稿两席FAIL保留在本批CSV。
