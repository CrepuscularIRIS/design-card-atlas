# Kimi 187 视频视觉筛选

依据 `docs/VISUAL_CARD_PROMPT.md` v3。CSV逐项保留原作品URL与直接播放URL。现分为 `kimi-videos-001-100.csv`（本工作者）与 `kimi-videos-101-187.csv`（rendering工作者）；index为1-based，与videos.json的0-based位置相差1。

## 粗筛

187条：3D 56、互动30、动效26、对比75。明确非视觉0条。全部进入实际看片队列，不能按标题代替视觉质量裁决。

两份CSV最终目录快照：**187条均有实际画面抽样裁决，8收 / 179不收 / 0待看 / 0打不开**。前100条本工作者完成100条抽样（7收/93不收）；后87条由rendering完成（1收/86不收），以对应CSV为准。前段入选引用7张原尺寸帧（022复用其他工作者同作品原帧；090仅玻璃材质辅助参考），本目录新增6张。**全量逐条抽样已完成，不等于连续看完全部视频**；每条实际时间点和范围在CSV，未验证音轨、模型生成归因或运行复现。

## 早期工具阻塞（历史记录，当前已恢复）

- Chrome创建MP4独立标签页两次，均在导航前返回 `Unable to load browser request-header policy. Retry the browser command.`。
- `cua.getState()`仅发现Chrome id=1，且同样无法列标签页。
- 重置当前cua内核、改开skillry作品页面，仍同一错误。
- 主任务提供其可用Chrome id=3；本子任务 `getBrowser({id:"3"})` 和 `createBrowserTab("3",...)` 都立即返回 `Browser is not available: 3`。
- 主任务与本子任务可见浏览器surface不同。未操作其他标签、未改全局viewport，也未通过其他技术绕过浏览器要求。

## 数据来源与去重

- README 5–13行说明合集范围、187视频与4类；README的具体条目行号逐项写入CSV。README仅提供来源声明，不代替本轮播放验证。
- 每条均保存 `watch_page_url`（Skillry作品播放页）、`source_url`（X原作者帖子）、`playable_url`（合集公开列出的MP4）；这是初始目录状态。实际观看进度见本文顶部与两份CSV；仅对已观察且入选的视频使用pageAssets/bundle保存原片并抽已看时间点，详见SOURCE。全部条目的观看裁决见两份CSV；X原帖未逐页验证，不把目录中链接存在等同于原帖已读取。
- ID、MP4 URL、mediaId、sourceSha256和Skillry页面各187个唯一值；X原帖173个。6个原帖组承载多个不同视频，不能按sourceUrl去重删掉。
  - https://x.com/Kmno4Z62942/status/2113671744011763942：2条独立媒体，序号 10, 11。
  - https://x.com/Kimi_Moonshot/status/2113680701770068067：8条独立媒体，序号 16, 17, 18, 19, 20, 21, 22, 23。
  - https://x.com/atomtanstudio/status/2113714196089287073：2条独立媒体，序号 73, 74。
  - https://x.com/atomtanstudio/status/2113730984965439743：2条独立媒体，序号 109, 110。
  - https://x.com/zstmfhy/status/2113804589174862231：2条独立媒体，序号 149, 150。
  - https://x.com/10xmylife/status/2113892200744653089：4条独立媒体，序号 177, 178, 179, 180。
- 元数据总时长约99.1分钟；119条原片长边≥1920，68条低于门槛。横向宽≥1920且宽≥高共110条。拆分对比画面后单个作品分辨率可能更低，不能只用整条视频尺寸判高清。
- `MEDIA-RIGHTS.md`全文已读：视频、音乐、品牌、模型和提示词仍归各权利人，MIT仅覆盖合集原创工具/整理结构。公开列出不等于商业复用许可。

## 最相关且原始长边≥1920：优先看片31项

仅标题/题材相关性与元数据分辨率筛选，不是视觉判断、不是入选。

