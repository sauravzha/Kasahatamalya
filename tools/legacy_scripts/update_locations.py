import re

files_to_update = ['index.html', 'story.html']

replacements = {
    'Delhi NCR': 'Delhi',
    'Kotra, Rajasthan': 'Rajasthan',
    'Gogunda, Rajasthan': 'Rajasthan',
    'Samastipur, Bihar': 'Bihar',
    'Patna, Bihar': 'Bihar'
}

for file in files_to_update:
    try:
        with open(file, 'r', encoding='utf-8') as f:
            text = f.read()
            
        for old, new in replacements.items():
            text = text.replace(old, new)
            
        with open(file, 'w', encoding='utf-8') as f:
            f.write(text)
        print(f"Updated {file}")
    except Exception as e:
        print(f"Failed on {file}: {e}")
