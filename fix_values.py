import re

values_html = '''
    <!-- VALUES -->
    <section class="section doodle-bg" id="values" aria-label="Our Values">
      <!-- Section Doodles -->
      <svg class="section-doodle section-doodle--bob1" style="top: 8%; left: 3%; width: 45px;" viewBox="0 0 45 45" aria-hidden="true">
        <path d="M22.5 5 L27 16 L38 16 L29 23 L33 35 L22.5 28 L12 35 L16 23 L7 16 L18 16 Z" fill="none" stroke="#FFC72C" stroke-width="1.5" stroke-linejoin="round"/>
      </svg>
      <div class="container">
        <div class="section-header reveal">
          <div class="section-header__eyebrow">Who We Are</div>
          <h2 class="section-header__title">Our <span class="doodle-highlight">Values</span></h2>
        </div>
        <style>
          .premium-values-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); gap: 2.5rem; margin-top: 3rem; }
          .premium-value-card { background: rgba(255, 255, 255, 0.6); backdrop-filter: blur(16px); padding: 3rem 2.5rem; border-radius: 30px; box-shadow: 0 10px 30px rgba(0,0,0,0.03); position: relative; overflow: hidden; transition: all 0.5s; display: flex; flex-direction: column; height: 100%; }
          .premium-value-card::before { content: ''; position: absolute; top: 0; left: 0; width: 100%; height: 6px; background: var(--value-color); transition: height 0.4s; }
          .premium-value-card:hover { transform: translateY(-10px); }
          .premium-value-card:hover::before { height: 10px; }
          .value-icon-box { width: 70px; height: 70px; border-radius: 20px; display: flex; align-items: center; justify-content: center; background: white; box-shadow: 0 10px 25px rgba(0,0,0,0.06); margin-bottom: 2rem; color: var(--value-color); font-size: 2rem; font-family: var(--font-heading); font-weight: 900; transition: transform 0.4s; }
          .value-title { font-size: 1.8rem; font-weight: 800; color: var(--color-charcoal); margin-bottom: 1rem; }
          .value-quote { font-style: italic; color: var(--value-color); font-weight: 600; margin-bottom: 1.5rem; font-size: 1.05rem; line-height: 1.5; }
          .value-desc { color: var(--color-text-secondary); font-size: 1.05rem; line-height: 1.6; margin: 0; flex-grow: 1; }
        </style>
        <div class="premium-values-grid" data-stagger>
          <!-- Compassion -->
          <div class="reveal premium-value-card" style="--value-color: #1CA6A0;">
            <div class="value-icon-box">1</div>
            <h3 class="value-title">करुणा Compassion</h3>
            <p class="value-desc">We recognise difficulty, treat it as universal, and act on it with care.</p>
          </div>
          <!-- Trust -->
          <div class="reveal premium-value-card" style="--value-color: #FFC72C;">
            <div class="value-icon-box">2</div>
            <h3 class="value-title">विश्वास Trust</h3>
            <p class="value-desc">We are transparent about our processes and treat mistakes as places to learn.</p>
          </div>
          <!-- Excellence -->
          <div class="reveal premium-value-card" style="--value-color: #FF6F59;">
            <div class="value-icon-box">3</div>
            <h3 class="value-title">उत्कृष्टता Excellence</h3>
            <p class="value-desc">We hold a high standard and improve it deliberately, year on year.</p>
          </div>
          <!-- Freedom with Responsibility -->
          <div class="reveal premium-value-card" style="--value-color: #38B6FF;">
            <div class="value-icon-box">4</div>
            <h3 class="value-title">स्वतंत्रता Freedom with responsibility</h3>
            <p class="value-desc">Our teams make their own decisions and own what follows.</p>
          </div>
          <!-- Innovation -->
          <div class="reveal premium-value-card" style="--value-color: #9B51E0;">
            <div class="value-icon-box">5</div>
            <h3 class="value-title">नवाचार Innovation</h3>
            <p class="value-desc">We test, adapt and discard. The model came from reflection, not a plan.</p>
          </div>
        </div>
      </div>
    </section>
'''

# Update index.html
with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

content = re.sub(r'<!-- ════════════════════════════════════════ -->\s*<!-- VALUES.*?<!-- ════════════════════════════════════════ -->\s*<!-- 4 AUDIENCE PATHWAYS', values_html + '\n    <!-- ════════════════════════════════════════ -->\n    <!-- 4 AUDIENCE PATHWAYS', content, flags=re.DOTALL)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

# Update story.html
with open('story.html', 'r', encoding='utf-8') as f:
    content = f.read()

content = re.sub(r'<!-- OUR VALUES -->.*?(?=<!-- GET INVOLVED CTA -->)', values_html + '\n    ', content, flags=re.DOTALL)

with open('story.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Values successfully updated in both index.html and story.html!")
