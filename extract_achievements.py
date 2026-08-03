import re

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

match = re.search(r'(<section[^>]*id="achievements-2025"[^>]*>[\s\S]*?</section>)', text, re.IGNORECASE)
if match:
    with open('temp_achievements.txt', 'w', encoding='utf-8') as out:
        out.write(match.group(1))
    print("Found achievements-2025 section and wrote to temp_achievements.txt")
else:
    print("Could not find achievements-2025 section")
