# Design Card Atlas

This is a domain induction library, not a leaderboard or a collection of effects to combine indiscriminately.

- Canonical imported material: `data/base.json`; source pinning: `data/sources.json`.
- Editorial additions: `data/editorial/*.json`; keep source fact, observed image, design inference, and proposed test separate.
- Never invent an effect image. Reference input, logo, author screenshot, historical runtime screenshot, and local video frame are different evidence types.
- Movie and frontend verdicts are independent and concern transfer suitability, not universal quality.
- Each mechanism needs conditions, failure modes and a discriminating comparison. Expand dimensions through actual case differences, not synonyms.
- Images retain their upstream rights. Do not apply this repository's code license to media or source projects.
- Run `python3 scripts/build.py` and `python3 scripts/check.py` after edits. Preview with `python3 -m http.server 3081 --bind 127.0.0.1`.
- The repo works without the original local source tree. Use immutable source URLs when available; never add credentials, private prompts, machine paths or source repo working trees.
- Source projects can be restored separately using `scripts/fetch_sources.py`; they are not embedded or recursively mirrored.
