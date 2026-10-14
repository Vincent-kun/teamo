# -*- coding: utf-8 -*-
"""v2: 3D 图标手动框选+填洞；扁平图标连通域近邻聚类"""
import os
import numpy as np
from PIL import Image, ImageDraw, ImageFilter
from scipy import ndimage

BASE = r'D:/work/sportmate/docs/product/design/assets/teamo-icons-20261009'

def alpha_from_crop(im, box, t_solid, t_soft, fill, pad=8):
    x0, y0, x1, y1 = box
    x0 = max(x0 - pad, 0); y0 = max(y0 - pad, 0)
    x1 = min(x1 + pad, im.width); y1 = min(y1 + pad, im.height)
    c = np.asarray(im.crop((x0, y0, x1, y1)).convert('RGB')).astype(np.int16)
    h, w, _ = c.shape
    border = np.concatenate([c[0, :, :], c[-1, :, :], c[:, 0, :], c[:, -1, :]])
    bg = np.median(border, axis=0)
    diff = np.abs(c - bg).max(axis=2).astype(np.float32)
    solid = diff > t_solid
    solid = ndimage.binary_closing(solid, iterations=2)
    if fill:
        solid = ndimage.binary_fill_holes(solid)
    lbl, n = ndimage.label(solid)
    if n > 1:
        sizes = ndimage.sum(solid, lbl, range(1, n + 1))
        keep = sizes >= max(sizes.max() * 0.02, 30)
        solid = keep[lbl - 1] if n > 1 else solid
    soft = np.clip((diff - t_soft) / max(t_solid - t_soft, 1), 0, 1)
    soft[soft < 0.1] = 0
    soft = soft * ndimage.binary_dilation(solid, iterations=12)
    alpha = np.maximum(solid.astype(np.float32), soft * 0.92)
    ai = Image.fromarray((alpha * 255).astype(np.uint8), 'L').filter(ImageFilter.GaussianBlur(0.7))
    out = im.crop((x0, y0, x1, y1)).convert('RGBA')
    out.putalpha(ai)
    return out

