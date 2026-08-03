import re

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

out = []
for match in re.finditer(r'<div class="leader-location">.*?</div>', text):
    out.append(match.group(0))

for match in re.finditer(r'<div class="leader-back-loc">.*?</div>', text):
    out.append(match.group(0))

with open('locations_list.txt', 'w', encoding='utf-8') as f:
    f.write('\n'.join(out))
