import re

profiles = [
    {
        'name': 'Mohd Asif Ameen',
        'role': 'Program Lead',
        'loc': 'Samastipur, Bihar',
        'photo': 'mohd_asif_ameen.jpg',
        'link': 'https://www.linkedin.com/in/mohd-asif-ameen-23b041175',
        'category': 'bihar',
        'bio': 'Pioneering community-led learning models and nurturing young minds in Samastipur.'
    },
    {
        'name': 'Tina Aggarwal',
        'role': 'Head of Programs, Delhi',
        'loc': 'Delhi NCR',
        'photo': 'tina_aggarwal.jpg',
        'link': 'https://www.linkedin.com/in/tina-aggarwal-75b41a154',
        'category': 'delhi',
        'bio': 'Leading urban education initiatives and systemic support in Delhi MCD schools.'
    },
    {
        'name': 'Abhishek Kumar Tiwari',
        'role': 'Head of Programs, Bihar',
        'loc': 'Patna, Bihar',
        'photo': 'abhishek_kumar_tiwari.jpg',
        'link': 'https://www.linkedin.com/in/abhishek-tiwari-54b947156',
        'category': 'bihar',
        'bio': 'Driving state-level educational partnerships and teacher capacity building across Bihar.'
    },
    {
        'name': 'Sneha Kumari',
        'role': 'Program Manager',
        'loc': 'Samastipur, Bihar',
        'photo': 'sneha_kumari.jpg',
        'link': 'https://www.linkedin.com/in/sneha-kshamtalaya-2678863a6',
        'category': 'bihar',
        'bio': 'Empowering girls and expanding Fale Fale Shiksha Muhim across rural clusters.'
    },
    {
        'name': 'Tamanna',
        'role': 'Program Lead',
        'loc': 'Delhi NCR',
        'photo': 'tamanna.jpg',
        'link': 'https://www.linkedin.com/in/tamanna-638a80359',
        'category': 'delhi',
        'bio': 'Designing socio-emotional learning frameworks and creative classroom workshops.'
    },
    {
        'name': 'Aman Gautam',
        'role': 'Program Lead',
        'loc': 'Samastipur, Bihar',
        'photo': 'aman_gautam.jpg',
        'link': 'https://www.linkedin.com/in/aman-gautam-8b365a253',
        'category': 'bihar',
        'bio': 'Fostering grassroots leadership and student-centric pedagogy in rural government schools.'
    },
    {
        'name': 'Subham Bhakat',
        'role': 'State Resource Person',
        'loc': 'Patna, Bihar',
        'photo': 'subham_bhakat.jpg',
        'link': 'https://www.linkedin.com/in/subham-bhakat',
        'category': 'bihar',
        'bio': 'Strengthening curriculum alignment and institutional research at the state level.'
    },
    {
        'name': 'Deepak Sirsam',
        'role': 'Program Lead',
        'loc': 'Samastipur, Bihar',
        'photo': 'deepak_sirsam.jpg',
        'link': 'https://www.linkedin.com/in/deepak-sirsam-b645a8256',
        'category': 'bihar',
        'bio': 'Championing experiential learning and community sports for development.'
    },
    {
        'name': 'Priya',
        'role': 'Program Leader',
        'loc': 'Delhi NCR',
        'photo': 'priya.jpg',
        'link': 'https://www.linkedin.com/in/priya-bisht-2319591a3',
        'category': 'delhi',
        'bio': 'Mentoring fellow educators and facilitating STAR Parent engagement circles.'
    },
    {
        'name': 'Aman Kumar',
        'role': 'Program Leader',
        'loc': 'Samastipur, Bihar',
        'photo': 'aman_kumar.jpg',
        'link': 'https://www.linkedin.com/in/aman-kumar-b1a760197',
        'category': 'bihar',
        'bio': 'Building foundation literacy models and joyful learning festivals.'
    },
    {
        'name': 'Reena',
        'role': 'Program Leader',
        'loc': 'Delhi NCR',
        'photo': 'reena.jpg',
        'link': 'https://www.linkedin.com/in/reena-gautam-5bb471245',
        'category': 'delhi',
        'bio': 'Nurturing holistic development and mindfulness practices for young learners.'
    },
    {
        'name': 'Sameep Sonkar',
        'role': 'Program Manager',
        'loc': 'Samastipur, Bihar',
        'photo': 'sameep_sonkar.jpg',
        'link': 'https://www.linkedin.com/in/sameep-sonkar-4148421b8',
        'category': 'bihar',
        'bio': 'Managing field operations, data analytics, and impact measurement frameworks.'
    },
    {
        'name': 'Ishu',
        'role': 'Program Manager',
        'loc': 'Bihar',
        'photo': 'ishu.jpg',
        'link': 'https://www.linkedin.com/in/ishu01',
        'category': 'bihar',
        'bio': 'Curating volunteer engagement and community learning hubs.'
    },
    {
        'name': 'Tabassum',
        'role': 'Community Leader',
        'loc': 'Delhi NCR',
        'photo': 'tabassum.jpg',
        'link': 'https://www.linkedin.com/in/tabassum-mansori-007b87360',
        'category': 'delhi',
        'bio': 'Strengthening parent-school bonds and community advocacy for education.'
    },
    {
        'name': 'Anjali',
        'role': 'Program Leader',
        'loc': 'Delhi NCR',
        'photo': 'anjali.jpg',
        'link': 'https://www.linkedin.com/in/anjali-kumari-01',
        'category': 'delhi',
        'bio': 'Facilitating expressive arts, drama, and creative writing workshops.'
    },
    {
        'name': 'Sangam',
        'role': 'Community Leader',
        'loc': 'Delhi NCR',
        'photo': 'sangam.jpg',
        'link': '#',
        'category': 'delhi',
        'bio': 'Supporting students to develop creative confidence and enhance their 21st-century life skills.',
        'img_pos': 'center 80%'
    },
    {
        'name': 'Pradeep Singh Rathore',
        'role': 'Program lead ( FFSM )',
        'loc': 'Rajasthan',
        'photo': 'pradeep_singh_rathore.jpg',
        'link': '#',
        'category': 'rajasthan',
        'bio': 'Leading foundational learning and community programs across Rajasthan.'
    },
    {
        'name': 'Nikhil Kumar',
        'role': 'Program Lead',
        'loc': 'Samastipur, Bihar',
        'photo': 'nikhil_kumar.jpg',
        'link': 'https://www.linkedin.com/in/nikhilllkr',
        'category': 'bihar',
        'bio': 'Working closely with local stakeholders to improve school ecosystems.'
    },
    {
        'name': 'Priyanka Rambol',
        'role': 'Program Coach, Rajasthan',
        'loc': 'Rajasthan',
        'photo': 'priyanka_rambol.jpg',
        'link': 'https://www.linkedin.com/in/priyankarambol',
        'category': 'rajasthan',
        'bio': 'Coaching educators to adopt holistic learning practices and empathy.'
    }
]

