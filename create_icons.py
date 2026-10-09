import os
from PIL import Image, ImageDraw, ImageFont

def create_icon(size, filename):
    img = Image.new('RGB', (size, size), color=(30, 63, 32))
    d = ImageDraw.Draw(img)
    
    # Try to load a font, fallback to default
    try:
        font_size = size // 5
        font = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", font_size)
    except Exception:
        font = ImageFont.load_default()
        
    text = "OLIVE\nCAFE"
    # We don't have textsize in newer PIL, so use textbbox
    try:
        bbox = d.textbbox((0,0), text, font=font)
        text_w = bbox[2] - bbox[0]
        text_h = bbox[3] - bbox[1]
    except Exception:
        text_w = 40
        text_h = 20

    # Draw centered text
    d.text(((size-text_w)/2, (size-text_h)/2), text, font=font, fill=(255, 255, 255), align="center")
    
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    img.save(filename)

print("Generating 192x192 icon...")
create_icon(192, "static/images/icon-192x192.png")
print("Generating 512x512 icon...")
create_icon(512, "static/images/icon-512x512.png")
print("Done!")