def cut_d3():
    src = r'C:/Users/13896/.workbuddy/clipboard-images/clipboard-2026-10-09T07-07-13-361Z-d6c72cd7.jpg'
    im = Image.open(src).convert('RGB')
    outdir = os.path.join(BASE, 'device3d')
    os.makedirs(outdir, exist_ok=True)
    for f in os.listdir(outdir):
        if f.endswith('.png') and not f.startswith('_'):
            os.remove(os.path.join(outdir, f))
    a = np.asarray(im).astype(np.int16)
    h, w, _ = a.shape
    border = np.concatenate([a[0, :, :], a[-1, :, :], a[:, 0, :], a[:, -1, :]])
    bg = np.median(border, axis=0)
    diff = np.abs(a - bg).max(axis=2).astype(np.float32)
    solid = diff > 14
    lbl, n = ndimage.label(solid)
    comps = []
    for i in range(1, n + 1):
        ys, xs = np.where(lbl == i)
        if len(ys) >= 300:
            comps.append([ys.min(), ys.max(), xs.min(), xs.max()])
    G = 45
    changed = True
    while changed:
        changed = False
        for i in range(len(comps)):
            for j in range(i + 1, len(comps)):
                a1, b1, c1, d1 = comps[i]; a2, b2, c2, d2 = comps[j]
                if not (c1 > d2 + G or c2 > d1 + G or a1 > b2 + G or a2 > b1 + G):
                    comps[i] = [min(a1, a2), max(b1, b2), min(c1, c2), max(d1, d2)]
                    comps.pop(j); changed = True; break
            if changed: break
    comps.sort(key=lambda r: (round((r[0] + r[1]) / 2 / 330), r[2]))
    names = ['device', 'runner', 'person', 'frame',
             'person-frame', 'ring', 'btn-pause',
             'check', 'cam-off', 'btn-play', 'btn-stop']
    fills = [True, True, True, True, True, False, False, False, False, False, False]
    assert len(comps) == len(names), f'cluster count {len(comps)} != {len(names)}'
    tiles = []
    for (y0, y1, x0, x1), name, fill in zip(comps, names, fills):
        t = alpha_from_crop(im, (x0, y0, x1 + 1, y1 + 1), t_solid=9, t_soft=4, fill=fill, pad=10)
        t.save(os.path.join(outdir, f'{name}.png'))
        tiles.append((name, t))
    cols, cw, ch = 4, 220, 230
    rows = (len(tiles) + cols - 1) // cols
    sheet = Image.new('RGB', (cols * cw, rows * ch), (136, 136, 136))
    d = ImageDraw.Draw(sheet)
    for i, (name, t) in enumerate(tiles):
        t.thumbnail((cw - 24, ch - 44))
        gx, gy = (i % cols) * cw, (i // cols) * ch
        sheet.paste(t, (gx + (cw - t.width) // 2, gy + 8 + (ch - 44 - t.height) // 2), t)
        d.text((gx + 8, gy + ch - 28), name, fill=(255, 255, 0))
    sheet.save(os.path.join(outdir, '_sheet_d3.png'))
    print('d3 done:', [n for n, _ in tiles])

def cut_flat():
    src = r'C:/Users/13896/.workbuddy/clipboard-images/clipboard-2026-10-09T07-07-13-362Z-e1c416cb.jpg'
    im = Image.open(src).convert('RGB')
    outdir = os.path.join(BASE, 'flat')
    os.makedirs(outdir, exist_ok=True)
    for f in os.listdir(outdir):
        if f.endswith('.png') and not f.startswith('_'):
            os.remove(os.path.join(outdir, f))
    a = np.asarray(im).astype(np.int16)
    h, w, _ = a.shape
    border = np.concatenate([a[0, :, :], a[-1, :, :], a[:, 0, :], a[:, -1, :]])
    bg = np.median(border, axis=0)
    diff = np.abs(a - bg).max(axis=2).astype(np.float32)
    solid = diff > 45
    lbl, n = ndimage.label(solid)
    comps = []
    for i in range(1, n + 1):
        ys, xs = np.where(lbl == i)
        if len(ys) >= 120:
            comps.append([ys.min(), ys.max(), xs.min(), xs.max()])
    # 近邻聚类：bbox 扩 14px 相交即合并
    G = 14
    changed = True
    while changed:
        changed = False
        for i in range(len(comps)):
            for j in range(i + 1, len(comps)):
                a1, b1, c1, d1 = comps[i]; a2, b2, c2, d2 = comps[j]
                if not (c1 > d2 + G or c2 > d1 + G or a1 > b2 + G or a2 > b1 + G):
                    comps[i] = [min(a1, a2), max(b1, b2), min(c1, c2), max(d1, d2)]
                    comps.pop(j); changed = True; break
            if changed: break
    comps.sort(key=lambda r: (round((r[0] + r[1]) / 2 / 110), r[2]))
    tiles = []
    for idx, (y0, y1, x0, x1) in enumerate(comps, 1):
        t = alpha_from_crop(im, (x0, y0, x1 + 1, y1 + 1), t_solid=38, t_soft=20, fill=False, pad=6)
        name = f'ft_{idx:02d}.png'
        t.save(os.path.join(outdir, name))
        tiles.append((name, t, idx))
    cols, cw, ch = 9, 130, 140
    rows = (len(tiles) + cols - 1) // cols
    sheet = Image.new('RGB', (cols * cw, rows * ch), (136, 136, 136))
    d = ImageDraw.Draw(sheet)
    for i, (name, t, idx) in enumerate(tiles):
        t.thumbnail((cw - 16, ch - 34))
        gx, gy = (i % cols) * cw, (i // cols) * ch
        sheet.paste(t, (gx + (cw - t.width) // 2, gy + 6 + (ch - 34 - t.height) // 2), t)
        d.text((gx + 6, gy + ch - 24), f'#{idx}', fill=(255, 255, 0))
    sheet.save(os.path.join(outdir, '_sheet_ft.png'))
    print('flat done:', len(tiles))

if __name__ == '__main__':
    cut_d3()
    cut_flat()
