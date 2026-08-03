import re

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

new_html = """
    <!-- ACHIEVEMENTS & IMPACT 2025 -->
    <section class="section" id="achievements-2025" aria-label="Achievements 2025" style="background-color: #FFFFFF; padding: 6rem 0;">
      <div class="container" style="max-width: 1280px; margin: 0 auto; padding: 0 1.5rem;">
        
        <div class="section-header reveal" style="text-align: center; margin-bottom: 3.5rem;">
          <h2 style="font-family: var(--font-heading); font-size: clamp(2rem, 4vw, 3rem); font-weight: 800; color: var(--color-charcoal); margin-bottom: 1rem;">
            ANNUAL REPORT 2025–26<br>
            <span class="doodle-highlight" style="color: var(--color-teal);">Achievements & Impact in 2025–26</span>
          </h2>
          <p style="max-width: 800px; margin: 0 auto; font-size: 1.25rem; color: var(--color-text-secondary); line-height: 1.6;">
            A year of scaling impact across 3 states — reaching thousands of children, empowering teachers, and strengthening communities.
          </p>
        </div>

        <style>
          .achieve-toggle-wrapper {
            display: flex;
            justify-content: center;
            margin-bottom: 4rem;
          }
          .achieve-toggle {
            display: inline-flex;
            background: #F1F5F9;
            border-radius: 50px;
            padding: 6px;
            box-shadow: inset 0 2px 5px rgba(0,0,0,0.05);
            position: relative;
          }
          .achieve-toggle-btn {
            background: transparent;
            border: none;
            padding: 12px 30px;
            font-size: 1.1rem;
            font-weight: 700;
            color: #64748B;
            cursor: pointer;
            border-radius: 40px;
            position: relative;
            z-index: 2;
            transition: color 0.3s ease;
          }
          .achieve-toggle-btn.active {
            color: #FFFFFF;
          }
          .achieve-toggle-pill {
            position: absolute;
            top: 6px;
            bottom: 6px;
            left: 6px;
            width: 50%; /* JS will update this */
            background: var(--color-teal);
            border-radius: 40px;
            z-index: 1;
            transition: all 0.4s cubic-bezier(0.34, 1.56, 0.64, 1);
            box-shadow: 0 4px 15px rgba(8, 185, 219, 0.4);
          }

          .achieve-panel {
            display: none;
            opacity: 0;
            transform: translateY(20px);
            transition: all 0.5s ease;
          }
          .achieve-panel.active {
            display: block;
            opacity: 1;
            transform: translateY(0);
          }

          /* STATE CARDS */
          .state-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 2rem;
          }
          .state-card {
            background: #FFFFFF;
            border-radius: 24px;
            border: 1px solid #E2E8F0;
            padding: 3rem 2.5rem;
            text-align: center;
            box-shadow: 0 10px 30px rgba(0,0,0,0.04);
            transition: all 0.4s cubic-bezier(0.2, 1, 0.3, 1);
            position: relative;
            overflow: hidden;
            z-index: 1;
          }
          .state-card::before {
            content: '';
            position: absolute;
            top: 0; left: 0; width: 100%; height: 6px;
            background: var(--card-color, var(--color-teal));
            z-index: 2;
          }
          .state-card:hover {
            transform: translateY(-10px);
            box-shadow: 0 20px 40px rgba(0,0,0,0.08);
            border-color: #CBD5E1;
          }
          .state-icon-wrapper {
            width: 80px;
            height: 80px;
            background: var(--card-bg, #F0FDF4);
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            margin: 0 auto 2rem;
            transition: transform 0.4s ease;
          }
          .state-card:hover .state-icon-wrapper {
            transform: scale(1.1) rotate(5deg);
          }
          .state-icon-wrapper svg {
            width: 40px;
            height: 40px;
            color: var(--card-color, var(--color-teal));
          }
          .state-title {
            font-family: var(--font-heading);
            font-size: 2.2rem;
            font-weight: 800;
            color: var(--color-charcoal);
            margin-bottom: 2rem;
          }
          .state-stat-grid {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 1.5rem;
            text-align: left;
          }
          .state-stat {
            display: flex;
            flex-direction: column;
            gap: 0.5rem;
          }
          .state-stat svg {
            width: 20px;
            height: 20px;
            color: var(--card-color, var(--color-teal));
          }
          .state-stat-val {
            font-size: 1.5rem;
            font-weight: 800;
            color: var(--color-charcoal);
          }
          .state-stat-label {
            font-size: 0.9rem;
            color: var(--color-text-secondary);
            font-weight: 600;
            text-transform: uppercase;
            letter-spacing: 0.5px;
          }

          /* PROGRAMS BENTO GRID */
          .bento-grid {
            display: grid;
            grid-template-columns: repeat(12, 1fr);
            gap: 1.5rem;
            grid-auto-rows: minmax(180px, auto);
          }
          .bento-item {
            background: #FFFFFF;
            border-radius: 20px;
            border: 1px solid #E2E8F0;
            padding: 2rem;
            box-shadow: 0 5px 15px rgba(0,0,0,0.02);
            transition: all 0.3s ease;
            display: flex;
            flex-direction: column;
            position: relative;
            overflow: hidden;
          }
          .bento-item:hover {
            box-shadow: 0 15px 30px rgba(0,0,0,0.06);
            transform: translateY(-5px);
          }
          .bento-item::before {
            content: '';
            position: absolute;
            top: 0; left: 0; bottom: 0; width: 4px;
            background: var(--bento-color, var(--color-teal));
          }
          
          /* Spans */
          .bento-col-4 { grid-column: span 4; }
          .bento-col-6 { grid-column: span 6; }
          .bento-col-8 { grid-column: span 8; }
          .bento-col-12 { grid-column: span 12; }
          
          @media (max-width: 1024px) {
            .bento-col-4, .bento-col-8 { grid-column: span 6; }
          }
          @media (max-width: 768px) {
            .bento-col-4, .bento-col-6, .bento-col-8 { grid-column: span 12; }
          }

          .bento-header {
            display: flex;
            justify-content: space-between;
            align-items: flex-start;
            margin-bottom: 1rem;
          }
          .bento-badge {
            background: var(--bento-bg, #F1F5F9);
            color: var(--bento-color, #64748B);
            font-size: 0.75rem;
            font-weight: 800;
            padding: 4px 12px;
            border-radius: 20px;
            text-transform: uppercase;
            letter-spacing: 1px;
          }
          .bento-title {
            font-family: var(--font-heading);
            font-size: 1.4rem;
            font-weight: 800;
            color: var(--color-charcoal);
            margin-bottom: 0.75rem;
            line-height: 1.3;
          }
          .bento-desc {
            font-size: 1rem;
            color: var(--color-text-secondary);
            line-height: 1.5;
            margin-bottom: 1.5rem;
            flex-grow: 1;
          }
          .bento-stats {
            display: flex;
            flex-wrap: wrap;
            gap: 1rem;
            margin-top: auto;
            padding-top: 1.5rem;
            border-top: 1px dashed #E2E8F0;
          }
          .bento-stat {
            display: flex;
            align-items: center;
            gap: 0.5rem;
            font-size: 0.95rem;
            color: var(--color-charcoal);
            font-weight: 600;
          }
          .bento-stat svg {
            width: 16px;
            height: 16px;
            color: var(--bento-color, var(--color-teal));
          }

          /* SVG Icons */
          .icon-school { stroke-width: 2; stroke: currentColor; fill: none; stroke-linecap: round; stroke-linejoin: round; }
          .icon-user { stroke-width: 2; stroke: currentColor; fill: none; stroke-linecap: round; stroke-linejoin: round; }
          .icon-users { stroke-width: 2; stroke: currentColor; fill: none; stroke-linecap: round; stroke-linejoin: round; }
          .icon-map { stroke-width: 2; stroke: currentColor; fill: none; stroke-linecap: round; stroke-linejoin: round; }
          .icon-star { stroke-width: 2; stroke: currentColor; fill: none; stroke-linecap: round; stroke-linejoin: round; }
        </style>

        <div class="achieve-toggle-wrapper reveal">
          <div class="achieve-toggle" id="achieveToggle">
            <div class="achieve-toggle-pill" id="achievePill"></div>
            <button class="achieve-toggle-btn active" data-target="panelState" onclick="switchAchieveTab('panelState', this)">Impact by State</button>
            <button class="achieve-toggle-btn" data-target="panelProgram" onclick="switchAchieveTab('panelProgram', this)">Programs in 2025-26</button>
          </div>
        </div>

        <!-- PANEL: BY STATE -->
        <div id="panelState" class="achieve-panel active">
          <div class="state-grid">
            
            <!-- RAJASTHAN -->
            <div class="state-card reveal" style="--card-color: #9B51E0; --card-bg: #F5EEFC;">
              <div class="state-icon-wrapper">
                <svg viewBox="0 0 24 24" class="icon-map"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"></path><circle cx="12" cy="10" r="3"></circle></svg>
              </div>
              <h3 class="state-title">Rajasthan</h3>
              <div class="state-stat-grid">
                <div class="state-stat">
                  <div style="display:flex; align-items:center; gap:8px;">
                    <svg viewBox="0 0 24 24" class="icon-school"><path d="M3 9l9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"></path><polyline points="9 22 9 12 15 12 15 22"></polyline></svg>
                    <span class="state-stat-val">60</span>
                  </div>
                  <span class="state-stat-label">Schools</span>
                </div>
                <div class="state-stat">
                  <div style="display:flex; align-items:center; gap:8px;">
                    <svg viewBox="0 0 24 24" class="icon-users"><path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"></path><circle cx="9" cy="7" r="4"></circle><path d="M23 21v-2a4 4 0 0 0-3-3.87"></path><path d="M16 3.13a4 4 0 0 1 0 7.75"></path></svg>
                    <span class="state-stat-val">35</span>
                  </div>
                  <span class="state-stat-label">Fellows</span>
                </div>
                <div class="state-stat">
                  <div style="display:flex; align-items:center; gap:8px;">
                    <svg viewBox="0 0 24 24" class="icon-user"><path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"></path><circle cx="12" cy="7" r="4"></circle></svg>
                    <span class="state-stat-val">1,644</span>
                  </div>
                  <span class="state-stat-label">Direct Children</span>
                </div>
                <div class="state-stat">
                  <div style="display:flex; align-items:center; gap:8px;">
                    <svg viewBox="0 0 24 24" class="icon-map"><polygon points="1 6 1 22 8 18 16 22 23 18 23 2 16 6 8 2 1 6"></polygon><line x1="8" y1="2" x2="8" y2="18"></line><line x1="16" y1="6" x2="16" y2="22"></line></svg>
                    <span class="state-stat-val">3</span>
                  </div>
                  <span class="state-stat-label">Blocks</span>
                </div>
              </div>
            </div>

            <!-- BIHAR -->
            <div class="state-card reveal" style="--card-color: #1CA6A0; --card-bg: #E8F8F7;">
              <div class="state-icon-wrapper">
                <svg viewBox="0 0 24 24" class="icon-map"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"></path><circle cx="12" cy="10" r="3"></circle></svg>
              </div>
              <h3 class="state-title">Bihar</h3>
              <div class="state-stat-grid">
                <div class="state-stat">
                  <div style="display:flex; align-items:center; gap:8px;">
                    <svg viewBox="0 0 24 24" class="icon-school"><path d="M3 9l9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"></path><polyline points="9 22 9 12 15 12 15 22"></polyline></svg>
                    <span class="state-stat-val">70</span>
                  </div>
                  <span class="state-stat-label">Schools</span>
                </div>
                <div class="state-stat">
                  <div style="display:flex; align-items:center; gap:8px;">
                    <svg viewBox="0 0 24 24" class="icon-user"><path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"></path><circle cx="12" cy="7" r="4"></circle></svg>
                    <span class="state-stat-val">7,418</span>
                  </div>
                  <span class="state-stat-label">Direct Children</span>
                </div>
                <div class="state-stat">
                  <div style="display:flex; align-items:center; gap:8px;">
                    <svg viewBox="0 0 24 24" class="icon-users"><path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"></path><circle cx="9" cy="7" r="4"></circle><path d="M23 21v-2a4 4 0 0 0-3-3.87"></path><path d="M16 3.13a4 4 0 0 1 0 7.75"></path></svg>
                    <span class="state-stat-val">210+</span>
                  </div>
                  <span class="state-stat-label">Teachers</span>
                </div>
                <div class="state-stat">
                  <div style="display:flex; align-items:center; gap:8px;">
                    <svg viewBox="0 0 24 24" class="icon-star"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"></polygon></svg>
                    <span class="state-stat-val">175+</span>
                  </div>
                  <span class="state-stat-label">Volunteers</span>
                </div>
              </div>
            </div>

            <!-- DELHI -->
            <div class="state-card reveal" style="--card-color: #FF6F59; --card-bg: #FFF0EE;">
              <div class="state-icon-wrapper">
                <svg viewBox="0 0 24 24" class="icon-map"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"></path><circle cx="12" cy="10" r="3"></circle></svg>
              </div>
              <h3 class="state-title">Delhi</h3>
              <div class="state-stat-grid">
                <div class="state-stat">
                  <div style="display:flex; align-items:center; gap:8px;">
                    <svg viewBox="0 0 24 24" class="icon-school"><path d="M3 9l9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"></path><polyline points="9 22 9 12 15 12 15 22"></polyline></svg>
                    <span class="state-stat-val">25</span>
                  </div>
                  <span class="state-stat-label">Schools</span>
                </div>
                <div class="state-stat">
                  <div style="display:flex; align-items:center; gap:8px;">
                    <svg viewBox="0 0 24 24" class="icon-users"><path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"></path><circle cx="9" cy="7" r="4"></circle><path d="M23 21v-2a4 4 0 0 0-3-3.87"></path><path d="M16 3.13a4 4 0 0 1 0 7.75"></path></svg>
                    <span class="state-stat-val">1,272</span>
                  </div>
                  <span class="state-stat-label">Champion Teachers</span>
                </div>
                <div class="state-stat">
                  <div style="display:flex; align-items:center; gap:8px;">
                    <svg viewBox="0 0 24 24" class="icon-user"><path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"></path><circle cx="12" cy="7" r="4"></circle></svg>
                    <span class="state-stat-val">4,053</span>
                  </div>
                  <span class="state-stat-label">Direct Students</span>
                </div>
                <div class="state-stat">
                  <div style="display:flex; align-items:center; gap:8px;">
                    <svg viewBox="0 0 24 24" class="icon-star"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"></polygon></svg>
                    <span class="state-stat-val">234</span>
                  </div>
                  <span class="state-stat-label">Star Parents</span>
                </div>
              </div>
            </div>

          </div>
        </div>

        <!-- PANEL: BY PROGRAM -->
        <div id="panelProgram" class="achieve-panel">
          <div class="bento-grid">
            
            <!-- 1. iDiscover Raj -->
            <div class="bento-item bento-col-6 reveal" style="--bento-color: #08B9DB; --bento-bg: #E6F8FC;">
              <div class="bento-header">
                <h4 class="bento-title">iDiscover</h4>
                <span class="bento-badge">Rajasthan</span>
              </div>
              <p class="bento-desc">Establishing Centres of Excellence in schools demonstrating the Whole School Transformation model, with active support of local community leadership.</p>
              <div class="bento-stats">
                <div class="bento-stat"><svg viewBox="0 0 24 24" class="icon-school"><path d="M3 9l9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"></path></svg> 50 Schools</div>
                <div class="bento-stat"><svg viewBox="0 0 24 24" class="icon-users"><path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"></path><circle cx="9" cy="7" r="4"></circle></svg> 25 Fellows</div>
                <div class="bento-stat"><svg viewBox="0 0 24 24" class="icon-user"><path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"></path><circle cx="12" cy="7" r="4"></circle></svg> 1,402 Children</div>
              </div>
            </div>

            <!-- 3. iDiscover Bihar -->
            <div class="bento-item bento-col-6 reveal" style="--bento-color: #1CA6A0; --bento-bg: #E8F8F7;">
              <div class="bento-header">
                <h4 class="bento-title">iDiscover</h4>
                <span class="bento-badge">Bihar</span>
              </div>
              <p class="bento-desc">Establishing Centres of Excellence in schools demonstrating the Whole School Transformation model, with active support of local community leadership.</p>
              <div class="bento-stats">
                <div class="bento-stat"><svg viewBox="0 0 24 24" class="icon-school"><path d="M3 9l9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"></path></svg> 30 Schools</div>
                <div class="bento-stat"><svg viewBox="0 0 24 24" class="icon-user"><path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"></path><circle cx="12" cy="7" r="4"></circle></svg> 1,050+ Children</div>
                <div class="bento-stat"><svg viewBox="0 0 24 24" class="icon-users"><path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"></path><circle cx="9" cy="7" r="4"></circle></svg> 90+ Teachers</div>
              </div>
            </div>

            <!-- 5. Teacher Support Program - Delhi -->
            <div class="bento-item bento-col-8 reveal" style="--bento-color: #FF6F59; --bento-bg: #FFF0EE;">
              <div class="bento-header">
                <h4 class="bento-title">Teacher Support Program</h4>
                <span class="bento-badge">Delhi</span>
              </div>
              <p class="bento-desc">Building a cohort of compassionate and pedagogically strong teachers who create high-impact classrooms for 4000+ children across 15 government schools.</p>
              <div class="bento-stats">
                <div class="bento-stat"><svg viewBox="0 0 24 24" class="icon-school"><path d="M3 9l9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"></path></svg> 15 Schools</div>
                <div class="bento-stat"><svg viewBox="0 0 24 24" class="icon-users"><path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"></path><circle cx="9" cy="7" r="4"></circle></svg> 100 Champion Teachers</div>
                <div class="bento-stat"><svg viewBox="0 0 24 24" class="icon-user"><path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"></path><circle cx="12" cy="7" r="4"></circle></svg> 4,053 Direct Students</div>
              </div>
            </div>
            
            <!-- 2. Fale Fale Shiksha Muhim - Raj -->
            <div class="bento-item bento-col-4 reveal" style="--bento-color: #9B51E0; --bento-bg: #F5EEFC;">
              <div class="bento-header">
                <h4 class="bento-title">Fale Fale Shiksha</h4>
                <span class="bento-badge">Rajasthan</span>
              </div>
              <p class="bento-desc">Supporting early childhood through Secondary children with Foundational Literacy and Numeracy.</p>
              <div class="bento-stats">
                <div class="bento-stat"><svg viewBox="0 0 24 24" class="icon-school"><path d="M3 9l9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"></path></svg> 10 Schools</div>
                <div class="bento-stat"><svg viewBox="0 0 24 24" class="icon-users"><path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"></path><circle cx="9" cy="7" r="4"></circle></svg> 10 Fellows</div>
              </div>
            </div>

            <!-- 4. Learning Festival Community Leadership -->
            <div class="bento-item bento-col-4 reveal" style="--bento-color: #4FB6E8; --bento-bg: #E6F8FC;">
              <div class="bento-header">
                <h4 class="bento-title">Learning Festival</h4>
                <span class="bento-badge">Bihar</span>
              </div>
              <p class="bento-desc">Bringing out innovation, creativity, and community participation with the spirit of learning.</p>
              <div class="bento-stats">
                <div class="bento-stat"><svg viewBox="0 0 24 24" class="icon-user"><path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"></path><circle cx="12" cy="7" r="4"></circle></svg> 6,368+ Children</div>
                <div class="bento-stat"><svg viewBox="0 0 24 24" class="icon-school"><path d="M3 9l9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"></path></svg> 40 Schools</div>
              </div>
            </div>

            <!-- 6. Star Parent Program - Delhi -->
            <div class="bento-item bento-col-4 reveal" style="--bento-color: #38B6FF; --bento-bg: #EBF8FF;">
              <div class="bento-header">
                <h4 class="bento-title">Star Parent</h4>
                <span class="bento-badge">Delhi</span>
              </div>
              <p class="bento-desc">Building active parents who bridge the gap of School and Community for stronger outcomes.</p>
              <div class="bento-stats">
                <div class="bento-stat"><svg viewBox="0 0 24 24" class="icon-star"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"></polygon></svg> 234 Star Parents</div>
              </div>
            </div>

            <!-- 7. Hausla - Delhi -->
            <div class="bento-item bento-col-4 reveal" style="--bento-color: #C06C84; --bento-bg: #FCF0F3;">
              <div class="bento-header">
                <h4 class="bento-title">Hausla</h4>
                <span class="bento-badge">Delhi</span>
              </div>
              <p class="bento-desc">Focusing on teachers' well-being that supports creating compassionate classrooms.</p>
              <div class="bento-stats">
                <div class="bento-stat"><svg viewBox="0 0 24 24" class="icon-users"><path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"></path><circle cx="9" cy="7" r="4"></circle></svg> 1,172 Teachers</div>
              </div>
            </div>

          </div>
        </div>

      </div>

      <script>
        function switchAchieveTab(panelId, btn) {
          document.querySelectorAll('.achieve-panel').forEach(p => p.classList.remove('active'));
          document.querySelectorAll('.achieve-toggle-btn').forEach(b => b.classList.remove('active'));
          
          document.getElementById(panelId).classList.add('active');
          btn.classList.add('active');
          
          const pill = document.getElementById('achievePill');
          if (panelId === 'panelProgram') {
            pill.style.left = '50%';
            pill.style.width = '50%';
          } else {
            pill.style.left = '6px';
            pill.style.width = 'calc(50% - 6px)'; // rough approx depending on padding
          }
          
          // Re-trigger reveal animations in the active panel
          const newReveals = document.getElementById(panelId).querySelectorAll('.reveal');
          newReveals.forEach(r => {
             r.classList.remove('active');
             setTimeout(() => r.classList.add('active'), 50);
          });
        }
        
        // Setup initial pill width
        document.addEventListener('DOMContentLoaded', () => {
           const btn = document.querySelector('.achieve-toggle-btn.active');
           if(btn) {
              const pill = document.getElementById('achievePill');
              if(pill) pill.style.width = btn.offsetWidth + 'px';
           }
        });
      </script>
    </section>
"""

pattern = r'(<section[^>]*id="achievements-2025"[^>]*>[\s\S]*?</section>)'
new_text = re.sub(pattern, new_html, text, flags=re.IGNORECASE)

if new_text != text:
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(new_text)
    print("Successfully replaced achievements section with new BENTO UI!")
else:
    print("Could not find the achievements section in index.html using regex.")
