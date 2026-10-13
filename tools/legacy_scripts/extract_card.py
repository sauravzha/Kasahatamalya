import re

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

match = re.search(r'(<div class="advisory-card reveal"[\s\S]*?</p>\s*</div>)', text)
if match:
    print(match.group(1))
