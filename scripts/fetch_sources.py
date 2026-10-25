"""Restore pinned references outside this repository. No source code is executed."""
import argparse,json,subprocess
from pathlib import Path
p=argparse.ArgumentParser();p.add_argument('--dest',type=Path,required=True);p.add_argument('--pro-only',action='store_true');p.add_argument('--execute',action='store_true',help='Without this, print a dry-run manifest.');a=p.parse_args()
r=Path(__file__).resolve().parents[1];sources=json.loads((r/'data/sources.json').read_text());audit=json.loads((r/'data/editorial/sources-audit.json').read_text());pro={x['repo'] for x in audit['pro_reconciliation']};dest=a.dest.expanduser().resolve()
if dest==r or r in dest.parents:raise SystemExit('Choose a directory outside the atlas repo; do not nest upstream working trees.')
for s in sources:
 if not s['is_git'] or not s['origin'] or (a.pro_only and s['repo'] not in pro):continue
 target=dest/s['repo'];pin=s['analysis_revision']
 print(s['repo'],pin,s['origin'],str(target))
 if not a.execute:continue
 if target.exists():print('  existing: preserved without checkout or reset');continue
 target.mkdir(parents=True)
 subprocess.run(['git','init','--quiet',str(target)],check=True)
 subprocess.run(['git','-C',str(target),'remote','add','origin',s['origin']],check=True)
 subprocess.run(['git','-C',str(target),'fetch','--depth=1','origin',pin],check=True)
 subprocess.run(['git','-C',str(target),'checkout','--detach','FETCH_HEAD'],check=True)
