import re
import os

html_path = r"C:\Users\Saurav\Desktop\Kshamatalaya\index.html"
with open(html_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Define the new HTML structure for the programs section
new_programs_html = """
    <section class="section section--cream doodle-bg" id="programs" aria-label="Our Programs">
      <!-- Section Doodles -->
      <svg class="section-doodle section-doodle--bob2" style="top: 5%; left: 4%; width: 42px;" viewBox="0 0 42 42" aria-hidden="true">
        <rect x="6" y="6" width="30" height="30" rx="6" fill="none" stroke="#1CA6A0" stroke-width="2" transform="rotate(12 21 21)" stroke-dasharray="6 4"/>
      </svg>
      <svg class="section-doodle section-doodle--bob1" style="bottom: 10%; right: 4%; width: 38px;" viewBox="0 0 38 38" aria-hidden="true">
        <path d="M19 4 L22 14 L33 14 L24 20 L27 31 L19 25 L11 31 L14 20 L5 14 L16 14 Z" fill="none" stroke="#FFC72C" stroke-width="1.5" stroke-linejoin="round"/>
      </svg>
      <svg class="section-doodle section-doodle--bob3" style="top: 45%; right: 2%; width: 24px;" viewBox="0 0 24 24" aria-hidden="true">
        <circle cx="12" cy="12" r="10" fill="none" stroke="#FF6F59" stroke-width="1.5"/>
        <circle cx="12" cy="12" r="5" fill="#FF6F59" opacity="0.15"/>
      </svg>
      
      <div class="container">
        <style>
          .programs-header-layout {
            display: flex; align-items: center; justify-content: center; gap: 2rem; 
            max-width: 900px; margin: 0 auto 3rem; text-align: left; flex-wrap: wrap;
          }
          .programs-header-text { flex: 1; min-width: 300px; }
          .programs-header-text .section-header__eyebrow { margin-left: 0; margin-right: 0; }
          .programs-header-text .section-header__title { margin-left: 0; margin-right: 0; text-align: left; }
          .programs-header-text .section-header__desc { margin-left: 0; margin-right: 0; text-align: left; }
          .programs-header-image { flex: 0 0 250px; text-align: center; }
          .programs-header-image img {
            width: 100%; height: auto; border-radius: 24px; box-shadow: 0 10px 30px rgba(0,0,0,0.1);
            transform: rotate(5deg); transition: transform 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
          }
          .programs-header-image img:hover { transform: rotate(0deg) scale(1.05); }

          /* ── Image-based Program Cards ── */
          .prog-masonry {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 2rem;
            margin-bottom: 3rem;
          }
          
          .prog-card {
            position: relative;
            border-radius: 24px;
            overflow: hidden;
            background: #000;
            aspect-ratio: 4/5;
            box-shadow: 0 15px 35px rgba(0,0,0,0.15);
            transition: all 0.5s cubic-bezier(0.2, 0.8, 0.2, 1);
            display: flex;
            flex-direction: column;
            justify-content: flex-end;
            text-decoration: none;
            color: #fff;
            group: prog-card;
          }
          
          .prog-card.horizontal {
            grid-column: span 2;
            aspect-ratio: 2/1;
          }
          
          @media (max-width: 768px) {
            .prog-card.horizontal { grid-column: span 1; aspect-ratio: 4/5; }
          }
          
          .prog-card__bg {
            position: absolute;
            top: 0; left: 0;
            width: 100%; height: 100%;
            object-fit: cover;
            transition: transform 0.7s cubic-bezier(0.2, 0.8, 0.2, 1), opacity 0.5s ease;
            opacity: 0.85;
          }
          
          .prog-card:hover .prog-card__bg {
            transform: scale(1.08);
            opacity: 0.5;
          }
          
          .prog-card__overlay {
            position: absolute;
            bottom: 0; left: 0;
            width: 100%; height: 75%;
            background: linear-gradient(to top, rgba(0,0,0,0.9) 0%, rgba(0,0,0,0.4) 50%, transparent 100%);
            transition: height 0.5s ease;
            z-index: 1;
          }
          
          .prog-card:hover .prog-card__overlay {
            height: 100%;
            background: linear-gradient(to top, rgba(0,0,0,0.9) 0%, rgba(0,0,0,0.6) 100%);
          }
          
          .prog-card__content {
            position: relative;
            z-index: 2;
            padding: 2.5rem 2rem;
            transform: translateY(35px);
            transition: transform 0.5s cubic-bezier(0.2, 0.8, 0.2, 1);
          }
          
          .prog-card:hover .prog-card__content {
            transform: translateY(0);
          }
          
          .prog-card__theme {
            display: inline-block;
            font-size: 0.75rem;
            font-weight: 700;
            text-transform: uppercase;
            letter-spacing: 1px;
            padding: 6px 14px;
            border-radius: 50px;
            margin-bottom: 1rem;
            backdrop-filter: blur(8px);
            -webkit-backdrop-filter: blur(8px);
          }
          
          .prog-card__title {
            font-family: 'Baloo 2', cursive;
            font-size: 2rem;
            line-height: 1.1;
            margin-bottom: 0.75rem;
            color: #ffffff;
            text-shadow: 0 2px 10px rgba(0,0,0,0.5);
          }
          
          .prog-card__location {
            display: flex;
            align-items: center;
            gap: 6px;
            font-size: 0.9rem;
            color: rgba(255,255,255,0.9);
            margin-bottom: 1rem;
            font-weight: 500;
          }
          
          .prog-card__desc {
            font-size: 1rem;
            line-height: 1.5;
            color: rgba(255,255,255,0.85);
            opacity: 0;
            max-height: 0;
            overflow: hidden;
            transition: all 0.5s cubic-bezier(0.2, 0.8, 0.2, 1);
          }
          
          .prog-card:hover .prog-card__desc {
            opacity: 1;
            max-height: 150px;
            margin-top: 1rem;
          }
          
          .prog-card__arrow {
            position: absolute;
            top: 2rem;
            right: 2rem;
            width: 48px;
            height: 48px;
            background: rgba(255,255,255,0.15);
            backdrop-filter: blur(10px);
            -webkit-backdrop-filter: blur(10px);
            border: 1px solid rgba(255,255,255,0.3);
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            color: #fff;
            transform: scale(0.8) rotate(-45deg);
            opacity: 0;
            transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
            z-index: 2;
          }
          
          .prog-card:hover .prog-card__arrow {
            transform: scale(1) rotate(0deg);
            opacity: 1;
            background: var(--theme-color);
            border-color: transparent;
          }
        </style>

        <div class="reveal programs-header-layout">
          <div class="programs-header-text">
            <div class="section-header__eyebrow">What We Do</div>
            <h2 class="section-header__title">Our <span class="doodle-highlight">Programs<svg class="doodle-highlight__squiggle" viewBox="0 0 200 16" preserveAspectRatio="none" aria-hidden="true"><path d="M0 8 Q 25 2, 50 8 T 100 8 T 150 8 T 200 8" fill="none" stroke="#1CA6A0" stroke-width="3" stroke-linecap="round" class="doodle-squiggle-draw" opacity="0.4"/></svg></span></h2>
            <p class="section-header__desc">
              Five interconnected programs working across three approaches — Demonstration, 
              Community Leadership, and Systems Excellence — all anchoring the child at the center.
            </p>
          </div>
          <div class="programs-header-image">
            <img src="/assets/illustrations/3d_pencils.jpg" alt="Creative 3D Pencils" />
          </div>
        </div>

        <div class="prog-masonry">
          
          <!-- School Excellence Program -->
          <a href="/programs/cell.html" class="prog-card horizontal reveal" style="--theme-color: #1CA6A0;">
            <img class="prog-card__bg" src="/assets/programs/joyful-learning.jpg" alt="School Excellence Program" loading="lazy">
            <div class="prog-card__overlay"></div>
            <div class="prog-card__arrow"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round"><path d="M5 12h14M12 5l7 7-7 7"/></svg></div>
            <div class="prog-card__content">
              <div class="prog-card__theme" style="background: rgba(28,166,160,0.85); border: 1px solid rgba(255,255,255,0.4);">Demonstration Approach</div>
              <h3 class="prog-card__title">School Excellence Program</h3>
              <div class="prog-card__location">
                <svg width="14" height="14" viewBox="0 0 14 14" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"><path d="M7 1C4.5 1 2.5 3 2.5 5.5C2.5 9 7 13 7 13C7 13 11.5 9 11.5 5.5C11.5 3 9.5 1 7 1Z"/><circle cx="7" cy="5.5" r="1.5"/></svg>
                Rajasthan
              </div>
              <p class="prog-card__desc">We embed dedicated facilitators directly inside government schools to systematically transition them into self-sustaining hubs of quality learning, student well-being, and structured institutional governance.</p>
            </div>
          </a>

          <!-- Teacher Support Program -->
          <a href="/programs/learning-festivals.html" class="prog-card reveal" style="--theme-color: #FFC72C;">
            <img class="prog-card__bg" src="/assets/programs/teachers-workshop.jpg" alt="Teacher Support Program" loading="lazy">
            <div class="prog-card__overlay"></div>
            <div class="prog-card__arrow"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round"><path d="M5 12h14M12 5l7 7-7 7"/></svg></div>
            <div class="prog-card__content">
              <div class="prog-card__theme" style="background: rgba(255,199,44,0.85); color: #2D2D2E; border: 1px solid rgba(255,255,255,0.4);">Demonstration Approach</div>
              <h3 class="prog-card__title">Teacher Support Program</h3>
              <div class="prog-card__location">
                <svg width="14" height="14" viewBox="0 0 14 14" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"><path d="M7 1C4.5 1 2.5 3 2.5 5.5C2.5 9 7 13 7 13C7 13 11.5 9 11.5 5.5C11.5 3 9.5 1 7 1Z"/><circle cx="7" cy="5.5" r="1.5"/></svg>
                Multiple Locations
              </div>
              <p class="prog-card__desc">A targeted, peer-led professional development model that equips public school educators with the precise instructional toolkits and mental health frameworks needed to manage complex classrooms.</p>
            </div>
          </a>

          <!-- Fale Fale Shiksha Muhim -->
          <a href="/programs/fale-fale.html" class="prog-card reveal" style="--theme-color: #FF6F59;">
            <img class="prog-card__bg" src="/assets/programs/kahani-utsav.jpg" alt="Fale Fale Shiksha Muhim" loading="lazy">
            <div class="prog-card__overlay"></div>
            <div class="prog-card__arrow"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round"><path d="M5 12h14M12 5l7 7-7 7"/></svg></div>
            <div class="prog-card__content">
              <div class="prog-card__theme" style="background: rgba(255,111,89,0.85); border: 1px solid rgba(255,255,255,0.4);">Community Leadership</div>
              <h3 class="prog-card__title">Fale Fale Shiksha Muhim</h3>
              <div class="prog-card__location">
                <svg width="14" height="14" viewBox="0 0 14 14" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"><path d="M7 1C4.5 1 2.5 3 2.5 5.5C2.5 9 7 13 7 13C7 13 11.5 9 11.5 5.5C11.5 3 9.5 1 7 1Z"/><circle cx="7" cy="5.5" r="1.5"/></svg>
                Gogunda, Rajasthan
              </div>
              <p class="prog-card__desc">A localized, doorstep-delivery learning model that maps, trains, and deploys neighborhood youth to bridge foundational literacy deficits right inside children's homes.</p>
            </div>
          </a>

          <!-- Learning Festivals Internship -->
          <a href="/programs/learning-festivals.html" class="prog-card reveal" style="--theme-color: #9B51E0;">
            <img class="prog-card__bg" src="/assets/programs/learning-festival.jpg" alt="Learning Festivals Internship" loading="lazy">
            <div class="prog-card__overlay"></div>
            <div class="prog-card__arrow"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round"><path d="M5 12h14M12 5l7 7-7 7"/></svg></div>
            <div class="prog-card__content">
              <div class="prog-card__theme" style="background: rgba(155,81,224,0.85); border: 1px solid rgba(255,255,255,0.4);">Community Leadership</div>
              <h3 class="prog-card__title">Learning Festivals Internship</h3>
              <div class="prog-card__location">
                <svg width="14" height="14" viewBox="0 0 14 14" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"><path d="M7 1C4.5 1 2.5 3 2.5 5.5C2.5 9 7 13 7 13C7 13 11.5 9 11.5 5.5C11.5 3 9.5 1 7 1Z"/><circle cx="7" cy="5.5" r="1.5"/></svg>
                Multiple Locations
              </div>
              <p class="prog-card__desc">A short-term immersion track where outside talent pairs with local youth to run intensive, project-based camps focused on children's practical reasoning and self-expression.</p>
            </div>
          </a>

          <!-- STAR Parents -->
          <a href="/donate.html#partner" class="prog-card horizontal reveal" style="--theme-color: #01BADE;">
            <img class="prog-card__bg" src="/assets/programs/star-parents.jpg" alt="STAR Parents" loading="lazy">
            <div class="prog-card__overlay"></div>
            <div class="prog-card__arrow"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round"><path d="M5 12h14M12 5l7 7-7 7"/></svg></div>
            <div class="prog-card__content">
              <div class="prog-card__theme" style="background: rgba(1,186,222,0.85); border: 1px solid rgba(255,255,255,0.4);">Systems Excellence</div>
              <h3 class="prog-card__title">STAR Parents</h3>
              <div class="prog-card__location">
                <svg width="14" height="14" viewBox="0 0 14 14" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"><path d="M7 1C4.5 1 2.5 3 2.5 5.5C2.5 9 7 13 7 13C7 13 11.5 9 11.5 5.5C11.5 3 9.5 1 7 1Z"/><circle cx="7" cy="5.5" r="1.5"/></svg>
                Adopted by MCD, All Regions
              </div>
              <p class="prog-card__desc">A structural intervention that organizes and coaches parents to actively run School Management Committees, establishing a permanent system of civic oversight and at-home learning routines.</p>
            </div>
          </a>

        </div>

        <div class="text-center reveal" style="margin-top: 1rem;">
          <a href="/programs.html" class="btn btn--secondary">
            Explore All Programs
            <svg width="16" height="16" viewBox="0 0 16 16" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="M4 8H12M12 8L8 4M12 8L8 12"/></svg>
          </a>
        </div>
      </div>
    </section>
"""

start_tag = '<section class="section section--cream doodle-bg" id="programs" aria-label="Our Programs">'
end_tag = '<!-- ════════════════════════════════════════ -->\n        <!-- ════════════════════════════════════════ -->\n    <section class="press-strip"'

start_idx = content.find(start_tag)
if start_idx == -1:
    print("Error: start_tag not found")
else:
    end_idx = content.find(end_tag, start_idx)
    if end_idx == -1:
        # try without the indentation on the second comment line
        alt_end_tag = '<!-- ════════════════════════════════════════ -->\n    <!-- ════════════════════════════════════════ -->\n    <section class="press-strip"'
        end_idx = content.find(alt_end_tag, start_idx)
        if end_idx == -1:
             # Just look for the press strip class
             alt_end_tag2 = '<section class="press-strip"'
             end_idx = content.find(alt_end_tag2, start_idx)
             if end_idx != -1:
                 # find the preceding comments
                 comment_idx = content.rfind('<!-- ════', start_idx, end_idx)
                 if comment_idx != -1:
                     end_idx = comment_idx

    if end_idx == -1:
        print("Error: end_tag not found")
    else:
        new_content = content[:start_idx] + new_programs_html + "\n    " + content[end_idx:]
        with open(html_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print("Successfully updated the Our Programs section in index.html")
