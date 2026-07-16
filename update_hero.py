import shutil
import os

source_img = r"C:\Users\Saurav\Desktop\Kshamatalaya\approach and mission\Picture1.jpg"
dest_img = r"C:\Users\Saurav\Desktop\Kshamatalaya\assets\photos\hero2.jpg"

try:
    shutil.copy2(source_img, dest_img)
    print("Successfully copied Picture1.jpg to hero2.jpg")
except Exception as e:
    print(f"Error copying file: {e}")

html_path = r"C:\Users\Saurav\Desktop\Kshamatalaya\index.html"
with open(html_path, 'r', encoding='utf-8') as f:
    content = f.read()

old_hero_visual = '''      <div class="hero__visual" style="position: relative; width: 100%; max-width: 600px; margin: 0 auto;">
        <div style="position: absolute; top: -15px; right: 20px; background: var(--color-yellow); border: 2px solid var(--color-charcoal); border-radius: 20px; padding: 4px 12px; font-weight: 800; font-size: 0.75rem; z-index: 10; transform: rotate(3deg);">
          क्षमता - POTENTIAL
        </div>
        <div style="border: 3px solid var(--color-charcoal); border-radius: 16px; overflow: hidden; box-shadow: 8px 8px 0 var(--color-teal); background: #f8f8f8; aspect-ratio: 16/9; display: flex; align-items: center; justify-content: center; position: relative;">
          <img src="/assets/photos/pic1.jpg" alt="Children sitting in a circle" style="width: 100%; height: 100%; object-fit: cover; opacity: 1;" />
        </div>
      </div>'''

new_hero_visual = '''      <div class="hero__visual" style="position: relative; width: 100%; max-width: 900px; margin: 0 auto; display: flex; gap: 2rem; justify-content: center; align-items: center; flex-wrap: wrap;">
        
        <div style="position: relative; width: 100%; max-width: 420px;">
          <div style="position: absolute; top: -15px; right: 20px; background: var(--color-yellow); border: 2px solid var(--color-charcoal); border-radius: 20px; padding: 4px 12px; font-weight: 800; font-size: 0.75rem; z-index: 10; transform: rotate(3deg);">
            क्षमता - POTENTIAL
          </div>
          <div style="border: 3px solid var(--color-charcoal); border-radius: 16px; overflow: hidden; box-shadow: -8px 8px 0 var(--color-teal); background: #f8f8f8; aspect-ratio: 4/3; display: flex; align-items: center; justify-content: center; position: relative; transform: rotate(-2deg); transition: transform 0.3s;">
            <img src="/assets/photos/pic1.jpg" alt="Children sitting in a circle" style="width: 100%; height: 100%; object-fit: cover; opacity: 1;" />
          </div>
        </div>

        <div style="position: relative; width: 100%; max-width: 420px;">
          <div style="position: absolute; bottom: -15px; left: 20px; background: var(--color-orange); border: 2px solid var(--color-charcoal); border-radius: 20px; padding: 4px 12px; font-weight: 800; font-size: 0.75rem; z-index: 10; transform: rotate(-3deg);">
            JOYFUL LEARNING
          </div>
          <div style="border: 3px solid var(--color-charcoal); border-radius: 16px; overflow: hidden; box-shadow: 8px 8px 0 var(--color-magenta); background: #f8f8f8; aspect-ratio: 4/3; display: flex; align-items: center; justify-content: center; position: relative; transform: rotate(2deg); transition: transform 0.3s;">
            <img src="/assets/photos/hero2.jpg" alt="Meaningful Education" style="width: 100%; height: 100%; object-fit: cover; opacity: 1;" />
          </div>
        </div>

      </div>'''

if old_hero_visual in content:
    content = content.replace(old_hero_visual, new_hero_visual)
    with open(html_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print("Successfully updated index.html with side-by-side images")
else:
    print("Could not find old hero visual in index.html to replace")
