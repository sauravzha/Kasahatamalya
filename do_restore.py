import re

with open('wider_team_html.txt', 'r', encoding='utf-8') as f:
    wider_text = f.read()

# Remove the leading </div></section>
wider_text = re.sub(r'^\s*</div>\s*</section>\s*', '', wider_text)

# We might also want to remove the toggleGovView script since the table view is gone.
wider_text = re.sub(r'<script>\s*function toggleGovView[\s\S]*?</script>\s*', '', wider_text)

# Also remove Advisory Board? Wait, the user said "why our old leadership team remove restore that". 
# The old leadership team includes BOTH the "Curious about Our Leaders?" flip cards AND the Advisory Board AND the Joshila banner!
# They are all in wider_text!

for file in ['index.html', 'story.html']:
    with open(file, 'r', encoding='utf-8') as f:
        text = f.read()
    
    # Insert wider_text right before PARTNERS SECTION
    new_text = text.replace('    <!-- PARTNERS SECTION', wider_text + '\n    <!-- PARTNERS SECTION')
    
    with open(file, 'w', encoding='utf-8') as f:
        f.write(new_text)
    print(f"Restored into {file}")
