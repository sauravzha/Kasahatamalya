import re

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

match = re.search(r'(<section[^>]*id="programs"[^>]*>[\s\S]*?</section>)', text, re.IGNORECASE)
if match:
    with open('temp_programs.txt', 'w', encoding='utf-8') as out:
        out.write(match.group(1))
    print("Found programs section and wrote to temp_programs.txt")
else:
    print("Could not find programs section")
