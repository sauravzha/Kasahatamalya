import re

html_path = r"C:\Users\Saurav\Desktop\Kshamatalaya\index.html"
with open(html_path, 'r', encoding='utf-8') as f:
    content = f.read()

# We will replace the entire style block and the div containing the cards
# Start index of <style> at line 293
start_str = "        <style>\n          .premium-approach-card {"
end_str = "          <!-- 3. Build -->"
# Actually we can just regex replace everything from <style> to the end of the cards div.

new_content = '''        <style>
          .approach-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 2rem;
            margin-top: 3rem;
          }
          .premium-approach-card {
            position: relative;
            background: rgba(255, 255, 255, 0.85);
            backdrop-filter: blur(12px);
            border-radius: 20px;
            padding: 2.5rem 2rem;
            display: flex;
            flex-direction: column;
            gap: 1.5rem;
            box-shadow: 0 10px 30px rgba(0,0,0,0.04), inset 0 0 0 1px rgba(255,255,255,1);
            transition: all 0.4s cubic-bezier(0.16, 1, 0.3, 1);
            overflow: hidden;
            border-top: 5px solid var(--card-color);
            z-index: 1;
          }
          .premium-approach-card:hover {
            transform: translateY(-8px) scale(1.02);
            box-shadow: 0 20px 40px rgba(0,0,0,0.1), inset 0 0 0 2px rgba(255,255,255,1);
            z-index: 2;
          }
          .approach-number {
            font-family: var(--font-heading);
            font-size: 6rem;
            font-weight: 900;
            line-height: 0.8;
            color: var(--card-color);
            opacity: 0.08;
            position: absolute;
            right: 1rem;
            bottom: 1rem;
            z-index: 0;
            transition: all 0.5s ease;
          }
          .premium-approach-card:hover .approach-number {
            opacity: 0.15;
            transform: scale(1.2) translate(-10px, -10px);
          }
          .approach-icon-wrap {
            display: flex;
            align-items: center;
            justify-content: center;
            width: 60px;
            height: 60px;
            border-radius: 16px;
            background: linear-gradient(135deg, var(--card-color) 0%, rgba(255,255,255,0.8) 100%);
            color: white;
            font-size: 1.8rem;
            font-weight: 800;
            box-shadow: 0 10px 20px rgba(0,0,0,0.1);
            z-index: 1;
            transition: transform 0.4s ease;
          }
          .premium-approach-card:hover .approach-icon-wrap {
            transform: rotate(-10deg) scale(1.1);
          }
          .approach-content { position: relative; z-index: 1; flex: 1; }
          .approach-title { font-size: 1.4rem; font-weight: 800; color: var(--color-charcoal); margin-bottom: 0.5rem; line-height: 1.3; }
          .approach-subtitle { font-size: 1rem; font-weight: 700; color: var(--card-color); margin-bottom: 1.25rem; }
          .approach-list { list-style: none; padding: 0; margin: 0; display: flex; flex-direction: column; gap: 0.5rem; }
          .approach-list li {
            position: relative; padding-left: 1.5rem; font-size: 0.95rem; color: var(--color-text-secondary); line-height: 1.5;
          }
          .approach-list li::before {
            content: '✓'; position: absolute; left: 0; top: 0; color: var(--card-color);
            font-weight: 900; font-size: 1rem;
          }
        </style>

        <div class="approach-grid" data-stagger>
          <!-- 1. Demonstrate -->
          <div class="reveal premium-approach-card" style="--card-color: #38B6FF;">
            <div class="approach-number">1</div>
            <div class="approach-icon-wrap" style="background: linear-gradient(135deg, #38B6FF, #0077B6);">1</div>
            <div class="approach-content">
              <h3 class="approach-title">Demonstrate & Support Excellence</h3>
              <p class="approach-subtitle">in Learning, Governance & Well-being</p>
              <p style="font-weight: 700; color: var(--color-charcoal); margin-bottom: 1rem; font-size: 1rem;">100 Schools of Excellence within primary grade government schools</p>
              <ul class="approach-list">
                <li>Increased child retention</li>
                <li>Improved quality in learning & well-being</li>
                <li>Increase in parental engagement in PTMs</li>
                <li>Print-rich & learner centric classrooms</li>
              </ul>
            </div>
          </div>
          <!-- 2. Cultivate -->
          <div class="reveal premium-approach-card" style="--card-color: #1CA6A0;">
            <div class="approach-number">2</div>
            <div class="approach-icon-wrap" style="background: linear-gradient(135deg, #1CA6A0, #0F6E69);">2</div>
            <div class="approach-content">
              <h3 class="approach-title">Cultivating Local Leadership</h3>
              <ul class="approach-list" style="margin-top: 1rem;">
                <li>Cultivating a cadre of local Edu leaders as Community Mentors who support govt. schools builds foundational skills in primary grade students belonging to remote rural geographies</li>
                <li>Cadre of govt. school teachers who are transformed to happy, purposeful & improved pedagogical leadership</li>
                <li>Cadre of Learning Festival Community Leaders supporting students develop creative confidence and enhance their 21st century life skills through access to art, music, theatre, movement, game design and other art related mediums.</li>
              </ul>
            </div>
          </div>
          <!-- 3. Build -->
          <div class="reveal premium-approach-card" style="--card-color: #FFC72C;">
            <div class="approach-number">3</div>
            <div class="approach-icon-wrap" style="background: linear-gradient(135deg, #FFC72C, #F9A825);">3</div>
            <div class="approach-content">
              <h3 class="approach-title">Building Systemic Excellence</h3>
              <p class="approach-subtitle">in Policy & Reforms</p>
              <ul class="approach-list">
                <li>Supporting the state in the mission of NEP 2020's State Curriculum Framework</li>
                <li>Advocating curriculum development & building a cadre of 100 Mentor Teachers for well-being curriculum to build happy schools.</li>
                <li>Partnering with state to support Assessment CELL initiatives & Module Development for Teacher Education</li>
              </ul>
            </div>
          </div>
        </div>'''

# Using regex to replace everything from <style> to </div></div></section>
pattern = re.compile(r'        <style>\s*\.premium-approach-card \{.*?</style>\s*<div style="display: flex; flex-direction: column; gap: 2\.5rem; margin-top: 3rem;" data-stagger>.*?</div>\s*</div>', re.DOTALL)
content = pattern.sub(new_content + '\n      </div>', content)

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(content)
print("Updated approach layout")
