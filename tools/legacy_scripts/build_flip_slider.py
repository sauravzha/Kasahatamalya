import re
import os
import random

profiles = [
    ('Mohd Asif Ameen', 'Program Lead', 'Samastipur', 'mohd_asif_ameen.jpg'),
    ('Sneha Kumari', 'Program manager', 'Samastipur', 'sneha_kumari.jpg'),
    ('Aman Gautam', 'Program Lead', 'Samastipur', 'aman_gautam.jpg'),
    ('Deepak Sirsam', 'Program Lead', 'Samastipur', 'deepak_sirsam.jpg'),
    ('Aman Kumar', 'Program Leader', 'Samastipur', 'aman_kumar.jpg'),
    ('Sameep Sonkar', 'Program Manager', 'Samastipur', 'sameep_sonkar.jpg'),
    ('Subham Bhakat', 'State Resource Person', 'Patna, Bihar', 'subham_bhakat.jpg'),
    ('Tina Aggarwal', 'Head of Programs, Delhi', 'Delhi', 'tina_aggarwal.jpg'),
    ('Tamanna', 'Program Lead', 'Delhi', 'tamanna.jpg'),
    ('Priya', 'Program Leader', 'Delhi', 'priya.jpg'),
    ('Abhishek Kumar Tiwari', 'Head of Programs, Bihar', 'Bihar', 'abhishek_kumar_tiwari.jpg'),
    ('Reena', 'Program Leader', 'Delhi', 'reena.jpg'),
    ('Ishu', 'Program Manager', 'Bihar', 'ishu.jpg'),
    ('Tabassum', 'Community Leader', 'Delhi', 'tabassum.jpg'),
    ('Anjali', 'Program Leader', 'Delhi', 'anjali.jpg'),
    ('Pradeep Singh Rathore', 'Program lead ( FFSM )', 'Rajasthan', 'pradeep_singh_rathore.jpg')
]

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

cards_html = ''

for name, role, loc, photo in profiles:
    link = links.get(name, '#')
    
    # Slight random rotation for curious/child-like polaroid aesthetic
    rotation = random.uniform(-4, 4)
    
    # Random fun accent color
    colors = ['#FF6F59', '#F2994A', '#01BADE', '#6DBE45', '#FFC72C']
    color = random.choice(colors)
    
    # We check if photo actually exists in assets/team
    photo_path = os.path.join(r"C:\Users\Saurav\Desktop\Kshamatalaya\assets\team", photo)
    if os.path.exists(photo_path):
        img_el = f'<img src="/assets/team/{photo}" alt="{name}" class="flip-photo">'
    else:
        initial = name[0]
        img_el = f'<div class="flip-photo-placeholder" style="background:{color};">{initial}</div>'

    cards_html += f'''
          <div class="flip-card-container" style="transform: rotate({rotation:.1f}deg);" onclick="this.classList.toggle('flipped')">
            <div class="flip-card">
              <!-- FRONT -->
              <div class="flip-card-front">
                <div class="flip-card-tape"></div>
                <div class="flip-photo-wrapper">
                    {img_el}
                </div>
                <h3 class="flip-name">{name}</h3>
                <div class="flip-hint">Click me! ✨</div>
              </div>
              <!-- BACK -->
              <div class="flip-card-back" style="border-color: {color};">
                <div class="flip-card-tape"></div>
                <h3 class="flip-back-name" style="color: {color};">{name}</h3>
                <div class="flip-role">{role}</div>
                <div class="flip-loc">📍 {loc}</div>
                <a href="{link}" target="_blank" rel="noopener noreferrer" class="flip-social" style="background: {color};" onclick="event.stopPropagation();">
                  <svg width="20" height="20" viewBox="0 0 24 24" fill="white"><path d="M20.447 20.452h-3.554v-5.569c0-1.328-.027-3.037-1.852-3.037-1.853 0-2.136 1.445-2.136 2.939v5.667H9.351V9h3.414v1.561h.046c.477-.9 1.637-1.85 3.37-1.85 3.601 0 4.267 2.37 4.267 5.455v6.286zM5.337 7.433c-1.144 0-2.063-.926-2.063-2.065 0-1.138.92-2.063 2.063-2.063 1.14 0 2.064.925 2.064 2.063 0 1.139-.925 2.065-2.064 2.065zm1.782 13.019H3.555V9h3.564v11.452zM22.225 0H1.771C.792 0 0 .774 0 1.729v20.542C0 23.227.792 24 1.771 24h20.451C23.2 24 24 23.227 24 22.271V1.729C24 .774 23.2 0 22.225 0z"/></svg>
                </a>
              </div>
            </div>
          </div>'''

