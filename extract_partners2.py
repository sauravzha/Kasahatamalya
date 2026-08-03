import re

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Find the partners section. We will search for id="partners" or the section containing "Our Partners"
match = re.search(r'(<section[^>]*id="partners"[^>]*>[\s\S]*?</section>)', text)
if match:
    with open('temp_partners.txt', 'w', encoding='utf-8') as out:
        out.write(match.group(1))
    print("Found partners section and wrote to temp_partners.txt")
else:
    print("Could not find partners section")
