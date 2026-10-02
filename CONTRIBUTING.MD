# Contributing to OpenText Studio

Thanks for your interest! Contributions of any size are welcome.

## Ground rules

- Be kind. See [Contributor Covenant](https://www.contributor-covenant.org/).
- Keep the tool **dependency-free** (stdlib only). This is a hard rule.
- Keep the **UI in English**. Output can be any language.
- Keep files self-contained — a user should be able to copy `studio.py` alone
  and run it.

## How to contribute

1. Fork the repo.
2. Create a feature branch:
   ```bash
   git checkout -b feat/my-new-animation
   ```
3. Make your changes.
4. Test:
   ```bash
   python3 studio.py
   # enter some text, check the generated folders
   cat 12345/text/shadow.txt
   python3 12345/anim/pulse.py
   ```
5. Commit with a clear message (see below).
6. Open a Pull Request.

## Commit message style

Loosely follows [Conventional Commits](https://www.conventionalcommits.org/):

```
feat: add zoom_in animation
fix: correct Cyrillic 'Й' bitmap
docs: clarify embed example
refactor: split renderer from writer
```

## Adding a new animation

1. Open `studio.py`.
2. Add a new entry to `ANIM_BODIES`. The body must define `_run(**kwargs)`
   and may reference `ART`, `COLORS`, `sys`, `time`.
3. If the animation needs a gradient to look right, add its key to
   `GRADIENT_ONLY`.
4. Register it in `anim_specs` inside `build()`.
5. Update `README.md` and `CHANGELOG.md`.

## Adding a new font style

1. Add an entry to `FONT_STYLES` (5×5) — or a new dict if it's a
   different-height font like `SHADOW_FONT`.
2. Add a renderer if needed.
3. Register in `static_specs` inside `build()`.

## Adding a new Cyrillic glyph

Find a hole in `FONT_5X5`, add 5 rows of `0`/`1`, exactly 5 chars each.
Please keep the visual weight consistent with neighbours.

## Reporting bugs

Open an issue with:
- OS + terminal (e.g. `Ubuntu 24.04 / GNOME Terminal`)
- Python version (`python3 --version`)
- The exact command you ran
- Expected vs actual output
- Screenshot if it's a rendering issue

## License

By contributing, you agree your work is released under the [MIT License](LICENSE).
