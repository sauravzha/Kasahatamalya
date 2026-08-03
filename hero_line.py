import re

def force_one_line():
    with open('index.html', 'r', encoding='utf-8') as f:
        text = f.read()

    # The user wants them in one line. We will change the child styles to flex: 1.
    old_style = 'style="position: relative; width: 100%; max-width: 420px;"'
    new_style = 'style="position: relative; flex: 1; min-width: 280px; max-width: 420px;"'
    
    # Also remove flex-wrap: wrap? No, wrap is good for mobile. But let's increase the container max-width to 1400px to give them more breathing room.
    text = text.replace('max-width: 1300px;', 'max-width: 1400px;')
    
    text = text.replace(old_style, new_style)

    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(text)
    
    print("Updated hero visuals to stay on one line.")

force_one_line()
