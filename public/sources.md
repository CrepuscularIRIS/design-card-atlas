# 来源与筛选记录

这是视觉卡的来源索引；数量用于核对范围，不代表模型排名或美术质量。每张卡的 SOURCE 保留机位、截图时间、观看范围、原图尺寸和权利信息。

## 阅读边界

- 卡片描述可见画面；数值分别标注目估、原作源码值或Blog试验值。
- 视频抽看片段、独立作者渲染成片、本轮网页运行截图分别记录，不把它们合并成“完整运行验证”。
- 合集条目的收录是候选判断，最终使用还要匹配具体视觉语言。转载和不同时间点不算新的独立作品。
- 本轮目标是3D场景与覆盖其上的UI；2D图解、工具、低清分屏、宣传海报不进入主图。
- 嵌套合集条目只判目录本身，明确记录实际展开的子项，不无限递归声称全看。

## 合集逐条记录

所有原始CSV保留独立代理的原字段；汇总脚本只读，不覆盖观察记录。

| 合集 | 条目 | 收 | 不收 | 打不开 | 尚未收束 | 筛选表 |
|---|---:|---:|---:|---:|---:|---|
| Kimi guide | 83 / 83 | 3 | 80 | 0 | 0 | [kimi-guide.csv](../screening/kimi-guide.csv) |
| Kimi videos | 187 / 187 | 8 | 179 | 0 | 0 | [kimi-videos-001-100.csv](../screening/kimi-videos-001-100.csv) · [kimi-videos-101-187.csv](../screening/kimi-videos-101-187.csv) |
| Kimi / Opus benchmark | 10 / 10 | 2 | 8 | 0 | 0 | [kimi-k31pro-opus55-benchmark-showcase.csv](../screening/kimi-k31pro-opus55-benchmark-showcase.csv) |
| Opus frontend | 91 / 91 | 2 | 87 | 2 | 0 | [awesome-opus5.5-frontend-showcases.csv](../screening/awesome-opus5.5-frontend-showcases.csv) |
| Opus usecases | 663 / 663 | 10 | 627 | 26 | 0 | [opus-usecases-000-170.csv](../screening/opus-usecases-000-170.csv) · [opus-usecases-171-220.csv](../screening/opus-usecases-171-220.csv) · [opus-usecases-221-400.csv](../screening/opus-usecases-221-400.csv) · [opus-usecases-401-441.csv](../screening/opus-usecases-401-441.csv) · [opus-usecases-442-552.csv](../screening/opus-usecases-442-552.csv) · [opus-usecases-553-662.csv](../screening/opus-usecases-553-662.csv) |
| Opus live demos | 3 / 3 | 2 | 1 | 0 | 0 | [opus55-live-demos.csv](../screening/opus55-live-demos.csv) |
| MG styles | 15 / 15 | 1 | 14 | 0 | 0 | [mg-styles-15.csv](../screening/mg-styles-15.csv) |

Opus frontend按当前文件枚举为91个HTML入口，包含导航/重复导出；提示词中的87是原索引口径。各入口都单列，排除原因保留在CSV，未把导航页当新作品。Kimi guide 83条之外的README索引亦已由负责代理核对，没有另列独立遗漏作品。

`尚未收束`包括尚未观看或待具体复核，不能当作“不收”或链接失败。浏览器工具中断与网站实际打不开分开记录；有清楚观察而尺寸不足的作品可以本轮不收，并在理由保留高清再访线索。

## 具名作品与补充入口

### strong-scenes.csv

[完整记录](../screening/strong-scenes.csv)

