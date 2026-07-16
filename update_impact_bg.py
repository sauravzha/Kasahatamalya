import re

html_path = r"C:\Users\Saurav\Desktop\Kshamatalaya\index.html"
with open(html_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Change the background of the impact section
old_bg_str = 'background: linear-gradient(135deg, #111 0%, #1a1a1a 100%);'
new_bg_str = 'background: #08B9DB;'

if old_bg_str in content:
    content = content.replace(old_bg_str, new_bg_str)
    
    # Also adjust the cards so they look good on the bright blue background
    # old: background: rgba(43, 43, 43, 0.4); border: 1px solid rgba(255,255,255,0.08);
    # hover: background: rgba(50, 50, 50, 0.7);
    
    content = content.replace(
        'background: rgba(43, 43, 43, 0.4);\n          backdrop-filter: blur(12px);\n          border: 1px solid rgba(255,255,255,0.08);',
        'background: rgba(0, 0, 0, 0.25);\n          backdrop-filter: blur(12px);\n          border: 1px solid rgba(255,255,255,0.15);'
    )
    content = content.replace(
        'border-color: rgba(56, 182, 255, 0.4);\n          background: rgba(50, 50, 50, 0.7);',
        'border-color: rgba(255, 255, 255, 0.5);\n          background: rgba(0, 0, 0, 0.35);'
    )
    # the subtitle color #bbb might be hard to read if the background is bright blue
    content = content.replace(
        'style="color: #bbb; font-size: 0.95rem; margin: 0; max-width: 400px; text-align: right;"',
        'style="color: rgba(255, 255, 255, 0.9); font-size: 0.95rem; margin: 0; max-width: 400px; text-align: right;"'
    )
    # the stats pulse effect was radial-gradient(circle, rgba(56,182,255,0.05) 0%, rgba(28,166,160,0.02) 40%, transparent 70%);
    content = content.replace(
        'background: radial-gradient(circle, rgba(56,182,255,0.05) 0%, rgba(28,166,160,0.02) 40%, transparent 70%);',
        'background: radial-gradient(circle, rgba(255,255,255,0.15) 0%, rgba(255,255,255,0.05) 40%, transparent 70%);'
    )

    with open(html_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print("Successfully updated impact section background to #08B9DB and adjusted card styles.")
else:
    print("Could not find the old background string.")
