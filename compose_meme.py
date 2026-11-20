#!/usr/bin/env python3
"""Compose the final GTA 6 meme for make.fun gta6-meme-x-01.

This is the program that built the meme in the entry's X post. It reads two
assets that live beside it in this repository and writes the finished meme
next to itself, so it runs from any working directory:

  assets/scene.webp      the AI-generated scene (skeleton gamer + ghost
                         holding a blank golden sign + GTA VI TV)
  assets/mark-1024.png   make.fun's official mark, from the press kit at
                         https://make.fun/press/
  meme.png               the composed meme (output)

Layers:
  1. AI scene (skeleton gamer + ghost holding a blank golden sign + GTA VI TV)
  2. Official make.fun mark badge pasted onto the sign
  3. Sign text: MAKE.FUN / MEME BOUNTY / $500
  4. Meme captions on the black bars (top / bottom)

Needs Pillow. Run: python3 compose_meme.py
"""
import os

from PIL import Image, ImageDraw, ImageFont

BASE = os.path.dirname(os.path.abspath(__file__))
SCENE = os.path.join(BASE, "assets", "scene.webp")
MARK = os.path.join(BASE, "assets", "mark-1024.png")
OUT = os.path.join(BASE, "meme.png")
FONT_BOLD = "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf"

DARK = (20, 16, 12)
MAGENTA = (197, 24, 141)
WHITE = (255, 255, 255)

img = Image.open(SCENE).convert("RGB")
W, H = img.size
draw = ImageDraw.Draw(img)


def fit_font(text, max_width, start_size):
    size = start_size
    while size > 10:
        f = ImageFont.truetype(FONT_BOLD, size)
        if draw.textlength(text, font=f) <= max_width:
            return f
        size -= 2
    return ImageFont.truetype(FONT_BOLD, 10)


def centered(text, cx, cy, max_width, start_size, fill):
    f = fit_font(text, max_width, start_size)
    draw.text((cx, cy), text, font=f, fill=fill, anchor="mm")


# --- sign geometry (relative to image, measured from the scene) ---
sx0, sy0, sx1, sy1 = 0.357 * W, 0.159 * H, 0.527 * W, 0.350 * H
sw, sh = sx1 - sx0, sy1 - sy0

# official badge on the left of the sign
badge = Image.open(MARK).convert("RGBA")
bs = int(sh * 0.52)
badge = badge.resize((bs, bs), Image.LANCZOS)
bx = int(sx0 + sw * 0.05)
by = int(sy0 + (sh - bs) / 2)
img.paste(badge, (bx, by), badge)
draw = ImageDraw.Draw(img)

# sign text block right of the badge
tx0 = bx + bs + sw * 0.04
tx1 = sx1 - sw * 0.09
tc = (tx0 + tx1) / 2
tw = tx1 - tx0
centered("MAKE.FUN", tc, sy0 + sh * 0.25, tw, int(sh * 0.26), DARK)
centered("MEME BOUNTY", tc, sy0 + sh * 0.53, tw, int(sh * 0.26), DARK)
centered("$500", tc, sy0 + sh * 0.81, tw, int(sh * 0.32), MAGENTA)

# --- black-bar captions ---
centered("WAITING FOR GTA VI SINCE 2013...", W / 2, H * 0.052, W * 0.94, int(H * 0.062), WHITE)
centered("STILL WAITING... BUT THE MEMES PAY NOW", W / 2, H * 0.950, W * 0.94, int(H * 0.058), WHITE)

img.save(OUT)
print("saved", OUT, img.size)
