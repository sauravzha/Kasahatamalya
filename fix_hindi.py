import re

files_to_update = ['index.html', 'story.html']

for file in files_to_update:
    try:
        with open(file, 'r', encoding='utf-8') as f:
            text = f.read()

        # Fix the corrupted text
        # Because we don't know exactly what the corrupted text looks like in bytes, 
        # we will just replace the whole tag div
        text = re.sub(
            r'<div class="joshila-tag">.*?</div>',
            r'<div class="joshila-tag">कोटड़ा से</div>',
            text
        )

        with open(file, 'w', encoding='utf-8') as f:
            f.write(text)
        print(f"Fixed Hindi text in {file}")
    except Exception as e:
        print(f"Failed on {file}: {e}")
