import os
from PIL import Image, ImageOps

source_path = r"C:\Users\Saurav\Downloads\1000004849 (1).jpg"
dest_path = r"C:\Users\Saurav\Desktop\Kshamatalaya\assets\team\mohd_asif_ameen.jpg"

try:
    img = Image.open(source_path)
    img = ImageOps.exif_transpose(img)
    img = img.convert('RGB')
    
    # Do a strict 1:1 crop focusing on the upper body/face
    # ImageOps.fit crops from the center by default, but we can set centering=(0.5, 0.2)
    # which centers horizontally and biases towards the top (face/chest area) vertically.
    
    img = ImageOps.fit(img, (600, 600), method=Image.Resampling.LANCZOS, centering=(0.5, 0.15))
    
    img.save(dest_path, 'JPEG', quality=90)
    print("Successfully cropped and updated Asif's photo as a perfect square!")
except Exception as e:
    print(f"Error: {e}")
