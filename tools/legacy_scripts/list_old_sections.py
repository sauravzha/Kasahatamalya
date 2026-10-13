import re

with open('old_index.html', 'r', encoding='utf-16') as f:
    text = f.read()

for match in re.finditer(r'<section.*?id="([^"]+)"', text):
    print(match.group(1))
