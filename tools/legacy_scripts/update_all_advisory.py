import os
import glob
import re

# 1. Advisory Board Members Data
advisory_members = [
    {
        'name': 'UJWAL THAKAR',
        'role': 'Chairperson & Co-founder',
        'org': 'Educate Girls / Ujwal Impact Advisers',
        'photo': '/assets/advisory/Ujjawalthakur.png',
        'bio': 'Chairperson of Educate Girls and Co-founder of Ujwal Impact Advisers, with over 30 years of leadership experience across the social and corporate sectors.'
    },
    {
        'name': 'LAKSHMI HIRANANDANI',
        'role': 'Social Entrepreneur',
        'org': 'Former CEO, Swara – Voice of Women',
        'photo': '/assets/advisory/LaxmiHiranandni.png',
        'bio': 'Social entrepreneur and former CEO of Swara – Voice of Women, working to advance women’s economic empowerment in rural India across education, employability, and entrepreneurship.'
    },
    {
        'name': 'RESHMA PIRAMAL',
        'role': 'Practice Lead & Facilitator',
        'org': 'The Karuna Practice (SEE Learning)',
        'photo': '/assets/advisory/Reshma Piramal.png',
        'bio': 'Practice Lead at The Karuna Practice and a senior facilitator in Social, Emotional, and Ethical Learning, dedicated to cultivating compassion and resilient cultures in schools and leadership spaces.'
    },
    {
        'name': 'DR. AVISHEK KUMAR',
        'role': 'Co-Founder & Board Advisor',
        'org': 'VFlowTech',
        'photo': '/assets/advisory/Avishek Kumar.png',
        'bio': 'Co-Founder and Board Advisor of VFlowTech, a global leader in long-duration energy storage, leading advancements in solar and storage technologies with over 1 GW of clean energy deployments worldwide.'
    },
    {
        'name': 'DR. ASHOK KUMAR',
        'role': 'Assistant Professor & Researcher',
        'org': 'NCERT',
        'photo': '/assets/advisory/Dr. Ashok Kumar.png',
        'bio': 'Assistant Professor at NCERT and an educator and researcher committed to strengthening teacher education and educational practices through academic and professional development initiatives.'
    },
    {
        'name': 'PROF. SADHNA SAXENA',
        'role': 'Renowned Educationist',
        'org': 'Teacher Educator & Researcher',
        'photo': '/assets/advisory/Sadhna Saxsena.png',
        'bio': 'Renowned educationist and teacher educator whose work focuses on literacy, science education, equity, teacher development, and creating inclusive, transformative learning environments.'
    },
    {
        'name': 'SANJIV JAIN',
        'role': 'Director – Finance',
        'org': 'Seva Mandir',
        'photo': '/assets/advisory/Sanjiv jain.png',
        'bio': 'Director – Finance at Seva Mandir and a Chartered Accountant with over 35 years of experience in financial management, governance, and strengthening institutional sustainability in the development sector.'
    },
    {
        'name': 'JOSHILA KUMARI',
        'role': 'Young Tribal Leader & Coach',
        'org': 'PlayQuity Coach & UPAI Fellow',
        'photo': '/assets/advisory/Joshila Kumari.png',
        'bio': 'Young tribal leader from Kotra, Rajasthan, and a former iDiscover Fellow with Kshamtalaya. Currently a PlayQuity Coach and Women Ultimate Fellow with UPAI, championing girls’ leadership worldwide.'
    }
]

