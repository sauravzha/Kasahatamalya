import re

def remove_part_2():
    with open('index.html', 'r', encoding='utf-8') as f:
        text = f.read()

    # The block to remove starts with:
    #         <!-- ─── PART 2: ACHIEVEMENT CATEGORIES ─── -->
    # And ends right before:
    #         <!-- ─── PART 3: PROGRAMS IN 2025-26 ─── -->
    
    pattern = r'\s*<!-- ─── PART 2: ACHIEVEMENT CATEGORIES ─── -->[\s\S]*?(?=<!-- ─── PART 3: PROGRAMS IN 2025-26 ─── -->)'
    
    new_text = re.sub(pattern, '\n\n        ', text)
    
    if new_text != text:
        with open('index.html', 'w', encoding='utf-8') as f:
            f.write(new_text)
        print("Successfully removed PART 2: ACHIEVEMENT CATEGORIES from index.html")
    else:
        print("Could not find PART 2 block.")

remove_part_2()