- **NexusCity** — 不收：实看开场、DAY、VISTA；大量黑面、巨构遮住主体，VISTA穿楼；低帧率迫使LITE，此次结果不代表原作者最佳品质。
- **synthcity** — 收：支持候选，非精选。补看Freeroam+固定5794，摆脱车辆遮挡；收1张密度节奏参考，但青白bloom仍过强，不作配色/首图。
- **TheBrutalizer** — 不收：实看默认楼体、重新生成、屋顶花园与地面公园；灰色方盒和锥形树显出样机感，固定设置面板，未发现足够完整的成片构图。
- **void-syndicate** — 不收：实看首屏与SYSTEM ENTRY/CORE LOGIC；主体是巨幅文字和暗色卡片，3D只露出少量绿色螺旋，不能支持强场景视觉卡。
- **neon-zenith** — 打不开：载入未完成：两次进入在线作品均停LOADING TEXTURES数分钟；WebGPU回退WebGL2，无进场画面。画廊独立图1400×788不满足1920，hero为标题画面不收。
- **The-Monolith** — 打不开：完整体验受权限限制：实际进入SYSTEM READY与白粒子线框待机；页面明确要求麦克风，未授权该权限，因此未进入音频驱动体验，不把待机当成片。
- **Singularity** — 打不开：渲染未完成：实际点BEGIN INVESTIGATION并滚动5%到42%及后续，叙事更新但画面一直为中心星点，未见黑洞，不以源码效果冒充实看。
- **offshore-tower** — 不收：本轮不收。本地无依赖且无公开demo；作者verification单张仅760×900，实看左视图模型完整但不足1920；reference/poster/contact sheet排除。
- **athenaion** — 收：收（作者成片）。已实际启动但生成期间工具连接中断；另逐张看作者9张独立最终render，选6张支持框景/阶梯/尺度/材质，不冒称本轮runtime。
- **invisible-cities-opus-5.5** — 收：支持候选，非精选。实看Atlas、Octavia、Zenobia、昼夜与Journey；3帧仅支持结构/昼夜对照，微缩圆台及紫灰外场占比大，不作为巨构主图。
- **map-of-middle-earth** — 不收：已看，图像尺寸不足。实际播放作者3分47秒电影，采看Hobbiton、山谷要塞、Minas Tirith；有效播放器画幅约1300宽，图库多数1280，未放大充数。

### light-water.csv

[完整记录](../screening/light-water.csv)

- **WebGPU Ocean** — 打不开：浏览器实际显示No WebGPU adapter found；未用README海景补位
- **Sponza体积光** — 不收：本次机位中间调过暗；只留反例
- **Shader与宇宙** — 不收：实际看06透镜/08吸积盘；太阳、金环与水面亮点同时抢焦，留真实视觉反例，不选为主卡正例。
- **江南山谷** — 收：实际看蓝调全景、清晨河边、蓝调山寺；收前两图，山寺保留对照
- **Three GPU pathtracer equirect** — 打不开：本环境实际持续加载，console显示renderer backend未初始化；没有最终画面
- **PathTracing Ocean and Sky** — 不收：新标签复看已成功渲染：灰海波浪、日落到白昼变化、中央Cornell测试盒；可作海面实现参考，但不是成熟场景构图，未选卡图。此前工具中断不是作品失败。
- **Yarn Planet** — 不收：实际看首屏并Begin进入NPC对话；纸底描线卡通小星球，与本轮巨构/电影场景目标不符；未走完整任务
- **小雨云** — 不收：实际白天看到远机位小云/草块/狐狸；R切夜与滚轮近景后画面黑，回日仍黑；未获得符合门槛的完整画面，不评价未看到夜景品质
- **Realism Effects v2 demo** — 打不开：README官方入口实际返回404 DEPLOYMENT_NOT_FOUND；未用README宣传图替代运行结果
- **Bruno Folio2025** — 不收：实际进入开场岛与BRUNO SIMON字牌区，查看控制说明；当前夜景紫蓝饱和灯光/玩具车风格不选本轮主参考；未遍历13区或完整昼夜周期
- **Diorama Day** — 不收：实际Click to play后看浅米色剖面客厅、低多边形家人及四人状态面板；图像明确但属简单微缩生活模拟，不满足本轮巨构冲击门槛
- **Apple Music liquid logo** — 不收：实际播放并定位1.5s/4s；小型液态环到品牌logo的短转场，不是空间/建模场景，保留实现思路不纳入视觉卡

### motion-extra.csv

[完整记录](../screening/motion-extra.csv)

