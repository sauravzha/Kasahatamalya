import re

with open('story.html', 'r', encoding='utf-8') as f:
    text = f.read()

for match in re.finditer(r'<section.*?id="([^"]+)"', text):
    print(match.group(1))
