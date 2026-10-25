# 来源盘点与 Pro 建议核对

审计日期：2026-10-25。原研究 **86 条来源记录**全部核对当前本地目录，其中 **84 个独立 Git 仓**、**2 个非 Git 本地条目**；84 个浅克隆。没有克隆、fetch、运行参考项目或发布。

**Pro 原答复明确提到的 14 个作品全部已实际 Git 克隆**：10 主推荐、2 补充观察候选、2 因模型归因降级的作品。完整原答复逐项读取后，结果与旧 expected=14 清单恰好一致；不是以该清单证明完整。两个观察候选与两个降级项均独立列出。

[机器可读盘点](../data/editorial/sources-audit.json)保存全部 origin、完整 HEAD、是否浅克隆、类别、许可范围与证据路径。

## Pro 作品逐项核对

| 原作品 | 本地仓 | Pro 原等级 | 当前 HEAD | Git / origin |
|---|---|---|---|---|
| Apple Music, Made by Code | apple-music-effect | 主推荐 | `e31a67602ea0` | 存在 / 与原链接匹配 |
| Yarn Planet | yarn-planet | 主推荐 | `5c8acce8df04` | 存在 / 与原链接匹配 |
| Athenaion | athenaion | 主推荐 | `9b8bd23b39c4` | 存在 / 与原链接匹配 |
| web-ocean | web-ocean | 主推荐 | `a07c7fd522ef` | 存在 / 与原链接匹配 |
| Invisible Cities — an atlas | invisible-cities-opus-5.5 | 主推荐 | `3c2d0cc6657d` | 存在 / 与原链接匹配 |
| Map of Middle-Earth / Journey Through Middle-Earth | map-of-middle-earth | 主推荐 | `696e968e9d55` | 存在 / 与原链接匹配 |
| ISOPOLIS — Let the City Grow | mg-styles-15 | 主推荐 | `49052d80bfaf` | 存在 / 与原链接匹配 |
| Induction Bench | electromagnetism | 主推荐 | `820835eb3d42` | 存在 / 与原链接匹配 |
| Dopa Drill | dopa-drill | 主推荐 | `e4da063f74c4` | 存在 / 与原链接匹配 |
| 冰岛黑沙滩 / Reynisfjara 双模型同题 | kimi-k31pro-opus55-benchmark-showcase | 主推荐 | `65e82c53b63f` | 存在 / 与原链接匹配 |
| Offshore Observation Tower | offshore-tower | 补充观察候选 | `3a67f5ea7aec` | 存在 / 与原链接匹配 |
| Diorama Day | csc35-diorama-day | 补充观察候选 | `aa88c6276e2d` | 存在 / 与原链接匹配 |
| scroll-glitch-hero | scroll-glitch-hero | 模型归因降级 | `6e0b8e6189dc` | 存在 / 与原链接匹配 |
| webgl-seascape-video | webgl-seascape-video | 模型归因降级 | `915cb7c9a318` | 存在 / 与原链接匹配 |

ISOPOLIS 只对应 mg-styles-15 的一个具体短片；本地克隆的是含15片的整仓，审读另扩至15片。冰岛黑沙滩是同仓两个模型目录的同题作品，计一项建议、一个Git。OpenVGLab 同名合集仅是排重上下文，不应额外计为第15个作品。原请求写错的 owner 不用于覆盖实际 origin。

Pro 的模型、日期、质量描述是研究来源，不能当本轮执行认证。用户已明确模型归因不是收录门槛，故两项降级作品均保留，原Pro等级仍存档。

## 86 条来源的 Git 与分类

