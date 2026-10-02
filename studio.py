#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
OpenText Studio
- Creates output folder named with 5 random digits
- Subfolders: text/ (static) and anim/ (runnable scripts)
- All variations are generated automatically
- UI language: English. Output supports ENG + RUS.
"""

import os
import random
import sys

# Windows VT (ANSI) enable
if sys.platform == "win32":
    try:
        import ctypes
        _k = ctypes.windll.kernel32
        _k.SetConsoleMode(_k.GetStdHandle(-11), 7)
    except Exception:
        pass

RESET = "\033[0m"
def fg(n): return "\033[%dm" % n

ANSI_16 = {
    "black":30,"red":31,"green":32,"yellow":33,"blue":34,"magenta":35,
    "cyan":36,"white":37,"bright_black":90,"bright_red":91,
    "bright_green":92,"bright_yellow":93,"bright_blue":94,
    "bright_magenta":95,"bright_cyan":96,"bright_white":97,
}
GRADIENTS = {
    "fire":    [91, 93, 33, 31],
    "ocean":   [94, 96, 36, 34],
    "forest":  [92, 32, 36, 92],
    "rainbow": [91, 93, 92, 96, 94, 95],
}

# =============================================================
# 5x5 BITMAP FONT (ENG + RUS + digits + punct)
# =============================================================
FONT_5X5 = {
    'A':["01110","10001","11111","10001","10001"],
    'B':["11110","10001","11110","10001","11110"],
    'C':["01111","10000","10000","10000","01111"],
    'D':["11110","10001","10001","10001","11110"],
    'E':["11111","10000","11110","10000","11111"],
    'F':["11111","10000","11110","10000","10000"],
    'G':["01111","10000","10111","10001","01111"],
    'H':["10001","10001","11111","10001","10001"],
    'I':["11111","00100","00100","00100","11111"],
    'J':["00111","00010","00010","10010","01100"],
    'K':["10001","10010","11100","10010","10001"],
    'L':["10000","10000","10000","10000","11111"],
    'M':["10001","11011","10101","10001","10001"],
    'N':["10001","11001","10101","10011","10001"],
    'O':["01110","10001","10001","10001","01110"],
    'P':["11110","10001","11110","10000","10000"],
    'Q':["01110","10001","10101","10010","01101"],
    'R':["11110","10001","11110","10010","10001"],
    'S':["01111","10000","01110","00001","11110"],
    'T':["11111","00100","00100","00100","00100"],
    'U':["10001","10001","10001","10001","01110"],
    'V':["10001","10001","10001","01010","00100"],
    'W':["10001","10001","10101","11011","10001"],
    'X':["10001","01010","00100","01010","10001"],
    'Y':["10001","01010","00100","00100","00100"],
    'Z':["11111","00010","00100","01000","11111"],
    '0':["01110","10011","10101","11001","01110"],
    '1':["00100","01100","00100","00100","01110"],
    '2':["01110","10001","00110","01000","11111"],
    '3':["11110","00001","01110","00001","11110"],
    '4':["00010","00110","01010","11111","00010"],
    '5':["11111","10000","11110","00001","11110"],
    '6':["01110","10000","11110","10001","01110"],
    '7':["11111","00001","00010","00100","01000"],
    '8':["01110","10001","01110","10001","01110"],
    '9':["01110","10001","01111","00001","01110"],
    ' ':["00000","00000","00000","00000","00000"],
    '.':["00000","00000","00000","00000","00100"],
    ',':["00000","00000","00000","00100","01000"],
    '!':["00100","00100","00100","00000","00100"],
    '?':["01110","10001","00110","00000","00100"],
    '-':["00000","00000","11111","00000","00000"],
    '_':["00000","00000","00000","00000","11111"],
    ':':["00000","00100","00000","00100","00000"],
    '+':["00000","00100","11111","00100","00000"],
    '/':["00001","00010","00100","01000","10000"],
    'А':["01110","10001","11111","10001","10001"],
    'Б':["11111","10000","11110","10001","11110"],
    'В':["11110","10001","11110","10001","11110"],
    'Г':["11111","10000","10000","10000","10000"],
    'Д':["00110","01010","01010","11111","10001"],
    'Е':["11111","10000","11110","10000","11111"],
    'Ё':["01010","11111","10000","11110","11111"],
    'Ж':["10101","10101","11111","10101","10101"],
    'З':["11110","00001","01110","00001","11110"],
    'И':["10001","10011","10101","11001","10001"],
    'Й':["01010","10011","10101","11001","10001"],
    'К':["10001","10010","11100","10010","10001"],
    'Л':["00110","01010","01010","01010","10001"],
    'М':["10001","11011","10101","10001","10001"],
    'Н':["10001","10001","11111","10001","10001"],
    'О':["01110","10001","10001","10001","01110"],
    'П':["11111","10001","10001","10001","10001"],
    'Р':["11110","10001","11110","10000","10000"],
    'С':["01111","10000","10000","10000","01111"],
    'Т':["11111","00100","00100","00100","00100"],
    'У':["10001","10001","01111","00001","11110"],
    'Ф':["00100","01110","10101","11111","01110"],
    'Х':["10001","01010","00100","01010","10001"],
    'Ц':["10001","10001","10001","11111","00001"],
    'Ч':["10001","10001","01111","00001","00001"],
    'Ш':["10101","10101","10101","10101","11111"],
    'Щ':["10101","10101","10101","11111","00001"],
    'Ъ':["11000","01000","01110","01001","01110"],
    'Ы':["10001","10001","11101","10011","11101"],
    'Ь':["10000","10000","11110","10001","11110"],
    'Э':["01110","10001","00111","10001","01110"],
    'Ю':["10100","10110","11101","10101","10110"],
    'Я':["01111","10001","01111","00101","10001"],
}

# =============================================================
# ANSI SHADOW FONT (6 rows per glyph) — ENG only
# Cyrillic falls back to 5x5 scaled x2 automatically.
# =============================================================
SHADOW_FONT = {
    'A':(" █████╗ ","██╔══██╗","███████║","██╔══██║","██║  ██║","╚═╝  ╚═╝"),
    'B':("██████╗ ","██╔══██╗","██████╔╝","██╔══██╗","██████╔╝","╚═════╝ "),
    'C':(" ██████╗","██╔════╝","██║     ","██║     ","╚██████╗"," ╚═════╝"),
    'D':("██████╗ ","██╔══██╗","██║  ██║","██║  ██║","██████╔╝","╚═════╝ "),
    'E':("███████╗","██╔════╝","█████╗  ","██╔══╝  ","███████╗","╚══════╝"),
    'F':("███████╗","██╔════╝","█████╗  ","██╔══╝  ","██║     ","╚═╝     "),
    'G':(" ██████╗ ","██╔════╝ ","██║  ███╗","██║   ██║","╚██████╔╝"," ╚═════╝ "),
    'H':("██╗  ██╗","██║  ██║","███████║","██╔══██║","██║  ██║","╚═╝  ╚═╝"),
    'I':("██╗","██║","██║","██║","██║","╚═╝"),
    'J':("     ██╗","     ██║","     ██║","██   ██║","╚█████╔╝"," ╚════╝ "),
    'K':("██╗  ██╗","██║ ██╔╝","█████╔╝ ","██╔═██╗ ","██║  ██╗","╚═╝  ╚═╝"),
    'L':("██╗     ","██║     ","██║     ","██║     ","███████╗","╚══════╝"),
    'M':("███╗   ███╗","████╗ ████║","██╔████╔██║","██║╚██╔╝██║","██║ ╚═╝ ██║","╚═╝     ╚═╝"),
    'N':("███╗   ██╗","████╗  ██║","██╔██╗ ██║","██║╚██╗██║","██║ ╚████║","╚═╝  ╚═══╝"),
    'O':(" ██████╗ ","██╔═══██╗","██║   ██║","██║   ██║","╚██████╔╝"," ╚═════╝ "),
    'P':("██████╗ ","██╔══██╗","██████╔╝","██╔═══╝ ","██║     ","╚═╝     "),
    'Q':(" ██████╗ ","██╔═══██╗","██║   ██║","██║▄▄ ██║","╚██████╔╝"," ╚══▀▀═╝ "),
    'R':("██████╗ ","██╔══██╗","██████╔╝","██╔══██╗","██║  ██║","╚═╝  ╚═╝"),
    'S':("███████╗","██╔════╝","███████╗","╚════██║","███████║","╚══════╝"),
    'T':("████████╗","╚══██╔══╝","   ██║   ","   ██║   ","   ██║   ","   ╚═╝   "),
    'U':("██╗   ██╗","██║   ██║","██║   ██║","██║   ██║","╚██████╔╝"," ╚═════╝ "),
    'V':("██╗   ██╗","██║   ██║","██║   ██║","╚██╗ ██╔╝"," ╚████╔╝ ","  ╚═══╝  "),
    'W':("██╗    ██╗","██║    ██║","██║ █╗ ██║","██║███╗██║","╚███╔███╔╝"," ╚══╝╚══╝ "),
    'X':("██╗  ██╗","╚██╗██╔╝"," ╚███╔╝ "," ██╔██╗ ","██╔╝ ██╗","╚═╝  ╚═╝"),
    'Y':("██╗   ██╗","╚██╗ ██╔╝"," ╚████╔╝ ","  ╚██╔╝  ","   ██║   ","   ╚═╝   "),
    'Z':("███████╗","╚══███╔╝","  ███╔╝ "," ███╔╝  ","███████╗","╚══════╝"),
    '0':(" ██████╗ ","██╔═████╗","██║██╔██║","████╔╝██║","╚██████╔╝"," ╚═════╝ "),
    '1':(" ██╗","███║","╚██║"," ██║"," ██║"," ╚═╝"),
    '2':("██████╗ ","╚════██╗"," █████╔╝","██╔═══╝ ","███████╗","╚══════╝"),
    '3':("██████╗ ","╚════██╗"," █████╔╝"," ╚═══██╗","██████╔╝","╚═════╝ "),
    '4':("██╗  ██╗","██║  ██║","███████║","╚════██║","     ██║","     ╚═╝"),
    '5':("███████╗","██╔════╝","███████╗","╚════██║","███████║","╚══════╝"),
    '6':(" ██████╗ ","██╔════╝ ","███████╗ ","██╔═══██╗","╚██████╔╝"," ╚═════╝ "),
    '7':("███████╗","╚════██║","    ██╔╝","   ██╔╝ ","   ██║  ","   ╚═╝  "),
    '8':(" █████╗ ","██╔══██╗","╚█████╔╝","██╔══██╗","╚█████╔╝"," ╚════╝ "),
    '9':(" █████╗ ","██╔══██╗","╚██████║"," ╚═══██║"," █████╔╝"," ╚════╝ "),
    ' ':(8*" ",8*" ",8*" ",8*" ",8*" ",8*" "),
    '!':("██╗","██║","██║","╚═╝","██╗","╚═╝"),
    '?':(" ██████╗ ","██╔═══██╗","     ██╔╝","    ██╔╝ ","    ╚═╝  ","    ██╗  "),
    '.':("   ","   ","   ","   ","██╗","╚═╝"),
    ',':("   ","   ","   ","   ","██╗","╚═╝"),
    '-':("       ","       ","██████╗","╚═════╝","       ","       "),
    ':':("   ","██╗","╚═╝","██╗","╚═╝","   "),
}

# =============================================================
# RENDERERS
# =============================================================
def render_5x5(text, fill_char, scale=1):
    scale = max(1, int(scale))
    rows = [""] * 5
    for ch in text.upper():
        bm = FONT_5X5.get(ch, FONT_5X5['?'])
        for i in range(5):
            rows[i] += bm[i] + " "
    out = []
    for r in rows:
        scaled = "".join((fill_char if c == '1' else ' ') * scale for c in r)
        for _ in range(scale):
            out.append(scaled)
    return out


def render_shadow(text):
    """6-row shadow style. Falls back to 5x5-upscaled for unknown chars."""
    rows = [""] * 6
    for ch in text.upper():
        g = SHADOW_FONT.get(ch)
        if g:
            for i in range(6):
                rows[i] += g[i]
        else:
            # fallback: 5x5 upscaled 2x, padded to 6 rows
            bm = FONT_5X5.get(ch, FONT_5X5['?'])
            up = []
            for r in bm:
                up.append("".join(c * 2 for c in r))
                up.append("".join(c * 2 for c in r))
            # up has 10 rows, take 6 (centered-ish): rows 1..6
            for i in range(6):
                rows[i] += up[i + 2] + " "
    return rows


def colorize_solid(lines, code):
    return ["%s%s%s" % (fg(code), ln, RESET) for ln in lines]


def colorize_gradient(lines, codes):
    out = []
    for ln in lines:
        n = len(ln)
        if n == 0:
            out.append(ln)
            continue
        buf = []
        for i, c in enumerate(ln):
            idx = (i * len(codes)) // n
            if idx >= len(codes):
                idx = len(codes) - 1
            buf.append(fg(codes[idx]))
            buf.append(c)
        buf.append(RESET)
        out.append("".join(buf))
    return out


def colorize_perrow(lines, codes):
    """Each row gets next color from the palette (like the logo example)."""
    out = []
    for i, ln in enumerate(lines):
        out.append("%s%s%s" % (fg(codes[i % len(codes)]), ln, RESET))
    return out


def boxed(plain_lines, color_fn):
    """Return list of strings forming a boxed panel around colored content."""
    inner = max((len(l) for l in plain_lines), default=0) + 2
    GRAY = fg(90)
    out = [GRAY + "┌" + "─" * inner + "┐" + RESET,
           GRAY + "│" + RESET + " " * inner + GRAY + "│" + RESET]
    for ln in plain_lines:
        colored = color_fn(ln)
        pad = inner - 2 - len(ln)
        if pad < 0:
            pad = 0
        out.append(GRAY + "│" + RESET + "  " + colored + " " * pad
                   + GRAY + "│" + RESET)
    out.append(GRAY + "│" + RESET + " " * inner + GRAY + "│" + RESET)
    out.append(GRAY + "└" + "─" * inner + "┘" + RESET)
    return out


# =============================================================
# ANIMATION BODIES
# =============================================================
ANIM_BODIES = {

"typewriter": r'''
def _run(delay=0.004):
    for line in ART:
        for ch in line:
            sys.stdout.write(ch)
            sys.stdout.flush()
            time.sleep(delay)
        sys.stdout.write("\n")
    sys.stdout.flush()
''',

"pulse": r'''
def _run(interval=0.25, cycles=20):
    for i in range(cycles):
        code = COLORS[i % len(COLORS)]
        sys.stdout.write("\033[H\033[J")
        for line in ART:
            sys.stdout.write("\033[%dm%s\033[0m\n" % (code, line))
        sys.stdout.flush()
        time.sleep(interval)
''',

"rainbow_sweep": r'''
def _run(interval=0.06, cycles=32):
    offset = 0
    for _ in range(cycles):
        sys.stdout.write("\033[H\033[J")
        for line in ART:
            s = []
            for i, ch in enumerate(line):
                idx = (i + offset) % len(COLORS)
                s.append("\033[%dm%s" % (COLORS[idx], ch))
            sys.stdout.write("".join(s) + "\033[0m\n")
        sys.stdout.flush()
        offset += 1
        time.sleep(interval)
''',

"fade_in": r'''
def _run(hold=0.2):
    for shade in (90, 37, 97):
        sys.stdout.write("\033[H\033[J")
        for line in ART:
            sys.stdout.write("\033[%dm%s\033[0m\n" % (shade, line))
        sys.stdout.flush()
        time.sleep(hold)
    sys.stdout.write("\033[H\033[J")
    for line in ART:
        sys.stdout.write("\033[%dm%s\033[0m\n" % (COLORS[0], line))
    sys.stdout.flush()
''',

"slide_left": r'''
def _run(delay=0.03):
    width = max((len(l) for l in ART), default=0)
    for pad in range(width, -1, -4):
        sys.stdout.write("\033[H\033[J")
        for line in ART:
            sys.stdout.write("\033[%dm%s%s\033[0m\n"
                             % (COLORS[0], " " * pad, line))
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write("\033[H\033[J")
    for line in ART:
        sys.stdout.write("\033[%dm%s\033[0m\n" % (COLORS[0], line))
    sys.stdout.flush()
''',

"blink": r'''
def _run(interval=0.35, cycles=10):
    for i in range(cycles):
        sys.stdout.write("\033[H\033[J")
        code = COLORS[i % len(COLORS)] if (i % 2 == 0) else 30
        for line in ART:
            sys.stdout.write("\033[%dm%s\033[0m\n" % (code, line))
        sys.stdout.flush()
        time.sleep(interval)
    sys.stdout.write("\033[H\033[J")
    for line in ART:
        sys.stdout.write("\033[%dm%s\033[0m\n" % (COLORS[0], line))
    sys.stdout.flush()
''',

"row_by_row": r'''
def _run(delay=0.12):
    for line in ART:
        sys.stdout.write("\033[%dm%s\033[0m\n" % (COLORS[0], line))
        sys.stdout.flush()
        time.sleep(delay)
''',

"wave": r'''
def _run(delay=0.1, cycles=3):
    for _ in range(cycles):
        for phase in range(len(ART) + len(COLORS)):
            sys.stdout.write("\033[H\033[J")
            for i, line in enumerate(ART):
                idx = (i + phase) % len(COLORS)
                sys.stdout.write("\033[%dm%s\033[0m\n" % (COLORS[idx], line))
            sys.stdout.flush()
            time.sleep(delay)
''',

"sparkle": r'''
def _run(delay=0.02, rounds=12):
    import random as _r
    targets = [(i, j) for i, l in enumerate(ART)
               for j, c in enumerate(l) if c != " "]
    if not targets:
        return
    _r.shuffle(targets)
    step = max(1, len(targets) // (rounds * 6))
    revealed = set()
    cur = 0
    while cur < len(targets):
        for _ in range(step):
            if cur < len(targets):
                revealed.add(targets[cur]); cur += 1
        sys.stdout.write("\033[H\033[J")
        for i, line in enumerate(ART):
            s = []
            for j, ch in enumerate(line):
                if ch == " " or (i, j) in revealed:
                    s.append("\033[%dm%s" % (COLORS[0], ch))
                else:
                    s.append(" ")
            sys.stdout.write("".join(s) + "\033[0m\n")
        sys.stdout.flush()
        time.sleep(delay)
''',

"gradient_cycle": r'''
def _run(interval=0.06, cycles=40):
    offset = 0
    for _ in range(cycles):
        sys.stdout.write("\033[H\033[J")
        for line in ART:
            s = []
            for i, ch in enumerate(line):
                idx = (i + offset) % len(COLORS)
                s.append("\033[%dm%s" % (COLORS[idx], ch))
            sys.stdout.write("".join(s) + "\033[0m\n")
        sys.stdout.flush()
        offset += 1
        time.sleep(interval)
''',

# ---- Fancy: boxed shadow logo, char-by-char, per-row gradient ----
"logo_animated": r'''
def _run(char_delay=0.0018, row_delay=0.05):
    """Reveal shadow art inside a bordered box, one char at a time."""
    GRAY = "\033[90m"
    R = "\033[0m"
    inner = max((len(l) for l in ART), default=0) + 2

    print()
    sys.stdout.write(GRAY + "  ┌" + "─" * inner + "┐" + R + "\n")
    sys.stdout.write(GRAY + "  │" + R + " " * inner + GRAY + "│" + R + "\n")

    for i, line in enumerate(ART):
        col = COLORS[i % len(COLORS)]
        sys.stdout.write(GRAY + "  │" + R + "  ")
        for ch in line:
            sys.stdout.write(col + ch + R)
            sys.stdout.flush()
            time.sleep(char_delay)
        pad = inner - 2 - len(line)
        if pad < 0:
            pad = 0
        sys.stdout.write(" " * pad)
        sys.stdout.write(GRAY + "│" + R + "\n")
        time.sleep(row_delay)

    sys.stdout.write(GRAY + "  │" + R + " " * inner + GRAY + "│" + R + "\n")
    sys.stdout.write(GRAY + "  └" + "─" * inner + "┘" + R + "\n")
    print()
''',
}

GRADIENT_ONLY = {"rainbow_sweep", "gradient_cycle"}

# =============================================================
# ANIM FILE WRITER
# =============================================================
def write_anim(path, text, anim_type, plain_lines, color_desc, colors):
    module_name = os.path.splitext(os.path.basename(path))[0]
    fn = os.path.basename(path)

    src = []
    src.append("#!/usr/bin/env python3")
    src.append("# -*- coding: utf-8 -*-")
    src.append('"""')
    src.append("OpenText Studio - Generated Animation")
    src.append("=" * 38)
    src.append("Animation : %s" % anim_type)
    src.append("Color     : %s" % color_desc)
    src.append("File      : %s" % fn)
    src.append("")
    src.append("RUN STANDALONE:")
    src.append("    python %s" % fn)
    src.append("")
    src.append("EMBED INTO YOUR OWN SCRIPT:")
    src.append("    # INSERT THIS IN IMPORTS:")
    src.append("    import %s" % module_name)
    src.append("    # MAIN ANIM:")
    src.append("    %s.animate()" % module_name)
    src.append('"""')
    src.append("")
    src.append('__all__ = ["ART", "COLORS", "animate"]')
    src.append("")
    src.append("import sys")
    src.append("import time")
    src.append("")
    src.append("try:")
    src.append('    sys.stdout.reconfigure(encoding="utf-8")')
    src.append("except Exception:")
    src.append("    pass")
    src.append("")
    src.append('if sys.platform == "win32":')
    src.append("    try:")
    src.append("        import ctypes")
    src.append("        _k = ctypes.windll.kernel32")
    src.append("        _k.SetConsoleMode(_k.GetStdHandle(-11), 7)")
    src.append("    except Exception:")
    src.append("        pass")
    src.append("")
    src.append("ART = [")
    for line in plain_lines:
        src.append("    %r," % line)
    src.append("]")
    src.append("")
    src.append("COLORS = %r" % list(colors))
    src.append("")
    src.append(ANIM_BODIES[anim_type].strip("\n"))
    src.append("")
    src.append("")
    src.append("def animate(**kwargs):")
    src.append('    """Public entry point — call from your own code."""')
    src.append("    return _run(**kwargs)")
    src.append("")
    src.append("")
    src.append('if __name__ == "__main__":')
    src.append("    try:")
    src.append("        animate()")
    src.append("    except KeyboardInterrupt:")
    src.append('        sys.stdout.write("\\n")')
    src.append("")

    with open(path, "w", encoding="utf-8") as f:
        f.write("\n".join(src))