color_palette = [
    {'accent': '#01BADE', 'light': '#E6F8FC', 'border': '#01BADE'},
    {'accent': '#FF6F59', 'light': '#FFF0EE', 'border': '#FF6F59'},
    {'accent': '#F2994A', 'light': '#FEF5EC', 'border': '#F2994A'},
    {'accent': '#6DBE45', 'light': '#F0F9EC', 'border': '#6DBE45'},
    {'accent': '#9B51E0', 'light': '#F5EEFC', 'border': '#9B51E0'}
]

cards_html = ''
for i, p in enumerate(profiles):
    col = color_palette[i % len(color_palette)]
    rot = (-2 + (i % 5) * 1.0)
    
    cards_html += f'''
          <div class="leader-card-item" data-category="{p['category']}">
            <div class="leader-flip-container" style="transform: rotate({rot:.1f}deg);" onclick="this.classList.toggle('flipped')">
              <div class="leader-flip-card">
                <!-- FRONT FACE -->
                <div class="leader-card-front" style="border-top: 5px solid {col['accent']};">
                  <div class="leader-tape"></div>
                  <div class="leader-photo-box">
                    <img src="/assets/team/{p['photo']}" alt="{p['name']}" loading="lazy" class="leader-photo" style="object-position: {p.get('img_pos', 'center 15%')};" />
                  </div>
                  <h3 class="leader-name">{p['name']}</h3>
                  <div class="leader-designation" style="color: {col['accent']}; background: {col['light']};">{p['role']}</div>
                  <div class="leader-location">📍 {p['loc']}</div>
                  
                  <div class="leader-front-actions">
                    <a href="{p['link']}" target="_blank" rel="noopener noreferrer" class="leader-linkedin-btn" onclick="event.stopPropagation();" title="View LinkedIn Profile">
                      <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor"><path d="M20.447 20.452h-3.554v-5.569c0-1.328-.027-3.037-1.852-3.037-1.853 0-2.136 1.445-2.136 2.939v5.667H9.351V9h3.414v1.561h.046c.477-.9 1.637-1.85 3.37-1.85 3.601 0 4.267 2.37 4.267 5.455v6.286zM5.337 7.433c-1.144 0-2.063-.926-2.063-2.065 0-1.138.92-2.063 2.063-2.063 1.14 0 2.064.925 2.064 2.063 0 1.139-.925 2.065-2.064 2.065zm1.782 13.019H3.555V9h3.564v11.452zM22.225 0H1.771C.792 0 0 .774 0 1.729v20.542C0 23.227.792 24 1.771 24h20.451C23.2 24 24 23.227 24 22.271V1.729C24 .774 23.2 0 22.225 0z"/></svg>
                      <span>LinkedIn</span>
                    </a>
                  </div>
                  
                  <div class="leader-flip-hint">Click card to peek bio ✨</div>
                </div>

                <!-- BACK FACE -->
                <div class="leader-card-back" style="border: 3px solid {col['accent']}; background: #FAFDFE;">
                  <div class="leader-tape"></div>
                  <h4 class="leader-back-name" style="color: {col['accent']};">{p['name']}</h4>
                  <div class="leader-back-role">{p['role']}</div>
                  <div class="leader-back-loc">📍 Location: <strong>{p['loc']}</strong></div>
                  
                  <p class="leader-back-bio">"{p['bio']}"</p>
                  
                  <a href="{p['link']}" target="_blank" rel="noopener noreferrer" class="leader-back-linkedin" style="background: {col['accent']};" onclick="event.stopPropagation();">
                    <svg width="18" height="18" viewBox="0 0 24 24" fill="white"><path d="M20.447 20.452h-3.554v-5.569c0-1.328-.027-3.037-1.852-3.037-1.853 0-2.136 1.445-2.136 2.939v5.667H9.351V9h3.414v1.561h.046c.477-.9 1.637-1.85 3.37-1.85 3.601 0 4.267 2.37 4.267 5.455v6.286zM5.337 7.433c-1.144 0-2.063-.926-2.063-2.065 0-1.138.92-2.063 2.063-2.063 1.14 0 2.064.925 2.064 2.063 0 1.139-.925 2.065-2.064 2.065zm1.782 13.019H3.555V9h3.564v11.452zM22.225 0H1.771C.792 0 0 .774 0 1.729v20.542C0 23.227.792 24 1.771 24h20.451C23.2 24 24 23.227 24 22.271V1.729C24 .774 23.2 0 22.225 0z"/></svg>
                    <span>Connect on LinkedIn</span>
                  </a>
                </div>
              </div>
            </div>
          </div>'''

