from pathlib import Path
from PIL import Image

base = Path(__file__).parent
pages_dir = base / "pages"
out_pdf = base / "ViThiTuyet_KLTN_2012.pdf"

jpgs = sorted(pages_dir.glob("page_*.jpg"))
if not jpgs:
    raise SystemExit("No JPG pages found")

images = []
for p in jpgs:
    im = Image.open(p)
    if im.mode != "RGB":
        im = im.convert("RGB")
    images.append(im)

first, rest = images[0], images[1:]
first.save(
    out_pdf,
    save_all=True,
    append_images=rest,
    resolution=200.0,
)

print(f"Wrote {out_pdf}")
print(f"Pages: {len(images)}")
print(f"Size: {out_pdf.stat().st_size:,} bytes")
