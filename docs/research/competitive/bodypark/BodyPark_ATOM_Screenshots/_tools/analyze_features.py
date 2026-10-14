import pathlib, csv, statistics, sys
from PIL import Image
import numpy as np

RAW = pathlib.Path("D:/work/sportmate/docs/research/competitive/bodypark/BodyPark_ATOM_Screenshots/00_Raw_Source")
OUT = pathlib.Path("D:/work/sportmate/docs/research/competitive/bodypark/BodyPark_ATOM_Screenshots/_tools")
OUT.mkdir(parents=True, exist_ok=True)

def frame_no(p):
    # name like 微信图片_20261013090836_521_470.jpg -> 521
    parts = p.stem.split("_")
    # find numeric token that is the frame index (the one before '470')
    nums = [t for t in parts if t.isdigit()]
    return int(nums[-2]) if len(nums) >= 2 else int(nums[-1])

files = sorted(RAW.glob("*.jpg"), key=frame_no)
print(f"total files: {len(files)}")
nums = [frame_no(f) for f in files]
present = set(nums)
mn, mx = min(nums), max(nums)
gaps = [n for n in range(mn, mx+1) if n not in present]
print(f"frame range: {mn}..{mx}  missing in range: {gaps}")

SZ = 64
def feat(p):
    im = Image.open(p).convert("RGB")
    w,h = im.size
    arr = np.asarray(im.resize((SZ,SZ)), dtype=np.float32)  # SZ,SZ,3
    r,g,b = arr[:,:,0], arr[:,:,1], arr[:,:,2]
    lum = 0.299*r + 0.587*g + 0.114*b
    mean = arr.reshape(-1,3).mean(0)
    mlum = float(lum.mean())
    lstd = float(lum.std())
    dark = float((lum < 20).mean())
    # skin-tone proxy
    skin = ((r>95)&(g>40)&(g<200)&(b>20)&(b<150)&(r>g)&(g>b)&((r-b)>15)).mean()
    skin = float(skin)
    # dominant hue bucket of mean color
    mr,mg,mb = mean
    hsv_max = max(mr,mg,mb); hsv_min = min(mr,mg,mb)
    if hsv_max < 25:
        hue = "black"
    elif hsv_max > 230 and (hsv_max-hsv_min) < 35:
        hue = "white/gray"
    else:
        if mb >= mg and mb >= mr:
            hue = "blue/purple"
        elif mr >= mg and mr >= mb:
            if mg > mb:
                hue = "orange/yellow" if mg>120 else "red"
            else:
                hue = "red"
        else:  # green dominant
            hue = "green"
    return dict(w=w,h=h,mlum=round(mlum,1),lstd=round(lstd,1),dark=round(dark,3),
                skin=round(skin,3),hue=hue,fsize=p.stat().st_size)

rows = []
grays = []
for f in files:
    d = feat(f)
    d["frame"] = frame_no(f)
    d["name"] = f.name
    rows.append(d)
    im = Image.open(f).convert("L").resize((SZ,SZ))
    grays.append(np.asarray(im, dtype=np.float32))

# frame diff (scene change)
diffs = [0.0]
for i in range(1, len(grays)):
    diffs.append(float(np.abs(grays[i]-grays[i-1]).mean()))

for i,r in enumerate(rows):
    r["diff"] = round(diffs[i],1)

# segmentation: chunk boundary where diff > threshold
dvals = [d for d in diffs[1:]]
med = statistics.median(dvals)
mad = statistics.median([abs(x-med) for x in dvals]) or 1
thr = max(med + 3*mad, 12)  # robust threshold
print(f"diff median={med:.1f} mad={mad:.1f} threshold={thr:.1f}")
boundaries = [0]
for i in range(1, len(diffs)):
    if diffs[i] > thr:
        boundaries.append(i)
print(f"chunk boundaries (frame indices): {boundaries}")
print(f"num chunks: {len(boundaries)}")

# write full CSV
with open(OUT/"frame_features.csv","w",newline="",encoding="utf-8-sig") as fh:
    w = csv.DictWriter(fh, fieldnames=["frame","name","w","h","mlum","lstd","dark","skin","hue","fsize","diff"])
    w.writeheader()
    for r in rows:
        w.writerow(r)

# condensed human-readable report
print("\n=== CONDENSED REPORT (frame | lum | std | dark | skin | hue | diff | chunk) ===")
ci = 0
for i,r in enumerate(rows):
    if ci < len(boundaries)-1 and i >= boundaries[ci+1]:
        ci += 1
    mark = " >>>CHUNK" if i in boundaries else ""
    print(f"#{r['frame']:>3} lum={r['mlum']:>6} std={r['lstd']:>6} dark={r['dark']:.2f} skin={r['skin']:.2f} {r['hue']:<11} diff={r['diff']:>5}{mark}")
print("\nCSV ->", OUT/"frame_features.csv")
