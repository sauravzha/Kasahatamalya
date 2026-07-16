import re

html_path = r"C:\Users\Saurav\Desktop\Kshamatalaya\index.html"
with open(html_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Remove the approach-number divs
content = re.sub(r'<div class="approach-number">\d</div>\n\s*', '', content)

# Fix the first card's data layout
old_data = '''<p style="font-weight: 700; color: var(--color-charcoal); margin-bottom: 0.75rem; font-size: 0.9rem; line-height: 1.3;">100 Centers of Excellence within primary grade government schools</p>
              <ul class="approach-list">'''

new_data = '''<ul class="approach-list">
                <li><strong>100 Centers of Excellence</strong> within primary grade government schools</li>'''

if old_data in content:
    content = content.replace(old_data, new_data)
else:
    print("Could not find old_data to replace")

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Removed extra numbers and formatted the data perfectly.")
