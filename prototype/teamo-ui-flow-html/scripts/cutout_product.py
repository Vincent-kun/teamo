from __future__ import annotations

from collections import deque
from pathlib import Path

from PIL import Image, ImageFilter


ROOT = Path(__file__).resolve().parents[1]
ASSETS = ROOT / "public" / "assets"


def cutout(source: Path, destination: Path) -> None:
    image = Image.open(source).convert("RGBA")
    width, height = image.size
    pixels = image.load()

    corners = [pixels[0, 0][:3], pixels[width - 1, 0][:3], pixels[0, height - 1][:3], pixels[width - 1, height - 1][:3]]
    background = tuple(sum(color[channel] for color in corners) / len(corners) for channel in range(3))

    def is_background(x: int, y: int) -> bool:
        red, green, blue, _ = pixels[x, y]
        distance = ((red - background[0]) ** 2 + (green - background[1]) ** 2 + (blue - background[2]) ** 2) ** 0.5
        return distance <= 18 and max(red, green, blue) - min(red, green, blue) <= 12

    visited = bytearray(width * height)
    queue: deque[tuple[int, int]] = deque()
    for x in range(width):
        queue.append((x, 0))
        queue.append((x, height - 1))
    for y in range(height):
        queue.append((0, y))
        queue.append((width - 1, y))

    while queue:
        x, y = queue.popleft()
        offset = y * width + x
        if visited[offset] or not is_background(x, y):
            continue
        visited[offset] = 1
        if x:
            queue.append((x - 1, y))
        if x + 1 < width:
            queue.append((x + 1, y))
        if y:
            queue.append((x, y - 1))
        if y + 1 < height:
            queue.append((x, y + 1))

    alpha = Image.new("L", (width, height), 255)
    alpha_pixels = alpha.load()
    for y in range(height):
        row = y * width
        for x in range(width):
            if visited[row + x]:
                alpha_pixels[x, y] = 0

    alpha = alpha.filter(ImageFilter.GaussianBlur(1.2))
    image.putalpha(alpha)
    box = alpha.getbbox()
    if not box:
        raise RuntimeError(f"No foreground found in {source}")
    pad = 12
    left = max(0, box[0] - pad)
    top = max(0, box[1] - pad)
    right = min(width, box[2] + pad)
    bottom = min(height, box[3] + pad)
    image.crop((left, top, right, bottom)).save(destination, optimize=True)


for name in ("open", "closed"):
    cutout(ASSETS / f"teamo-cover-{name}.png", ASSETS / f"teamo-cover-{name}-cutout.png")

