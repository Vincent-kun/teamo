# -*- coding: utf-8 -*-
import os, numpy as np
from PIL import Image
from scipy import ndimage

OUT = r"D:/work/sportmate/docs/product/design/assets/teamo-icons-20261009/status"
# 1) fix AI-chip names
fix = {"st-badge-n.png":"st-chip-ai.png","st-badge-ring.png":"st-dots-ring.png",
       "st-badge-target.png":"st-chip-ai-active.png","st-badge-x.png":"st-chip-ai-error.png"}
for o,n in fix.items():
    p=os.path.join(OUT,o)
    if os.path.exists(p): os.rename(p, os.path.join(OUT,n))

# 2) denoise white silhouettes: keep components >= 400px, close gaps, rebuild alpha as solid white where mask
whites = ["st-back","st-camera","st-camera-off","st-camera-error","st-home","st-play",
          "st-pause","st-stop","st-refresh","st-signal","st-wifi-on","st-wifi-off"]
for nm in whites:
    p = os.path.join(OUT, nm+".png")
    im = Image.open(p).convert("RGBA")
    a = np.array(im)
    rgb = a[...,:3].astype(int)
    d = np.sqrt((rgb**2).sum(axis=2))
    fg = d > 55
    # keep large components only (icon strokes), kill speckle
    lab, n = ndimage.label(fg, structure=np.ones((3,3)))
    sizes = ndimage.sum(fg, lab, range(1,n+1))
    keep = np.zeros_like(fg)
    for i,s in enumerate(sizes, start=1):
        if s >= 400: keep |= (lab==i)
    # smooth mask edge
    keep = ndimage.binary_closing(keep, structure=np.ones((3,3)))
    keep = ndimage.binary_opening(keep, structure=np.ones((2,2)))
    # alpha: soft edge from distance transform of mask, color forced white
    alpha = np.where(keep, 255, 0).astype(np.uint8)
    alpha = ndimage.gaussian_filter(alpha.astype(float), 1.0)
    alpha = np.clip(alpha,0,255).astype(np.uint8)
    # crop to content
    ys, xs = np.where(alpha > 10)
    if len(ys)==0: continue
    y0,y1,x0,x1 = ys.min(), ys.max()+1, xs.min(), xs.max()+1
    out = np.zeros((y1-y0, x1-x0, 4), dtype=np.uint8)
    out[...] = (255,255,255,0)
    out[...,3] = alpha[y0:y1, x0:x1]
    Image.fromarray(out).save(p)
    print(f"cleaned {nm}.png -> {x1-x0}x{y1-y0}")

# rebuild contact sheet
files = sorted(f for f in os.listdir(OUT) if f.startswith("st-") and f.endswith(".png"))
cell=140; pad=14; cols=6
rows=(len(files)+cols-1)//cols
sheet = Image.new("RGB",(cols*cell, rows*(cell+22)),(110,114,118))
from PIL import ImageDraw
dr = ImageDraw.Draw(sheet)
for i,f in enumerate(files):
    im = Image.open(os.path.join(OUT,f)); im.thumbnail((cell-2*pad,cell-2*pad))
    cx,cy=(i%cols)*cell,(i//cols)*(cell+22)
    sheet.paste(im,(cx+(cell-im.width)//2, cy+(cell-im.height)//2), im)
    dr.text((cx+6,cy+cell+2), f.replace("st-","").replace(".png",""), fill=(255,255,255))
sheet.save(os.path.join(OUT,"_sheet_status.png"))
print("sheet rebuilt,", len(files), "icons")
