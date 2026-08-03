import re

def change_button_color():
    with open('index.html', 'r', encoding='utf-8') as f:
        text = f.read()

    old_btn = 'class="btn btn--primary" style="font-size: 1.15rem; padding: 0.9rem 2rem; box-shadow: 0 8px 25px rgba(28, 166, 160, 0.35);"'
    new_btn = 'class="btn" style="background-color: #0C4957; color: white; font-size: 1.15rem; padding: 0.9rem 2rem; box-shadow: 0 8px 25px rgba(12, 73, 87, 0.35); border-radius: 6px; font-weight: 700;"'

    if old_btn in text:
        text = text.replace(old_btn, new_btn)
        with open('index.html', 'w', encoding='utf-8') as f:
            f.write(text)
        print("Updated button color.")
    else:
        print("Could not find button to update.")

change_button_color()
