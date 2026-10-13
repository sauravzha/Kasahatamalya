import re

html_path = r"C:\Users\Saurav\Desktop\Kshamatalaya\index.html"
with open(html_path, 'r', encoding='utf-8') as f:
    content = f.read()

new_content = '''        <style>
          .approach-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
            gap: 1.5rem;
            margin-top: 2rem;
          }
          .premium-approach-card {
            position: relative;
            background: linear-gradient(145deg, rgba(255, 255, 255, 0.95) 0%, rgba(245, 245, 245, 0.8) 100%);
            backdrop-filter: blur(16px);
            border-radius: 16px;
            padding: 1.5rem;
            display: flex;
            flex-direction: column;
            gap: 1rem;
            box-shadow: 0 4px 15px rgba(0,0,0,0.03), inset 0 0 0 1px rgba(255,255,255,0.8);
            transition: all 0.4s cubic-bezier(0.16, 1, 0.3, 1);
            overflow: hidden;
            border-top: 4px solid var(--card-color);
            z-index: 1;
          }
          .premium-approach-card:hover {
            transform: translateY(-5px);
            box-shadow: 0 15px 30px rgba(0,0,0,0.08), inset 0 0 0 2px var(--card-color);
            background: rgba(255,255,255,1);
            z-index: 2;
          }
          .approach-number {
            font-family: var(--font-heading);
            font-size: 4rem;
            font-weight: 900;
            line-height: 0.8;
            color: var(--card-color);
            opacity: 0.05;
            position: absolute;
            right: -0.5rem;
            bottom: -0.5rem;
            z-index: 0;
            transition: all 0.5s ease;
          }
          .premium-approach-card:hover .approach-number {
            opacity: 0.12;
            transform: scale(1.1) translate(-5px, -5px);
          }
          .approach-header {
            display: flex;
            align-items: center;
            gap: 1rem;
            position: relative;
            z-index: 1;
          }
          .approach-icon-wrap {
            display: flex;
            align-items: center;
            justify-content: center;
            width: 48px;
            height: 48px;
            flex-shrink: 0;
            border-radius: 12px;
            background: linear-gradient(135deg, var(--card-color) 0%, rgba(255,255,255,0.5) 100%);
            color: white;
            font-size: 1.5rem;
            font-weight: 800;
            box-shadow: 0 5px 15px rgba(0,0,0,0.1);
            z-index: 1;
            transition: transform 0.4s cubic-bezier(0.34, 1.56, 0.64, 1);
          }
          .premium-approach-card:hover .approach-icon-wrap {
            transform: rotate(-10deg) scale(1.05);
          }
          .approach-title { font-size: 1.15rem; font-weight: 800; color: var(--color-charcoal); line-height: 1.2; margin: 0; }
          .approach-subtitle { font-size: 0.85rem; font-weight: 700; color: var(--card-color); margin-top: 0.25rem; }
          .approach-content { position: relative; z-index: 1; flex: 1; display: flex; flex-direction: column; }
          .approach-list { list-style: none; padding: 0; margin: 0; display: flex; flex-direction: column; gap: 0.4rem; }
          .approach-list li {
            position: relative; padding-left: 1.2rem; font-size: 0.85rem; color: var(--color-text-secondary); line-height: 1.4;
          }
          .approach-list li::before {
            content: '✓'; position: absolute; left: 0; top: 0; color: var(--card-color);
            font-weight: 900; font-size: 0.9rem;
          }
        </style>

        <div class="approach-grid" data-stagger>
          <!-- 1. Demonstrate -->
          <div class="reveal premium-approach-card" style="--card-color: #38B6FF;">
            <div class="approach-number">1</div>
            <div class="approach-header">
              <div class="approach-icon-wrap" style="background: linear-gradient(135deg, #38B6FF, #0077B6);">1</div>
              <div>
                <h3 class="approach-title">Demonstrate & Support Excellence</h3>
                <p class="approach-subtitle">in Learning, Governance & Well-being</p>
              </div>
            </div>
            <div class="approach-content">
              <p style="font-weight: 700; color: var(--color-charcoal); margin-bottom: 0.75rem; font-size: 0.9rem; line-height: 1.3;">100 Schools of Excellence within primary grade government schools</p>
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
            <div class="approach-header">
              <div class="approach-icon-wrap" style="background: linear-gradient(135deg, #1CA6A0, #0F6E69);">2</div>
              <div>
                <h3 class="approach-title">Cultivating Local Leadership</h3>
              </div>
            </div>
            <div class="approach-content">
              <ul class="approach-list">
                <li>Cultivating a cadre of local Edu leaders as Community Mentors who support govt. schools builds foundational skills in primary grade students belonging to remote rural geographies</li>
                <li>Cadre of govt. school teachers who are transformed to happy, purposeful & improved pedagogical leadership</li>
                <li>Cadre of Learning Festival Community Leaders supporting students develop creative confidence and enhance their 21st century life skills through access to art, music, theatre, movement, game design and other art related mediums.</li>
              </ul>
            </div>
          </div>
          <!-- 3. Build -->
          <div class="reveal premium-approach-card" style="--card-color: #FFC72C;">
            <div class="approach-number">3</div>
            <div class="approach-header">
              <div class="approach-icon-wrap" style="background: linear-gradient(135deg, #FFC72C, #F9A825);">3</div>
              <div>
                <h3 class="approach-title">Building Systemic Excellence</h3>
                <p class="approach-subtitle">in Policy & Reforms</p>
              </div>
            </div>
            <div class="approach-content">
              <ul class="approach-list">
                <li>Supporting the state in the mission of NEP 2020's State Curriculum Framework</li>
                <li>Advocating curriculum development & building a cadre of 100 Mentor Teachers for well-being curriculum to build happy schools.</li>
                <li>Partnering with state to support Assessment CELL initiatives & Module Development for Teacher Education</li>
              </ul>
            </div>
          </div>
        </div>'''

pattern = re.compile(r'        <style>\s*\.approach-grid \{.*?</style>\s*<div class="approach-grid" data-stagger>.*?</div>', re.DOTALL)
if pattern.search(content):
    content = pattern.sub(new_content, content)
    with open(html_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print("Updated approach layout to be smaller and more dynamic")
else:
    print("Could not find the approach grid block")
