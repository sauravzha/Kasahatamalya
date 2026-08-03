import re

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

match = re.search(r'(<!-- JOSHILA BANNER -->[\s\S]*?</div>\s*</div>)', text)
if match:
    print(match.group(1))
else:
    print("Not found")