| 来源 | 类别 | Git | 浅克隆 | HEAD | origin |
|---|---|---|---|---|---|
| 3DTilesRendererJS | library | 是 | 是 | `eb6ea84c74fa` | https://github.com/NASA-AMMOS/3DTilesRendererJS.git |
| 3dcitydb-web-map | implementation | 是 | 是 | `2e779d9e8a5b` | https://github.com/3dcitydb/3dcitydb-web-map.git |
| ChatdollKit | library | 是 | 是 | `e694f443247e` | https://github.com/uezo/ChatdollKit.git |
| Gaussian-Splat-Lite | tool | 是 | 是 | `581864925d74` | https://github.com/WilliamLiu-1997/Gaussian-Splat-Lite.git |
| NexusCity | implementation | 是 | 是 | `bc3373739617` | https://github.com/vineetsharma96/NexusCity.git |
| Open-LLM-VTuber | implementation | 是 | 是 | `992309c0aa19` | https://github.com/Open-LLM-VTuber/Open-LLM-VTuber.git |
| OpenRoom | implementation | 是 | 是 | `02468154c4d9` | https://github.com/MiniMax-AI/OpenRoom.git |
| SillyTavern | implementation | 是 | 是 | `06bde939fb1e` | https://github.com/SillyTavern/SillyTavern.git |
| Singularity | implementation | 是 | 是 | `363c12d0e092` | https://github.com/broskell/Singularity.git |
| THREE.js-PathTracing-Renderer | library | 是 | 是 | `f8ded116a3c6` | https://github.com/erichlof/THREE.js-PathTracing-Renderer.git |
| The-Monolith | implementation | 是 | 是 | `f931b85ada56` | https://github.com/val00813/The-Monolith.git |
| TheBrutalizer | implementation | 是 | 是 | `ec8708101d5d` | https://github.com/KrishGaur1354/TheBrutalizer.git |
| TrendRadar | implementation | 是 | 是 | `792bcc3928b1` | https://github.com/sansan0/TrendRadar |
| _libsmoke | local | 否 | 不适用 | `null` | null |
| ag-ui | library | 是 | 是 | `63ad50838231` | https://github.com/ag-ui-protocol/ag-ui.git |
| ai-town | implementation | 是 | 是 | `8e05997f2409` | https://github.com/a16z-infra/ai-town.git |
| airi | implementation | 是 | 是 | `bc41885f0bfb` | https://github.com/moeru-ai/airi.git |
| amica | implementation | 是 | 是 | `ca2415c77d20` | https://github.com/semperai/amica.git |
| apple-music-effect | implementation | 是 | 是 | `e31a67602ea0` | https://github.com/transitive-bullshit/apple-music-effect.git |
| athenaion | implementation | 是 | 是 | `9b8bd23b39c4` | https://github.com/Leonxlnx/athenaion.git |
| awesome-kimi-k3-1-videos | catalog | 是 | 是 | `286a15bbaa7b` | https://github.com/yihui-dev/awesome-kimi-k3-1-videos.git |
| awesome-kimi-k3.1-guide-and-use-cases | catalog | 是 | 是 | `af01ea7a4bcc` | https://github.com/cheercheung/awesome-kimi-k3.1-guide-and-use-cases.git |
| awesome-opus-5.5-usecase | catalog | 是 | 是 | `0ba0febb2e97` | https://github.com/coolbat/awesome-opus-5.5-usecase.git |
| awesome-opus5.5-frontend-showcases | catalog | 是 | 是 | `cac43b250f07` | https://github.com/OpenVGLab/awesome-opus5.5-frontend-showcases.git |
| codrops-depth-gallery | implementation | 是 | 是 | `28190e0920df` | https://github.com/houmahani/codrops-depth-gallery.git |
| concordia | library | 是 | 是 | `239f0e8275a5` | https://github.com/google-deepmind/concordia.git |
| csc35-diorama-day | implementation | 是 | 是 | `aa88c6276e2d` | https://github.com/agent-marsha/csc35-diorama-day.git |
| daedalOS | implementation | 是 | 是 | `f017b393d417` | https://github.com/DustinBrett/daedalOS.git |
| detect-gpu | library | 是 | 是 | `628b7c0aefbc` | https://github.com/pmndrs/detect-gpu.git |
| dopa-drill | implementation | 是 | 是 | `e4da063f74c4` | https://github.com/grmchn/dopa-drill.git |
| ecctrl | library | 是 | 是 | `e2cab804f9f1` | https://github.com/pmndrs/ecctrl.git |
| electromagnetism | implementation | 是 | 是 | `820835eb3d42` | https://github.com/thebuggeddev/electromagnetism.git |
| excalidraw | implementation | 是 | 是 | `bee01e3a1281` | https://github.com/excalidraw/excalidraw.git |
| folio-2025 | implementation | 是 | 是 | `41046b57eeed` | https://github.com/brunosimon/folio-2025.git |
| generative_agents | implementation | 是 | 是 | `fe05a71d3e4e` | https://github.com/joonspk-research/generative_agents.git |
| glTF-Transform | tool | 是 | 是 | `8e2a94a2616d` | https://github.com/donmccurdy/glTF-Transform.git |
| gpu-curtains | library | 是 | 是 | `f06ae9782d5b` | https://github.com/martinlaxenaire/gpu-curtains.git |
| gsap-threejs-codrops | implementation | 是 | 是 | `f236f2a7805e` | https://github.com/J0SUKE/gsap-threejs-codrops.git |
| ink | library | 是 | 是 | `35c63e52f1d3` | https://github.com/inkle/ink.git |
| inkjs | library | 是 | 是 | `6b1153410ab1` | https://github.com/y-lohse/inkjs.git |
| instanced-mesh | library | 是 | 是 | `56786de4651b` | https://github.com/agargaro/instanced-mesh.git |
| interactive-3d-portfolio | implementation | 是 | 是 | `3f8e87827f09` | https://github.com/Shaun520/interactive-3d-portfolio.git |
| invisible-cities-opus-5.5 | implementation | 是 | 是 | `3c2d0cc6657d` | https://github.com/stared/invisible-cities-opus-5.5.git |
| json-render | library | 是 | 是 | `72568f990e55` | https://github.com/vercel-labs/json-render.git |
| kimi-k31pro-opus55-benchmark-showcase | implementation | 是 | 是 | `65e82c53b63f` | https://github.com/Zp-Peter/kimi-k31pro-opus55-benchmark-showcase.git |
| letta | tool | 是 | 是 | `8816d3a85168` | https://github.com/letta-ai/letta.git |
| letta-archive | tool | 是 | 是 | `56ba9c255526` | https://github.com/letta-ai/letta.git |
| line-item-review | implementation | 是 | 是 | `c4e995a2e360` | https://github.com/pshankinclarke/line-item-review.git |
| little-rain-cloud | implementation | 是 | 是 | `8180c1b1c98e` | https://github.com/dososo/little-rain-cloud.git |
| lygia | library | 是 | 是 | `ce08fe351478` | https://github.com/patriciogonzalezvivo/lygia.git |
| map-of-middle-earth | implementation | 是 | 是 | `696e968e9d55` | https://github.com/earthwalker17/map-of-middle-earth.git |
| mem0 | library | 是 | 是 | `0724291bd864` | https://github.com/mem0ai/mem0.git |
| mesh2motion-app | tool | 是 | 是 | `653a9698f5f3` | https://github.com/Mesh2Motion/mesh2motion-app.git |
| meshoptimizer | tool | 是 | 是 | `f0a684f11ead` | https://github.com/zeux/meshoptimizer.git |
| mg-styles-15 | implementation | 是 | 是 | `49052d80bfaf` | https://github.com/Vincentwei1021/mg-styles-15.git |
| miniflux | implementation | 是 | 是 | `c52bdef6e981` | https://github.com/miniflux/v2 |
| neon-zenith | implementation | 是 | 是 | `27ad04ef04aa` | https://github.com/billpwchan/neon-zenith.git |
| newsnow | implementation | 是 | 是 | `0f95b2c998df` | https://github.com/ourongxing/newsnow |
| offshore-tower | implementation | 是 | 是 | `3a67f5ea7aec` | https://github.com/thebuggeddev/offshore-tower.git |
| opus55-live-demos | local | 否 | 不适用 | `null` | null |
| premium-saas-web-skill | tool | 是 | 是 | `813c8801649b` | https://github.com/MiddleSugar7000/premium-saas-web-skill.git |
| r3f-scroll-rig | library | 是 | 是 | `123663599e4b` | https://github.com/14islands/r3f-scroll-rig.git |
| r3f-theatrejs-starter | implementation | 是 | 是 | `77583f3e7c04` | https://github.com/gabrielagbese/r3f-theatrejs-starter.git |
| racing-game | implementation | 是 | 是 | `7816a5d954b7` | https://github.com/pmndrs/racing-game.git |
| react-postprocessing | library | 是 | 是 | `3da552af77f5` | https://github.com/pmndrs/react-postprocessing.git |
| readability | library | 是 | 是 | `ab4027a8b376` | https://github.com/mozilla/readability.git |
| realism-effects | library | 是 | 是 | `061daeaefb77` | https://github.com/0beqz/realism-effects.git |
| recast-navigation-js | library | 是 | 是 | `8769e8b9995f` | https://github.com/isaac-mason/recast-navigation-js.git |
| sandspiel | implementation | 是 | 是 | `9936e06b07a5` | https://github.com/MaxBittker/sandspiel.git |
| scroll-glitch-hero | implementation | 是 | 是 | `6e0b8e6189dc` | https://github.com/CoderMaurice/scroll-glitch-hero.git |
| synthcity | implementation | 是 | 是 | `5a4ee0dd231c` | https://github.com/jeffbeene/synthcity.git |
| theatre | tool | 是 | 是 | `6ea82b938ea4` | https://github.com/theatre-js/theatre.git |
| three-good-godrays | library | 是 | 是 | `70ad1c41c787` | https://github.com/Ameobea/three-good-godrays.git |
| three-gpu-pathtracer | library | 是 | 是 | `288363980a20` | https://github.com/gkjohnson/three-gpu-pathtracer.git |
| three-mesh-bvh | library | 是 | 是 | `1d7a4249d4ac` | https://github.com/gkjohnson/three-mesh-bvh.git |
| three-vrm | library | 是 | 是 | `68c7d6b1f73b` | https://github.com/pixiv/three-vrm.git |
| threejs-procedural-dungeon | implementation | 是 | 是 | `0a2aa0980028` | https://github.com/majidmanzarpour/threejs-procedural-dungeon.git |
| tidewater | implementation | 是 | 是 | `4811ba48d795` | https://github.com/dgreenheck/tidewater.git |
| tinylittleoffice | implementation | 是 | 是 | `07f771ceab9e` | https://github.com/aboard-io/tinylittleoffice |
| uikit | library | 是 | 是 | `2aaf8aba2e5d` | https://github.com/pmndrs/uikit.git |
| void-syndicate | implementation | 是 | 是 | `01a752e59031` | https://github.com/ademmrewind/void-syndicate.git |
| wawa-lipsync | library | 是 | 是 | `312dc31a1ee9` | https://github.com/wass08/wawa-lipsync.git |
| web-ocean | implementation | 是 | 是 | `a07c7fd522ef` | https://github.com/Noniv/web-ocean.git |
| webamp | implementation | 是 | 是 | `f01369fc2d7a` | https://github.com/captbaritone/webamp.git |
| webgl-seascape-video | implementation | 是 | 是 | `915cb7c9a318` | https://github.com/holooooo/webgl-seascape-video.git |
| yarn-planet | implementation | 是 | 是 | `5c8acce8df04` | https://github.com/makerjackie/yarn-planet.git |

