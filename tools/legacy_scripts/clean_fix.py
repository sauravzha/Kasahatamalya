import re

# Read current index.html
with open('index.html', 'r', encoding='utf-8') as f:
    current_idx = f.read()

# Read old_index.html
with open('old_index.html', 'r', encoding='utf-16') as f:
    old_idx = f.read()

# 1. Extract TOP of index.html (everything before #core-governance)
# AND the first #core-governance itself (which is the Awwwards grid)
# Wait, we need to extract the new #core-governance.
match = re.search(r'([\s\S]*?<section class="section" id="core-governance"[\s\S]*?      </div>\n    </section>)', current_idx)
if not match:
    print("Could not find top and core-governance in current index.html")
    exit(1)
top_and_core = match.group(1)

# 2. Extract #team and #advisory-board from old_index.html
match2 = re.search(r'(    <!-- OUR TEAM -->\s*<section class="section" id="team"[\s\S]*?</section>\s*<!-- OUR ADVISORY BOARD -->\s*<section class="section" id="advisory-board"[\s\S]*?</div>\s*</section>)', old_idx)
if not match2:
    print("Could not find team and advisory in old_index.html")
    exit(1)
old_team_and_advisory = match2.group(1)

# 3. Extract BOTTOM of index.html (everything from PARTNERS SECTION onwards)
match3 = re.search(r'(    <!-- PARTNERS SECTION                         -->[\s\S]*)', current_idx)
if not match3:
    print("Could not find bottom in current index.html")
    exit(1)
bottom = match3.group(1)

# 4. Reconstruct
final_html = top_and_core + '\n\n' + old_team_and_advisory + '\n\n' + bottom

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(final_html)

print("index.html fixed!")
