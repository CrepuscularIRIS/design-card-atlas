"""Structural/provenance checks. Does not certify visual quality."""
import hashlib,json,re,sys
from pathlib import Path
R=Path(__file__).resolve().parents[1];d=json.loads((R/'data/catalog.json').read_text());errors=[]
def require(ok,msg):
 if not ok:errors.append(msg)
ids={c['id'] for c in d['cards']};repos={c['repo'] for c in d['cases']};lenses={l['id'] for l in d['lenses']}
require(len(ids)==len(d['cards']),'duplicate card IDs')
for c in d['cards']:
 require(c['repo'] in repos,f"{c['id']} unknown repo")
 for key in ['principle','implementation','conditions','failure_modes','minimum_test','source_evidence'] :require(bool(c.get(key)),f"{c['id']} missing {key}")
 require(all(x in lenses for x in c['lens_ids']),f"{c['id']} unknown lens")
 for e in c['source_evidence']:
  require(e.get('revision_content_match') is not False,f"{c['id']} pinned source mismatch")
for c in d['cards']:
 for v in c['images']:
  if 'card_ids' in v:require(c['id'] in v['card_ids'],f"{c['id']} mismatched subwork image")
for l in d['lenses']:
 require(all(i in ids for i in l['card_ids']),f"{l['id']} unknown card")
 require(all(x in repos for x in l['case_repos']),f"{l['id']} unknown repo")
for m in d['patterns']:require(all(i in ids for i in m['subcards']),f"{m['id']} unknown card")
for t in d['trajectories']:
 require(len(t['steps'])>=3,f"{t['id']} too short")
 for s in t['steps']:require(all(i in ids for i in s['card_ids']),f"{t['id']} unknown card")
for v in d['visuals']:
 p=R/v['path'];require(p.is_file(),f"missing image {v['path']}")
 if p.exists():require(hashlib.sha256(p.read_bytes()).hexdigest()==v['sha256'],f"changed image {v['path']}")
 require(bool(v.get('observation') and v.get('scope') and v.get('rights')),f"incomplete image provenance {v['path']}")
for p in list((R/'cards').glob('*.md'))+list((R/'cases').glob('*.md'))+list((R/'patterns').glob('*.md'))+list((R/'lenses').glob('*.md'))+list((R/'docs').glob('*.md'))+[R/'README.md']:
 if not p.exists():errors.append(f'missing {p.name}');continue
 for link in re.findall(r'\]\(([^)]+)\)',p.read_text()):
  if '://' in link or link.startswith('#'):continue
  require((p.parent/link.split('#')[0]).exists(),f"broken local link {p.relative_to(R)}: {link}")
for p in [R/'data/catalog.json',R/'README.md']:
 if p.exists():require('/home/lingxufeng/' not in p.read_text(),f'absolute private workspace path in {p.name}')
r={'schema_version':'2.0','counts':d['stats'],'pro_recommendations':len(d.get('pro_reconciliation',[])),'errors':errors,'scope':'schema, immutable source pointers, image hashes and local links; browser actions checked separately; no source-project runtime certification'}
(R/'evidence/check.json').write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n');print(json.dumps(r,ensure_ascii=False,indent=2));sys.exit(bool(errors))
