# Visual Reel rebuild — work state

Canonical specification: [VISUAL_CARD_PROMPT.md](VISUAL_CARD_PROMPT.md) v3. Active goal created 2026-10-25. Deliver Markdown, original frames, provenance and recipes. No new frontend.

## Directory ownership

| Agent | Independently owned screening file(s) | Reference directory |
|---|---|---|
| frontend_motion | opus-usecases-000-170.csv | opus-a |
| systems_assets | opus-usecases-171-220.csv; completed opus-usecases-442-552.csv and kimi-guide.csv | opus-a-tail, opus-c-guide |
| showcases | opus-usecases-221-400.csv | opus-b |
| rendering | opus-usecases-401-441.csv; completed Kimi videos101–187 and local frontend/benchmark/live/MG collections | opus-b-tail, kimi-videos-tail, local-collections |
| characters_narrative | completed kimi-videos-001-100.csv; final read-only editorial crosscheck | kimi-videos |
| scene_design | completed strong-scenes.csv, motion-extra.csv, opus-usecases-553-662.csv; independent new-card review | strong-scenes, opus-d |
| root | light-water.csv; selected cards, recipes, README, source indexes and validators | light-water |

Original broad Opus segments were split only at explicit handoff boundaries; no overlapping active CSV ownership. Historical handoff backups remain ignored under .local, not part of published screening. The current canonical list of segments is in scripts/visual_screening.py.

## Publication boundary

New content: public/cards/<id>/README.md + SOURCE.md + shots/, public/recipes/, public/docs/DIMENSIONS.md, public/sources.md. Root README and public/README are visual Reels with adjusted relative links. public/ names a directory; remote visibility remains private.

Old257 mechanism cards remain engineering background. The old application and README are archived under archive/engineering-v1. Do not run scripts/build.py: it regenerates the old README. The new scripts/build_visual_readme.py publishes Markdown only.

## Evidence rules

- Keep entries pending until actually observed, except clearly nonvisual title/description exclusions. A browser-tool outage does not mean the artwork failed.
- Video entries were sampled at recorded moments, not watched continuously end-to-end. Timestamped source frames are valid only after observation; posters and editorial contact sheets are excluded.
- Athenaion selected images are independent author-rendered final frames, explicitly not this round's runtime screenshots.
- Native capture sizes are recorded. Shared browser connection instability prevented a universal1920×1080 viewport; images retain native dimensions with long edge at least1920. No upscale or invented viewport claims.
- Dynamic frames identify actual state and observed scope; exact time-dependent pixels are not promised reproducible.
- Recipes propose Blog scene changes. They do not claim an implementation or restore retired navigation routes. Characters remain2D screen-space.

## Editorial decisions

25 formal cards; warm-stone-cool-shadow moved to public/candidates because only one positive frame proves the stated relation. Do not replenish it with near-duplicate frames. Independent visual review and responses are in screening/visual-editorial-review.md and screening/visual-editorial-resolution.md.

Final collection completeness is determined by the live CSV files and scripts/check_visual_cards.py. The checker validates structure, links, source bytes and screening coverage; it is not an aesthetic or full-runtime verdict. sources.md is regenerated from these files and carries the numerical audit, while the README stays image-led.

## Git archive scope

The14 explicitly recommended Pro repos have verified localHEAD/origin records. New qingming-bianjing, clearwater and falcon9-blender clones completed. New cybercity and ProceduralBuildingsThreeJS have fixedHEAD and source checkout, with large media/assets excluded; this is not a full asset archive. Exact records: public/pro-git-recheck.json and public/new-source-clones.json.