| 序号 | 作品 | 原始尺寸 | 秒数 | 播放页 | 原作者 | MP4 |
|---:|---|---|---:|---|---|---|
| 14 | 天空中的宝塔浮岛 | 2560×1440 | 47.08 | [观看页](https://skillry.dev/ai-videos/kimi-k3-1/itsmeajaykv-476408) | [source](https://x.com/ItsmeAjayKV/status/2113680041712476408) | [MP4](https://media.skillry.dev/kimi-k3-1/2113680041712476408/2113679890432372736.1bd529cae97e.mp4) |
| 16 | Unreal 云上神殿与巨龙 | 1920×1080 | 40.90 | [观看页](https://skillry.dev/ai-videos/kimi-k3-1/kimi-moonshot-068067-1) | [source](https://x.com/Kimi_Moonshot/status/2113680701770068067) | [MP4](https://media.skillry.dev/kimi-k3-1/2113680701770068067-1/celestial-palace.4c4aaddcefbf.mp4) |
| 17 | 御剑飞越云海 RPG | 1920×1080 | 15.84 | [观看页](https://skillry.dev/ai-videos/kimi-k3-1/kimi-moonshot-068067-2) | [source](https://x.com/Kimi_Moonshot/status/2113680701770068067) | [MP4](https://media.skillry.dev/kimi-k3-1/2113680701770068067-2/sword-flight.6629872b9f45.mp4) |
| 19 | Blender 机场室内雨林 | 1920×1080 | 19.50 | [观看页](https://skillry.dev/ai-videos/kimi-k3-1/kimi-moonshot-068067-4) | [source](https://x.com/Kimi_Moonshot/status/2113680701770068067) | [MP4](https://media.skillry.dev/kimi-k3-1/2113680701770068067-4/airport-rainforest.2de609d595b9.mp4) |
| 22 | 科隆大教堂内景构建动画 | 1920×1080 | 19.12 | [观看页](https://skillry.dev/ai-videos/kimi-k3-1/kimi-moonshot-068067-7) | [source](https://x.com/Kimi_Moonshot/status/2113680701770068067) | [MP4](https://media.skillry.dev/kimi-k3-1/2113680701770068067-7/cologne-interior.15db0edc4a38.mp4) |
| 23 | 末日机器人短片 | 1920×1080 | 14.04 | [观看页](https://skillry.dev/ai-videos/kimi-k3-1/kimi-moonshot-068067-8) | [source](https://x.com/Kimi_Moonshot/status/2113680701770068067) | [MP4](https://media.skillry.dev/kimi-k3-1/2113680701770068067-8/robot-film.b148c45cfee4.mp4) |
| 32 | Corsair 海盗船 | 1920×1080 | 20.00 | [观看页](https://skillry.dev/ai-videos/kimi-k3-1/dan-zh18-470924) | [source](https://x.com/dan_zh18/status/2113687336093470924) | [MP4](https://media.skillry.dev/kimi-k3-1/2113687336093470924/2113687076751224832.8b232bc3f345.mp4) |
| 43 | 高精度 3D 战舰 | 1920×1080 | 24.53 | [观看页](https://skillry.dev/ai-videos/kimi-k3-1/notjazii-952826) | [source](https://x.com/notjazii/status/2113697560103952826) | [MP4](https://media.skillry.dev/kimi-k3-1/2113697560103952826/2113697522371936257.487fbad99bcc.mp4) |
| 57 | 28 分钟建成的城堡 | 1920×1080 | 57.30 | [观看页](https://skillry.dev/ai-videos/kimi-k3-1/doe-naps-536156) | [source](https://x.com/doe_naps/status/2113705794554536156) | [MP4](https://media.skillry.dev/kimi-k3-1/2113705794554536156/2113705240801529856.c7744f00a0c2.mp4) |
| 59 | 中式幻想 RPG | 1920×1080 | 12.49 | [观看页](https://skillry.dev/ai-videos/kimi-k3-1/crangerus-549203) | [source](https://x.com/crangerus/status/2113706417714549203) | [MP4](https://media.skillry.dev/kimi-k3-1/2113706417714549203/2113704116807421953.8cd71e410ad9.mp4) |
| 63 | 四组太空场景：Kimi 与 Opus 对比 | 1920×1440 | 28.05 | [观看页](https://skillry.dev/ai-videos/kimi-k3-1/hug0-plat-459697) | [source](https://x.com/hug0_plat/status/2113708170132459697) | [MP4](https://media.skillry.dev/kimi-k3-1/2113708170132459697/2113707264078995456.3313fe54fa59.mp4) |
| 84 | 黑客帝国风宝塔 | 1920×1080 | 30.00 | [观看页](https://skillry.dev/ai-videos/kimi-k3-1/ivanfioravanti-507206) | [source](https://x.com/ivanfioravanti/status/2113721778128507206) | [MP4](https://media.skillry.dev/kimi-k3-1/2113721778128507206/2113721265584267264.b44b3f8c9ea2.mp4) |
| 89 | 悬浮 3D 空间站 | 1920×1080 | 33.90 | [观看页](https://skillry.dev/ai-videos/kimi-k3-1/haleeeemahh-732335) | [source](https://x.com/Haleeeemahh/status/2113723899074732335) | [MP4](https://media.skillry.dev/kimi-k3-1/2113723899074732335/2113723479254024192.06d7f8a0cf17.mp4) |
| 90 | 纯程序化 Three.js 着色器场景 | 1920×1080 | 22.34 | [观看页](https://skillry.dev/ai-videos/kimi-k3-1/liambraus-194589) | [source](https://x.com/liambraus/status/2113724051332194589) | [MP4](https://media.skillry.dev/kimi-k3-1/2113724051332194589/2113723996214611968.5ef8504a45d7.mp4) |
| 112 | 纳布之战 | 1920×1080 | 20.00 | [观看页](https://skillry.dev/ai-videos/kimi-k3-1/adityavg13-041507) | [source](https://x.com/adityavg13/status/2113734566947041507) | [MP4](https://media.skillry.dev/kimi-k3-1/2113734566947041507/2113734424097337344.d617ee7a1d8a.mp4) |
| 125 | 雾林光照：Kimi 与 Astra 对比 | 1920×1080 | 25.02 | [观看页](https://skillry.dev/ai-videos/kimi-k3-1/developedbyed-115532) | [source](https://x.com/developedbyed/status/2113752024106115532) | [MP4](https://media.skillry.dev/kimi-k3-1/2113752024106115532/2113751634811469824.0bae1e0c6e7e.mp4) |
| 137 | 体素宝塔宇宙 | 3782×1978 | 60.41 | [观看页](https://skillry.dev/ai-videos/kimi-k3-1/leo114119-847691) | [source](https://x.com/leo114119/status/2113781747208847691) | [MP4](https://media.skillry.dev/kimi-k3-1/2113781747208847691/2113751575957032960.5f3417b9a267.mp4) |
| 138 | 程序化海岸灯塔 | 2560×1440 | 83.09 | [观看页](https://skillry.dev/ai-videos/kimi-k3-1/itsmeajaykv-669347) | [source](https://x.com/ItsmeAjayKV/status/2113785039158669347) | [MP4](https://media.skillry.dev/kimi-k3-1/2113785039158669347/2113757141198950400.57bd5485cfd5.mp4) |
| 139 | 克苏鲁生物水族馆 | 1920×1080 | 56.82 | [观看页](https://skillry.dev/ai-videos/kimi-k3-1/gmi-cloud-735669) | [source](https://x.com/gmi_cloud/status/2113786855619735669) | [MP4](https://media.skillry.dev/kimi-k3-1/2113786855619735669/2113785476868091904.014e0478cc59.mp4) |
| 141 | 鹈鹕海上夜航 | 1920×1080 | 27.46 | [观看页](https://skillry.dev/ai-videos/kimi-k3-1/finiyang-372172) | [source](https://x.com/FiniYang/status/2113791833822372172) | [MP4](https://media.skillry.dev/kimi-k3-1/2113791833822372172/2113732266711191553.43d2fa898024.mp4) |
| 157 | 池塘生态横截面 | 1920×1080 | 30.00 | [观看页](https://skillry.dev/ai-videos/kimi-k3-1/loktar00-291602) | [source](https://x.com/loktar00/status/2113825664902291602) | [MP4](https://media.skillry.dev/kimi-k3-1/2113825664902291602/2113825253944102912.15252b1b7b27.mp4) |
| 158 | 阶梯生态建筑与玻璃穹顶 | 3826×1776 | 32.92 | [观看页](https://skillry.dev/ai-videos/kimi-k3-1/shafreeck-740244) | [source](https://x.com/shafreeck/status/2113844146754740244) | [MP4](https://media.skillry.dev/kimi-k3-1/2113844146754740244/2113840461345665024.763f4ec49a2c.mp4) |
| 159 | 冰川湖与浮冰 | 1920×1080 | 30.13 | [观看页](https://skillry.dev/ai-videos/kimi-k3-1/quimedesu-185485) | [source](https://x.com/quimedesu/status/2113849430441185485) | [MP4](https://media.skillry.dev/kimi-k3-1/2113849430441185485/2113849318004137984.9b8af9a96f76.mp4) |
| 162 | 红砂尖塔上空的热气球 | 1920×1080 | 30.13 | [观看页](https://skillry.dev/ai-videos/kimi-k3-1/quimedesu-453994) | [source](https://x.com/quimedesu/status/2113851074163453994) | [MP4](https://media.skillry.dev/kimi-k3-1/2113851074163453994/2113850966353043456.0161a61c781b.mp4) |
| 163 | 暴雨中的大西洋灯塔 | 1920×1080 | 30.13 | [观看页](https://skillry.dev/ai-videos/kimi-k3-1/quimedesu-849997) | [source](https://x.com/quimedesu/status/2113851797479849997) | [MP4](https://media.skillry.dev/kimi-k3-1/2113851797479849997/2113851654005047296.c01e3d6d7a53.mp4) |
| 164 | 樱花宝塔昼夜场景 | 2532×1212 | 19.62 | [观看页](https://skillry.dev/ai-videos/kimi-k3-1/ciruai-677109) | [source](https://x.com/ciruai/status/2113854163163677109) | [MP4](https://media.skillry.dev/kimi-k3-1/2113854163163677109/2113853884338728960.4a5315271e30.mp4) |
| 166 | 绿色未来城市飞行镜头 | 1920×1080 | 30.13 | [观看页](https://skillry.dev/ai-videos/kimi-k3-1/quimedesu-427797) | [source](https://x.com/quimedesu/status/2113858314899427797) | [MP4](https://media.skillry.dev/kimi-k3-1/2113858314899427797/2113858024393646080.32be547762a3.mp4) |
| 175 | 冰海峡湾无线电小屋 | 2828×1846 | 19.27 | [观看页](https://skillry.dev/ai-videos/kimi-k3-1/thebuggeddev-444329) | [source](https://x.com/thebuggeddev/status/2113889721185444329) | [MP4](https://media.skillry.dev/kimi-k3-1/2113889721185444329/2113889520164966400.c31f53b1c8f1.mp4) |
| 176 | StillWild 程序化草地漫游 | 3840×2100 | 87.51 | [观看页](https://skillry.dev/ai-videos/kimi-k3-1/ivanfioravanti-825112) | [source](https://x.com/ivanfioravanti/status/2113890712097825112) | [MP4](https://media.skillry.dev/kimi-k3-1/2113890712097825112/2113890197939085312.848217fc1eb5.mp4) |
| 178 | 像素空中城堡：四模型对比 | 1920×1200 | 15.07 | [观看页](https://skillry.dev/ai-videos/kimi-k3-1/10xmylife-653089-2) | [source](https://x.com/10xmylife/status/2113892200744653089) | [MP4](https://media.skillry.dev/kimi-k3-1/2113892200744653089-2/2113882906200571904.b22109f2afa1.mp4) |
| 182 | 环形行星与浮岛生成器 | 2940×1664 | 49.27 | [观看页](https://skillry.dev/ai-videos/kimi-k3-1/anxin-37-899753) | [source](https://x.com/AnXin_37/status/2113906644291899753) | [MP4](https://media.skillry.dev/kimi-k3-1/2113906644291899753/2113903937107685376.355151496410.mp4) |

### 题材相关但原片较小

37 黑洞：Kimi 与 Opus 对比（1280×1620）, 45 古城遗迹与河谷（960×388）, 54 雨夜便利店（1440×1080）, 58 黑曜巨龙 3D 交互网页（860×1080）, 71 黄金时刻纽约飞越：Kimi 与 Opus 对比（1280×1264）, 115 夕阳下的帆船（1886×1080）, 135 云上漂浮城堡：Kimi 与 Opus 对比（1088×1440）, 144 暴风雨海面：Kimi 与 Gemini 对比（1284×672）, 151 暴风雨灯塔：Kimi、Opus 与 Astra 对比（1080×1080）, 167 荧光幽灵船：Kimi 与 Astra 对比（1280×1620）, 169 湖畔童话城堡（1280×720）, 172 云海浮空宝塔（1432×788）。现已抽样裁决，具体见CSV；这份初始题材清单不代表入选。可寻找原作更高质量入口，不能把低清原片放大后冒充高清。

## 现有场景对照：初期题材建议，未作为实施验证

已读真实注册表 `citadel/src/game/places.js` 和 `placeBatches/index.js`。`places.js:458`调用applyBatches，故不能把基础表中的queued误当最终关闭；b4/b5/b6/b7会开放海滩、船舱、水族馆和宅邸。以下只是看完后可评估的迁移落点。这里的注册表映射仍为题材建议；已看片条目的实际构图/配色/光照/材质分析另在CSV，不把题材映射当验证。

| 候选序号 | 现有场景 | 迁移假设 | 注册表证据 |
|---|---|---|---|
| 14, 16, 17, 31, 41, 59, 84, 118, 129, 135, 137, 164, 172, 178, 182 | shrine-1 / Shrine | 若看片后建筑轮廓和云雾层级合格，可研究神社远景、灯笼与高低台阶的东方空间语言；浮岛/巨龙不直接植入现有剧情。 | citadel/src/game/places.js:407-421 |
| 22, 26, 45, 57, 122, 128, 169 | haunted-mansion-1 / HauntedMansionHall | 若看片确认柱列和纵深有力，可借轴线、拱/柱节律与高窗方向光；不把现有宅邸硬改为同一历史建筑。 | citadel/src/game/placeBatches/b7-haunted.js:43-53 |
| 19, 46, 158, 166 | company-entrance / CompanyEntrance | 可看片研究大型入口的层级、天光与植栽尺度，作为现有大厅构图候选；未判断是否适配当前空间尺寸。 | citadel/src/game/places.js:58-74 |
| 32, 43, 80, 100, 115, 124, 138, 141, 144, 151, 159, 162, 163, 167, 175 | beach-1 / Beach；goodboat-room-1 / GoodboatRoom | 海面/岸线题材可先看波面明暗、远处地标与天气；船舱只考虑窗外海景和光色，不移入军舰/海盗剧情。 | citadel/src/game/placeBatches/b4-outdoor.js:75-106；citadel/src/game/placeBatches/b5-boat.js:64-73 |
| 66, 139, 157 | black-city-2 / BlackCityAquarium | 若水下层次和生物剪影可读，可借大缸纵深、冷水光与主体尺度参照；不直接替换既有巨型生物。 | citadel/src/game/placeBatches/b6-blackcity.js:48-56 |
| 33, 52, 71, 82, 87, 116, 131 | street-1 / StreetDay・StreetNight | 先看街道/天际线的构图与昼夜分区，再决定能否借到现有街道；题材相似不代表已入选。 | citadel/src/game/places.js:132-149 |
| 54 | store-1 / Store；alley-1 / Alley1 | 雨夜便利店题材与现有街角店/巷口接近；看片后再判断可借哪一种光源、湿地面和招牌比例。 | citadel/src/game/places.js:265-317 |
| 125, 132, 176 | shrine-1 / Shrine；amusement-park-1 / AmusementPark | 森林/草地题材可探索入口路径的前景植被和空气层次；不把复杂植被当作现有场景必须增加的负担。 | citadel/src/game/places.js:353-369；407-421 |
| 13, 20, 28, 39, 106, 107, 179 | company-office / CompanyOffice；landfill-1 / Landfill | 仅候选机械表面/构件尺度研究，若视频全是产品转台而缺空间冲击就不收；不建议直接放显卡/发动机当场景。 | citadel/src/game/places.js:80-110；citadel/src/game/placeBatches/b4-outdoor.js:29-47 |
| 171, 185, 186 | car-1 / Car | 仅候选车辆轮廓、金属表面与分件构图研究；交互配置器UI或编辑器画面不能充作场景效果。 | citadel/src/game/places.js:209-225 |

CSV为全部187候选保留映射字段；未列入表的候选明确写“暂无直接映射”，不硬指定场景。Title不动，Atlas后置，hIE仍仅2D；这些建议不构成实施任务。

## 初期阶段交接（历史快照，已被后续实际看片更新）

以下为浏览器恢复前记录，非当前总数：187条待看、0条实际看片、0张截图、0条最终视觉裁决。主任务/可用浏览器agent继续视觉观看；本阶段完成的是目录、去重、播放页与原作链接、分辨率优先序、真实场景注册表的建议性对照。

后续逐条填写viewed_scope、best_time_seconds、decision、reason；入选图片再写至少4维具体画面分析。不能把本阶段标题分类当作四维分析。

原始videos.json SHA256：`04d06ff4f9c43418ad9ea26f58eafe835095c8deaccbff4239f2d537a96bec95`。


## 浏览器恢复后早期增量（历史快照，2026-10-25）
Chrome独立tab409452147已恢复。此前工具不可用记录是历史阶段，不代表作品打不开。当时实际观察1、14、16：收1、不收2；184待看。均记录抽样时刻，未冒充全片连续观看。16已保存1920×1080实际画面。公开页实际流常含`.w1920.mp4`，仅使用页面DOM观察到的URL，不猜改地址。


## 前段最终记录（2026-10-25）

- 前100条完成100条实际画面抽样裁决：7收、93不收。每条保留时间点和具体原因，无标题直接拒收，无工具失败冒充作品失败。
- 046与019成片中央瀑布、列车、穹顶与环花园一致，按同作品转载去重，不计独立参考。
- 041武士园林、052暖光城市飞行、067篝火海岸有局部参考价值，但可用流分别1730×1080、1280×720、1254×720，未放大作为高清主图。067可继续追溯原作者高清版本，其橙色帐篷/火光、蓝色月海、暗岩框景、砂地投影具清楚冷暖层级。
- 029首个0.343秒截图异常显示其他内容，未用于结论；20.342秒稳定播放确认为Loopwick编织村庄。
- 026已在新独立页复核1.878s与5.131s，均为中式园林双屏比较，与“Roman ruin”目录标题不符。仅记录该身份差异，不拿标题替代所见；因半幅玩具式园林不合方向而不收。
- 047、048此前的导航/0×0问题已在新标签恢复，并分别实际看到平面HOMEHOP游戏与低多边形火箭；095初始缓冲也恢复，实际看到40.000s孔板尾帧。均按实际内容裁决，不留假“打不开”。
- 074抽样8.148s与18.427s均是篮球队伍选择UI，记录范围即此；没有声称看到其整段玩法。拒收基于现有内容与本轮题材范围，不保存设置页作为效果图。
- 所有入选引用路径存在；前段100个index唯一且完整，viewed_scope均非空。原媒体/截图权利和哈希见 `public/references/kimi-videos/SOURCE.md`。
