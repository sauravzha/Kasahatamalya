import re

with open('old_index.html', 'r', encoding='utf-16') as f:
    text = f.read()

match = re.search(r'(<section class="section" id="core-governance"[\s\S]*?</section>)', text)
if match:
    with open('temp_core.txt', 'w', encoding='utf-8') as f:
        f.write(match.group(1))
    print("Extracted to temp_core.txt")
else:
    print("Not found")