# Generate Advisory Section HTML
cards_html = ''
for m in advisory_members:
    cards_html += f'''
        <div class="advisory-card reveal" style="background: rgba(255, 255, 255, 0.12); backdrop-filter: blur(16px); -webkit-backdrop-filter: blur(16px); border-radius: 24px; padding: 2rem 1.5rem; border: 1px solid rgba(255, 255, 255, 0.22); box-shadow: 0 15px 35px rgba(0,0,0,0.1); display: flex; flex-direction: column; align-items: center; text-align: center; transition: all 0.4s cubic-bezier(0.16, 1, 0.3, 1);">
          <div style="width: 140px; height: 140px; border-radius: 50%; overflow: hidden; border: 4px solid #FFFFFF; box-shadow: 0 10px 25px rgba(0,0,0,0.2); margin-bottom: 1.25rem; flex-shrink: 0; background: #ffffff; transition: transform 0.4s ease;">
            <img src="{m['photo']}" alt="{m['name']}" loading="lazy" style="width: 100%; height: 100%; object-fit: cover; object-position: center top;" />
          </div>
          <h3 style="font-family: 'Baloo 2', cursive; font-size: 1.4rem; font-weight: 800; color: #FFFFFF; margin: 0 0 0.25rem 0; letter-spacing: 0.5px;">{m['name']}</h3>
          <div style="font-size: 0.85rem; font-weight: 700; color: #FFC72C; text-transform: uppercase; letter-spacing: 1px; margin-bottom: 0.25rem;">{m['role']}</div>
          <div style="font-size: 0.8rem; color: rgba(255,255,255,0.75); margin-bottom: 1rem; font-weight: 500;">{m['org']}</div>
          <p style="font-size: 0.95rem; color: rgba(255, 255, 255, 0.92); line-height: 1.65; margin: 0; font-weight: 400; text-align: left;">
            {m['bio']}
          </p>
        </div>'''

advisory_section_html = f'''
    <!-- OUR ADVISORY BOARD -->
    <!-- ════════════════════════════════════════ -->
    <section class="section" id="advisory-board" aria-label="Our Advisory Board" style="background: linear-gradient(135deg, #3A96AA 0%, #206E80 100%); color: white; padding: 6rem 0; position: relative; overflow: hidden;">
      <div style="position: absolute; top: -100px; right: -100px; width: 450px; height: 450px; background: rgba(255,255,255,0.08); border-radius: 50%; filter: blur(70px); pointer-events: none;"></div>
      <div style="position: absolute; bottom: -100px; left: -100px; width: 450px; height: 450px; background: rgba(1, 186, 222, 0.15); border-radius: 50%; filter: blur(70px); pointer-events: none;"></div>

      <div class="container" style="position: relative; z-index: 2; max-width: 1280px; margin: 0 auto; padding: 0 1.5rem;">
        <div class="section-header reveal" style="text-align: center; margin-bottom: 3.5rem;">
          <div style="display: inline-flex; align-items: center; gap: 8px; background: rgba(255, 255, 255, 0.15); backdrop-filter: blur(10px); padding: 6px 18px; border-radius: 50px; font-weight: 700; font-size: 0.85rem; letter-spacing: 1px; text-transform: uppercase; margin-bottom: 1.25rem; border: 1px solid rgba(255,255,255,0.25);">
            <span>Governance & Vision</span>
            <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><path d="M12 2v20M17 5H9.5a3.5 3.5 0 0 0 0 7h5a3.5 3.5 0 0 1 0 7H6"/></svg>
          </div>
          <h2 style="font-family: 'Baloo 2', cursive; font-size: clamp(2.5rem, 4.5vw, 3.6rem); font-weight: 800; color: #FFFFFF; margin: 0 0 1rem 0; line-height: 1.15; display: flex; align-items: center; justify-content: center; gap: 12px; flex-wrap: wrap;">
            Our Advisory Board
          </h2>
          <p style="max-width: 720px; margin: 0 auto; font-size: 1.2rem; color: rgba(255,255,255,0.9); line-height: 1.6; font-weight: 400;">
            Distinguished leaders, researchers, and social entrepreneurs guiding Kshamtalaya's mission to unlock potential across India.
          </p>
        </div>

        <style>
          .advisory-card:hover {{
            transform: translateY(-8px);
            background: rgba(255, 255, 255, 0.18) !important;
            border-color: rgba(255, 255, 255, 0.4) !important;
            box-shadow: 0 25px 45px rgba(0,0,0,0.18) !important;
          }}
          .advisory-card:hover img {{
            transform: scale(1.08);
          }}
        </style>

        <div class="advisory-grid" style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 2rem; align-items: stretch;">
{cards_html}
        </div>
      </div>
    </section>'''

# 2. Update Navbars across all HTML files
html_files = glob.glob('*.html')

