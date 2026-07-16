import re

values = [
    {
        "num": "1",
        "title": "Compassion",
        "quote": '"Compassion is recognizing suffering, understanding its universality, and taking action to alleviate it with empathy and care."',
        "text": "At Kshamtalaya, we integrate compassion by supporting students, teachers, and communities in their challenges, ensuring we respond with empathy and create nurturing environments for growth.",
        "color": "#08B9DB",
        "light": "rgba(8, 185, 219, 0.1)",
        "icon": "M4.318 6.318a4.5 4.5 0 000 6.364L12 20.364l7.682-7.682a4.5 4.5 0 00-6.364-6.364L12 7.636l-1.318-1.318a4.5 4.5 0 00-6.364 0z"
    },
    {
        "num": "2",
        "title": "Freedom with Responsibility",
        "quote": '"True freedom comes with the responsibility to be accountable for your actions, making choices that impact others and owning both successes and mistakes."',
        "text": "We empower our educators and students to make decisions and take ownership of their learning and growth, fostering an environment where responsibility is valued alongside freedom.",
        "color": "#F2994A",
        "light": "rgba(242, 153, 74, 0.1)",
        "icon": "M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"
    },
    {
        "num": "3",
        "title": "Excellence",
        "quote": '"Excellence is about striving to be better every day, dedicating yourself to doing your best and growing through each experience."',
        "text": "In our work, excellence is evident in our commitment to continuously improving educational practices and striving for the highest standards in every program we implement.",
        "color": "#6DBE45",
        "light": "rgba(109, 190, 69, 0.1)",
        "icon": "M11.049 2.927c.3-.921 1.603-.921 1.902 0l1.519 4.674a1 1 0 00.95.69h4.915c.969 0 1.371 1.24.588 1.81l-3.976 2.888a1 1 0 00-.363 1.118l1.518 4.674c.3.922-.755 1.688-1.538 1.118l-3.976-2.888a1 1 0 00-1.176 0l-3.976 2.888c-.783.57-1.838-.197-1.538-1.118l1.518-4.674a1 1 0 00-.363-1.118l-3.976-2.888c-.784-.57-.38-1.81.588-1.81h4.914a1 1 0 00.951-.69l1.519-4.674z"
    },
    {
        "num": "4",
        "title": "Trust",
        "quote": '"Trust is the foundation of a safe and engaged environment, built on transparency, unconditional support, and the reliability of keeping commitments."',
        "text": "Kshamtalaya fosters trust by being transparent in our processes, encouraging open communication, and creating spaces where mistakes are seen as opportunities for growth rather than failures.",
        "color": "#FF6F59",
        "light": "rgba(255, 111, 89, 0.1)",
        "icon": "M17 20h5v-2a3 3 0 00-5.356-1.857M17 20H7m10 0v-2c0-.656-.126-1.283-.356-1.857M7 20H2v-2a3 3 0 015.356-1.857M7 20v-2c0-.656.126-1.283.356-1.857m0 0a5.002 5.002 0 019.288 0M15 7a3 3 0 11-6 0 3 3 0 016 0zm6 3a2 2 0 11-4 0 2 2 0 014 0zM7 10a2 2 0 11-4 0 2 2 0 014 0z"
    }
]

grid_html = ""
for val in values:
    grid_html += f'''
          <div class="val-card" style="--val-color: {val['color']}; --val-light: {val['light']};">
            <div class="val-card-front">
              <div class="val-number">{val['num']}</div>
              <div class="val-icon">
                <svg width="40" height="40" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                  <path d="{val['icon']}"></path>
                </svg>
              </div>
              <h3 class="val-title">{val['title']}</h3>
              <div class="val-hint">Hover to explore</div>
            </div>
            
            <div class="val-card-content">
              <div class="val-quote">{val['quote']}</div>
              <div class="val-desc">{val['text']}</div>
            </div>
          </div>
    '''

