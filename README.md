# OpenText Studio

> Turn any text into colored ASCII art — static files **and** runnable animations.  
> ENG + RUS supported in output. English-only UI.

```
┌──────────────────────────────────────────────────────────┐
│                                                          │
│  ██████╗ ██████╗ ███████╗███╗   ██╗████████╗███████╗██╗  │
│  ██╔═══██╗██╔══██╗██╔════╝████╗  ██║╚══██╔══╝██╔════╝╚██╗ │
│  ██║   ██║██████╔╝█████╗  ██╔██╗ ██║   ██║   █████╗   ╚██╗│
│  ██║   ██║██╔═══╝ ██╔══╝  ██║╚██╗██║   ██║   ██╔══╝   ██╔╝│
│  ╚██████╔╝██║     ███████╗██║ ╚████║   ██║   ███████╗██╔╝ │
│   ╚═════╝ ╚═╝     ╚══════╝╚═╝  ╚═══╝   ╚═╝   ╚══════╝╚═╝  │
│                                                          │
│                      by magic4n                          │
└──────────────────────────────────────────────────────────┘
```

## Features

- **Two output types**
  - `text/` — static colored ASCII art, viewable with `cat`
  - `anim/` — runnable Python animations, also embeddable as modules
- **6 rendering styles**
  - 5×5 bitmap font (Latin / Cyrillic / digits / punctuation)
  - ANSI Shadow font (block letters, ENG)
  - Boxed panel variant
- **17 colors**: 16 ANSI + 4 gradients (`fire`, `ocean`, `forest`, `rainbow`)
- **11 animation types**: typewriter, pulse, rainbow sweep, fade-in,
  slide-left, blink, row-by-row, wave, sparkle, gradient cycle, boxed logo
- **No dependencies** — pure Python 3.7+ standard library
- **Cross-platform** — enables ANSI (VT) on Windows 10+ automatically

## Requirements

- Python **3.7+**
- A terminal that supports ANSI escape codes (Linux, macOS, Windows Terminal,
  or Win10+ `cmd` / `PowerShell`)
- UTF-8 capable terminal for Cyrillic output

## Install

No install needed. Just grab the script:

```bash
git clone https://github.com/magic4n/opentext-studio.git
cd opentext-studio
```

## Usage

```bash
python3 studio.py
```

You'll be prompted for the text to render (ENG or RUS). A new folder named
with **5 random digits** is created next to the script:

```
12345/
├── text/
│   ├── solid.txt
│   ├── hash.txt
│   ├── at.txt
│   ├── shade.txt
│   ├── star.txt
│   ├── solid_big.txt
│   ├── shadow.txt
│   ├── shadow_rainbow.txt
│   └── shadow_box.txt
└── anim/
    ├── typewriter.py
    ├── pulse.py
    ├── rainbow_sweep.py
    ├── fade_in.py
    ├── slide_left.py
    ├── blink.py
    ├── row_by_row.py
    ├── wave.py
    ├── sparkle.py
    ├── gradient_cycle.py
    └── logo_animated.py
```

### View static art

```bash
cat 12345/text/shadow.txt
```

> The `.txt` files contain ANSI escape codes. In a terminal you'll see colors.
> In a plain text editor you'll see raw codes — that's expected.

### Run an animation

```bash
python3 12345/anim/logo_animated.py
```

### Embed an animation in your own script

Every generated `anim/*.py` is a valid module:

```python
# INSERT THIS IN IMPORTS:
import logo_animated

# MAIN ANIM:
logo_animated.animate()
```

Optional keyword args are passed through to `_run()`:

```python
logo_animated.animate(char_delay=0.005, row_delay=0.1)
```

## Embedding example

```python
# main.py
import sys, time
import logo_animated

def boot():
    print("Starting up...")
    logo_animated.animate()

if __name__ == "__main__":
    boot()
```

## License

[MIT](LICENSE) © 2026 magic4n

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md).
