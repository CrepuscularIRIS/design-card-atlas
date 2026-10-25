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

def render(prefix):
    cards = [json.loads(p.read_text()) for p in sorted((PUBLIC / 'cards').glob('*/card.json'))]
    lines = ['# Citadel · 视觉设计卡', '',
             '给 Crepuscular Citadel 的 3D 建模、电影感镜头与场景 UI 一组可以直接指着画面讨论的参考：看它如何组织光、尺度、材质和注意力。', '']
    lines += [' '.join(f'<a href="{prefix}{file}"><img src="{prefix}{file}" width="360" alt="{label}"></a>' for file, label, url in HEROES), '',
              ' · '.join(f'[{label}]({url})' for file, label, url in HEROES), '']
    lines += ['每张卡只讲一种视觉语言；图片点击看完整截图，作品名打开原作。先确定想要的感觉，再读拆解与迁移做法。', '',
              f'[视觉维度]({prefix}docs/DIMENSIONS.md) · [来源与筛选记录]({prefix}sources.md)', '']
    for group in GROUPS:
        rows = [c for c in cards if c['group'] == group]
        if not rows:
            continue
        lines += ['## ' + group, '']
        for c in rows:
            folder = prefix + 'cards/' + c['id'] + '/'
            lines += [f'### [{c["title"]}]({folder}README.md)', '', c['summary'], '']
            refs = [s for s in c['shots'] if s['role'] == 'reference'][:4]
            lines += [' '.join(f'<a href="{folder}{s["local"]}"><img src="{folder}{s["local"]}" width="280" alt="{s["work"]}：{s["proof"]}"></a>' for s in refs), '',
                      ' · '.join(f'[{s["work"]}]({s["url"]})' for s in refs), '',
                      '**用在博客：**' + c['blog'] + '。', '']
    recipes = sorted((PUBLIC / 'recipes').glob('*.md'))
    if recipes:
        lines += ['## 场景配方', '']
        for p in recipes:
            title = p.read_text().splitlines()[0].lstrip('# ')
            lines += [f'- [{title}]({prefix}recipes/{p.name})']
        lines += ['']
    lines += ['---', '', '图像保留原作者权利。卡内区分实际网页截图、作品视频帧与作者独立渲染成片；每张图的出处与复现方式见对应 SOURCE。', '']
    return '\n'.join(lines)

if __name__ == '__main__':
    (ROOT / 'README.md').write_text(render('public/'))
    (PUBLIC / 'README.md').write_text(render(''))