- **r3f-theatrejs-starter** — 不收：已完整加载首屏并向下滚动至 Section 1 / Features；基础形体、编辑器面板及占位内容，缺少独立成片。
- **gsap-threejs-codrops** — 不收：线上索引/详情反复白屏；改用已有本地依赖启动后实际成功。黑白北地探险图像画廊的块状揭示已看到，适合前端转场思路，不是3D强场景成片；只借思路，不复制代码。
- **codrops-depth-gallery** — 不收：实际加载完成并滚动 Golden→Violet→Cobalt；花卉平面在深度方向叠放，适合前端动效参考，不是本轮强3D场景成片。
- **scroll-glitch-hero** — 不收：实看完成的银灰雾山与慢速横条/代码碎片转场；中央巨大 MERIDIAN 字样且山脊重复，主图更像品牌 hero，本轮不硬收。
- **r3f-scroll-rig** — 打不开：README 的 Hello world 示例实际停在 Cloudflare Performing security verification，后续复查仍未进入作品；未进行验证挑战。仓本体是滚动绑定库，不以文档截图替代成片。
- **_libsmoke** — 打不开：使用现有依赖启动后黑屏；页面控制台 TypeError: Cannot read properties of undefined (reading ReactCurrentOwner)，栈位于3018的reconciler/createRenderer。未装依赖或修复。

## 图像档案

- [kimi-videos](references/kimi-videos/SOURCE.md)
- [kimi-videos-tail](references/kimi-videos-tail/SOURCE.md)
- [light-water](references/light-water/SOURCE.md)
- [local-collections](references/local-collections/SOURCE.md)
- [opus-a](references/opus-a/SOURCE.md)
- [opus-a-tail](references/opus-a-tail/SOURCE.md)
- [opus-b](references/opus-b/SOURCE.md)
- [opus-b-tail](references/opus-b-tail/SOURCE.md)
- [opus-c-guide](references/opus-c-guide/SOURCE.md)
- [opus-d](references/opus-d/SOURCE.md)
- [strong-scenes](references/strong-scenes/SOURCE.md)

## 卡片与实际作品

