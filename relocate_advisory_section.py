import re

# Advisory Section Template
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
            <svg width="42" height="42" viewBox="0 0 24 24" fill="none" stroke="#FFC72C" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><path d="M12 12c-2-2.67-4-4-6-4a4 4 0 1 0 0 8c2 0 4-1.33 6-4Zm0 0c2 2.67 4 4 6 4a4 4 0 1 0 0-8c-2 0-4 1.33-6 4Z"/></svg>
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

# 1. Clean index.html
with open('index.html', 'r', encoding='utf-8') as f:
    idx = f.read()

# Strip any existing advisory section
idx = re.sub(r'\s*<!-- OUR ADVISORY BOARD.*?<\/section>', '', idx, flags=re.DOTALL)

# Insert before PARTNERS SECTION or after TEAM SECTION inside <main>
if '<!-- PARTNERS SECTION' in idx:
    idx = idx.replace('<!-- PARTNERS SECTION', f'{advisory_section_html}\n\n    <!-- PARTNERS SECTION')
elif '<!-- FOOTER -->' in idx:
    idx = idx.replace('<!-- FOOTER -->', f'{advisory_section_html}\n\n    <!-- FOOTER -->')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(idx)

# 2. Clean story.html
with open('story.html', 'r', encoding='utf-8') as f:
    sty = f.read()

# Strip any existing advisory section
sty = re.sub(r'\s*<!-- OUR ADVISORY BOARD.*?<\/section>', '', sty, flags=re.DOTALL)

# Insert before FOOTER
if '<!-- FOOTER -->' in sty:
    sty = sty.replace('<!-- FOOTER -->', f'{advisory_section_html}\n\n    <!-- FOOTER -->')
elif '<footer' in sty:
    sty = sty.replace('<footer', f'{advisory_section_html}\n\n    <footer')

with open('story.html', 'w', encoding='utf-8') as f:
    f.write(sty)

print('Relocated Advisory Board section cleanly BEFORE footer on index.html and story.html!')
