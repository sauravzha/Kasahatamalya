import os
import glob

# Files to update
html_files = glob.glob('*.html')

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 1. Update Desktop Nav (Our Team)
    # The active class might be on Home or somewhere else, so we match the Home link carefully
    if 'class="navbar__link active">Home</a>' in content:
        content = content.replace('class="navbar__link active">Home</a>', 'class="navbar__link active">Home</a>\n        <a href="/#team" class="navbar__link">Our Team</a>')
    elif 'class="navbar__link">Home</a>' in content:
        content = content.replace('class="navbar__link">Home</a>', 'class="navbar__link">Home</a>\n        <a href="/#team" class="navbar__link">Our Team</a>')
        
    # 2. Update Desktop Nav (Our Alumni)
    if 'href="/contact.html" class="navbar__link">Contact' in content:
        content = content.replace('<a href="/contact.html" class="navbar__link">Contact</a>', '<a href="/alumni.html" class="navbar__link">Our Alumni</a>\n        <a href="/contact.html" class="navbar__link">Contact</a>')

    # 3. Update Mobile Nav (Our Team)
    if 'href="/" class="navbar__mobile-link">Home</a>' in content:
        content = content.replace('href="/" class="navbar__mobile-link">Home</a>', 'href="/" class="navbar__mobile-link">Home</a>\n      <a href="/#team" class="navbar__mobile-link">Our Team</a>')
    elif 'href="/" class="navbar__mobile-link active">Home</a>' in content:
        content = content.replace('href="/" class="navbar__mobile-link active">Home</a>', 'href="/" class="navbar__mobile-link active">Home</a>\n      <a href="/#team" class="navbar__mobile-link">Our Team</a>')

    # 4. Update Mobile Nav (Our Alumni)
    if 'href="/contact.html" class="navbar__mobile-link">Contact' in content:
        content = content.replace('<a href="/contact.html" class="navbar__mobile-link">Contact Us</a>', '<a href="/alumni.html" class="navbar__mobile-link">Our Alumni</a>\n      <a href="/contact.html" class="navbar__mobile-link">Contact Us</a>')

    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)
        
print(f"Updated {len(html_files)} HTML files.")
