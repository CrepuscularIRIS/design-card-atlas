# Opus C / Kimi Guide：v3 逐条筛选交付

日期：2026-10-25。完整读取 `docs/VISUAL_CARD_PROMPT.md` v3；仅做视觉实看、筛选和来源记录，未开发前端、运行参考源码或安装依赖。

## 最终覆盖

| 清单 | 数量 | 浏览器实际观察页面或视频 | 明确非视觉元信息排除 | 收 | 不收 | 打不开 | 待看 |
|---|---:|---:|---:|---:|---:|---:|---:|
| Opus 零基 442–552 | 111 | 103 | 8 | 1 | 108 | 2 | 0 |
| Kimi Guide cases 1–83 | 83 | 77 | 6 | 3 | 80 | 0 | 0 |

“浏览器观察”包括实际原帖、README、运行页错误和成片，不表示每条都看到运行成品。逐条 `reason` 区分范围。所有行已处理。七项高清/输出缺口本轮判不收并保留再访说明；Emberwick 运行环境阻碍判打不开，不意味着网站永久失效。无未处理待看。

Opus 原责任段 442–662 已拆分：本 worker 最终只维护 `opus-usecases-442-552.csv`。553–662 由 scene_design 的 `opus-usecases-553-662.csv` 独立维护，不计入上述统计。后者的已观察交接包括 561、638、648、658；没有合并后覆盖他人的文件。

## 合格来源图片

4 件作品、5 张原生尺寸 JPEG，均已人工实看；未插值放大。逐张复现、时间点、尺寸、SHA256、版权边界和至少四维位置/比例估测见 `public/references/opus-c-guide/SOURCE.md`。

- Kimi 17 云上城堡：1920×1080 浏览器截图，26.58 秒附近。冷蓝雾海、暖窗和倒锥浮岛；对应 title 右下建筑 / atlas 远景雾层。
- Kimi 56 彩色玻璃杯：原片 12s、21s 各一张，1920×1080。折射层次与冷背景暖杯足；对应 Shrine 器物 / Platform 展示道具。
- Kimi 63 教堂内景：原片 18s，1920×1080。柱列透视、左侧窗光与远端小焦点；对应 BlackCityHall / Shrine 中轴入口。
- Opus 499 Bay Ride：实际运行页 2494×905。斜栈桥、金蓝海面、描边人物与柔软水面；对应 Beach 近岸动线。亲密滨海尺度，不称巨构；保留底部小型登船提示。

所有模型归属均为作者/整理者自述。截图证明所观察时刻的画面，视频证明录屏内容；没有因此证明生成过程、完整交互、物理正确性或迁移效果。媒体权利归原作者，合集代码许可不覆盖外部媒体。本轮仅本地设计研究引用，没有发布许可或商用授权。

## 八项本轮未收录候选与再访入口

| Opus index | 项目 | 已看到 | 缺口 |
|---|---|---|---|
| 445 | SILO in 60 seconds | 中央螺旋楼梯、人物剪影、仓库片段 | 当前竖幅约607×1080；需原生长边≥1920的主画面 |
| 446 | LATENT | 2:00后洞窟星点、黑水、文字与双螺旋 | DOM原片1920×1080，当前显示约1272×532；documented downloadMedia两轮超时，未保存合规原帧。不是作品打不开 |
| 472 | Yugong Moves the Mountains | 月夜小屋暖火与山/人剪影 | 当前480×270流，需高清原片 |
| 495 | IRONLINE | README工业FPS截图，低太阳/烟柱/电塔 | 图1600×900；未有已打开在线场景，不执行源码 |
| 501 | Emberwick | 实际启动页与错误信息 | 浏览器提示 no compatible GPU adapter，无场景；环境缺口，不是网站失效 |
| 503 | Iron Citadel | Opus Web Entry Hall：棕石板、吊灯、暗柱、火炬 | 当前960×600；页面全屏触发Unity pointer-lock WrongDocumentError。其他房间和高清未验证 |
| 513 | Haiku vs Opus Turkish | GitHub README与HTML文件列表 | 无已看到的在线场景/图像；本轮不收：缺视觉，不以源码描述代替观看 |
| 520 | Victoria Falls Bridge | 夜桥钢架、峡谷植被片段 | 480×270流且原帖夹模型对话图；需高清成片再裁决 |

Kimi 54 东方河城的黄昏层次有参考潜力，但原片上下白模/成片叠放，整体1280×1440、单幅约1280×720；本轮不收，不放大凑1920。原帖声明下游视频模型参与，未归为纯Kimi渲染。

Opus 531 已实际进入 Sandscape 的 Proving Grounds 赛道，不以美化封面作效果图；其他四张锁定地图没有观看，当前默认赛道未进入精选。

## README 额外独立作品核查

Kimi README 1314 行，Case 标题 1–83 与 JSON 的83条对应，无额外独立编号作品。原帖补充链接保留在各 case，不冒充新主作品。未递归展开作者账号或外部合集：

- https://evolink.ai?utm_source=github&utm_medium=banner&utm_campaign=kimi-k3-1-usecases&utm_content=readme_banner
- https://github.com/Evolink-AI/awesome-kimi-k3-usecases
- https://github.com/cheercheung/awesome-gemini-4-carbon-guide-and-use-cases
- https://www.kimi.com/
- https://x.com/xueyu1125

## 工具与验证边界

早期浏览器连接故障、Debugger detached 与 downloadMedia 超时都保留为工具/获取限制，未映射成作品404。遵照根任务协调停止 viewport/reset 后，以独立 tab 继续实际观察。最终“打不开”包括 Opus 451 的 Deployment Paused 页面与 501 的无可用 GPU 适配器运行阻碍。CSV行号连续性、唯一ID、194条非空原因及5张图片尺寸/hash已经核对；这是台账/资产完整性检查，不是参考软件运行测试。
