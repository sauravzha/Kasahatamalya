import os
from PIL import Image, ImageOps
from pillow_heif import register_heif_opener

register_heif_opener()

source_path = r"C:\Users\Saurav\Desktop\Kshamatalaya\Photos of leadeship team\Asif.HEIC"
dest_path = r"C:\Users\Saurav\Desktop\Kshamatalaya\assets\team\mohd_asif_ameen.jpg"

try:
    img = Image.open(source_path)
    img = ImageOps.exif_transpose(img)
    img = img.convert('RGB')
    
    # Resize to match others (600x600 thumbnail max constraint)
    img.thumbnail((600, 600), Image.Resampling.LANCZOS)
    
    img.save(dest_path, 'JPEG', quality=85)
    print("Successfully updated Asif's photo from Asif.HEIC")
except Exception as e:
    print(f"Error: {e}")
