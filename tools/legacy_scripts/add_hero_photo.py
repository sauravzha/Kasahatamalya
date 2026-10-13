import re

new_photo = """
        <div style="position: relative; width: 100%; max-width: 420px;">
          <div style="position: absolute; top: 12px; right: 12px; background: var(--color-teal); border: 2.5px solid var(--color-charcoal); border-radius: 24px; padding: 6px 16px; font-weight: 800; font-size: 0.8rem; z-index: 10; transform: rotate(-3deg); box-shadow: -3px 3px 0 var(--color-charcoal); letter-spacing: 0.5px; color: #fff;">
            GROWING TOGETHER 🌱
          </div>
          <div style="border: 3px solid var(--color-charcoal); border-radius: 16px; overflow: hidden; box-shadow: -8px 8px 0 var(--color-sunshine); background: #f8f8f8; aspect-ratio: 4/3; display: flex; align-items: center; justify-content: center; position: relative; transform: rotate(-1deg); transition: transform 0.3s;">
            <img src="/assets/photos/hero3.jpg" alt="Children reading together" style="width: 100%; height: 100%; object-fit: cover; opacity: 1;" />
          </div>
        </div>
"""

def add_third_photo():
    with open('index.html', 'r', encoding='utf-8') as f:
        text = f.read()

    # Find the hero visual container to update its max-width so they can fit or wrap beautifully
    text = text.replace('<div class="hero__visual" style="position: relative; width: 100%; max-width: 900px;', '<div class="hero__visual" style="position: relative; width: 100%; max-width: 1300px;')

    # Insert the third photo right after the second photo
    # The second photo ends with:
    #             <img src="/assets/photos/hero2.jpg" alt="Meaningful Education" style="width: 100%; height: 100%; object-fit: cover; opacity: 1;" />
    #           </div>
    #         </div>
    
    target = '            <img src="/assets/photos/hero2.jpg" alt="Meaningful Education" style="width: 100%; height: 100%; object-fit: cover; opacity: 1;" />\n          </div>\n        </div>'
    
    if target in text:
        text = text.replace(target, target + '\n' + new_photo)
        with open('index.html', 'w', encoding='utf-8') as f:
            f.write(text)
        print("Added third photo successfully.")
    else:
        print("Could not find the second photo to append after.")

add_third_photo()
