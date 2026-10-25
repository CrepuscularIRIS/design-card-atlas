#!/usr/bin/env python3
"""Structural acceptance only. Passing this does not verify visual taste."""
import collections
import json
import hashlib
import re
from pathlib import Path
from PIL import Image
from urllib.parse import unquote, urlsplit
from visual_screening import COLLECTIONS, read_rows

ROOT = Path(__file__).resolve().parents[1]
cards = []
errors = []
for p in sorted((ROOT / 'public/cards').glob('*/card.json')):
    c = json.loads(p.read_text())
    cards.append(c)
    refs = [s for s in c['shots'] if s['role'] == 'reference']
    bad = [s for s in c['shots'] if s['role'] == 'counterexample']
    if not 3 <= len(refs) <= 8:
        errors.append(f'{c["id"]}: requires 3–8 reference frames')
    if not 1 <= len(bad) <= 2:
        errors.append(f'{c["id"]}: requires 1–2 visual counterexamples')
    if len(c['dimensions']) < 4:
        errors.append(f'{c["id"]}: requires at least four concrete dimensions')
    for s in c['shots']:
        file = p.parent / s['local']
        if not file.exists():
            errors.append(f'missing: {file}')
        elif max(Image.open(file).size) < 1920:
            errors.append(f'long edge below 1920: {file}')
        else:
            if list(Image.open(file).size) != s['dimensions']:
                errors.append(f'dimension metadata mismatch: {file}')
            original = ROOT / 'public/references' / s['file']
            if not original.exists() or hashlib.sha256(file.read_bytes()).digest() != hashlib.sha256(original.read_bytes()).digest():
                errors.append(f'card copy differs from archived source: {file}')
        if not s.get('work_id'):
            errors.append(f'{c["id"]}: missing canonical work_id')
    body = (p.parent/'README.md').read_text()
    for section in ['一句话', '看哪里', '拆解', '做法', '迁移到博客', '反例']:
        if '## '+section not in body:
            errors.append(f'{c["id"]}: missing section {section}')
    for name in ['README.md', 'SOURCE.md']:
        if not (p.parent/name).exists():
            errors.append(f'missing: {p.parent/name}')
coverage = collections.Counter(c['dimension'] for c in cards)
multi = sum(len({s.get('work_id',s['url']) for s in c['shots'] if s['role']=='reference'}) >= 2 for c in cards)
pending = []
if not 25 <= len(cards) <= 35:
    pending.append(f'cards {len(cards)} / required 25–35')
for dim in 'ABCDEFGH':
    if coverage[dim] < 2:
        pending.append(f'{dim}: {coverage[dim]} / required 2')
if multi * 2 < len(cards):
    pending.append('fewer than half of cards have multiple works')
recipes = list((ROOT/'public/recipes').glob('*.md'))
if len(recipes) != 3:
    pending.append(f'recipes {len(recipes)} / required 3')
# Exact coverage and conclusions matter separately from the number of cards.
screening = {}
for name, files, expected in COLLECTIONS:
    rows = sum([read_rows(f) for f in files], [])
    unresolved = [r['id'] for r in rows if r['decision'] not in ('收','不收','打不开')]
    screening[name] = {'rows':len(rows), 'expected':expected, 'unresolved':len(unresolved)}
    if len(rows) != expected or len({r['id'] for r in rows}) != expected:
        pending.append(f'{name}: coverage or duplicate-id mismatch')
    if unresolved:
        pending.append(f'{name}: {len(unresolved)} unresolved entries')
    for r in rows:
        if not r['reason'].strip():
            errors.append(f'{r["ledger"]}:{r["id"]}: missing decision reason')
for name in ['strong-scenes.csv','light-water.csv','motion-extra.csv']:
    rows=read_rows(name)
    if not rows or any(r['decision'] not in ('收','不收','打不开') for r in rows):
        pending.append(f'{name}: missing or unresolved named sources')
# Resolve Markdown/HTML local targets, including linked original images.
documents = [ROOT/'README.md', ROOT/'sources.md'] + list((ROOT/'public').rglob('*.md'))
for doc in documents:
    content=doc.read_text()
    targets=re.findall(r'\]\(([^)]+)\)',content)+re.findall(r'(?:src|href)="([^"]+)"',content)
    for target in targets:
        target=target.strip().strip('<>')
        if not target or urlsplit(target).scheme or target.startswith('#'):
            continue
        local=unquote(target.split('#',1)[0].split('?',1)[0])
        if not (doc.parent/local).exists():
            errors.append(f'broken local link: {doc.relative_to(ROOT)} -> {target}')
print(json.dumps({'structural_errors': errors, 'incomplete_delivery_requirements': pending,
                  'cards':len(cards),'multi_work_cards':multi,'coverage':dict(coverage),'screening':screening,
                  'note': 'Requires separate visual review and complete screening CSV audit.'}, ensure_ascii=False, indent=2))
raise SystemExit(1 if errors else 2 if pending else 0)
