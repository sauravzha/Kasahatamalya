import re

with open('wider_team_html.txt', 'r', encoding='utf-8') as f:
    wider = f.read()

# Extract from <!-- OUR TEAM --> down to the end of wider_team_html.txt
match_wider = re.search(r'(    <!-- OUR TEAM -->[\s\S]*)', wider)
if not match_wider:
    print("Could not find OUR TEAM in wider_team_html.txt")
    exit(1)
clean_wider = match_wider.group(1)

# Now fix story.html
with open('story.html', 'r', encoding='utf-8') as f:
    current_story = f.read()

# Extract top and the first core-governance
match = re.search(r'([\s\S]*?<section class="section" id="core-governance"[\s\S]*?      </div>\n    </section>)', current_story)
if not match:
    print("Could not find core-governance in story.html")
    exit(1)
top_and_core = match.group(1)

# Extract bottom (from FOOTER onwards)
match3 = re.search(r'(    <!-- FOOTER -->[\s\S]*)', current_story)
if not match3:
    print("Could not find FOOTER in story.html")
    exit(1)
bottom = match3.group(1)

# Combine!
final_story = top_and_core + '\n\n' + clean_wider + '\n\n' + bottom

with open('story.html', 'w', encoding='utf-8') as f:
    f.write(final_story)

print("story.html fixed perfectly!")