section_html = f'''
    <!-- OUR VALUES -->
    <!-- ════════════════════════════════════════ -->
    <section class="section" id="values" aria-label="Our Values" style="background: #FAFCFC; position: relative; overflow: hidden; padding: 6rem 0;">
      <!-- Floating bubbles -->
      <div style="position: absolute; top: 5%; left: -5%; width: 300px; height: 300px; background: rgba(8, 185, 219, 0.05); border-radius: 50%; filter: blur(40px);"></div>
      <div style="position: absolute; bottom: -5%; right: -5%; width: 400px; height: 400px; background: rgba(242, 153, 74, 0.05); border-radius: 50%; filter: blur(60px);"></div>

      <div class="container" style="position: relative; z-index: 2;">
        <div class="section-header reveal" style="text-align: center;">
          <h2 class="partners-title-premium" style="font-family: 'Baloo 2', cursive; font-size: 3.5rem; color: var(--color-charcoal);">Our <span style="color: var(--color-teal); position:relative;">Core Values</span></h2>
          <p class="partners-intro__desc" style="margin: 1rem auto 3rem; max-width: 600px; font-size: 1.25rem; font-weight: 500;">
            The guiding principles that shape our culture, our actions, and our commitment to every child.
          </p>
        </div>

        <style>
          .val-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 2rem;
            max-width: 1000px;
            margin: 0 auto;
          }}
          .val-card {{
            background: white;
            border-radius: 24px;
            padding: 3rem 2rem;
            text-align: center;
            box-shadow: 0 10px 30px rgba(0,0,0,0.04);
            position: relative;
            overflow: hidden;
            transition: all 0.5s cubic-bezier(0.34, 1.56, 0.64, 1);
            border: 2px solid transparent;
            display: flex;
            flex-direction: column;
            justify-content: center;
            cursor: pointer;
            min-height: 280px;
          }}
          .val-card::before {{
            content: '';
            position: absolute;
            top: 0; left: 0; width: 100%; height: 10px;
            background: var(--val-color);
            transition: height 0.4s ease;
          }}
          .val-card-front {{
            transition: all 0.4s ease;
            transform: translateY(0);
          }}
          .val-number {{
            position: absolute;
            top: 20px;
            left: 20px;
            font-size: 8rem;
            font-family: 'Baloo 2', cursive;
            font-weight: 800;
            color: var(--val-light);
            line-height: 1;
            z-index: 0;
            pointer-events: none;
            transition: all 0.4s ease;
          }}
          .val-icon {{
            width: 80px; height: 80px;
            border-radius: 50%;
            background: var(--val-light);
            color: var(--val-color);
            display: inline-flex;
            align-items: center;
            justify-content: center;
            margin-bottom: 1.5rem;
            position: relative;
            z-index: 1;
            transition: transform 0.4s ease;
          }}
          .val-title {{
            font-family: 'Baloo 2', cursive;
            font-size: 1.8rem;
            color: var(--color-charcoal);
            position: relative;
            z-index: 1;
            margin-bottom: 0.5rem;
          }}
          .val-hint {{
            font-size: 0.9rem;
            color: var(--color-text-muted);
            text-transform: uppercase;
            letter-spacing: 2px;
            font-weight: 600;
            opacity: 1;
            transition: opacity 0.3s;
          }}
          
          /* The hidden content */
          .val-card-content {{
            position: absolute;
            bottom: 0; left: 0; width: 100%; height: 100%;
            padding: 3rem 2rem;
            background: var(--val-color);
            color: white;
            display: flex;
            flex-direction: column;
            justify-content: center;
            opacity: 0;
            transform: translateY(100%);
            transition: all 0.5s cubic-bezier(0.34, 1.56, 0.64, 1);
            text-align: left;
            z-index: 10;
          }}
          .val-quote {{
            font-family: 'Georgia', serif;
            font-style: italic;
            font-size: 1.1rem;
            line-height: 1.5;
            margin-bottom: 1.5rem;
            color: rgba(255,255,255,0.95);
            border-left: 3px solid rgba(255,255,255,0.5);
            padding-left: 1rem;
          }}
          .val-desc {{
            font-size: 1rem;
            line-height: 1.6;
            color: rgba(255,255,255,0.9);
            font-weight: 500;
          }}

          /* Hover Effects */
          .val-card:hover {{
            box-shadow: 0 20px 40px rgba(0,0,0,0.12);
            transform: translateY(-10px);
          }}
          .val-card:hover .val-card-front {{
            transform: translateY(-20px);
            opacity: 0;
          }}
          .val-card:hover .val-card-content {{
            opacity: 1;
            transform: translateY(0);
          }}
        </style>

        <div class="val-grid reveal">
            {grid_html}
        </div>
      </div>
    </section>'''

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace existing OUR VALUES section
pattern = re.compile(r'<!-- OUR VALUES -->.*?(?=<!--)', re.DOTALL)
new_content = pattern.sub(section_html + '\n    ', content)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Our Values section updated!")
