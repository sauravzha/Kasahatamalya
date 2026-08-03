import re

html_to_remove = """
          <div class="gov-card reveal">
            <div class="gov-img-wrapper">
              <div class="gov-tbc">TBC</div>
            </div>
            <div class="gov-info">
              <h4>Further Directors</h4>
              <div class="gov-role" style="color: rgba(255,255,255,0.6);">UNDER REVIEW</div>
              <p>Board composition is under review. Names, roles and DINs to be published once appointments are confirmed and filed.</p>
            </div>
          </div>
"""

def remove_tbc_card(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        text = f.read()

    # Create a flexible regex pattern to remove the card, accounting for whitespace variations
    # We want to match: <div class="gov-card reveal">\s*<div class="gov-img-wrapper">\s*<div class="gov-tbc">TBC</div>...</div>\s*</div>
    pattern = r'<div class="gov-card reveal">\s*<div class="gov-img-wrapper">\s*<div class="gov-tbc">TBC</div>\s*</div>\s*<div class="gov-info">\s*<h4>Further Directors</h4>\s*<div class="gov-role" style="color: rgba\(255,255,255,0\.6\);">UNDER REVIEW</div>\s*<p>Board composition is under review\. Names, roles and DINs to be published once appointments are confirmed and filed\.</p>\s*</div>\s*</div>'
    
    new_text = re.sub(pattern, '', text)

    if text != new_text:
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(new_text)
        print(f"Removed TBC card in {filename}")
    else:
        print(f"Could not find TBC card to remove in {filename}")

remove_tbc_card('story.html')
remove_tbc_card('index.html')
