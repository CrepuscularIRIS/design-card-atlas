# Opus A 视觉来源

仅保存本人用Chrome浏览真实在线作品的画面；不是作者README截图，不构成动态/性能验证。日期2026-10-25。数值为目测估计。

## 清明上河 · 汴京（index 10）

源页 https://github.com/SilentFleetKK/qingming-bianjing

源页明确链接的demo https://silentfleetkk.github.io/qingming-bianjing/opus-5.5/qingming-bianjing.html

作者声明代码及文档许可证待定；仅用作注明出处的视觉分析，不声称取得资产复用授权。模型归因为源页作者声明，未独立验证。

### qingming-dusk-wide.jpg

复现：打开Opus版demo，等待加载层消失；默认汴河全景；点击“黄昏，华灯初上”，待天空/灯窗变化稳定；点击“隐藏界面（H）”，待控件消失后截图。

可见：①河从左中景斜贯右下，带状高光把视线引向中间桥；②近景瓦屋深棕、中景灰褐、远景浅黄雾，至少三层明度分离；③黄白窗洞是小而离散的亮点，不把整面墙照亮；④远中右塔楼伸出重复屋顶，约屏高1/7，普通屋顶构成尺度基准；⑤太阳在左上，天空约占上方1/3。建议视觉卡“暖窗点亮密集古城”“河谷光带串联城景”。

### qingming-dusk-bridge.jpg

复现：上述黄昏模式，显示界面→“虹桥河岸”→隐藏界面，待镜头稳定。

可见：①拱桥顶约画面中高，桥拱孔中的远景亮、水面也亮，桥体保持深色剪影；②桥上人影约桥高的1/7至1/10形成尺度；③右侧暗船体占约半幅宽，方形暖窗沿船重复；④岸沿从左下向桥底收束，斜线和拱线交汇；⑤低太阳被栏杆和伞遮挡，局部轮廓光不过度涂亮前景。建议“低位逆光的桥与小人”“暗体量上的离散暖洞”。

### qingming-rain-bridge.jpg

复现：虹桥河岸镜头，显示界面→“清明时节雨纷纷”→隐藏界面，待阴云和雨线出现。

可见：①青灰天空与褐黑桥船降低整体饱和度；②竖向细雨线覆盖前景，而背景雾更浅，雨与距离层次可区分；③水面断裂反射比天空更暗，窗灯形成短暖反光；④行人伞帽与桥栏重复节奏保留小尺度；⑤同一桥岸构图可与黄昏图作氛围对照，不推断真实物理准确度。建议“雨雾把暗建筑层层推远”。

## 文件校验

- `qingming-dusk-bridge.jpg` | (2494, 905) | SHA256 `6e1e4f8911ec0b246c4ad2d845aedce9e5ff9beddc70ecde94e2beb361ce99cc`
- `qingming-dusk-wide.jpg` | (2494, 905) | SHA256 `5fdbc04616d583ed57f24d71285249262edf8a6e70c8dbe8549529808bd0680e`
- `qingming-rain-bridge.jpg` | (2494, 905) | SHA256 `7ecd1b00cadbf84d5907156ed454640eb4f355712d17a734f7801f4ab9e467a6`

## Ozymandias（index 17）

日期2026-10-25；源页 https://www.echohive.ai/ozymandias 明确链接体验页 https://www.echohive.ai/posts/ozymandias/animation.html 。作者网页归因为Opus 5.5，未独立验证；诗歌已属公有领域不代表网站画面和配乐许可，画面仅注明出处作视觉分析。

复现：打开体验→Enter the desert→Pause，用Playback position或±10秒按钮定位。播放器显示存在约1秒取整差，截图时以slider DOM值确认，未修改页面内状态。16s图为约16秒；110s slider为110而时间字显1:49；100s同理字显1:39。屏幕包含原片字幕和播放器，非海报或设置。

- `ozymandias-traveller-16s.jpg`：①右下旅人深色剪影站在唯一暖光圈；②远左巨像断腿加底座，高约旅人画面高度的0.8，但处于远景，靠前后尺寸关系暗示巨大真实体量；③暗蓝近黑沙地大留白，主亮区仅底部约1/8画面；④细沙波纹被斜光照见，远处轮廓简化；⑤暖光圈柔边，人物正面保持黑，建议卡“微小暖光把人放进巨大暗场”。
- `ozymandias-isolation-110s.jpg`：①孤立残腿和散落石块只占中下约1/5面积；②无建筑沙丘从清晰近景向低对比地平线层层推远；③左后低太阳给右下长阴影，约跨画面1/4高；④整体沙褐低饱和，结构主要用明暗塑造；⑤横向超宽天空和地面留白让物体显孤独，建议“空旷景观吞没纪念物”。字幕居中是原作叙事层，迁移场景时无需照搬文字。
- `ozymandias-ruins-100s.jpg`：失败对照，非主视觉推荐。金字塔和巨像叠在强白黄光晕里，左中大面积过亮抹掉体块，宽大金色字幕又压住空间主体。可以用于说明‘发光不能代替轮廓和体量’。

