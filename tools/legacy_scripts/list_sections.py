import re

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

for match in re.finditer(r'<section.*?id="([^"]+)"', text):
    print(match.group(1))
