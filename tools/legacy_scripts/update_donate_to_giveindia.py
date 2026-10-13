import glob
import re

html_files = glob.glob('*.html')

for filepath in html_files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 1. Replace button text 'Donate ❤' with 'Give India ❤'
    content = content.replace('Donate ❤', 'Give India ❤')
    
    # 2. Replace 'Donate Now ❤' with 'Give India ❤'
    content = content.replace('Donate Now ❤', 'Give India ❤')
    
    # 3. Replace footer link '>Donate</a>' with '>Give India</a>'
    content = re.sub(r'href="/donate\.html"([^>]*)>Donate</a>', r'href="/donate.html"\1>Give India</a>', content)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

print(f'Updated {len(html_files)} HTML files: replaced Donate button/nav text with Give India!')
