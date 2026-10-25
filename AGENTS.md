# Visual cards for Crepuscular Citadel

Canonical specification: `docs/VISUAL_CARD_PROMPT.md` (v3). Read it before editing.

- README is the visual Reel. Do not build a frontend or drawing interface.
- A card is one visual language, not a repository, implementation trick, or code component.
- New publishable material lives in `public/`: cards, recipes, sources and dimension guide. Root README links into it.
- Each selected card needs 3–8 real observed artwork screenshots, visible meaning, at least four concrete visual dimensions, and a specific current Citadel destination. Prefer multiple works per language.
- Reject posters, logos, loading/error screens, editor/settings screenshots, generic 2D tools, and visually weak frames. Never invent an image or silently upscale a low-resolution source.
- Browser-observe every visually eligible collection entry. Record nonvisual filtering, accepted/rejected/inaccessible decisions; unseen items remain pending. Source code or HTTP response is not a visual observation.
- Record each frame's source, original URL, route, actions/camera/time, capture date, dimensions and rights in SOURCE.md. Distinguish pixel estimates, measured values, source parameters and proposed transfer parameters.
- Preserve original 257 mechanism cards as engineering background only; never count them as new visual cards. Old application is archived in archive/engineering-v1.
- Do not run the legacy scripts/build.py: it overwrites the new README. Use the visual publishing/check scripts when created.
- Source repositories are read-only. Respect Blog/PORTS.md and avoid occupied ports 3025/3026. Use --strictPort for Vite.
- Workers own separate screening CSVs and reference folders. Do not overwrite others' work.
- Root README must not be a statistics dashboard: large clickable pictures, clear card meaning, and Blog use first. Keep provenance and completeness details in sources/screening.
