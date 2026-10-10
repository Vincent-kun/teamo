# Segment sprite sheet by projection (no fixed grid): find content bands by rows, then columns.
import os
from PIL import Image

SRC = r"C:\Users\13896\.workbuddy\clipboard-images\clipboard-2026-10-09T07-01-12-834Z-6eba5c3f.jpg"
OUT = r"D:\work\sportmate\prototype\ui-style-lab-20261008\assets\icons"
NAMES = [
    "device", "bell", "sparkle", "run-green",
    "bars-green", "home-green", "check", "person",
    "doc", "calendar", "chat", "send",
    "jack", "squat", "step", "eq",
]

im = Image.open(SRC).convert("RGB")
W, H = im.size
px = im.load()

# alpha map: 0 for near-white, up to 255 for dark/saturated
alpha = [[0] * W for _ in range(H)]
for y in range(H):
    for x in range(W):
        r, g, b = px[x, y]
        a = 255 - min(r, g, b)
        a = min(255, int(a * 1.35))
        alpha[y][x] = 0 if a < 12 else a

T = 40  # content threshold for segmentation
row_has = [sum(1 for x in range(W) if alpha[y][x] > T) for y in range(H)]
# find row bands (allow small gaps of <=6px)
bands = []
y = 0
while y < H:
    if row_has[y] > 0:
        y0 = y
        gap = 0
        y1 = y
        while y < H and gap <= 6:
            if row_has[y] > 0:
                gap = 0
                y1 = y
            else:
                gap += 1
            y += 1
        bands.append((y0, y1))
    else:
        y += 1

items = []
for (y0, y1) in bands:
    col_has = [sum(1 for yy in range(y0, y1 + 1) if alpha[yy][x] > T) for x in range(W)]
    x = 0
    while x < W:
        if col_has[x] > 0:
            x0 = x
            gap = 0
            x1 = x
            while x < W and gap <= 60:
                if col_has[x] > 0:
                    gap = 0
                    x1 = x
                else:
                    gap += 1
                x += 1
            items.append((x0, y0, x1, y1))
        else:
            x += 1

print("segments:", len(items))
os.makedirs(OUT, exist_ok=True)
if len(items) == 16:
    # sort by band then column
    items.sort(key=lambda b: (b[1] // 100, b[0]))
    for (x0, y0, x1, y1), name in zip(items, NAMES):
        # local bbox with soft alpha (>12) inside segment, padded
        region = (max(0, x0 - 6), max(0, y0 - 6), min(W, x1 + 7), min(H, y1 + 7))
        cell = im.crop(region)
        cw, chh = cell.size
        cpx = cell.load()
        a_img = Image.new("L", cell.size, 0)
        ap = a_img.load()
        for yy in range(chh):
            for xx in range(cw):
                r, g, b = cpx[xx, yy]
                m = min(r, g, b)
                if name == "device":
                    # white body must stay opaque; only true background goes transparent
                    if m >= 246:
                        a = 0
                    elif m >= 235:
                        a = int(255 * (246 - m) / 11)
                    else:
                        a = 255
                else:
                    a = 255 - m
                ap[xx, yy] = min(255, int(a * 1.35)) if a >= 12 else 0
        bbox = a_img.getbbox()
        rgba = cell.convert("RGBA")
        rgba.putalpha(a_img)
        icon = rgba.crop(bbox)
        icon.save(os.path.join(OUT, name + ".png"))
        print(name, icon.size)
else:
    for i, it in enumerate(items):
        print(i, it)
