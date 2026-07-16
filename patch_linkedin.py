import re

# Mapping of names as they appear in the HTML to their LinkedIn URLs
links = {
    'Mohd Asif Ameen': 'https://www.linkedin.com/in/mohd-asif-ameen-23b041175',
    'Sneha Kumari': 'https://www.linkedin.com/in/sneha-kshamtalaya-2678863a6',
    'Aman Gautam': 'https://www.linkedin.com/in/aman-gautam-8b365a253',
    'Deepak Sirsam': 'https://www.linkedin.com/in/deepak-sirsam-b645a8256',
    'Aman Kumar': 'https://www.linkedin.com/in/aman-kumar-b1a760197',
    'Sameep Sonkar': 'https://www.linkedin.com/me',
    'Subham Bhakat': 'https://www.linkedin.com/in/subham-bhakat',
    'Tina Aggarwal': 'https://www.linkedin.com/in/tina-aggarwal-75b41a154',
    'Tamanna': 'https://www.linkedin.com/in/tamanna-638a80359',
    'Priya': 'https://www.linkedin.com/in/priya-bisht-2319591a3',
    'Abhishek Kumar Tiwari': 'https://www.linkedin.com/in/abhishek-tiwari-54b947156',
    'Reena': 'https://www.linkedin.com/in/reena-gautam-5bb471245',
    'Ishu': 'https://www.linkedin.com/in/ishu01',
    'Tabassum': 'https://www.linkedin.com/in/tabassum-mansori-007b87360'
}

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# We need to find the block for each person and replace href="#" with href="<link>"
for name, link in links.items():
    # regex to find the name header, then the next href="#"
    # team-name-pro" style="text-transform: capitalize;">{name}</h3> ... href="#"
    # Since name matching might have slight casing differences, use re.IGNORECASE
    
    pattern = re.compile(r'(<h3 class="team-name-pro"[^>]*>\s*' + re.escape(name) + r'\s*</h3>.*?)(href="#")', re.IGNORECASE | re.DOTALL)
    
    # We only replace the first occurrence of href="#" after the name
    def repl(m):
        return m.group(1) + f'href="{link}" target="_blank" rel="noopener noreferrer"'
        
    content = pattern.sub(repl, content, count=1)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("LinkedIn links updated!")
