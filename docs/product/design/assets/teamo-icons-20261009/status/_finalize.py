# -*- coding: utf-8 -*-
import os, numpy as np
from PIL import Image

OUT = r"D:/work/sportmate/docs/product/design/assets/teamo-icons-20261009/status"
renames = {
    "status-01.png":"st-trophy.png",      # 奖杯(橙)
    "status-02.png":"st-star.png",        # 星星(黄)
    "status-03.png":"st-medal.png",       # 勋章绶带(绿)
    "status-04.png":"st-check-circle.png",# 圆形勾(绿)
    "status-05.png":"st-signal.png",      # 信号柱(白)
    "status-09.png":"st-badge-ring.png",  # 圆环徽章(绿)
    "status-10.png":"st-badge-n.png",     # N 徽章(绿)
    "status-11.png":"st-badge-target.png",# 齿轮徽章(绿)
    "status-12.png":"st-badge-x.png",     # X 徽章(红)
    "status-13.png":"st-battery.png",     # 电池(绿)
}
for old, new in renames.items():
    p = os.path.join(OUT, old)
    if os.path.exists(p): os.rename(p, os.path.join(OUT, new))
for junk in ["status-06.png","status-07.png","status-08.png","status-14.png","status-15.png"]:
    p = os.path.join(OUT, junk)
    if os.path.exists(p): os.remove(p)

# contact sheet on neutral gray
files = sorted(f for f in os.listdir(OUT) if f.startswith("st-") and f.endswith(".png"))
cell = 140; pad = 14; cols = 6
rows = (len(files)+cols-1)//cols
sheet = Image.new("RGB", (cols*cell, rows*(cell+22)), (110,114,118))
from PIL import ImageDraw
dr = ImageDraw.Draw(sheet)
for i, f in enumerate(files):
    im = Image.open(os.path.join(OUT,f))
    im.thumbnail((cell-2*pad, cell-2*pad))
    cx, cy = (i%cols)*cell, (i//cols)*(cell+22)
    sheet.paste(im, (cx+(cell-im.width)//2, cy+(cell-im.height)//2), im)
    dr.text((cx+6, cy+cell+2), f.replace("st-","").replace(".png",""), fill=(255,255,255))
sheet.save(os.path.join(OUT,"_sheet_status.png"))
print("files:", len(files))
for f in files: print(" ", f)
