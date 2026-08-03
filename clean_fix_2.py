import re

with open('wider_team_html.txt', 'r', encoding='utf-8') as f:
    wider = f.read()

# Extract from <!-- OUR TEAM --> down to the end of wider_team_html.txt
match_wider = re.search(r'(    <!-- OUR TEAM -->[\s\S]*)', wider)
if not match_wider:
    print("Could not find OUR TEAM in wider_team_html.txt")
    exit(1)
clean_wider = match_wider.group(1)

with open('index.html', 'r', encoding='utf-8') as f:
    current_idx = f.read()

# Extract top and core-governance
match = re.search(r'([\s\S]*?<section class="section" id="core-governance"[\s\S]*?      </div>\n    </section>)', current_idx)
top_and_core = match.group(1)

# Extract bottom
match3 = re.search(r'(    <!-- PARTNERS SECTION                         -->[\s\S]*)', current_idx)
bottom = match3.group(1)

final_html = top_and_core + '\n\n' + clean_wider + '\n\n' + bottom

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(final_html)

# DO THE SAME FOR STORY.HTML
with open('story.html', 'r', encoding='utf-8') as f:
    current_story = f.read()

match = re.search(r'([\s\S]*?<section class="section" id="core-governance"[\s\S]*?      </div>\n    </section>)', current_story)
top_and_core = match.group(1)

match3 = re.search(r'(    <!-- PARTNERS SECTION                         -->[\s\S]*)', current_story)
bottom = match3.group(1)

final_story = top_and_core + '\n\n' + clean_wider + '\n\n' + bottom

with open('story.html', 'w', encoding='utf-8') as f:
    f.write(final_story)

print("Both files fixed cleanly!")
