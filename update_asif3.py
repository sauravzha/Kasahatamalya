import os
from PIL import Image, ImageOps

source_path = r"C:\Users\Saurav\Desktop\Kshamatalaya\Photos of leadeship team\Asif.jpg"
dest_path = r"C:\Users\Saurav\Desktop\Kshamatalaya\assets\team\mohd_asif_ameen.jpg"

try:
    img = Image.open(source_path)
    img = ImageOps.exif_transpose(img)
    img = img.convert('RGB')
    
    # Using fit with center 15% to ensure it's a perfect square focused on the face
    img = ImageOps.fit(img, (600, 600), method=Image.Resampling.LANCZOS, centering=(0.5, 0.15))
    
    img.save(dest_path, 'JPEG', quality=90)
    print("Successfully updated Asif's photo from Asif.jpg")
except Exception as e:
    print(f"Error: {e}")
