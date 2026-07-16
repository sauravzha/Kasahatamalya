import re

profiles = [
    ('Mohd Asif Ameen', 'Program Lead', 'Samastipur'),
    ('Sneha kumari', 'Program manager', 'Samastipur'),
    ('Aman Gautam', 'Program Lead', 'Samastipur'),
    ('Deepak Sirsam', 'Program Lead', 'Samastipur'),
    ('Aman Kumar', 'Program Leader', 'Samastipur'),
    ('Sameep Sonkar', 'Program Manager', 'Samastipur'),
    ('Subham Bhakat', 'State Resource Person', 'Patna, Bihar'),
    ('TINA AGGARWAL', 'Head of Programs, Delhi', 'Delhi'),
    ('TAMANNA', 'Program Lead', 'Delhi'),
    ('PRIYA', 'Program Leader', 'Delhi'),
    ('Abhishek Kumar Tiwari', 'Head of Programs, Bihar', 'Bihar'),
    ('REENA', 'Program Leader', 'Delhi'),
    ('Ishu', 'Program Manager', 'Bihar'),
    ('Tabassum', 'Community Leader', 'Delhi'),
    ('ANJALI', 'Program Leader', 'Delhi'),
    ('Pradeep Singh Rathore', 'Program lead ( FFSM )', 'Rajasthan')
]

cards_html = ''
for i, (name, role, loc) in enumerate(profiles):
    colors = [
        {'color': '#01BADE', 'light': 'rgba(1, 186, 222, 0.15)', 'grad': 'linear-gradient(135deg, #01BADE 0%, #4FB6E8 100%)', 'shadow': 'rgba(1, 186, 222, 0.4)'},
        {'color': '#F2994A', 'light': 'rgba(242, 153, 74, 0.15)', 'grad': 'linear-gradient(135deg, #F2994A 0%, #F5B073 100%)', 'shadow': 'rgba(242, 153, 74, 0.4)'},
        {'color': '#FF6F59', 'light': 'rgba(255, 111, 89, 0.15)', 'grad': 'linear-gradient(135deg, #FF9080 0%, #FF6F59 100%)', 'shadow': 'rgba(255, 111, 89, 0.4)'},
        {'color': '#6DBE45', 'light': 'rgba(109, 190, 69, 0.15)', 'grad': 'linear-gradient(135deg, #8ED46A 0%, #6DBE45 100%)', 'shadow': 'rgba(109, 190, 69, 0.4)'}
    ]
    c = colors[i % len(colors)]
    
    avatar_letter = name.strip()[0].upper() if name.strip() else ''
    title_name = name.title()
    
    cards_html += f'''
          <div class="team-card-pro" style="--team-color: {c['color']}; --team-color-light: {c['light']}; --team-gradient: {c['grad']}; --team-shadow: {c['shadow']};">
            <!-- Photo placeholder: Replace {avatar_letter} with <img src="photo_url" alt="{title_name}"> when ready -->
            <div class="team-avatar-pro">{avatar_letter}</div>
            <h3 class="team-name-pro" style="text-transform: capitalize;">{title_name}</h3>
            <div class="team-role-pro">{role}</div>
            <p class="team-details-pro">
              <strong>Location</strong> {loc}
            </p>
            <!-- LinkedIn placeholder -->
            <a href="#" class="team-social-link" aria-label="LinkedIn Profile" style="margin-top: 1.5rem; display: inline-flex; align-items: center; justify-content: center; width: 40px; height: 40px; background: var(--team-color-light); color: var(--team-color); border-radius: 50%; transition: all 0.3s; text-decoration: none;">
              <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor"><path d="M20.447 20.452h-3.554v-5.569c0-1.328-.027-3.037-1.852-3.037-1.853 0-2.136 1.445-2.136 2.939v5.667H9.351V9h3.414v1.561h.046c.477-.9 1.637-1.85 3.37-1.85 3.601 0 4.267 2.37 4.267 5.455v6.286zM5.337 7.433c-1.144 0-2.063-.926-2.063-2.065 0-1.138.92-2.063 2.063-2.063 1.14 0 2.064.925 2.064 2.063 0 1.139-.925 2.065-2.064 2.065zm1.782 13.019H3.555V9h3.564v11.452zM22.225 0H1.771C.792 0 0 .774 0 1.729v20.542C0 23.227.792 24 1.771 24h20.451C23.2 24 24 23.227 24 22.271V1.729C24 .774 23.2 0 22.225 0z"/></svg>
            </a>
          </div>'''

