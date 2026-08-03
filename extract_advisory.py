import re

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

match = re.search(r'(<section class="section" id="advisory-board"[\s\S]*?<div class="advisory-grid"[\s\S]*?>)', text)
if match:
    print(match.group(1))