分类用于检索：implementation=具体应用/演示；library=渲染/协议/行为库；tool=资产/编排/工作流工具；catalog=索引合集（可能兼含部分实作）；local=无独立Git的本地条目。不是质量排名。

_libsmoke 与 opus55-live-demos 没有独立 Git 根；head/origin=null。不能把父目录的提交号贴到它们身上。所有21条补充clone receipts已对照当前HEAD/origin，差异：无。

## 无视觉输出证据的后端、库与工具

本轮识别 **30 个**尚无实看视觉证据的后端/库/工具条目。以下保留 not_applicable 或 missing；不拿logo、目录截图或README宣传当效果图。

- **not_applicable**：当前案例研究的是协议、记忆、空间查询或资产加工机制，不要求成片截图。
- **missing**：该实现或其示例会产生画面，但当前研究未查看可用效果证据；并不表示仓库没有图片或程序运行失败。
- **observed_still**：继承原review实际查看记录；本轮不重新观察，也不提升为动画/运行验证。

| 来源 | visual_expectation | 原因 |
|---|---|---|
| 3DTilesRendererJS | missing | 该实现/示例会产生可见输出，但已审记录无实际查看的静帧；不能以源码或README宣传代替效果图。 |
| ChatdollKit | missing | 该实现/示例会产生可见输出，但已审记录无实际查看的静帧；不能以源码或README宣传代替效果图。 |
| Gaussian-Splat-Lite | missing | 该实现/示例会产生可见输出，但已审记录无实际查看的静帧；不能以源码或README宣传代替效果图。 |
| Open-LLM-VTuber | missing | 该实现/示例会产生可见输出，但已审记录无实际查看的静帧；不能以源码或README宣传代替效果图。 |
| THREE.js-PathTracing-Renderer | missing | 该实现/示例会产生可见输出，但已审记录无实际查看的静帧；不能以源码或README宣传代替效果图。 |
| ag-ui | not_applicable | 事件协议/SDK；协议成功不等于可见UI正确。 |
| concordia | not_applicable | 文本事件/场景状态仿真；非渲染输出。 |
| detect-gpu | not_applicable | GPU分类/benchmark查询库；不产生场景画面，logo或表格不应包装为效果。 |
| ecctrl | missing | 该实现/示例会产生可见输出，但已审记录无实际查看的静帧；不能以源码或README宣传代替效果图。 |
| glTF-Transform | not_applicable | 资产转换/压缩工具；质量应比较输入输出模型，不靠工具宣传图证明。 |
| gpu-curtains | missing | 该实现/示例会产生可见输出，但已审记录无实际查看的静帧；不能以源码或README宣传代替效果图。 |
| ink | not_applicable | 叙事编译/状态引擎；具体画面由宿主界面生成。 |
| inkjs | missing | 该实现/示例会产生可见输出，但已审记录无实际查看的静帧；不能以源码或README宣传代替效果图。 |
| json-render | missing | 该实现/示例会产生可见输出，但已审记录无实际查看的静帧；不能以源码或README宣传代替效果图。 |
| letta | not_applicable | 当前checkout是迁移入口/landing，无可审视觉实现。 |
| letta-archive | not_applicable | 历史记忆schema与服务逻辑；非场景效果。 |
| lygia | missing | 该实现/示例会产生可见输出，但已审记录无实际查看的静帧；不能以源码或README宣传代替效果图。 |
| mem0 | not_applicable | 记忆持久化与检索库；非视觉实现。 |
| meshoptimizer | not_applicable | 几何优化库；无独立场景审美输出，轮廓误差需另测。 |
| r3f-scroll-rig | missing | 该实现/示例会产生可见输出，但已审记录无实际查看的静帧；不能以源码或README宣传代替效果图。 |
| react-postprocessing | missing | 该实现/示例会产生可见输出，但已审记录无实际查看的静帧；不能以源码或README宣传代替效果图。 |
| readability | not_applicable | 正文抽取库；提取内容不等于最终页面排版。 |
| realism-effects | missing | 该实现/示例会产生可见输出，但已审记录无实际查看的静帧；不能以源码或README宣传代替效果图。 |
| recast-navigation-js | not_applicable | 寻路/导航底层机制；调试navmesh不是场景美术效果。 |
| theatre | missing | 该实现/示例会产生可见输出，但已审记录无实际查看的静帧；不能以源码或README宣传代替效果图。 |
| three-good-godrays | missing | 该实现/示例会产生可见输出，但已审记录无实际查看的静帧；不能以源码或README宣传代替效果图。 |
| three-gpu-pathtracer | missing | 该实现/示例会产生可见输出，但已审记录无实际查看的静帧；不能以源码或README宣传代替效果图。 |
| three-mesh-bvh | not_applicable | 空间查询/碰撞加速库；机制卡不期待独立美术成片。 |
| uikit | missing | 该实现/示例会产生可见输出，但已审记录无实际查看的静帧；不能以源码或README宣传代替效果图。 |
| wawa-lipsync | missing | 该实现/示例会产生可见输出，但已审记录无实际查看的静帧；不能以源码或README宣传代替效果图。 |

全部86条的视觉期望计数：{"missing": 38, "observed_still": 32, "not_applicable": 16}。instanced-mesh/three-vrm等仓级宣传静帧只支持图像观察，不自动证明各库参数效果；JSON保留仓级证据路径与限制。

## 许可与未覆盖边界

licensed_scope 保留原分组审查的逐仓许可注记；本轮复核根目录声明文件存在、头部与哈希。代码许可不自动覆盖照片、角色、Logo、音乐、字体、参考影像、GIS或外链作品；未知许可仍保持未知。

**合集外链没有递归全部 Git。** 187条视频、663条URL等索引规模不等于取得对应作品源码，也不等于拥有媒体复用授权。仓内已有实作与README外链分开处理。

浅克隆不证明完整提交历史已归档；本轮仅核本地HEAD/origin，不重新认证Pro声称的首发日期、模型共署名、GPU性能或线上运行状态。剩余问题见JSON unresolved；14项明确作品的本地Git缺口为0。
