import re

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Find the press-strip section
# It is between <!-- PRESS & MEDIA STRIP --> and the next section or the end of the section tag
press_pattern = r'(<!--  \? \? \?.*?PRESS & MEDIA STRIP.*?<section class="press-strip".*?</section>)'

match = re.search(press_pattern, text, re.DOTALL | re.IGNORECASE)
if not match:
    # try just the section
    press_pattern = r'(<section class="press-strip"[\s\S]*?</section>)'
    match = re.search(press_pattern, text, re.DOTALL | re.IGNORECASE)

if match:
    press_html = match.group(1)
    
    # Remove from original location
    text_without_press = text.replace(press_html, '')
    
    # Insert before impact-map
    # Find the impact-map section
    insert_pattern = r'(<!-- GEOGRAPHICAL REACH 3D MAP)'
    if re.search(insert_pattern, text_without_press):
        new_text = re.sub(insert_pattern, lambda m: press_html + '\n\n    ' + m.group(1), text_without_press)
        
        if new_text != text_without_press:
            with open('index.html', 'w', encoding='utf-8') as f:
                f.write(new_text)
            print("Successfully moved 'Featured In' section above Geographical Reach!")
        else:
            print("Failed to insert.")
    else:
        print("Could not find impact-map section to insert before.")
else:
    print("Could not find press-strip section to move.")
