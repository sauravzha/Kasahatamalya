import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

def update_card(match):
    card_html = match.group(0)
    
    # Extract role
    role_m = re.search(r'<div class="flip-role">(.*?)</div>', card_html)
    role = role_m.group(1) if role_m else ''
    
    # Extract loc
    loc_m = re.search(r'<div class="flip-loc">(.*?)</div>', card_html)
    loc = loc_m.group(1) if loc_m else ''
    
    # Extract linkedin URL
    link_m = re.search(r'<a href="(.*?)"[^>]*class="flip-social"', card_html)
    linkedin_url = link_m.group(1) if link_m else '#'
    
    if 'flip-front-role' in card_html:
        return card_html
        
    front_replacement = f'''<div class="flip-front-role">{role}</div>
                <div class="flip-front-loc">{loc}</div>
                <a href="{linkedin_url}" target="_blank" rel="noopener noreferrer" class="flip-front-linkedin" onclick="event.stopPropagation();" title="LinkedIn Profile">
                  <svg width="15" height="15" viewBox="0 0 24 24" fill="white"><path d="M20.447 20.452h-3.554v-5.569c0-1.328-.027-3.037-1.852-3.037-1.853 0-2.136 1.445-2.136 2.939v5.667H9.351V9h3.414v1.561h.046c.477-.9 1.637-1.85 3.37-1.85 3.601 0 4.267 2.37 4.267 5.455v6.286zM5.337 7.433c-1.144 0-2.063-.926-2.063-2.065 0-1.138.92-2.063 2.063-2.063 1.14 0 2.064.925 2.064 2.063 0 1.139-.925 2.065-2.064 2.065zm1.782 13.019H3.555V9h3.564v11.452zM22.225 0H1.771C.792 0 0 .774 0 1.729v20.542C0 23.227.792 24 1.771 24h20.451C23.2 24 24 23.227 24 22.271V1.729C24 .774 23.2 0 22.225 0z"/></svg>
                </a>
              </div>'''
    
    card_html = re.sub(
        r'<div class="flip-hint">Click me! ✨</div>\s*</div>',
        front_replacement,
        card_html
    )
    return card_html

new_content = re.sub(r'<div class="flip-card-container".*?<!-- BACK -->.*?</div>\s*</div>\s*</div>', update_card, content, flags=re.DOTALL)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(new_content)

print('Successfully updated flip cards front face!')