- `ozymandias-isolation-110s.jpg` | (2494, 905) | SHA256 `37f358fe44002ca98bd09b14cbc161aaad322043cc1339a469b84e197ab491b1`
- `ozymandias-ruins-100s.jpg` | (2494, 905) | SHA256 `26ed95243eb14c86f09c935894d8f7a67384bb5f0563cbbb6dd25a310e3eacae`
- `ozymandias-traveller-16s.jpg` | (2494, 905) | SHA256 `5afe21ad9695b237183d99c7663c08e2c9b6f23ad653c5ca1f2d0121cbfce67d`

## Clearwater — clearwater-caustics.jpg
- Source/demo: https://aureliengmz.github.io/clearwater/ ; author link visible: Aurélien / Lumaris. Opened from original collection URL.
- Captured: 2026-10-25; 2494×905; original browser screenshot, not enlarged/cropped.
- SHA256: 246952aa7fe5be18f0a9739fc2e8f72b3846dbc5d72defca4333118e6b7e00a5
- Reproduce: open route; allow initial water rendering; default downward camera, no drag or water tap. Dynamic water means exact wave phase is not fixed.
- Visible dimensions (estimates, not shader parameters): cool cyan/blue water covers the frame; irregular pale green caustic nets resolve across the lower two thirds; rounded dark submerged pebbles remain readable beneath these nets; elongated soft white sun glints form a broken vertical chain through upper middle; wave ridges become more tightly compressed toward upper edge, creating perspective without a visible horizon.
- Use: transparent shallow water / layered caustics, suitable for citadel waterfront detail rather than skyline composition. One still does not establish fluid accuracy, frame rate, or interaction quality.
- Rights: original author retains rights. License not verified; analytical reference only, no permission to reuse site assets implied.

## The Battle of the Golden Ford
- Source/demo: https://www.echohive.ai/experiments/the-golden-ford
- Author attribution displayed: collaboration between Echo, Opus 5.5 and Grok 4.6; attribution not independently verified. Actual live 2.5D painted layers, not promotional poster.
- Date: 2026-10-25. Steps: wait full artwork; ENTER THE PAINTING; Pause scene around 217.9 seconds for clash; timeline Home/PageUp navigation (10% each, playback resumes on seek), Pause at 255.6 seconds for Siege. Exact paused value verified from visible timeline DOM.
- Fullscreen reports unavailable. Siege crop is browser clip x=0,y=65,w=2494,h=700; no enlargement; excludes navigation/player/toast, retains original full screenshot below. Some transient chapter text faded between original and cropped capture; same paused scene.
- Visible dimensions: gold/orange sky illuminates hilltop castle above centre; dark near-ground troops have roughly 5–8× the on-screen height of distant troop marks; repeated red/blue arrays fill lower half with density that falls toward the hill; staggered smoke columns occlude left background and separate planes; slope paths climb toward luminous castle, while right sea is a broad quiet midtone. Ratios are visual estimates, not measured geometry.
- Suggested language: crowd density as scale ruler; luminous high-ground focal point; smoke-column depth; dark foreground diagonal. Limit: painterly parallax does not prove 3D modeling/lighting or historical accuracy.
- Rights: artwork and assets retain author rights; paid download link does not authorize reuse. Analytical reference only; license unverified.
- golden-ford-clash-218.jpg: (2494, 905); SHA256 d648f6f6d2ac48a522445b72c62893cfb0a264ba2c8372dbedac126d00594d01
- golden-ford-siege-256-original.jpg: (2494, 905); SHA256 b4c296f41fef9c872b24fb923be661bd4afd349bd3720bd2d6ae7ceb744c8d70
- golden-ford-siege-256-crop.jpg: (2494, 700); SHA256 2ec59153a5d8f4bfd112cedfad92f31d5d5e16591436c62204880372f806ebbb

### Ozymandias clean analysis crop

`ozymandias-isolation-110s-crop.png`: 2494×750, SHA256 `8ee1ed7a8db7413a986022b910e756b00dd607e6b033ec55f6607b8ddf3fbeaf`. Derived 2026-10-25 from the preserved original `ozymandias-isolation-110s.jpg` by crop box x=0,y=65,right=2494,bottom=815. No resizing, retouching, generated pixels, or enlargement. Removes top letterbox and bottom playback controls; lower end of long shadow is partly cropped. Keeps original narrative subtitle. Prefer this clean crop for card display; original remains evidence of playback position. All image reading above refers to the original unless otherwise noted.

