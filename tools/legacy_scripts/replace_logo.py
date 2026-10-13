import glob
import re

html_files = glob.glob('*.html')

svg_pattern = re.compile(
    r'<svg viewBox="0 0 200 60" height="32" fill="none" xmlns="http://www\.w3\.org/2000/svg">.*?</svg>',
    re.DOTALL
)

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Replace SVG footer logo
    content = svg_pattern.sub('<img src="/assets/logo.png" alt="Kshamtalaya Logo" style="height: 60px; width: auto; object-fit: contain;" />', content)

    # Replace navbar logo
    content = content.replace('src="/assets/logo.svg"', 'src="/assets/logo.png"')

    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)

print(f"Replaced logos in {len(html_files)} files.")
