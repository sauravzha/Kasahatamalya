import os
import glob
import re

html_files = glob.glob('*.html')

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Add target="_blank" rel="noopener noreferrer" to facebook
    content = content.replace('href="https://www.facebook.com/kshamtalaya" style', 'href="https://www.facebook.com/kshamtalaya" target="_blank" rel="noopener noreferrer" style')
    
    # Add to twitter
    content = content.replace('href="https://twitter.com/kshamtalaya" style', 'href="https://twitter.com/kshamtalaya" target="_blank" rel="noopener noreferrer" style')

    # Add to instagram
    content = content.replace('href="https://www.instagram.com/kshamtalaya" style', 'href="https://www.instagram.com/kshamtalaya" target="_blank" rel="noopener noreferrer" style')
    
    # Add to youtube
    content = content.replace('href="https://www.youtube.com/@kshamtalayafoundation9946" style', 'href="https://www.youtube.com/@kshamtalayafoundation9946" target="_blank" rel="noopener noreferrer" style')

    # Remove "+ ABODE OF POTENTIAL" if it exists in index.html or others
    content = content.replace('<span style="color: var(--color-teal);">+ ABODE OF POTENTIAL</span>', '')
    
    # Clean up empty line if it was the only thing there
    content = re.sub(r'^[ \t]*$\n', '', content, flags=re.MULTILINE)

    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)

print(f"Updated social links and removed text in {len(html_files)} files.")