for filepath in html_files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Replace 'Our Alumni' links with 'Our Advisory Board'
    content = content.replace(
        '<a href="/alumni.html" class="navbar__link">Our Alumni</a>',
        '<a href="/index.html#advisory-board" class="navbar__link">Our Advisory Board</a>'
    )
    content = content.replace(
        '<a href="/alumni.html" class="navbar__mobile-link">Our Alumni</a>',
        '<a href="/index.html#advisory-board" class="navbar__mobile-link">Our Advisory Board</a>'
    )
    content = re.sub(
        r'href="/alumni\.html"([^>]*)>Our Alumni</a>',
        r'href="/index.html#advisory-board"\1>Our Advisory Board</a>',
        content
    )
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

print('Updated navbar links across all HTML files!')

# 3. Add Advisory Board Section to index.html and story.html
for target_file in ['index.html', 'story.html']:
    with open(target_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if 'id="advisory-board"' in content:
        # Replace existing advisory section
        pattern = re.compile(r'<!-- OUR ADVISORY BOARD.*?</section>', re.DOTALL)
        content = pattern.sub(advisory_section_html, content)
    else:
        # Insert after OUR TEAM or before FOOTER
        if '<!-- FOOTER -->' in content:
            content = content.replace('<!-- FOOTER -->', f'{advisory_section_html}\n\n    <!-- FOOTER -->')
        elif '</footer>' in content:
            content = content.replace('</footer>', f'{advisory_section_html}\n</footer>')
    
    with open(target_file, 'w', encoding='utf-8') as f:
        f.write(content)

print('Added Advisory Board section to index.html and story.html!')

# 4. Standardize font styling in story.html (What Drove Us section lines 60-75)
with open('story.html', 'r', encoding='utf-8') as f:
    story_content = f.read()

drove_us_replacement = '''<div class="container text-center" style="position: relative; z-index: 2;">
        <div class="section-header__eyebrow reveal" style="display: inline-block; background: var(--color-yellow); color: var(--color-charcoal); padding: 4px 16px; border-radius: 20px; font-weight: bold; font-size: 0.9rem; margin-bottom: 1.5rem;">What Drove Us</div>
        <h1 class="reveal" style="margin-bottom: var(--space-lg); font-size: clamp(2.5rem, 5vw, 4rem); letter-spacing: -1px; line-height: 1.1;">
          <span style="color: var(--color-teal);">15,000 hours.</span><br />
          That's how long a child spends in school.
        </h1>
        <p class="reveal" style="max-width: 820px; margin: 0 auto 1.5rem; font-size: 1.15rem; color: var(--color-text-secondary); line-height: 1.7; font-weight: 400;">
          Think about that. It's the same time it takes to master classical dance, become a skilled cricket player, or learn the intricate art of pottery making. Now imagine those hours filled with purpose. Not just memorizing facts, but discovering talents, following curiosities, and building dreams.
        </p>
        <p class="reveal" style="max-width: 820px; margin: 0 auto 1.5rem; font-size: 1.15rem; color: var(--color-text-secondary); line-height: 1.7; font-weight: 400;">
          <a href="https://www.youtube.com/watch?v=iG9CE55wbtY" target="_blank" rel="noopener noreferrer" style="color: var(--color-teal); text-decoration: underline; font-weight: 600;">Sir Ken Robinson’s influential TED Talk</a> and book "The Element" explore how creativity is a natural part of human development that is often suppressed in traditional education systems. We are all born with infinite potential to thrive; we just need the right environment to flourish.
        </p>
        <p class="reveal" style="max-width: 820px; margin: 0 auto; font-size: 1.15rem; color: var(--color-text-secondary); line-height: 1.7; font-weight: 400;">
          Kshamtalaya is reimagining the foundational stages (about 45% of those 15,000 hours) to build a strong foundation in children, helping them navigate challenges and enhance their creative potential.
        </p>
      </div>'''

drove_pattern = re.compile(r'<div class="container text-center".*?</h1>\s*<p class="reveal".*?</p>\s*<p class="reveal".*?</p>\s*</div>', re.DOTALL)
story_content = drove_pattern.sub(drove_us_replacement, story_content)

with open('story.html', 'w', encoding='utf-8') as f:
    f.write(story_content)

print('Standardized font styling in story.html!')
