#!/usr/bin/env python3
"""Publish the Markdown reel only; never generate a web application."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PUBLIC = ROOT / 'public'
GROUPS = ['光影', '色彩', '构图重心', '造型尺度', '材质', '水与大气', '镜头运动', '排版 UI']
HEROES = [
    ('references/kimi-videos/016-celestial-palace-33.376.jpg', '云上神殿与巨龙 · 用人物标定巨物', 'https://skillry.dev/ai-videos/kimi-k3-1/kimi-moonshot-068067-1'),
    ('references/strong-scenes/athenaion-author-shot1.jpg', 'Athenaion · 神殿、民居与山脉的尺度阶梯', 'https://github.com/Leonxlnx/athenaion'),
    ('references/kimi-videos/059-mist-colossi-1.788.jpg', '雾中巨像 · 近舟、暗水与层层远山', 'https://skillry.dev/ai-videos/kimi-k3-1/crangerus-549203'),
]

BANNER = ('cards/fog-separates-depth/shots/03.jpg', '清明上河 · 黄昏全城', 'https://silentfleetkk.github.io/qingming-bianjing/opus-5.5/qingming-bianjing.html')
ANCHORS = {g: g.lower().replace(' ', '-') for g in GROUPS}


def _img_row(items, prefix_img):
    """Three-column table: images on top, linked captions below."""
    cells = ''.join(f'<td width="33%" valign="top"><a href="{prefix_img(i)}"><img src="{prefix_img(i)}" width="100%" alt="{alt}"></a></td>'
                    for i, alt, _ in items)
    caps = ''.join(f'<td valign="top"><sub>{cap}</sub></td>' for _, _, cap in items)
    return ['<table>', f'<tr>{cells}</tr>', f'<tr>{caps}</tr>', '</table>', '']


def _recipe(p):
    lines = p.read_text().splitlines()
    title = lines[0].lstrip('# ')
    lead = next((l for l in lines[1:] if l.strip() and not l.startswith(('#', '|', '['))), '').replace('**', '')
    shot = next((l.split('](')[1].split(')')[0] for l in lines if '[![' in l), '')
    return title, lead, shot


def render(prefix):
    cards = [json.loads(p.read_text()) for p in sorted((PUBLIC / 'cards').glob('*/card.json'))]
    recipes = [(p, *_recipe(p)) for p in sorted((PUBLIC / 'recipes').glob('*.md'))]
    file, label, url = BANNER
    nav = ' · '.join(f'<a href="#{ANCHORS[g]}">{g}</a>' for g in GROUPS if any(c['group'] == g for c in cards))
    lines = ['<div align="center">', '',
             f'<a href="{prefix}{file}"><img src="{prefix}{file}" width="100%" alt="{label}"></a>', '',
             '# Citadel · 视觉设计卡', '',
             '**光 · 尺度 · 材质 · 镜头 · 排版**', '',
             '给 Crepuscular Citadel 的 3D 场景与 UI 的参考图册。<br>每张卡只讲一种视觉语言，配一组真实画面；指着图说「做成这样」。', '',
             f'<sub>{len(cards)} 张视觉卡 · {len(recipes)} 个场景配方 · 头图：<a href="{url}">{label}</a></sub>', '',
             nav + ' · <a href="#场景配方">场景配方</a>', '',
             '</div>', '', '<br>', '']
    lines += _img_row([(f, label, f'<a href="{u}">{label}</a>') for f, label, u in HEROES], lambda f: prefix + f)
    lines += ['| 1 · 找感觉 | 2 · 读拆解 | 3 · 组场景 |', '|---|---|---|',
              '| 先翻图，挑出和目标场景气质最接近的卡 | 卡内按光影、色彩、构图等维度拆开，给出色值、比例与源码参数 | 用配方把多张卡分到不同维度，检查光源、色彩与明暗是否打架 |', '',
              f'维度定义见 [视觉维度]({prefix}docs/DIMENSIONS.md)，每张图的出处与筛选结论见 [来源与筛选记录]({prefix}sources.md)。', '']
    for group in GROUPS:
        rows = [c for c in cards if c['group'] == group]
        if not rows:
            continue
        lines += ['<br>', '', f'## {group}', '']
        for c in rows:
            folder = prefix + 'cards/' + c['id'] + '/'
            refs = [s for s in c['shots'] if s['role'] == 'reference'][:3]
            lines += [f'### {c["title"]}', '', f'> {c["summary"]}', '']
            lines += _img_row([(s['local'], f'{s["work"]}：{s["proof"]}', f'<a href="{s["url"]}">{s["work"]}</a>') for s in refs],
                              lambda f, folder=folder: folder + f)
            lines += [f'<sub>**情绪** {c.get("mood", "")} · **用在博客** {c["blog"]} · <a href="{folder}README.md">拆解与做法 →</a></sub>', '']
    if recipes:
        lines += ['<br>', '', '## 场景配方', '', '把多张卡分配到不同维度，组成一个完整场景的情绪板与检查表。', '']
        items = []
        for p, title, lead, shot in recipes:
            img = str((PUBLIC / 'recipes' / shot).resolve().relative_to(PUBLIC)) if shot else ''
            items.append((img, title, f'<a href="{prefix}recipes/{p.name}"><b>{title}</b></a><br>{lead[:60]}{"…" if len(lead) > 60 else ""}'))
        lines += _img_row(items, lambda f: prefix + f)
    lines += ['---', '',
              '<sub>图像保留原作者权利，本库仅作设计研究与评论引用；每张图的出处、复现方式与图像类型（网页截图、视频帧、作者渲染）见各卡 SOURCE.md。'
              f'抽卡方法见 <a href="{"" if prefix else "../"}docs/VISUAL_CARD_PROMPT.md">提示词</a>；旧版机制卡归档在 <a href="{"" if prefix else "../"}archive/engineering-v1/">archive</a>。</sub>', '']
    return '\n'.join(lines)


if __name__ == '__main__':
    (ROOT / 'README.md').write_text(render('public/'))
    (PUBLIC / 'README.md').write_text(render(''))
