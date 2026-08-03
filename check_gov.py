import re

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

match = re.search(r'(<section.*?id="governance"[\s\S]*?</section>)', text)
if match:
    print(match.group(1)[:500])
else:
    print("Not found")
