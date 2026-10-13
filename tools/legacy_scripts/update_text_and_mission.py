import glob
import re

html_files = glob.glob('*.html')

# 1. Update "With 8+ years..." text across all HTML files
for filepath in html_files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Replace "With 8+ years in this sector working in 3 geographies"
    content = content.replace(
        'With 8+ years in this sector working in 3 geographies',
        'After 10 years of working across 3 geographies'
    )
    content = content.replace(
        'With 8+ years in this sector working across 3 geographies',
        'After 10 years of working across 3 geographies'
    )
    content = content.replace(
        'With 8+ years in this sector',
        'After 10 years of working across 3 geographies'
    )
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

print('Updated 8+ years text to After 10 years of working across 3 geographies across all HTML files!')

# 2. Update mission.png image tag in index.html to remove box-shadow & border radius box
with open('index.html', 'r', encoding='utf-8') as f:
    idx = f.read()

idx = idx.replace(
    'style="width: 100%; max-width: 900px; height: auto; margin: 3rem auto 0; display: block; border-radius: 16px; box-shadow: 0 10px 30px rgba(0,0,0,0.05);"',
    'style="width: 100%; max-width: 900px; height: auto; margin: 3rem auto 0; display: block; filter: drop-shadow(0 8px 20px rgba(0,0,0,0.04));"'
)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(idx)

print('Updated mission.png styling in index.html!')
