import re

bento_html = """
        <div class="section-header reveal">
          <div class="section-header__eyebrow">Who We Are</div>
          <h2 class="section-header__title">Our <span class="doodle-highlight">Values</span></h2>
        </div>
        
        <style>
          .bento-values {
            display: grid;
            grid-template-columns: repeat(4, 1fr);
            grid-auto-rows: 240px;
            gap: 1.5rem;
            margin-top: 4rem;
          }
          .bento-card {
            position: relative;
            border-radius: 32px;
            padding: 2.5rem;
            overflow: hidden;
            display: flex;
            flex-direction: column;
            justify-content: space-between;
            transition: all 0.5s cubic-bezier(0.25, 1, 0.3, 1);
            background: white;
            border: 1px solid rgba(0,0,0,0.04);
            box-shadow: 0 10px 30px rgba(0,0,0,0.03);
            z-index: 1;
            cursor: default;
          }
          .bento-card:hover {
            transform: translateY(-8px) scale(1.02);
            box-shadow: 0 20px 40px rgba(0,0,0,0.08);
          }
          .bento-card::before {
            content: '';
            position: absolute;
            top: 0; left: 0; right: 0; bottom: 0;
            background: var(--v-color);
            opacity: 0.05;
            transition: all 0.5s ease;
            z-index: -2;
          }
          .bento-card:hover::before {
            opacity: 0.15;
          }
          .bento-hindi {
            position: absolute;
            right: -5%;
            bottom: -15%;
            font-family: var(--font-heading);
            font-size: 8rem;
            font-weight: 900;
            color: var(--v-color);
            opacity: 0.06;
            z-index: -1;
            transition: all 0.5s cubic-bezier(0.25, 1, 0.3, 1);
            pointer-events: none;
            white-space: nowrap;
          }
          .bento-card:hover .bento-hindi {
            transform: scale(1.1) rotate(-5deg);
            opacity: 0.12;
            right: 0%;
            bottom: -10%;
          }
          .bento-header {
            display: flex;
            align-items: center;
            gap: 1.25rem;
            margin-bottom: 1.5rem;
          }
          .bento-icon {
            width: 54px;
            height: 54px;
            border-radius: 18px;
            background: var(--v-color);
            color: white;
            display: flex;
            align-items: center;
            justify-content: center;
            box-shadow: 0 8px 20px rgba(0,0,0,0.1);
            transition: transform 0.5s cubic-bezier(0.25, 1, 0.3, 1);
          }
          .bento-card:hover .bento-icon {
            transform: scale(1.1) rotate(10deg);
          }
          .bento-title {
            font-family: var(--font-heading);
            font-size: 1.8rem;
            font-weight: 800;
            color: var(--color-charcoal);
            margin: 0;
            line-height: 1.2;
          }
          .bento-desc {
            font-size: 1.15rem;
            color: var(--color-text-secondary);
            line-height: 1.6;
            margin: 0;
            font-weight: 500;
            max-width: 90%;
          }
          
          /* Bento mapping */
          .bento-card:nth-child(1) { grid-column: span 2; }
          .bento-card:nth-child(2) { grid-column: span 2; }
          .bento-card:nth-child(3) { grid-column: span 1; }
          .bento-card:nth-child(4) { grid-column: span 2; }
          .bento-card:nth-child(5) { grid-column: span 1; }

          @media (max-width: 1024px) {
            .bento-values {
              grid-template-columns: repeat(2, 1fr);
              grid-auto-rows: minmax(220px, auto);
            }
            .bento-card:nth-child(n) { grid-column: span 2; }
            .bento-card:nth-child(3) { grid-column: span 1; }
            .bento-card:nth-child(5) { grid-column: span 1; }
          }
          @media (max-width: 768px) {
            .bento-values {
              grid-template-columns: 1fr;
              grid-auto-rows: auto;
            }
            .bento-card:nth-child(n) { grid-column: span 1; padding: 2rem; }
            .bento-hindi { font-size: 6rem; }
            .bento-desc { max-width: 100%; }
          }
        </style>

        <div class="bento-values reveal" data-stagger>
          <!-- 1. Compassion -->
          <div class="bento-card" style="--v-color: #FF6F59;">
            <div class="bento-hindi">करुणा</div>
            <div class="bento-header">
              <div class="bento-icon">
                <svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><path d="M20.84 4.61a5.5 5.5 0 0 0-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 0 0-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 0 0 0-7.78z"></path></svg>
              </div>
              <h3 class="bento-title">Compassion</h3>
            </div>
            <p class="bento-desc">We recognise difficulty, treat it as universal, and act on it with care.</p>
          </div>
          
          <!-- 2. Trust -->
          <div class="bento-card" style="--v-color: #38B6FF;">
            <div class="bento-hindi">विश्वास</div>
            <div class="bento-header">
              <div class="bento-icon">
                <svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"></path></svg>
              </div>
              <h3 class="bento-title">Trust</h3>
            </div>
            <p class="bento-desc">We are transparent about our processes and treat mistakes as places to learn.</p>
          </div>
          
          <!-- 3. Excellence -->
          <div class="bento-card" style="--v-color: #FFC72C;">
            <div class="bento-hindi" style="right: -15%;">उत्कृष्टता</div>
            <div class="bento-header">
              <div class="bento-icon">
                <svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"></polygon></svg>
              </div>
              <h3 class="bento-title">Excellence</h3>
            </div>
            <p class="bento-desc">We hold a high standard and improve it deliberately, year on year.</p>
          </div>
          
          <!-- 4. Freedom -->
          <div class="bento-card" style="--v-color: #1CA6A0;">
            <div class="bento-hindi">स्वतंत्रता</div>
            <div class="bento-header">
              <div class="bento-icon">
                <svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><path d="M11 20A7 7 0 0 1 9.8 6.1C15.5 5 17 4.48 19 2c1 2 2 4.18 2 8 0 5.5-4.78 10-10 10Z"></path><path d="M2 21c0-3 1.85-5.36 5.08-6C9.5 14.52 12 13 13 12"></path></svg>
              </div>
              <h3 class="bento-title">Freedom</h3>
            </div>
            <p class="bento-desc">Our teams make their own decisions and take full responsibility for what follows.</p>
          </div>
          
          <!-- 5. Innovation -->
          <div class="bento-card" style="--v-color: #9B51E0;">
            <div class="bento-hindi">नवाचार</div>
            <div class="bento-header">
              <div class="bento-icon">
                <svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="7"></circle><line x1="12" y1="19" x2="12" y2="22"></line><line x1="9" y1="22" x2="15" y2="22"></line></svg>
              </div>
              <h3 class="bento-title">Innovation</h3>
            </div>
            <p class="bento-desc">We test, adapt and discard. The model came from reflection, not a plan.</p>
          </div>
        </div>
"""

def update_values():
    with open('index.html', 'r', encoding='utf-8') as f:
        text = f.read()

    # Pattern to match the existing values grid
    # From: <div class="section-header reveal">
    #          <div class="section-header__eyebrow">Who We Are</div>
    # Up to: </div> before </section> <!-- 4 AUDIENCE PATHWAYS -->
    
    pattern = r'<div class="section-header reveal">\s*<div class="section-header__eyebrow">Who We Are</div>[\s\S]*?(?=      </div>\n    </section>\n\n    <!-- ════════════════════════════════════════ -->\n    <!-- 4 AUDIENCE PATHWAYS                      -->)'
    
    new_text = re.sub(pattern, bento_html.strip() + '\n', text)
    
    if new_text != text:
        with open('index.html', 'w', encoding='utf-8') as f:
            f.write(new_text)
        print("Successfully updated Our Values to a Bento Box layout!")
    else:
        print("Could not find the target values block in index.html.")

update_values()
