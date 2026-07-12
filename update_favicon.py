import glob

html_files = glob.glob('*.html')

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Replace favicon
    content = content.replace(
        '<link rel="icon" type="image/svg+xml" href="/assets/favicon.svg" />',
        '<link rel="icon" type="image/png" href="/assets/logo.png" />'
    )

    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)

print(f"Replaced favicon in {len(html_files)} files.")
