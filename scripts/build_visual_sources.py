#!/usr/bin/env python3
"""Generate the audit index, keeping counts out of the visual Reel."""
import json,collections
from pathlib import Path
from visual_screening import ROOT,COLLECTIONS,read_rows
P=ROOT/'public'
cards=[json.loads(p.read_text()) for p in sorted((P/'cards').glob('*/card.json'))]
lines=['# 来源与筛选记录','','这是视觉卡的来源索引；数量用于核对范围，不代表模型排名或美术质量。每张卡的 SOURCE 保留机位、截图时间、观看范围、原图尺寸和权利信息。','',
'## 阅读边界','','- 卡片描述可见画面；数值分别标注目估、原作源码值或Blog试验值。','- 视频抽看片段、独立作者渲染成片、本轮网页运行截图分别记录，不把它们合并成“完整运行验证”。','- 合集条目的收录是候选判断，最终使用还要匹配具体视觉语言。转载和不同时间点不算新的独立作品。','- 本轮目标是3D场景与覆盖其上的UI；2D图解、工具、低清分屏、宣传海报不进入主图。','- 嵌套合集条目只判目录本身，明确记录实际展开的子项，不无限递归声称全看。','',
'## 合集逐条记录','','所有原始CSV保留独立代理的原字段；汇总脚本只读，不覆盖观察记录。','',
'| 合集 | 条目 | 收 | 不收 | 打不开 | 尚未收束 | 筛选表 |','|---|---:|---:|---:|---:|---:|---|']
allrows=[]
for name,files,expected in COLLECTIONS:
 rows=sum([read_rows(f) for f in files],[]);allrows+=rows;c=collections.Counter(r['decision'] for r in rows);pending=sum(n for k,n in c.items() if k not in ['收','不收','打不开'])
 lines.append(f'| {name} | {len(rows)} / {expected} | {c["收"]} | {c["不收"]} | {c["打不开"]} | {pending} | '+ ' · '.join(f'[{f}](../screening/{f})' for f in files)+' |')
 if len(rows)!=expected:lines.append(f'\n该集合条数待核：{name}。\n')
lines+=['','Opus frontend按当前文件枚举为91个HTML入口，包含导航/重复导出；提示词中的87是原索引口径。各入口都单列，排除原因保留在CSV，未把导航页当新作品。Kimi guide 83条之外的README索引亦已由负责代理核对，没有另列独立遗漏作品。','',
'`尚未收束`包括尚未观看或待具体复核，不能当作“不收”或链接失败。浏览器工具中断与网站实际打不开分开记录；有清楚观察而尺寸不足的作品可以本轮不收，并在理由保留高清再访线索。','',
'## 具名作品与补充入口','']
for f in ['strong-scenes.csv','light-water.csv','motion-extra.csv']:
 if not (ROOT/'screening'/f).exists():continue
 lines+=['### '+f,'',f'[完整记录](../screening/{f})','']
 for r in read_rows(f):lines.append(f'- **{r["title"]}** — {r["decision"]}：{r["reason"]}')
 lines.append('')
lines+=['## 图像档案','']
for s in sorted((P/'references').glob('*/SOURCE.md')):lines.append(f'- [{s.parent.name}]({s.relative_to(P).as_posix()})')
lines+=['','## 卡片与实际作品','', '| 卡片 | 独立作品标识 | 选图说明 |','|---|---|---|']
for c in cards:
 refs=[s for s in c['shots'] if s['role']=='reference'];works={}
 for s in refs:works.setdefault(s.get('work_id',s['url']),s)
 lines.append(f'| [{c["title"]}](cards/{c["id"]}/README.md) | '+' · '.join(f'[{s["work"]}]({s["url"]})' for s in works.values())+f' | {len(refs)}帧；{len(works)}个作品；另有真实视觉对照 |')
lines+=['','## 编辑取舍','','[独立审图](../screening/visual-editorial-review.md)与[修订记录](../screening/visual-editorial-resolution.md)记录图片是否真正支持卡的判断。原始审查保留当时版本的问题，修订记录说明最终处理。','',
'[暖石冷影候选](candidates/warm-stone-cool-shadow/README.md)目前只有一张足够明确的正例，不进入Reel。不能用不同物体的环境分色替代同一石面暖冷关系，也不以相邻视频帧凑图。候选可以为配方提供单帧视点参考，但不算已完成视觉语言。','',
'## Git 与模型归因','','Pro原答复的14个明确作品已有本地Git；[旧阶段逐项对照](../docs/SOURCE_AUDIT.md)保留原答复行号、origin与HEAD。[本次重新读取的Git记录](pro-git-recheck.json)只核克隆存在和版本，不认证模型贡献或发布先后。','',
'本轮新增的可追溯源码记录在 [new-source-clones.json](new-source-clones.json)：qingming-bianjing、clearwater、falcon9-blender已克隆；cybercity与ProceduralBuildingsThreeJS取得固定HEAD与源码检出，大体积媒体/模型未完整检出，不能称为完整资产归档。没有公开源码链接的网页或视频仍只记视觉出处；不把视频条数等同已取得的Git仓数量。原有参考仓保持原文件，不修改其实现。','',
'Opus、Kimi、Sonnet、DeepSeek等归因保留作者/发布者自述；混合制作也可参考。不把仓库标题、宣传句或单帧画质当作某模型独立完成的证明。','',
'## 权利与工程旧版','','截图与视频帧保留原作者/素材权利人的权利，本库文档许可不覆盖第三方媒体；有明确许可者单独注明。`lygia`、`gsap-threejs-codrops`、`opus55-live-demos`只借思路，不粘贴代码。','',
'旧257张机制卡和旧网页只作工程背景，旧入口移入 [archive/engineering-v1](../archive/engineering-v1/)。新交付为Markdown README、卡片、图片和配方。`public/`是本地目录名，不表示已更改远端私有仓库的可见性。','']
(P/'sources.md').write_text('\n'.join(lines))
