# 巨像越画框 · 逐图来源

2026-10-28 重新浏览归档原图后编辑。图片原尺寸复制，未放大、改色、生成或重绘；图像版权归原作者，不随代码许可重授权。静帧不宣称本轮运行原作引擎。

## 01.jpg · 云上石像

- 角色：reference。
- 来源：https://skillry.dev/ai-videos/kimi-k3-1/kimi-moonshot-068067-2
- [归档原图](../../references/kimi-videos/017-stone-deity-7.918.jpg)；尺寸 1920×1080。
- 类型：浏览器实看后的原画面。
- 机位 / 时间 / 观察范围：浏览器抽看1.699、6.793、7.918、10.914s与尾段；7.918004s原尺寸视频帧，非连续全片。
- SHA256：`3bffd14ed1e201811f6f5e3c7c82f7b6690748942dd8d05c9c137b1514f8c33d`。

## 02.jpg · 中式幻想 RPG · 雾中巨像

- 角色：reference。
- 来源：https://skillry.dev/ai-videos/kimi-k3-1/crangerus-549203
- [归档原图](../../references/kimi-videos/059-mist-colossi-1.788.jpg)；尺寸 1920×1080。
- 类型：浏览器实看后的原画面。
- 机位 / 时间 / 观察范围：浏览器实际看10.03/12.49s并拖回1.788s；已观察原片1.788s原尺寸抽帧；非连续全片验收。
- SHA256：`32384732eb314b5b13efe24d1905eb39f56f2ed0e9696355b7c928b939269475`。

## 03.jpg · Unreal 云上神殿与巨龙

- 角色：reference。
- 来源：https://skillry.dev/ai-videos/kimi-k3-1/kimi-moonshot-068067-1
- [归档原图](../../references/kimi-videos/016-celestial-palace-33.376.jpg)；尺寸 1920×1080。
- 类型：本轮实际观察后截取。
- 机位 / 时间 / 观察范围：浏览器抽看12.65/18.31/33.38秒；已观察原片33.376s原尺寸抽帧。
- SHA256：`59234760c7ba398c0bdba16a2d2b1c927364036a36c19d9b97235509d83ade47`。

## 04.jpg · 水牛露营 · 浮岛

- 角色：counterexample。
- 来源：https://github.com/Zp-Peter/kimi-k31pro-opus55-benchmark-showcase/blob/65e82c53b63f2fdd918617269c057d8e53af2c6f/opus/buffalo/02-camp.html
- [归档原图](../../references/local-collections/counter-buffalo-camp-miniature.jpg)；尺寸 2479×900。
- 类型：本轮实际观察后截取。
- 机位 / 时间 / 观察范围：实际完整首屏；真实作品对照，不是故障图。
- SHA256：`5bd51ef63adc50e1015e85905da2aee224d1775769e13a81220d9e18ab422e6c`。

历史两席FAIL保留于 screening/cards-20261028-b3.csv 与对应目录，本次为重出编辑稿，尚不宣称通过新的双席核卡。旧图未重拍，capture字段保留原观察时间；本轮只重新浏览这些已归档画面。

## 实现来源版本与许可

本轮只读核对，未修改第三方仓或 citadel；尚未新增 cardfx 模块。下面是读源码的固定版本，不意味着所有旧媒体都由该版本实测生成。

- `athenaion`：`9b8bd23b39c458a50fb1201037360047781c45b5`；[固定版本](https://github.com/Leonxlnx/athenaion/tree/9b8bd23b39c458a50fb1201037360047781c45b5)；MIT，Leon Lin 2026。

- citadel 只读版本：`498bb2fb07a78754f8cd6df113d720f220546a8c`。README 的具体路径与行已读；这是可复用代码索引，不是移植完成声明。

## 已读实现的永久行链接

- [`Repos/athenaion/src/modules/statues.js:197-269`](https://github.com/Leonxlnx/athenaion/blob/9b8bd23b39c458a50fb1201037360047781c45b5/src/modules/statues.js#L197-L269)
- [`Repos/athenaion/src/world/shots.js:24-42`](https://github.com/Leonxlnx/athenaion/blob/9b8bd23b39c458a50fb1201037360047781c45b5/src/world/shots.js#L24-L42)
