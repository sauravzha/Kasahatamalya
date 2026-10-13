import re

html_path = r"C:\Users\Saurav\Desktop\Kshamatalaya\index.html"
with open(html_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Fix 1: Update approach grid CSS for overlapping issue
content = content.replace("grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));", "grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));")

content = content.replace(
'''          .approach-header {
            display: flex;
            align-items: center;
            gap: 1rem;
            position: relative;
            z-index: 1;
          }''',
'''          .approach-header {
            display: flex;
            align-items: flex-start;
            gap: 1rem;
            position: relative;
            z-index: 1;
          }'''
)

# Fix 2: Remove grayscale filter from marquee-logo
content = content.replace(
'''            .marquee-logo {
              height: 45px;
              width: auto;
              object-fit: contain;
              filter: grayscale(100%) opacity(60%);
              transition: all 0.3s ease;
            }
            .marquee-logo:hover {
              filter: grayscale(0%) opacity(100%);
              transform: scale(1.05);
            }''',
'''            .marquee-logo {
              height: 45px;
              width: auto;
              object-fit: contain;
              transition: all 0.3s ease;
            }
            .marquee-logo:hover {
              transform: scale(1.05);
            }'''
)

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Applied CSS fixes for approach grid and marquee logos.")
