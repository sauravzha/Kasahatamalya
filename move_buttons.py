import re

def move_buttons_to_hero():
    with open('index.html', 'r', encoding='utf-8') as f:
        text = f.read()

    # Remove the standalone CTA banner
    pattern_cta = r'<!-- ════════════════════════════════════════ -->\s*<!-- CTA BANNER\s*-->\s*<!-- ════════════════════════════════════════ -->\s*<section class="section" aria-label="Call to Action".*?</section>'
    
    new_text = re.sub(pattern_cta, '', text, flags=re.DOTALL)
    
    if text != new_text:
        print("Removed separate CTA banner.")
    else:
        print("Could not find CTA banner to remove.")

    # Insert buttons in the hero section right after the subtitle paragraph
    buttons_html = """
        <div style="display: flex; gap: 1rem; justify-content: center; align-items: center; margin-top: 2rem;">
          <a href="/press.html" class="btn btn--primary" style="font-size: 1.15rem; padding: 0.9rem 2rem; box-shadow: 0 8px 25px rgba(28, 166, 160, 0.35);">Read our Impact Report</a>
          <a href="/story.html" class="btn btn--outline" style="font-size: 1.15rem; padding: 0.9rem 2rem; border-width: 2px;">See how we work</a>
        </div>
"""
    
    # We look for the closing </p> of the hero__subtitle. Since there are newlines, we use regex.
    pattern_subtitle = r'(with joyful, whole-school learning\.\s*</p>)'
    
    match = re.search(pattern_subtitle, new_text)
    if match:
        new_text = new_text[:match.end()] + '\n' + buttons_html + new_text[match.end():]
        print("Added buttons to hero section.")
    else:
        print("Could not find hero subtitle paragraph to append to.")

    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(new_text)

move_buttons_to_hero()