# We need a double marquee track for infinite seamless scroll
marquee_html = f'''
        <div class="marquee-track">
            {cards_html}
        </div>
        <div class="marquee-track">
            {cards_html}
        </div>
'''

section_html = f'''
    <!-- OUR TEAM -->
    <!-- ════════════════════════════════════════ -->
    <section class="section" id="team" aria-label="Our Leadership Profile" style="background: #FFF9EE; overflow: hidden; position: relative; padding: 6rem 0;">
      <!-- Playful background doodles -->
      <svg class="team-doodle team-doodle-1" width="120" height="120" viewBox="0 0 120 120" style="position:absolute; top: 10%; left: 5%; opacity:0.3; animation: anim-float 6s infinite ease-in-out;"><path fill="none" stroke="#FF6F59" stroke-width="4" stroke-linecap="round" stroke-linejoin="round" d="M10,60 Q30,10 60,60 T110,60"/></svg>
      <svg class="team-doodle team-doodle-2" width="80" height="80" viewBox="0 0 120 120" style="position:absolute; bottom: 15%; right: 8%; opacity:0.3; animation: anim-rotate 15s infinite linear;"><polygon fill="none" stroke="#01BADE" stroke-width="4" points="60,10 110,110 10,110" stroke-linejoin="round"/></svg>
      <svg class="team-doodle team-doodle-3" width="100" height="100" viewBox="0 0 120 120" style="position:absolute; top: 20%; right: 15%; opacity:0.3; animation: anim-wiggle 4s infinite;"><circle fill="none" stroke="#F2994A" stroke-width="4" cx="60" cy="60" r="40" stroke-dasharray="10 10"/></svg>

      <div class="container" style="position: relative; z-index: 2; max-width: 100%; overflow: hidden;">
        <div class="section-header reveal" style="text-align: center;">
          <h2 class="partners-title-premium" style="font-family: 'Baloo 2', cursive; font-size: 3.5rem; color: #3A3A3C;">Curious about <span style="color: #01BADE; position:relative;">Our Leaders?</span></h2>
          <p class="partners-intro__desc" style="margin: 1rem auto 3rem; max-width: 600px; font-size: 1.25rem; font-weight: 500;">
            A passionate group of educators and system thinkers. Click a card to peek behind the scenes!
          </p>
        </div>

        <style>
          .marquee-container {{
            position: relative;
            width: 100%;
            overflow: hidden;
            display: flex;
            padding: 2rem 0 4rem;
            mask-image: linear-gradient(to right, transparent, black 5%, black 95%, transparent);
            -webkit-mask-image: linear-gradient(to right, transparent, black 5%, black 95%, transparent);
          }}
          .marquee-track {{
            display: flex;
            gap: 3rem;
            padding-right: 3rem;
            animation: teamMarquee 40s linear infinite;
            flex-shrink: 0;
            align-items: center;
          }}
          .marquee-container:hover .marquee-track {{
            animation-play-state: paused;
          }}
          @keyframes teamMarquee {{
            0% {{ transform: translateX(0); }}
            100% {{ transform: translateX(-100%); }}
          }}
          
          /* Flip Card Mechanics */
          .flip-card-container {{
            width: 280px;
            height: 340px;
            perspective: 1200px;
            cursor: pointer;
            flex-shrink: 0;
            transition: transform 0.4s cubic-bezier(0.34, 1.56, 0.64, 1);
          }}
          .flip-card-container:hover {{
            transform: scale(1.05) rotate(0deg) !important;
            z-index: 10;
          }}
          .flip-card {{
            width: 100%;
            height: 100%;
            position: relative;
            transform-style: preserve-3d;
            transition: transform 0.8s cubic-bezier(0.34, 1.56, 0.64, 1);
          }}
          .flip-card-container.flipped .flip-card {{
            transform: rotateY(180deg);
          }}
          
          /* Card Faces */
          .flip-card-front, .flip-card-back {{
            width: 100%;
            height: 100%;
            position: absolute;
            top: 0; left: 0;
            backface-visibility: hidden;
            border-radius: 20px;
            box-shadow: 0 15px 35px rgba(0,0,0,0.1);
            background: #FFFFFF;
            padding: 1.5rem;
            display: flex;
            flex-direction: column;
            align-items: center;
            border: 4px solid #fff;
          }}
          
          /* Tape Effect */
          .flip-card-tape {{
            position: absolute;
            top: -12px;
            left: 50%;
            transform: translateX(-50%) rotate(-3deg);
            width: 80px;
            height: 25px;
            background: rgba(255,255,255,0.6);
            backdrop-filter: blur(4px);
            border: 1px solid rgba(0,0,0,0.05);
            box-shadow: 0 2px 5px rgba(0,0,0,0.05);
            z-index: 10;
          }}
          
          /* Front Specifics */
          .flip-photo-wrapper {{
            width: 100%;
            height: 220px;
            border-radius: 12px;
            overflow: hidden;
            margin-bottom: 1rem;
            background: #f0f0f0;
            box-shadow: inset 0 4px 10px rgba(0,0,0,0.05);
          }}
          .flip-photo {{
            width: 100%;
            height: 100%;
            object-fit: cover;
            object-position: center 15%;
          }}
          .flip-photo-placeholder {{
            width: 100%; height: 100%;
            display: flex; align-items: center; justify-content: center;
            font-size: 5rem; color: white; font-family: 'Baloo 2', cursive; font-weight: 800;
          }}
          .flip-name {{
            font-family: 'Baloo 2', cursive;
            font-size: 1.5rem;
            color: #3A3A3C;
            margin: 0;
            text-align: center;
            line-height: 1.2;
          }}
          .flip-hint {{
            font-size: 0.85rem;
            color: #01BADE;
            font-weight: 700;
            text-transform: uppercase;
            letter-spacing: 1px;
            margin-top: 0.5rem;
            opacity: 0.7;
          }}
          
          /* Back Specifics */
          .flip-card-back {{
            transform: rotateY(180deg);
            background: #FAFCFC;
            border-width: 6px;
            justify-content: center;
            text-align: center;
            background-image: radial-gradient(#00000010 1px, transparent 1px);
            background-size: 15px 15px;
          }}
          .flip-back-name {{
            font-family: 'Baloo 2', cursive;
            font-size: 1.8rem;
            margin-bottom: 0.5rem;
            line-height: 1.1;
          }}
          .flip-role {{
            font-weight: 700;
            color: #3A3A3C;
            font-size: 1.1rem;
            margin-bottom: 1rem;
            background: white;
            padding: 8px 16px;
            border-radius: 50px;
            box-shadow: 0 4px 10px rgba(0,0,0,0.05);
            display: inline-block;
          }}
          .flip-loc {{
            font-size: 1rem;
            color: #888;
            font-weight: 500;
            margin-bottom: 2rem;
          }}
          .flip-social {{
            display: inline-flex;
            align-items: center;
            justify-content: center;
            width: 50px;
            height: 50px;
            border-radius: 50%;
            box-shadow: 0 8px 20px rgba(0,0,0,0.15);
            transition: transform 0.3s cubic-bezier(0.34, 1.56, 0.64, 1);
          }}
          .flip-social:hover {{
            transform: scale(1.15) translateY(-5px);
          }}
        </style>

        <div class="marquee-container">
            {marquee_html}
        </div>
      </div>
    </section>'''

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

pattern = re.compile(r'<!-- OUR TEAM.*?</section>', re.DOTALL)
new_content = pattern.sub(section_html, content)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(new_content)
