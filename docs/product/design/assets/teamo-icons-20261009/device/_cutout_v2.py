"""V2 抠图：背景差分+软边 alpha，去白底，存为 teamo-device-v2.png。
参考图：白底奶白机身，需要识别浅米白和纯白背景的差异。
策略：取角落纯白像素 RGB 作为背景色，按色彩距离+亮度做 alpha mask。
"""
from PIL import Image
import numpy as np
from scipy.ndimage import binary_fill_holes, gaussian_filter

SRC = r'D:/work/sportmate/docs/product/design/assets/teamo-icons-20261009/device/teamo-device-v2-src.jpg'
DST = r'D:/work/sportmate/docs/product/design/assets/teamo-icons-20261009/device/teamo-device-v2.png'

img = Image.open(SRC).convert('RGB')
arr = np.asarray(img, dtype=np.float32)
H, W, _ = arr.shape
print(f'size: {W}x{H}')

# 取四角 30x30 区域估算背景色
def corner_avg(x, y):
    return arr[y:y+30, x:x+30].reshape(-1, 3).mean(axis=0)

bg_samples = [
    corner_avg(0, 0),
    corner_avg(W-30, 0),
    corner_avg(0, H-30),
    corner_avg(W-30, H-30),
]
bg = np.mean(bg_samples, axis=0)
print(f'bg RGB: {bg}')

# 距离 = |R-bgR| + |G-bgG| + |B-bgB|  (粗略)
dist = np.abs(arr - bg).sum(axis=2)

# 阈值：奶白 vs 纯白。dist>30 视为前景
mask = (dist > 25).astype(np.uint8)
# 填洞
mask_filled = binary_fill_holes(mask).astype(np.uint8)
# 软边：高斯模糊 alpha
alpha = gaussian_filter(mask_filled.astype(np.float32), sigma=1.2)
alpha = np.clip(alpha, 0, 1)
print(f'alpha range: {alpha.min():.3f} - {alpha.max():.3f}')
print(f'前景像素: {(alpha > 0.5).sum()} / {H*W} = {(alpha > 0.5).sum()/(H*W)*100:.1f}%')

# 合成 RGBA
rgba = np.dstack([arr.astype(np.uint8), (alpha * 255).astype(np.uint8)])
out = Image.fromarray(rgba, mode='RGBA')
out.save(DST)
print(f'saved: {DST}')

# 几何测量：找屏幕（最暗大块）和椭圆模组
# 屏幕：低亮度像素
luma = arr.mean(axis=2)
dark = (luma < 60).astype(np.uint8)
dark_filled = binary_fill_holes(dark).astype(np.uint8)
# 找最大连通域
from scipy.ndimage import label
dlbl, dn = label(dark_filled)
sizes = [(dlbl == i).sum() for i in range(1, dn+1)]
top = int(np.argmax(sizes)) + 1
ys, xs = np.where(dlbl == top)
if len(xs) > 0:
    cx, cy = xs.mean(), ys.mean()
    rad = np.sqrt(((xs - cx)**2 + (ys - cy)**2).max())
    print(f'屏幕：圆心=({cx/W*100:.1f}%, {cy/H*100:.1f}%)，直径={2*rad/W*100:.1f}% 机宽')

# 椭圆模组：在机身范围内，亮度低、面积大
# 简化：用 upper 30% 区域的最大暗连通域
upper_dark = dark.copy()
upper_dark[int(H*0.32):, :] = 0
ulbl, un = label(upper_dark)
usizes = [(ulbl == i).sum() for i in range(1, un+1)]
if usizes:
    utop = int(np.argmax(usizes)) + 1
    uys, uxs = np.where(ulbl == utop)
    if len(uxs) > 0:
        ux0, uy0, ux1, uy1 = uxs.min(), uys.min(), uxs.max(), uys.max()
        print(f'椭圆模组：bbox=({ux0/W*100:.1f}%, {uy0/H*100:.1f}%, {(ux1-ux0)/W*100:.1f}%, {(uy1-uy0)/H*100:.1f}%)')
