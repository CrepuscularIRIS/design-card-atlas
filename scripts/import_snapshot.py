"""One-time import; the built atlas never depends on the original workspace."""
import argparse,copy,hashlib,json,re,shutil,subprocess
from pathlib import Path
R=Path(__file__).resolve().parents[1]
p=argparse.ArgumentParser();p.add_argument('snapshot',type=Path);p.add_argument('workspace',type=Path);a=p.parse_args()
d=json.loads((a.snapshot/'cards.json').read_text()); sources={}
def git(p,*args):
 try:return subprocess.check_output(['git','-C',str(p),*args],text=True,stderr=subprocess.DEVNULL).strip()
 except subprocess.CalledProcessError:return ''
def remote_web(s):
 if s.startswith('git@github.com:'):s='https://github.com/'+s.split(':',1)[1]
 return s.removesuffix('.git')
for r in d['repos']:
 local=a.workspace/'Repos'/r['repo'];origin=remote_web(git(local,'remote','get-url','origin'));head=git(local,'rev-parse','HEAD');pin=r.get('source_sha') or head
 if not re.fullmatch('[0-9a-f]{40}',str(pin)):pin=head
 sources[r['repo']]={'repo':r['repo'],'origin':origin,'head':head,'analysis_revision':pin,'is_git':bool(head),'is_shallow':git(local,'rev-parse','--is-shallow-repository')=='true','license':r.get('license',{})}
# All original observed images are copied byte-for-byte.
media=[];seen=set()
live=json.loads((a.snapshot/'evidence/live-observations.json').read_text())['samples']
livemap={Path(v['path']).name:v for v in live}
for i,v in enumerate(d['visuals']):
 old=Path(v['path']);old=old if old.is_absolute() else a.workspace/old
 key=str(old.resolve())
 if key in seen:continue
 seen.add(key); digest=hashlib.sha256(old.read_bytes()).hexdigest()
 slug=re.sub('[^a-zA-Z0-9_-]','-',v['repo']);dest=Path('assets/previews')/f'{slug}-{digest[:12]}{old.suffix.lower()}'
 shutil.copyfile(old,R/dest)
 repo=sources[v['repo']];source=livemap.get(old.name,{}).get('source_url','')
 rel=old.relative_to(a.workspace).as_posix() if old.is_relative_to(a.workspace) else old.name
 prefix='Repos/'+v['repo']+'/'
 if not source and rel.startswith(prefix) and repo['origin']:source=repo['origin']+'/blob/'+repo['analysis_revision']+'/'+rel[len(prefix):]
 media.append({'repo':v['repo'],'path':dest.as_posix(),'source_url':source,'original_path':rel,'kind':v.get('kind') or v.get('status') or v.get('stage') or ('video_still' if 'time_seconds' in v else 'observed_still'),'time_seconds':v.get('time_seconds'),'card_id':v.get('card_id'),'observation':v.get('observation') or v.get('inspection') or ('本地影片 '+str(v['time_seconds'])+' 秒静帧。' if 'time_seconds' in v else '已查看的来源静帧；不证明当前版本运行。'),'scope':v.get('scope') or v.get('limits') or '静帧观察；没有由此验证连续动画或性能。','sha256':digest,'rights':'Third-party media; upstream rights retained. Code license does not establish image rights.'})
# Retain general mechanisms, remove project-specific implementation instructions.
for c in d['cards']:
 c['visual_sha256']=[v['sha256'] for v in c.get('visual_evidence',[]) if v.get('sha256')]
 for k in ['citadel_application','coverage_limits','visual_evidence','main_patterns']:c.pop(k,None)
 c['source_evidence']=copy.deepcopy(c['source_evidence'])
 for e in c['source_evidence']:
  raw=e['path'].replace(str(a.workspace)+'/','');e['path']=raw
  prefix='Repos/'+c['repo']+'/';rel=raw[len(prefix):] if raw.startswith(prefix) else ''
  s=sources[c['repo']];e['url']=s['origin']+'/blob/'+s['analysis_revision']+'/'+rel+'#L'+str(e['line_start'])+'-L'+str(e['line_end']) if rel and s['origin'] else ''
  local=a.workspace/raw
  e['sha256']=hashlib.sha256(local.read_bytes()).hexdigest() if local.exists() else None
  if rel and s['is_git']:
   pinned=git(a.workspace/'Repos'/c['repo'],'rev-parse',s['analysis_revision']+':'+rel)
   current=git(a.workspace/'Repos'/c['repo'],'hash-object',str(local))
   e['revision_content_match']=bool(pinned and pinned==current)
  else:e['revision_content_match']=None
for r in d['repos']:
 for k in ['cards','visual_evidence','file_hashes']:r.pop(k,None)
for m in d['patterns']:
 m.pop('citadel_targets',None)
 m['file']='patterns/'+m['id']+'.md'
# Historical generic verdicts may reference the application context; keep the constraint visible.
d['visuals']=media;d['sources']=list(sources.values());d['schema_version']='2.0';d['origin_note']='2026-10-25 source-reading atlas; editorial additions are separately versioned.'
def clean(v):
 if isinstance(v,str):return v.replace(str(a.workspace)+'/','').replace('/home/lingxufeng/','~/')
 if isinstance(v,list):return [clean(x) for x in v]
 if isinstance(v,dict):return {k:clean(x) for k,x in v.items()}
 return v
(R/'data/base.json').write_text(json.dumps(clean(d),ensure_ascii=False,indent=2)+'\n')
(R/'data/sources.json').write_text(json.dumps(list(sources.values()),ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'cases':len(d['repos']),'cards':len(d['cards']),'images':len(media),'revision_mismatches':sum(e.get('revision_content_match') is False for c in d['cards'] for e in c['source_evidence'])}))
