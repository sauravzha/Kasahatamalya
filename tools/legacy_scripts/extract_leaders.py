import re
import sys
import subprocess

html_content = subprocess.check_output(['git', 'show', 'HEAD~1:index.html']).decode('utf-8')

pattern = re.compile(
    r'<div class="leader-card-item" data-category="(.*?)">.*?<img src="/assets/team/(.*?)" alt="(.*?)" loading="lazy" class="leader-photo" />.*?<h3 class="leader-name">.*?</h3>.*?<div class="leader-designation".*?>(.*?)</div>.*?<div class="leader-location">📍 (.*?)</div>.*?<a href="(.*?)" target="_blank".*?<div class="leader-bio-text">(.*?)</div>',
    re.DOTALL
)

matches = pattern.findall(html_content)

out = "profiles = [\n"
for match in matches:
    category = match[0].strip()
    photo = match[1].strip()
    name = match[2].strip()
    role = match[3].strip()
    loc = match[4].strip()
    link = match[5].strip()
    bio = match[6].strip()
    
    out += "    {\n"
    out += f"        'name': '{name}',\n"
    out += f"        'role': '{role}',\n"
    out += f"        'loc': '{loc}',\n"
    out += f"        'photo': '{photo}',\n"
    out += f"        'link': '{link}',\n"
    out += f"        'category': '{category}',\n"
    out += f"        'bio': '{bio}'\n"
    out += "    },\n"

out += "]"

with open('extracted_profiles.py', 'w', encoding='utf-8') as f:
    f.write(out)

print(f"Extracted {len(matches)} profiles to extracted_profiles.py")