section_html = f'''
    <!-- OUR TEAM -->
    <!-- ════════════════════════════════════════ -->
    <section class="section" id="team" aria-label="Our Leadership Profile" style="background: #FAFCFC; overflow: hidden; position: relative; padding: 8rem 0;">
      <div style="position: absolute; top: 0; left: -100px; width: 400px; height: 400px; background: rgba(56, 182, 255, 0.08); border-radius: 50%; filter: blur(60px); z-index: 0;"></div>
      <div style="position: absolute; bottom: 0; right: -100px; width: 500px; height: 500px; background: rgba(242, 153, 74, 0.08); border-radius: 50%; filter: blur(60px); z-index: 0;"></div>
      <div class="container" style="position: relative; z-index: 2; max-width: 100%;">
        <div class="section-header reveal" style="text-align: center;">
          <div class="partners-badge-premium" style="justify-content: center; margin-bottom: 1rem;">
            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M23 21v-2a4 4 0 0 0-3-3.87"/><path d="M16 3.13a4 4 0 0 1 0 7.75"/></svg>
            Leadership Profile
          </div>
          <h2 class="partners-title-premium">The <span>Leaders</span> Behind Kshamtalaya</h2>
          <p class="partners-intro__desc" style="margin: 1rem auto 3rem; max-width: 700px; font-size: 1.15rem;">
            A passionate group of educators, community builders, and system thinkers dedicated to making quality education accessible to every child.
          </p>
        </div>

        <style>
          .premium-team-slider {{
            display: flex;
            overflow-x: auto;
            scroll-snap-type: x mandatory;
            gap: 2.5rem;
            padding: 1rem 3rem 4rem;
            -webkit-overflow-scrolling: touch;
            scrollbar-width: thin;
            scrollbar-color: var(--color-teal) rgba(0,0,0,0.05);
          }}
          .premium-team-slider::-webkit-scrollbar {{
            height: 10px;
          }}
          .premium-team-slider::-webkit-scrollbar-track {{
            background: rgba(0,0,0,0.05);
            border-radius: 10px;
          }}
          .premium-team-slider::-webkit-scrollbar-thumb {{
            background: var(--color-teal);
            border-radius: 10px;
          }}
          .team-card-pro {{
            scroll-snap-align: start;
            flex: 0 0 auto;
            width: 320px;
            background: rgba(255, 255, 255, 0.6); backdrop-filter: blur(20px); -webkit-backdrop-filter: blur(20px);
            border-radius: 36px; padding: 3.5rem 2rem; text-align: center;
            box-shadow: 0 15px 40px rgba(0,0,0,0.03), inset 0 0 0 1px rgba(255,255,255,0.8);
            position: relative; overflow: hidden; transition: all 0.5s cubic-bezier(0.16, 1, 0.3, 1);
            z-index: 1; display: flex; flex-direction: column; align-items: center; justify-content: flex-start;
          }}
          .team-card-pro::before {{
            content: ''; position: absolute; top: 0; left: 0; width: 100%; height: 180px;
            background: linear-gradient(180deg, var(--team-color-light) 0%, rgba(255,255,255,0) 100%);
            z-index: -1; opacity: 0.6; transition: opacity 0.5s;
          }}
          .team-card-pro:hover {{
            transform: translateY(-12px);
            box-shadow: 0 30px 60px rgba(0,0,0,0.08), inset 0 0 0 2px rgba(255,255,255,1);
          }}
          .team-card-pro:hover::before {{ opacity: 1; }}
          .team-avatar-pro {{
            width: 140px; height: 140px; margin: 0 auto 2rem; border-radius: 50%;
            background: var(--team-gradient);
            display: flex; align-items: center; justify-content: center;
            font-size: 3.5rem; color: white; font-weight: 900; font-family: var(--font-heading);
            border: 6px solid white; box-shadow: 0 15px 35px var(--team-shadow);
            position: relative; transition: all 0.6s cubic-bezier(0.34, 1.56, 0.64, 1);
            overflow: hidden;
          }}
          .team-avatar-pro img {{
            width: 100%; height: 100%; object-fit: cover; border-radius: 50%;
          }}
          .team-avatar-pro::after {{
            content: ''; position: absolute; inset: -12px; border-radius: 50%;
            border: 2.5px dashed var(--team-color); opacity: 0; transform: rotate(0deg);
            transition: all 0.6s cubic-bezier(0.34, 1.56, 0.64, 1);
          }}
          .team-card-pro:hover .team-avatar-pro {{
            transform: scale(1.08) translateY(-5px); box-shadow: 0 25px 45px var(--team-shadow);
          }}
          .team-card-pro:hover .team-avatar-pro::after {{
            opacity: 0.5; transform: rotate(180deg);
          }}
          .team-name-pro {{ font-family: var(--font-heading); font-size: 1.6rem; font-weight: 800; color: var(--color-charcoal); margin-bottom: 0.75rem; letter-spacing: -0.5px; line-height: 1.2; min-height: 3.8rem; display: flex; align-items: center; justify-content: center; }}
          .team-role-pro {{ 
            display: inline-block; padding: 6px 18px; border-radius: 100px;
            background: var(--team-color-light); color: var(--team-color);
            font-size: 0.75rem; font-weight: 800; text-transform: uppercase; letter-spacing: 1px;
            margin-bottom: 1.5rem; border: 1px solid rgba(255,255,255,0.5);
            min-height: 2.5rem; display: inline-flex; align-items: center; justify-content: center; text-align: center;
          }}
          .team-details-pro {{ font-size: 1.05rem; color: var(--color-text-secondary); line-height: 1.7; margin: 0; flex-grow: 1; }}
          .team-details-pro strong {{ color: var(--color-charcoal); font-weight: 700; display: block; margin-top: 0.5rem; font-size: 0.85rem; text-transform: uppercase; letter-spacing: 1px; color: var(--team-color); }}
          .team-social-link:hover {{
            background: var(--team-color) !important; color: white !important; transform: scale(1.1);
          }}
          
          /* Navigation Buttons for Slider */
          .slider-nav-btn {{
             width: 48px; height: 48px; border-radius: 50%; background: white; 
             box-shadow: 0 4px 15px rgba(0,0,0,0.1); display: flex; align-items: center; justify-content: center;
             cursor: pointer; transition: all 0.3s; color: var(--color-charcoal); border: 2px solid transparent; outline: none;
          }}
          .slider-nav-btn:hover {{ background: var(--color-teal); color: white; transform: scale(1.1); border-color: var(--color-teal); }}
          .slider-controls {{ display: flex; justify-content: center; gap: 1rem; margin-top: 1rem; }}
        </style>

        <div class="slider-wrapper" style="position: relative;">
            <div class="premium-team-slider" id="teamSlider" data-stagger>
{cards_html}
            </div>
            
            <div class="slider-controls">
                <button class="slider-nav-btn" onclick="document.getElementById('teamSlider').scrollBy({{left: -350, behavior: 'smooth'}})" aria-label="Previous">
                    <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M15 18l-6-6 6-6"/></svg>
                </button>
                <button class="slider-nav-btn" onclick="document.getElementById('teamSlider').scrollBy({{left: 350, behavior: 'smooth'}})" aria-label="Next">
                    <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M9 18l6-6-6-6"/></svg>
                </button>
            </div>
        </div>
      </div>
    </section>'''

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

pattern = re.compile(r'<!-- OUR TEAM.*?</section>', re.DOTALL)
new_content = pattern.sub(section_html, content)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(new_content)
