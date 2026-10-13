import re

with open('old_index.html', 'r', encoding='utf-16') as f:
    text = f.read()

# The wider team grid has class="leader-flip-container" or similar.
# Let's search from the end of the Core team table to the Joshila banner.

match = re.search(r'(<!-- VIEW 2: Executive Matrix Table View -->[\s\S]*?</table>\s*</div>)([\s\S]*?)<!-- PARTNERS SECTION', text)
if match:
    with open('wider_team_html.txt', 'w', encoding='utf-8') as f:
        f.write(match.group(2))
    print("Extracted!")
else:
    print("Not found")
