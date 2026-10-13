import re

def recover():
    # Read the old index.html
    with open('old_index.html', 'r', encoding='utf-16') as f:
        old_text = f.read()
    
    # Extract everything from Advisory Board title down to the end of the container
    # I will look for: <h3 class="section-header__title" ...>Advisory Board</h3>
    
    match = re.search(r'(<h3 class="section-header__title"[^>]*>\s*Advisory Board\s*</h3>[\s\S]*?</div>\s*)\s*</section>', old_text)
    if not match:
        print("Could not find Advisory Board in old_index.html")
        return
        
    advisory_html = match.group(1)
    
    # Now insert it into index.html
    with open('index.html', 'r', encoding='utf-8') as f:
        idx_text = f.read()
        
    # We want to insert it right before the closing </div> of the .container, which is right before </section>
    idx_text_new = re.sub(r'(      </div>\n    </section>\n\n\n\n    <!-- PARTNERS SECTION)', '\n' + advisory_html + r'\1', idx_text)
    
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(idx_text_new)
        
    # Now insert it into story.html
    with open('story.html', 'r', encoding='utf-8') as f:
        story_text = f.read()
        
    story_text_new = re.sub(r'(      </div>\n    </section>\n\n    <!-- PARTNERS SECTION)', '\n' + advisory_html + r'\1', story_text)
    
    with open('story.html', 'w', encoding='utf-8') as f:
        f.write(story_text_new)
        
    print("Successfully recovered Advisory Board and Joshila banner into index.html and story.html!")

recover()