| 卡片 | 独立作品标识 | 选图说明 |
|---|---|---|
| [逆光露轮廓](cards/backlight-reveals-silhouette/README.md) | [清明上河 · 黄昏虹桥](https://silentfleetkk.github.io/qingming-bianjing/opus-5.5/qingming-bianjing.html) · [Unreal 云上神殿与巨龙](https://skillry.dev/ai-videos/kimi-k3-1/kimi-moonshot-068067-1) · [中式幻想 RPG · 雾中巨像](https://skillry.dev/ai-videos/kimi-k3-1/crangerus-549203) · [长风 · 草原风起](https://jbang2004.github.io/long-wind/) | 4帧；4个作品；另有真实视觉对照 |
| [残损仍识原形](cards/broken-form-remains-legible/README.md) | [Ozymandias · 孤立残像](https://www.echohive.ai/posts/ozymandias/animation.html) · [Athenaion · Fallen head](https://github.com/Leonxlnx/athenaion) | 3帧；2个作品；另有真实视觉对照 |
| [焦散落在表面](cards/caustics-on-receivers/README.md) | [Clearwater](https://aureliengmz.github.io/clearwater/) · [Glass goblets · 12s](https://x.com/liambraus/status/2113724051332194589) · [清流 · 浅滩河床](https://seiryu.miraicode.one/) | 4帧；3个作品；另有真实视觉对照 |
| [冷境暖灯](cards/cold-world-warm-refuge/README.md) | [Castle above the clouds](https://x.com/i/status/2113279019005460816) · [末日机器人短片](https://skillry.dev/ai-videos/kimi-k3-1/kimi-moonshot-068067-8) · [江南山谷 · 蓝调全景](https://github.com/holooooo/webgl-seascape-video/blob/915cb7c9a318e03bd2228bc232494b496ff2316c/episodes/04-jiangnan-voxel/interactive.html) | 3帧；3个作品；另有真实视觉对照 |
| [柱廊明暗节奏](cards/colonnade-rhythm/README.md) | [Blender cathedral interior](https://x.com/k1rallik/status/2113693629713633435) · [Athenaion · Temple facade](https://github.com/Leonxlnx/athenaion) · [Unreal 云上神殿与巨龙](https://skillry.dev/ai-videos/kimi-k3-1/kimi-moonshot-068067-1) | 3帧；3个作品；另有真实视觉对照 |
| [巨像越画框](cards/colossus-crosses-the-frame/README.md) | [云上石像](https://skillry.dev/ai-videos/kimi-k3-1/kimi-moonshot-068067-2) · [中式幻想 RPG · 雾中巨像](https://skillry.dev/ai-videos/kimi-k3-1/crangerus-549203) · [Unreal 云上神殿与巨龙](https://skillry.dev/ai-videos/kimi-k3-1/kimi-moonshot-068067-1) | 3帧；3个作品；另有真实视觉对照 |
| [斜向配重](cards/diagonal-mass-balance/README.md) | [Athenaion · Panorama](https://github.com/Leonxlnx/athenaion) · [Unreal 云上神殿与巨龙](https://skillry.dev/ai-videos/kimi-k3-1/kimi-moonshot-068067-1) · [雷尼斯黑沙滩 · 海滩](https://github.com/Zp-Peter/kimi-k31pro-opus55-benchmark-showcase/blob/65e82c53b63f2fdd918617269c057d8e53af2c6f/opus/reynisfjara/index.html) | 3帧；3个作品；另有真实视觉对照 |
| [留空放大孤立物](cards/emptiness-isolates-landmark/README.md) | [Falcon 9 · 暮空尾迹](https://github.com/noahsabaj/falcon9-blender/releases/tag/v1.0) · [Ozymandias · 孤立残像](https://www.echohive.ai/posts/ozymandias/animation.html) · [雷尼斯黑沙滩 · 海滩](https://github.com/Zp-Peter/kimi-k31pro-opus55-benchmark-showcase/blob/65e82c53b63f2fdd918617269c057d8e53af2c6f/opus/reynisfjara/index.html) | 3帧；3个作品；另有真实视觉对照 |
| [雾层分远近](cards/fog-separates-depth/README.md) | [中式幻想 RPG · 雾中巨像](https://skillry.dev/ai-videos/kimi-k3-1/crangerus-549203) · [江南山谷 · 蓝调全景](https://github.com/holooooo/webgl-seascape-video/blob/915cb7c9a318e03bd2228bc232494b496ff2316c/episodes/04-jiangnan-voxel/interactive.html) · [清明上河 · 黄昏全城](https://silentfleetkk.github.io/qingming-bianjing/opus-5.5/qingming-bianjing.html) | 3帧；3个作品；另有真实视觉对照 |
| [近框套远景](cards/framed-distant-view/README.md) | [Athenaion · Ruined portico](https://github.com/Leonxlnx/athenaion) · [中式幻想 RPG · 雾中巨像](https://skillry.dev/ai-videos/kimi-k3-1/crangerus-549203) | 3帧；2个作品；另有真实视觉对照 |
| [金饰点亮哑面](cards/gold-accents-matte-mass/README.md) | [Athenaion · Temple facade](https://github.com/Leonxlnx/athenaion) · [悟空 · 金箍与棍端](https://skillry.dev/ai-videos/kimi-k3-1/oddjolt-160428) | 3帧；2个作品；另有真实视觉对照 |
| [俯瞰读层级](cards/high-view-reads-hierarchy/README.md) | [清明上河 · 黄昏全城](https://silentfleetkk.github.io/qingming-bianjing/opus-5.5/qingming-bianjing.html) · [Athenaion · Panorama](https://github.com/Leonxlnx/athenaion) · [江南山谷 · 蓝调全景](https://github.com/holooooo/webgl-seascape-video/blob/915cb7c9a318e03bd2228bc232494b496ff2316c/episodes/04-jiangnan-voxel/interactive.html) | 3帧；3个作品；另有真实视觉对照 |
| [低彩分灰阶](cards/low-chroma-value-steps/README.md) | [黑沙之境 · 海岸全景](https://github.com/Zp-Peter/kimi-k31pro-opus55-benchmark-showcase/blob/65e82c53b63f2fdd918617269c057d8e53af2c6f/kimi/iceland-black-sand/dist/index.html) · [雷尼斯黑沙滩 · 海滩](https://github.com/Zp-Peter/kimi-k31pro-opus55-benchmark-showcase/blob/65e82c53b63f2fdd918617269c057d8e53af2c6f/opus/reynisfjara/index.html) · [中式幻想 RPG · 雾中巨像](https://skillry.dev/ai-videos/kimi-k3-1/crangerus-549203) | 3帧；3个作品；另有真实视觉对照 |
| [低机位入场](cards/low-eye-entry/README.md) | [Sakura River Valley · 行船](https://valley.mengto.here.now/) · [雾中巨像 · 人舟水路](https://skillry.dev/ai-videos/kimi-k3-1/crangerus-549203) · [Warp Striker · 城市峡谷](https://github.com/OpenVGLab/awesome-opus5.5-frontend-showcases/blob/cac43b250f07b7b86f4709c61effc84269f46494/repro/warp-shooter/index.html) | 3帧；3个作品；另有真实视觉对照 |
| [镜面邻粗面](cards/mirror-beside-roughness/README.md) | [Falcon 9 · 海面降落](https://github.com/noahsabaj/falcon9-blender/releases/tag/v1.0) · [雷尼斯黑沙滩 · 海滩](https://github.com/Zp-Peter/kimi-k31pro-opus55-benchmark-showcase/blob/65e82c53b63f2fdd918617269c057d8e53af2c6f/opus/reynisfjara/index.html) · [Unreal 云上神殿与巨龙](https://skillry.dev/ai-videos/kimi-k3-1/kimi-moonshot-068067-1) | 3帧；3个作品；另有真实视觉对照 |
| [骨架规整草木野](cards/ordered-frame-wild-growth/README.md) | [Blender 机场室内雨林](https://skillry.dev/ai-videos/kimi-k3-1/kimi-moonshot-068067-4) · [Athenaion · 水庭](https://github.com/Leonxlnx/athenaion) | 3帧；2个作品；另有真实视觉对照 |
| [河道串景](cards/river-leads-the-eye/README.md) | [Poseidia · Sea Canal](https://poseidia.vercel.app/) · [清明上河 · 黄昏全城](https://silentfleetkk.github.io/qingming-bianjing/opus-5.5/qingming-bianjing.html) · [Sakura River Valley](https://valley.mengto.here.now/) · [江南山谷 · 清晨河岸](https://github.com/holooooo/webgl-seascape-video/blob/915cb7c9a318e03bd2228bc232494b496ff2316c/episodes/04-jiangnan-voxel/interactive.html) | 4帧；4个作品；另有真实视觉对照 |
| [熟悉物标定巨构](cards/scale-by-familiar-objects/README.md) | [Unreal 云上神殿与巨龙](https://skillry.dev/ai-videos/kimi-k3-1/kimi-moonshot-068067-1) · [Athenaion · Panorama](https://github.com/Leonxlnx/athenaion) · [Blender 机场室内雨林](https://skillry.dev/ai-videos/kimi-k3-1/kimi-moonshot-068067-4) | 3帧；3个作品；另有真实视觉对照 |
| [侧光刻石](cards/side-light-carves-stone/README.md) | [Athenaion · Fallen head](https://github.com/Leonxlnx/athenaion) · [Blender cathedral interior](https://x.com/k1rallik/status/2113693629713633435) | 3帧；2个作品；另有真实视觉对照 |
| [分级机位靠近](cards/staged-camera-approach/README.md) | [雷尼斯黑沙滩 · 海滩](https://github.com/Zp-Peter/kimi-k31pro-opus55-benchmark-showcase/blob/65e82c53b63f2fdd918617269c057d8e53af2c6f/opus/reynisfjara/index.html) · [黑沙之境 · 海岸全景](https://github.com/Zp-Peter/kimi-k31pro-opus55-benchmark-showcase/blob/65e82c53b63f2fdd918617269c057d8e53af2c6f/kimi/iceland-black-sand/dist/index.html) | 3帧；2个作品；另有真实视觉对照 |
| [阶台托举主殿](cards/terraces-carry-the-temple/README.md) | [Athenaion · 水庭](https://github.com/Leonxlnx/athenaion) | 3帧；1个作品；另有真实视觉对照 |
| [HUD细线叠层](cards/thin-line-hud/README.md) | [KESTREL-9 · 扫描](https://vincentwei1021.github.io/mg-styles-15/#22-hud) · [Warp Striker · 城市峡谷](https://github.com/OpenVGLab/awesome-opus5.5-frontend-showcases/blob/cac43b250f07b7b86f4709c61effc84269f46494/repro/warp-shooter/index.html) | 3帧；2个作品；另有真实视觉对照 |
| [巨字随景退场](cards/type-yields-to-scene/README.md) | [黑沙之境 · 海岸全景](https://github.com/Zp-Peter/kimi-k31pro-opus55-benchmark-showcase/blob/65e82c53b63f2fdd918617269c057d8e53af2c6f/kimi/iceland-black-sand/dist/index.html) · [雷尼斯黑沙滩 · 海滩](https://github.com/Zp-Peter/kimi-k31pro-opus55-benchmark-showcase/blob/65e82c53b63f2fdd918617269c057d8e53af2c6f/opus/reynisfjara/index.html) | 3帧；2个作品；另有真实视觉对照 |
| [水面续轮廓](cards/water-continues-silhouette/README.md) | [江南山谷 · 清晨河岸](https://github.com/holooooo/webgl-seascape-video/blob/915cb7c9a318e03bd2228bc232494b496ff2316c/episodes/04-jiangnan-voxel/interactive.html) · [清明上河 · 雨中虹桥](https://silentfleetkk.github.io/qingming-bianjing/opus-5.5/qingming-bianjing.html) · [Falcon 9 · 海面降落](https://github.com/noahsabaj/falcon9-blender/releases/tag/v1.0) | 3帧；3个作品；另有真实视觉对照 |
| [风化依附形体](cards/weathering-follows-form/README.md) | [Athenaion · Grand staircase](https://github.com/Leonxlnx/athenaion) | 3帧；1个作品；另有真实视觉对照 |

## 编辑取舍

[独立审图](../screening/visual-editorial-review.md)与[修订记录](../screening/visual-editorial-resolution.md)记录图片是否真正支持卡的判断。原始审查保留当时版本的问题，修订记录说明最终处理。

[暖石冷影候选](candidates/warm-stone-cool-shadow/README.md)目前只有一张足够明确的正例，不进入Reel。不能用不同物体的环境分色替代同一石面暖冷关系，也不以相邻视频帧凑图。候选可以为配方提供单帧视点参考，但不算已完成视觉语言。

## Git 与模型归因

Pro原答复的14个明确作品已有本地Git；[旧阶段逐项对照](../docs/SOURCE_AUDIT.md)保留原答复行号、origin与HEAD。[本次重新读取的Git记录](pro-git-recheck.json)只核克隆存在和版本，不认证模型贡献或发布先后。

本轮新增的可追溯源码记录在 [new-source-clones.json](new-source-clones.json)：qingming-bianjing、clearwater、falcon9-blender已克隆；cybercity与ProceduralBuildingsThreeJS取得固定HEAD与源码检出，大体积媒体/模型未完整检出，不能称为完整资产归档。没有公开源码链接的网页或视频仍只记视觉出处；不把视频条数等同已取得的Git仓数量。原有参考仓保持原文件，不修改其实现。

Opus、Kimi、Sonnet、DeepSeek等归因保留作者/发布者自述；混合制作也可参考。不把仓库标题、宣传句或单帧画质当作某模型独立完成的证明。

## 权利与工程旧版

截图与视频帧保留原作者/素材权利人的权利，本库文档许可不覆盖第三方媒体；有明确许可者单独注明。`lygia`、`gsap-threejs-codrops`、`opus55-live-demos`只借思路，不粘贴代码。

旧257张机制卡和旧网页只作工程背景，旧入口移入 [archive/engineering-v1](../archive/engineering-v1/)。新交付为Markdown README、卡片、图片和配方。本仓库已公开（2026-10-25）。
