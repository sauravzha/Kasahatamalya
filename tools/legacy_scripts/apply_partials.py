import os
import re

html_files = ['index.html', 'story.html', 'programs.html', 'press.html', 'contact.html', 'donate.html']

nav_pattern = re.compile(r'<!-- ════════════════════════════════════════ -->\s*<!-- NAVBAR\s*-->\s*<!-- ════════════════════════════════════════ -->\s*<nav class="navbar" id="navbar".*?</nav>', re.DOTALL)

footer_pattern = re.compile(r'<!-- ════════════════════════════════════════ -->\s*<!-- FOOTER\s*-->\s*<!-- ════════════════════════════════════════ -->\s*<footer.*?>.*?</footer>', re.DOTALL)
footer_fallback_pattern = re.compile(r'<footer.*?>.*?</footer>', re.DOTALL)

for filepath in html_files:
    if not os.path.exists(filepath):
        continue
        
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Replace navbar
    if nav_pattern.search(content):
        content = nav_pattern.sub('{{> navbar }}', content)
    else:
        # Try finding just <nav...
        simple_nav = re.compile(r'<nav class="navbar".*?</nav>', re.DOTALL)
        content = simple_nav.sub('{{> navbar }}', content)

    # Replace footer
    if footer_pattern.search(content):
        content = footer_pattern.sub('{{> footer }}', content)
    else:
        content = footer_fallback_pattern.sub('{{> footer }}', content)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
        
    print(f"Applied partials to {filepath}")
