"""Read independently owned ledgers without changing their source schemas."""
import csv
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
COLLECTIONS=[
 ('Kimi guide', ['kimi-guide.csv'],83),
 ('Kimi videos',['kimi-videos-001-100.csv','kimi-videos-101-187.csv'],187),
 ('Kimi / Opus benchmark',['kimi-k31pro-opus55-benchmark-showcase.csv'],10),
 ('Opus frontend',['awesome-opus5.5-frontend-showcases.csv'],91),
 ('Opus usecases',['opus-usecases-000-170.csv','opus-usecases-171-220.csv','opus-usecases-221-400.csv','opus-usecases-401-441.csv','opus-usecases-442-552.csv','opus-usecases-553-662.csv'],663),
 ('Opus live demos',['opus55-live-demos.csv'],3),
 ('MG styles',['mg-styles-15.csv'],15),
]
def first(r,*keys):
 return next((r[k] for k in keys if r.get(k)), '')
def read_rows(name):
 p=ROOT/'screening'/name
 if not p.exists():return []
 rows=[]
 for r in csv.DictReader(p.open(encoding='utf-8-sig',newline='')):
  rows.append(dict(raw=r,ledger=name,id=first(r,'source_index','index','id'),title=first(r,'标题','title'),url=first(r,'链接/本地路径','url','source_url'),decision=first(r,'结论','conclusion','decision'),reason=first(r,'一句理由','reason'),shot=first(r,'截图文件','screenshot','screenshot_file'),observed=first(r,'browser_observed','viewed','viewed_scope')))
 return rows
