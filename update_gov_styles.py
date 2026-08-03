import re

def update_gov_css(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        text = f.read()

    # We will replace the style block for the grid
    # Instead of fragile regex, we'll replace specific lines if they exist
    
    # Image size
    text = text.replace('.gov-img { width: 72px; height: 72px;', '.gov-img { width: 110px; height: 110px; box-shadow: 0 4px 12px rgba(0,0,0,0.1);')
    text = text.replace('.gov-tbc { width: 72px;', '.gov-tbc { width: 110px; height: 110px;')
    
    # Gap in gov-card
    text = text.replace('.gov-card { display: flex; gap: var(--space-lg);', '.gov-card { display: flex; gap: var(--space-xl); align-items: center;')

    # Text sizes and colors
    text = text.replace(
        '.gov-info h4 { font-family: var(--font-heading); font-size: 1.15rem; color: var(--color-teal-dark); margin-bottom: 2px; }',
        '.gov-info h4 { font-family: var(--font-heading); font-size: 1.6rem; color: var(--color-teal-dark); margin-bottom: 4px; font-weight: 800; }'
    )
    
    # Remove yellow class overrides to make everything blue
    text = text.replace(
        '.gov-info h4.yellow { color: var(--color-sunshine-dark); }',
        '/* yellow classes removed */'
    )
    text = text.replace(
        '.gov-info .gov-role.yellow { color: var(--color-sunshine-dark); }',
        '/* yellow classes removed */'
    )
    
    # Role sizes and colors (Making them blue)
    text = text.replace(
        '.gov-info .gov-role { font-size: 0.75rem; font-weight: bold; text-transform: uppercase; letter-spacing: 1px; color: var(--color-teal); margin-bottom: 10px; }',
        '.gov-info .gov-role { font-size: 0.9rem; font-weight: bold; text-transform: uppercase; letter-spacing: 1.5px; color: var(--color-teal); margin-bottom: 12px; }'
    )

    # Paragraph size
    text = text.replace(
        '.gov-info p { font-size: 0.9rem; color: var(--color-text-secondary); line-height: 1.5; margin: 0; }',
        '.gov-info p { font-size: 1.05rem; color: var(--color-text-secondary); line-height: 1.6; margin: 0; }'
    )

    # Actually, the user also wants to make the yellow roles blue ("enko blue color mai kardo")
    # In HTML we had <div class="gov-role yellow">, so if we just remove the .yellow rule they will fall back to blue!
    # I already replaced the .yellow rules with comments above! Let's ensure the divider can stay yellow, or maybe the user wants everything blue. 
    # Let's also make the divider blue.
    text = text.replace('.gov-divider.yellow { color: var(--color-sunshine-dark); }', '.gov-divider.yellow { color: var(--color-teal); }')

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(text)
    
    print(f"Updated CSS in {filename}")

update_gov_css('story.html')
update_gov_css('index.html')
