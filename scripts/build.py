"""Build portable Markdown and static atlas. Standard library only."""
import collections,hashlib,json,re
from pathlib import Path
R=Path(__file__).resolve().parents[1]
def dump(path,data): (R/path).write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
def fmt(v):
 if isinstance(v,str):return v
 if isinstance(v,list):return '\n'.join('- '+fmt(x) for x in v)
 if isinstance(v,dict):return '\n'.join(f'- **{k}**：{fmt(x)}' for k,x in v.items())
 return str(v)
def image_block(v,prefix='../'):
 return f"![{v.get('repo','')} · {v.get('kind','静帧')}]({prefix}{v['path']})\n\n{v.get('observation','')}\n\n来源：{('[原作者/出处]('+v['source_url']+')') if v.get('source_url') else '本轮已观察的历史截图'} · {v.get('kind','observed_still')}。{v.get('scope','静帧不证明连续运动与性能。')}\n"
def run():
 d=json.loads((R/'data/base.json').read_text());d['lenses']=[];d['trajectories']=[];d['professional_sources']=[];analysis={};gaps=[];bindings=[]
 for p in sorted((R/'data/editorial').glob('*.json')):
  e=json.loads(p.read_text());bindings+=e.get('bindings',[])
  d['lenses']+=e.get('lenses',[]);d['trajectories']+=e.get('trajectories',[]);d['professional_sources']+=e.get('sources',[]) if p.stem in ['cinematic','interface'] else []
  for a in e.get('case_analyses',[]):analysis.setdefault(a['repo'],[]).append(a)
  d['visuals']+=e.get('media',[]);gaps+=e.get('gaps',[])
  if 'pro_reconciliation' in e:d['pro_reconciliation']=e['pro_reconciliation']
  if p.stem=='sources-audit':d['source_audit']=e
 seen=set();media=[]
 for v in d['visuals']:
  key=(v['repo'],v['sha256'])
  if key not in seen:media.append(v);seen.add(key)
 for b in bindings:
  for v in media:
   if v['repo']==b['repo'] and v['sha256']==b['sha256']:v.update(b)
 d['visuals']=media;byrepo=collections.defaultdict(list)
 for v in media:byrepo[v['repo']].append(v)
 cards={c['id']:c for c in d['cards']};repo_map={r['repo']:r for r in d['repos']};sources={s['repo']:s for s in d['sources']}
 d['cases']=[]
 for r in d['repos']:
  name=r['repo'];cs=[c for c in cards.values() if c['repo']==name];visuals=byrepo[name]
  case=dict(r,card_ids=[c['id'] for c in cs],images=visuals,analyses=analysis.get(name,[]),source=sources[name],lens_ids=[l['id'] for l in d['lenses'] if name in l.get('case_repos',[])],image_gap=[g for g in gaps if g['repo']==name])
  # No logo or promotional card masquerades as a scene result.
  usable=[v for v in visuals if v.get('primary_eligible',True) and not any(t in str(v.get('kind','')).lower() for t in ['logo','promotional','reference_input'])]
  case['cover']=usable[0]['path'] if usable else None
  case['visual_status']='observed' if usable else 'missing_or_not_applicable'
  d['cases'].append(case)
  lines=[f'# {name}',r.get('summary',''),'','## 案例档案','',f"[来源仓库]({sources[name]['origin']})" if sources[name]['origin'] else '本地目录，无可公开定位的上游仓库。',f"分析版本：`{sources[name]['analysis_revision'] or 'unversioned'}`",'',fmt(r.get('model_attribution','模型归属未独立认证。')),'','## 初始源码审计边界','',fmt(r.get('coverage_limits','仅所列机制切片。')),'','以下保留初始源码审计的观察范围。后续新增静帧独立列于视觉材料，不追溯证明全部机制或运行状态。','']
  for a in case['analyses']:
   lines+=['## 领域分析','',a['thesis'],'', '### 画面与证据','',fmt(a['visual_reading']),'','### 因果链','',fmt(a['causal_chain']),'','### 审美决策','',fmt(a['aesthetic_rules']),'','### 相邻方案','',fmt(a['alternatives']),'','### 迁移顺序','',fmt(a['transfer_steps']),'','### 局限','',fmt(a['limits']),'']
  lines+=['## 机制与案例分析','']
  for c in cs:
   lines += [f"### [{c['id']} · {c['title']}](../cards/{c['id']}.md)",'',c['principle'],'',fmt(c.get('design_details',c['implementation'])),'',f"**Movie：{c['movie']['verdict']}** · {c['movie'].get('reason','')}",f"**前端：{c['frontend']['verdict']}** · {c['frontend'].get('reason','')}",'','失败条件：'+fmt(c['failure_modes']),'']
  if not cs:lines+=['此仓是资料/支撑工具来源，未硬凑成视觉机制卡。','']
  lines+=['## 项目效果与观察材料','']
  if visuals:lines += [image_block(v) for v in visuals]
  else:lines+=['尚无已观察的项目效果图；不以Logo、概念图或生成图代替。库/后端可能没有独立画面，详见来源审计。','']
  lines+=['## 复用边界','',fmt(r.get('license','未知')),'','图片及第三方素材的权利单独保留；源代码许可证不自动授权媒体。','']
  (R/'cases'/f'{name}.md').write_text('\n'.join(lines))
 for c in cards.values():
  c['lens_ids']=[l['id'] for l in d['lenses'] if c['id'] in l.get('card_ids',[])];c['pattern_ids']=[m['id'] for m in d['patterns'] if c['id'] in m['subcards']]
  c['trajectory_ids']=[t['id'] for t in d['trajectories'] if any(c['id'] in s['card_ids'] for s in t['steps'])]
  vs=byrepo[c['repo']];direct=[v for v in vs if v.get('sha256') in c.get('visual_sha256',[]) or v.get('card_id')==c['id'] or c['id'] in v.get('card_ids',[])];general=[v for v in vs if not v.get('card_id') and 'card_ids' not in v];c['images']=(direct or general[:2]);c['case_cover']=next((v['path'] for v in c['images'] if v.get('primary_eligible',True) and not any(x in str(v.get('kind','')).lower() for x in ['logo','promotional','reference_input'])),None)
  lines=[f"# {c['id']} · {c['title']}",f"案例：[ {c['repo']} ](../cases/{c['repo']}.md) · 机制证据：`{c['evidence_stage']}`",'','效果图用于理解来源作品，不自动验证本卡中的每个机制。','']
  for label,key in [('设计动作','principle'),('实现与参数','implementation'),('审美细节','design_details'),('适用条件','conditions'),('相邻方案与区别','alternatives'),('失败模式','failure_modes'),('Movie 裁决','movie'),('Frontend 裁决','frontend'),('最小对照','minimum_test')]:
   if c.get(key):lines += ['## '+label,'',fmt(c[key]),'']
  lines+=['## 源码证据','']
  for e in c['source_evidence']:
   lines.append(f"- [{e['path']}:{e['line_start']}–{e['line_end']}]({e['url']})：{e.get('claim','')}" if e.get('url') else f"- `{e['path']}:{e['line_start']}–{e['line_end']}`：{e.get('claim','')}（无上游永久链接）")
  lines+=['','## 项目效果图','']+[image_block(v) for v in c['images']]
  if not c['images']:lines+=['尚无已核实效果图，保留缺口。','']
  lines+=['## 归纳与练习','', ' / '.join(f"[{i}](../lenses/{i}.md)" for i in c['lens_ids']) or '暂未归入新增专业视角；保留原机制边界。','', ' / '.join(f"[{i}](../patterns/{i}.md)" for i in c['pattern_ids']) or '保留独立案例。','']
  (R/'cards'/f"{c['id']}.md").write_text('\n'.join(lines))
 for l in d['lenses']:
  lines=[f"# {l['id']} · {l['title']}",l['question'],'',l['why'],'']
  for label,key in [('诊断问题','diagnostics'),('失败信号','failure_signs'),('最小对照','minimum_test'),('归纳边界','limits')]:lines += ['## '+label,'',fmt(l[key]),'']
  lines+=['## 具体卡片','']+[f"- [{i} · {cards[i]['title']}](../cards/{i}.md)" for i in l['card_ids'] if i in cards]
  (R/'lenses'/f"{l['id']}.md").write_text('\n'.join(lines)+'\n')
 for m in d['patterns']:
  lines=[f"# {m['id']} · {m['title']}",m['principle'],'']
  for k in ['shared_invariants','branches','conditions','conflicts','failure_modes','movie','frontend','minimum_test']:lines+=['## '+k,'',fmt(m.get(k,'')),'']
  lines+=['## 子卡','']+[f"- [{i} · {cards[i]['title']}](../cards/{i}.md)" for i in m['subcards']]
  (R/'patterns'/f"{m['id']}.md").write_text('\n'.join(lines)+'\n')
 d['stats']={'cases':len(d['cases']),'cards':len(cards),'patterns':len(d['patterns']),'lenses':len(d['lenses']),'trajectories':len(d['trajectories']),'visuals':len(media),'illustrated_cases':sum(bool(c['cover']) for c in d['cases']),'expanded_cases':len(analysis)}
 dump('data/catalog.json',d)
 (R/'data/catalog.js').write_text('window.ATLAS='+json.dumps(d,ensure_ascii=False).replace('</','<\\/')+';\n')
 dump('data/media.json',media)
 missing=[{'repo':c['repo'],'card_count':len(c['card_ids']),'gaps':c['image_gap']} for c in d['cases'] if not c['cover']]
 dump('data/visual-gaps.json',missing)
 # Every case remains discoverable from GitHub without opening the browser app.
 table=['# 全部案例','','| 案例 | 子卡 | 效果证据 | 专项分析 |','|---|---:|---|---|']
 for c in d['cases']:table.append(f"| [{c['repo']}](../cases/{c['repo']}.md) | {len(c['card_ids'])} | {'有已观察图' if c['cover'] else '未补图 / 无独立画面'} | {'深入补充' if c['analyses'] else '机制级分析'} |")
 (R/'docs/CASES.md').write_text('\n'.join(table)+'\n')
 sourcesdoc=['# 专业视角的一手参考','','这些资料支持诊断视角，不替代每个项目的源码与视觉证据。','']
 for s in d['professional_sources']:sourcesdoc += [f"## [{s['title']}]({s['url']})",'',fmt(s['supports']),'','边界：'+fmt(s['limits']),'']
 (R/'docs/PROFESSIONAL_SOURCES.md').write_text('\n'.join(sourcesdoc))
 from readme import generate
 generate(d,R)
 print(json.dumps(d['stats'],ensure_ascii=False))
if __name__=='__main__':run()
