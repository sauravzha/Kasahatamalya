import re
with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

# find all sections
matches = re.finditer(r'<section[^>]*id="([^"]+)"', text)
for m in matches:
    print("Section ID:", m.group(1))

# find header text of each section
matches2 = re.finditer(r'<section[^>]*id="([^"]+)"[\s\S]*?<h2[^>]*>([\s\S]*?)</h2>', text)
for m in matches2:
    header = re.sub(r'<[^>]+>', '', m.group(2)).strip().replace('\n', ' ')
    print(f"{m.group(1)}: {header[:100]}")