## Seiryu 清流（index 120；作者后续可玩版）
- Source: https://x.com/hayashimon1/status/2102576886182453454 ; original author reply links their later fishing version https://seiryu.miraicode.one/ . This capture is that later playable version, not claimed identical to the original short video.
- Date: 2026-10-25. Browser steps: open author-linked site, wait 清流 loading, TAP TO START, Skip tutorial, default Summer / Lower Riffle; initial camera, no cast, no drag. Wait introductory angler dialogue to disappear.
- Crop: preserve original full 2494×905 screenshot with HUD; analytical image is crop box (0,185,2335,735), 2335×550, no resizing or retouching. Removes top HUD, right controls and bottom hints; loses top forest depth and lower foreground. Fishing rod remains a real scene object.
- Visible dimensions (estimates): cyan water forms a narrowing central corridor toward a small white cascade; pale exposed boulders step down in apparent size with distance; dense dark green vegetation frames both banks, contrasting bright mineral surfaces; submerged stones retain softer edges than dry banks; broken fine caustic lines overlay the visible pebbled bed, whereas deeper middle water becomes a flatter turquoise; near leaves blur while central rocks are sharper.
- Candidate use: shallow clear water with visible bed; alternate pale rock / dark foliage banks as depth rhythm. Local waterfront detail for fantasy environments, not itself evidence of epic scale. Better read alongside Clearwater: this adds bank geometry and a vanishing corridor instead of a top-down material study.
- Limits: only initial still observed; no gameplay, water physics, performance or whole-site validation. Author model attribution unverified. License unverified; analytical reference only, original author retains rights.
- seiryu-riffle-original.jpg: (2494, 905); SHA256 d6d68a181e9820f62bcdcf1606ef3bc7526fd829fdf7257fb6b1f4ecff1b4bb8
- seiryu-riffle-crop.png: (2335, 550); SHA256 d1cb4a50253dccbc2774288cf8d3456d2b5c12fc882298eae219c5200d3460d3

## Poseidia — 轴线水道与晶灯阵列（索引126）
- 来源：https://x.com/DannyLimanseta/status/2103169095034400772 ，源帖真实链接 https://poseidia.vercel.app/ 。2026-10-25 Chrome 在线实际进入；不是本地源码或宣传海报。
- 复现：等待 Raising the city 完成，点击 Click to set sail；等待开场穿过巨门到 The Sea Canal。此时按 F 进入照片模式，Hour 09:04 / Lens 50° / Focus 40 m；Aperture 滑块按 Home，H 隐藏控件。小船与水面仍持续运动，不能保证像素级同帧。夜图在照片模式 H 显示→Hour 按 End→H 隐藏，不代表完整夜间巡游。仅看入城水道，未看环城全程。
- `poseidia-gates-original.jpg`：2494×905，SHA256 `459df890a7ea9ca4d9a239d4e68b273011521436ea8260816e0ac8e6eb39a574`。命名是历史保存名，实际帧已穿过巨门，为 Sea Canal 航行画面；有上下电影黑边及细章节字，无播放器面板。
- `poseidia-canal-photo.jpg`：2494×905，SHA256 `94077f92fd9191ab85988c2dbe8eb27084d545c41f12d32f8eeb1fc779240b0c`。照片模式隐藏控件后实际截图，无裁切/放大/后期。
- `poseidia-canal-night.jpg`：2494×905，SHA256 `b00de1120898dd3efe2b08ea86e7df3268a394c628be4a426a2d835618903480`。夜间同机位色彩风险对照：晶灯与远塔光晕偏紫，不直接复制此色彩到博客。
- 构图：左右栏桥从两底角汇聚约画宽51%、画高32%神殿；水道构成约中央1/3宽的负空间。
- 造型/尺度：近处晶灯柱显著高于行人，拱孔与灯柱重复并随距离缩小；中央小舟宽约画宽1.5%，远岸建筑横跨山脚。
- 色彩：白天水道近似青蓝 #3B8A9A，桥石为低饱和米灰 #9E9A87，暗山蓝绿；色值为目测估计，非源码参数。夜图大面积深蓝，紫色灯光为迁移禁区风险。
- 大气：远岸薄雾横向切开水面与山脚，上方山谷另有局部云带；不把截图推断为已确认体积雾实现。
- 材质/光影：桥面哑光与水面长条白反光相对；晶灯高亮核心略失细节，神殿星芒是焦点，近景斜影提供立体感。
- 镜头：实际见航行向前推近，照片视点冻结后舟仍前移；未测性能或全部相机模式。
- 许可：作者/模型归因仅来源帖陈述；素材及截图再分发权未核实，仅设计分析参考。
