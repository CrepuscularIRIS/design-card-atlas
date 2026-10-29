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

## 04.jpg · Kōyō-en · 入口

- 角色：counterexample。
- 来源：https://modelzengarden.com/garden/opus-5-5-claude-code
- [归档原图](../../references/opus-b/268-koyo-en-entry.jpg)；尺寸 2494×905。
- 类型：浏览器实看后的原画面。
- 机位 / 时间 / 观察范围：Show me the results→Opus5.5 garden→Step inside；入口原生2494×905截图，未移动。
- SHA256：`988a5babca574591e5c428a0d4b207d1de47e1d2b61f5291c0bf0ba43a97ac2d`。

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
- [`Repos/athenaion/src/ruins/ivy.js:112-189`](https://github.com/Leonxlnx/athenaion/blob/9b8bd23b39c458a50fb1201037360047781c45b5/src/ruins/ivy.js#L112-L189)
