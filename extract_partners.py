import re

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

match = re.search(r'(<!-- PARTNERS SECTION -->[\s\S]*?)(?=<!-- FOOTER -->)', text)
if match:
    print(match.group(1))
else:
    print("Partners section not found")
