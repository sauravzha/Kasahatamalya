import os
from PIL import Image, ImageOps

source_path = r"C:\Users\Saurav\Downloads\1000004849 (1).jpg"
dest_path = r"C:\Users\Saurav\Desktop\Kshamatalaya\assets\team\mohd_asif_ameen.jpg"

try:
    img = Image.open(source_path)
    img = ImageOps.exif_transpose(img)
    img = img.convert('RGB')
    
    # Just resize maintaining aspect ratio, CSS will crop
    img.thumbnail((600, 600), Image.Resampling.LANCZOS)
    
    img.save(dest_path, 'JPEG', quality=85)
    print("Successfully updated Asif's photo from Downloads!")
except Exception as e:
    print(f"Error: {e}")