section_html = f'''
    <!-- OUR TEAM -->
    <!-- ════════════════════════════════════════ -->
    <section class="section" id="team" aria-label="Our Leadership Profile" style="background: #FFF9EE; overflow: hidden; position: relative; padding: 6rem 0;">
      <!-- Playful background doodles -->
      <svg class="team-doodle team-doodle-1" width="120" height="120" viewBox="0 0 120 120" style="position:absolute; top: 8%; left: 4%; opacity:0.25; animation: anim-float 6s infinite ease-in-out;"><path fill="none" stroke="#FF6F59" stroke-width="4" stroke-linecap="round" stroke-linejoin="round" d="M10,60 Q30,10 60,60 T110,60"/></svg>
      <svg class="team-doodle team-doodle-2" width="80" height="80" viewBox="0 0 120 120" style="position:absolute; bottom: 12%; right: 5%; opacity:0.25; animation: anim-rotate 15s infinite linear;"><polygon fill="none" stroke="#01BADE" stroke-width="4" points="60,10 110,110 10,110" stroke-linejoin="round"/></svg>

      <div class="container" style="position: relative; z-index: 2; max-width: 1280px; margin: 0 auto; padding: 0 1.5rem;">
        <!-- Header -->
        <div class="section-header reveal" style="text-align: center; margin-bottom: 2rem;">
          <h2 class="partners-title-premium" style="font-family: 'Baloo 2', cursive; font-size: 3.2rem; color: #3A3A3C; line-height: 1.2;">
            Curious about <span style="color: #01BADE; position:relative;">Our Leaders?</span>
          </h2>
          <p class="partners-intro__desc" style="margin: 1rem auto 2rem; max-width: 650px; font-size: 1.2rem; font-weight: 500; color: #55555A;">
            A passionate group of educators and system thinkers. Click a card to peek behind the scenes!
          </p>
          
          <!-- Filter Tabs -->
          <div class="leader-filters" style="display: inline-flex; gap: 0.75rem; background: rgba(0,0,0,0.04); padding: 6px; border-radius: 50px; margin-bottom: 1rem;">
            <button class="filter-btn active" onclick="filterLeaders('all', this)">All Leaders (19)</button>
            <button class="filter-btn" onclick="filterLeaders('rajasthan', this)">📍 Rajasthan Team</button>
            <button class="filter-btn" onclick="filterLeaders('bihar', this)">📍 Bihar Team</button>
            <button class="filter-btn" onclick="filterLeaders('delhi', this)">📍 Delhi Team</button>
          </div>
        </div>

        <style>
          /* 3-Card Carousel Styling */
          .leader-carousel-container {{
            position: relative;
            width: 100%;
            padding: 1rem 0 2rem;
          }}
          .leader-track-wrapper {{
            overflow: hidden;
            border-radius: 24px;
            padding: 1rem 0.5rem 2.5rem;
          }}
          .leader-track {{
            display: flex;
            gap: 2rem;
            overflow-x: auto;
            scroll-snap-type: x mandatory;
            scroll-behavior: smooth;
            padding: 0.5rem 0.5rem 1.5rem;
            -webkit-overflow-scrolling: touch;
            scrollbar-width: thin;
            scrollbar-color: #01BADE rgba(0,0,0,0.05);
          }}
          .leader-track::-webkit-scrollbar {{
            height: 8px;
          }}
          .leader-track::-webkit-scrollbar-track {{
            background: rgba(0,0,0,0.04);
            border-radius: 10px;
          }}
          .leader-track::-webkit-scrollbar-thumb {{
            background: #01BADE;
            border-radius: 10px;
          }}
          
          /* Card Sizing: Exactly 3 visible on Desktop */
          .leader-card-item {{
            flex: 0 0 calc((100% - 4rem) / 3);
            min-width: 320px;
            scroll-snap-align: start;
            transition: all 0.4s ease;
          }}
          @media (max-width: 1024px) {{
            .leader-card-item {{
              flex: 0 0 calc((100% - 2rem) / 2);
            }}
          }}
          @media (max-width: 640px) {{
            .leader-card-item {{
              flex: 0 0 100%;
              min-width: 280px;
            }}
          }}
          
          /* Flip Card Container & Mechanics */
          .leader-flip-container {{
            width: 100%;
            height: 490px;
            perspective: 1200px;
            cursor: pointer;
            transition: transform 0.4s cubic-bezier(0.34, 1.56, 0.64, 1);
          }}
          .leader-flip-container:hover {{
            transform: scale(1.03) rotate(0deg) !important;
            z-index: 10;
          }}
          .leader-flip-card {{
            width: 100%;
            height: 100%;
            position: relative;
            transform-style: preserve-3d;
            transition: transform 0.8s cubic-bezier(0.34, 1.56, 0.64, 1);
          }}
          .leader-flip-container.flipped .leader-flip-card {{
            transform: rotateY(180deg);
          }}
          
          /* Front & Back Card Design */
          .leader-card-front, .leader-card-back {{
            width: 100%;
            height: 100%;
            position: absolute;
            top: 0; left: 0;
            backface-visibility: hidden;
            border-radius: 24px;
            box-shadow: 0 14px 35px rgba(0,0,0,0.08);
            background: #FFFFFF;
            padding: 1.25rem 1.25rem 1rem;
            display: flex;
            flex-direction: column;
            align-items: center;
            border: 1px solid rgba(0,0,0,0.06);
          }}
          
          .leader-tape {{
            position: absolute;
            top: -12px;
            left: 50%;
            transform: translateX(-50%) rotate(-3deg);
            width: 75px;
            height: 22px;
            background: rgba(255,255,255,0.85);
            backdrop-filter: blur(4px);
            border: 1px solid rgba(0,0,0,0.08);
            border-radius: 3px;
            z-index: 10;
          }}
          
          /* Larger, Generous Photo Frame */
          .leader-photo-box {{
            width: 100%;
            height: 260px;
            border-radius: 18px;
            overflow: hidden;
            margin-bottom: 0.85rem;
            background: #f5f5f7;
            box-shadow: inset 0 2px 6px rgba(0,0,0,0.05);
          }}
          .leader-photo {{
            width: 100%;
            height: 100%;
            object-fit: cover;
            object-position: center 15%;
            transition: transform 0.5s ease;
          }}
          .leader-flip-container:hover .leader-photo {{
            transform: scale(1.06);
          }}
          
          .leader-name {{
            font-family: 'Baloo 2', cursive;
            font-size: 1.45rem;
            color: #2D2D2E;
            margin: 0 0 0.3rem 0;
            text-align: center;
            line-height: 1.15;
            font-weight: 700;
          }}
          .leader-designation {{
            font-size: 0.82rem;
            font-weight: 700;
            padding: 4px 12px;
            border-radius: 50px;
            text-align: center;
            margin-bottom: 0.35rem;
            display: inline-block;
          }}
          .leader-location {{
            font-size: 0.85rem;
            color: #666;
            font-weight: 500;
            margin-bottom: 0.5rem;
          }}
          
          .leader-front-actions {{
            margin-top: auto;
            display: flex;
            align-items: center;
            gap: 0.5rem;
          }}
          .leader-linkedin-btn {{
            display: inline-flex;
            align-items: center;
            gap: 6px;
            background: #0A66C2;
            color: #ffffff;
            padding: 6px 16px;
            border-radius: 50px;
            font-size: 0.82rem;
            font-weight: 600;
            text-decoration: none;
            box-shadow: 0 4px 12px rgba(10,102,194,0.25);
            transition: all 0.25s ease;
          }}
          .leader-linkedin-btn:hover {{
            background: #084e96;
            transform: translateY(-2px);
            box-shadow: 0 6px 16px rgba(10,102,194,0.35);
          }}
          
          .leader-flip-hint {{
            font-size: 0.75rem;
            color: #01BADE;
            font-weight: 700;
            margin-top: 0.4rem;
            opacity: 0.85;
          }}
          
          /* Back Card Specifics */
          .leader-card-back {{
            transform: rotateY(180deg);
            justify-content: center;
            text-align: center;
            padding: 2rem 1.5rem;
          }}
          .leader-back-name {{
            font-family: 'Baloo 2', cursive;
            font-size: 1.6rem;
            margin-bottom: 0.25rem;
          }}
          .leader-back-role {{
            font-size: 0.9rem;
            font-weight: 700;
            color: #444;
            margin-bottom: 0.5rem;
          }}
          .leader-back-loc {{
            font-size: 0.85rem;
            color: #666;
            margin-bottom: 1.25rem;
          }}
          .leader-back-bio {{
            font-size: 0.95rem;
            line-height: 1.6;
            color: #4A4A4F;
            font-style: italic;
            margin-bottom: 1.75rem;
            background: rgba(0,0,0,0.02);
            padding: 1rem;
            border-radius: 12px;
            border-left: 3px solid #01BADE;
          }}
          .leader-back-linkedin {{
            display: inline-flex;
            align-items: center;
            justify-content: center;
            gap: 8px;
            color: white;
            padding: 10px 20px;
            border-radius: 50px;
            font-weight: 700;
            font-size: 0.9rem;
            text-decoration: none;
            box-shadow: 0 6px 18px rgba(0,0,0,0.15);
            transition: all 0.3s ease;
          }}
          .leader-back-linkedin:hover {{
            transform: translateY(-3px) scale(1.04);
          }}
          
          /* Navigation Buttons & Dots */
          .filter-btn {{
            background: transparent;
            border: none;
            padding: 8px 18px;
            border-radius: 50px;
            font-size: 0.9rem;
            font-weight: 600;
            color: #555;
            cursor: pointer;
            transition: all 0.25s ease;
          }}
          .filter-btn.active, .filter-btn:hover {{
            background: #ffffff;
            color: #01BADE;
            box-shadow: 0 3px 10px rgba(0,0,0,0.08);
          }}
          
          .leader-controls {{
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 1.5rem;
            margin-top: 1rem;
          }}
          .leader-nav-btn {{
            width: 48px;
            height: 48px;
            border-radius: 50%;
            background: #FFFFFF;
            border: 2px solid #E5E7EB;
            color: #2D2D2E;
            display: flex;
            align-items: center;
            justify-content: center;
            cursor: pointer;
            transition: all 0.3s ease;
            box-shadow: 0 4px 12px rgba(0,0,0,0.05);
          }}
          .leader-nav-btn:hover {{
            background: #01BADE;
            color: #FFFFFF;
            border-color: #01BADE;
            transform: scale(1.1);
            box-shadow: 0 6px 18px rgba(1, 186, 222, 0.3);
          }}
          
          .leader-dots {{
            display: flex;
            gap: 8px;
            align-items: center;
          }}
          .leader-dot {{
            width: 10px;
            height: 10px;
            border-radius: 50%;
            background: #D1D5DB;
            cursor: pointer;
            transition: all 0.3s ease;
          }}
          .leader-dot.active {{
            width: 28px;
            border-radius: 10px;
            background: #01BADE;
          }}
        </style>

        <!-- Carousel Wrapper -->
        <div class="leader-carousel-container">
          <div class="leader-track-wrapper">
            <div class="leader-track" id="leaderTrack">
{cards_html}
            </div>
          </div>

          <!-- Bottom Navigation Controls -->
          <div class="leader-controls">
            <button class="leader-nav-btn" onclick="scrollLeaderTrack(-1)" aria-label="Previous Leaders">
              <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><path d="M15 18l-6-6 6-6"/></svg>
            </button>

            <div class="leader-dots" id="leaderDots">
              <div class="leader-dot active" onclick="jumpLeaderSlide(0)"></div>
              <div class="leader-dot" onclick="jumpLeaderSlide(1)"></div>
              <div class="leader-dot" onclick="jumpLeaderSlide(2)"></div>
              <div class="leader-dot" onclick="jumpLeaderSlide(3)"></div>
              <div class="leader-dot" onclick="jumpLeaderSlide(4)"></div>
            </div>

            <button class="leader-nav-btn" onclick="scrollLeaderTrack(1)" aria-label="Next Leaders">
              <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><path d="M9 18l6-6-6-6"/></svg>
            </button>
          </div>
        </div>
      </div>
    </section>'''

files_to_update = ['index.html', 'story.html']
pattern = re.compile(r'<!-- OUR TEAM.*?</section>', re.DOTALL)

for file_path in files_to_update:
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        new_content = pattern.sub(section_html, content)
        
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f'Successfully updated {file_path}')
    except Exception as e:
        print(f"Failed to update {file_path}: {e}")

print('Successfully enlarged leader photo box to 260px and card height to 490px!')