# =============================================================
# STATIC FILE WRITER
# =============================================================
def write_static(path, lines):
    with open(path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")


# =============================================================
# BUILD
# =============================================================
def build(text):
    root = "%05d" % random.randint(0, 99999)
    while os.path.exists(root):
        root = "%05d" % random.randint(0, 99999)

    tdir = os.path.join(root, "text")
    adir = os.path.join(root, "anim")
    os.makedirs(tdir)
    os.makedirs(adir)

    created = []

    # -------- STATIC (text/) --------
    # 5x5 based
    static_specs = [
        ("solid.txt",   "solid", 1, "solid",    "bright_green"),
        ("hash.txt",    "hash",  1, "solid",    "bright_cyan"),
        ("at.txt",      "at",    1, "solid",    "bright_yellow"),
        ("shade.txt",   "shade", 1, "gradient", "fire"),
        ("star.txt",    "star",  1, "gradient", "rainbow"),
        ("solid_big.txt","solid",2, "gradient", "ocean"),
    ]
    for fname, style, scale, mode, name in static_specs:
        plain = render_5x5(text, style, scale)
        if mode == "solid":
            colored = colorize_solid(plain, ANSI_16[name])
        else:
            colored = colorize_gradient(plain, GRADIENTS[name])
        p = os.path.join(tdir, fname)
        write_static(p, colored)
        created.append(p)

    # ANSI Shadow based
    sh_plain = render_shadow(text)
    p = os.path.join(tdir, "shadow.txt")
    write_static(p, colorize_gradient(sh_plain, GRADIENTS["ocean"]))
    created.append(p)

    p = os.path.join(tdir, "shadow_rainbow.txt")
    write_static(p, colorize_perrow(sh_plain, GRADIENTS["rainbow"]))
    created.append(p)

    # Boxed shadow
    def row_colorizer(line):
        # gradient along the row
        return colorize_gradient([line], GRADIENTS["rainbow"])[0]
    p = os.path.join(tdir, "shadow_box.txt")
    write_static(p, boxed(sh_plain, row_colorizer))
    created.append(p)

    # -------- ANIM (anim/) --------
    anim_specs = [
        ("typewriter.py",     "typewriter",     "solid",    "bright_green", 1),
        ("pulse.py",          "pulse",          "gradient", "rainbow",      1),
        ("rainbow_sweep.py",  "rainbow_sweep",  "gradient", "rainbow",      1),
        ("fade_in.py",        "fade_in",        "solid",    "bright_cyan",  1),
        ("slide_left.py",     "slide_left",     "solid",    "bright_yellow",1),
        ("blink.py",          "blink",          "gradient", "fire",         1),
        ("row_by_row.py",     "row_by_row",     "solid",    "bright_red",   1),
        ("wave.py",           "wave",           "gradient", "ocean",        1),
        ("sparkle.py",        "sparkle",        "solid",    "bright_magenta",1),
        ("gradient_cycle.py", "gradient_cycle", "gradient", "rainbow",      1),
    ]
    for fname, anim, mode, name, scale in anim_specs:
        if anim in GRADIENT_ONLY and mode != "gradient":
            mode, name = "gradient", "rainbow"
        plain = render_5x5(text, "█", scale)
        colors = [ANSI_16[name]] if mode == "solid" else GRADIENTS[name]
        desc = ("solid %s" % name) if mode == "solid" else ("gradient %s" % name)
        p = os.path.join(adir, fname)
        write_anim(p, text, anim, plain, desc, colors)
        created.append(p)

    # Special: logo_animated.py uses shadow font
    p = os.path.join(adir, "logo_animated.py")
    write_anim(p, text, "logo_animated", sh_plain,
               "per-row gradient rainbow (shadow font)",
               GRADIENTS["rainbow"])
    created.append(p)

    return root, created


# =============================================================
# MAIN
# =============================================================
def main():
    print("=" * 56)
    print("                OpenText Studio")
    print("=" * 56)
    print("Output languages : ENG + RUS")
    print("UI language      : English")
    print("Text is UPPERCASED for bitmap rendering.")
    print()

    try:
        text = input("Enter text to render: ").strip()
    except (EOFError, UnicodeDecodeError):
        text = sys.stdin.buffer.readline().decode("utf-8", "replace").strip()
    if not text:
        text = "OPENTEXT"

    root, files = build(text)

    print()
    print("[*] Output folder: %s/" % root)
    print("    text/  -> static colored art")
    print("    anim/  -> runnable animations")
    print()
    for p in files:
        print("    " + p)
    print()
    print("[*] %d files created." % len(files))
    print()
    print("  View static : cat %s/text/shadow.txt" % root)
    print("  Run anim    : python %s/anim/logo_animated.py" % root)
    print("  Embed anim  : import logo_animated; logo_animated.animate()")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n[!] Aborted.")
        sys.exit(1)