import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace Geographical Reach section with compact right-side card deck
new_reach_section = '''    <!-- ════════════════════════════════════════ -->
    <!-- GEOGRAPHICAL REACH 3D MAP                -->
    <!-- ════════════════════════════════════════ -->
    <section class="section" id="impact-map" aria-label="Our Geographical Reach" style="overflow: hidden; background: linear-gradient(135deg, #08B9DB 0%, #0194B1 100%); padding: 5rem 0;">
      <!-- Background Doodles -->
      <svg class="section-doodle section-doodle--bob1" style="top: 10%; left: 5%; width: 40px; opacity: 0.3;" viewBox="0 0 40 40" aria-hidden="true">
        <circle cx="20" cy="20" r="16" fill="none" stroke="white" stroke-width="2" stroke-dasharray="4 4"/>
      </svg>
      <div class="container text-center" style="max-width: 1240px; margin: 0 auto; padding: 0 1.5rem;">
        <div class="section-header reveal" style="margin-bottom: 2rem;">
          <div class="section-header__eyebrow" style="background: rgba(255,255,255,0.2); color: #fff;">Geographical Reach</div>
          <h2 class="section-header__title" style="color: #fff;">Impact <span class="doodle-highlight" style="color: var(--color-sunshine);">Across India<svg class="doodle-highlight__squiggle" viewBox="0 0 200 16" preserveAspectRatio="none" aria-hidden="true"><path d="M0 8 Q 25 2, 50 8 T 100 8 T 150 8 T 200 8" fill="none" stroke="rgba(255,255,255,0.4)" stroke-width="4" stroke-linecap="round" class="doodle-squiggle-draw" opacity="0.8"/></svg></span></h2>
          <p class="section-header__desc" style="color: rgba(255,255,255,0.9); margin-bottom: 0;">Hover over the markers to explore our active programs and regional scale.</p>
        </div>
        
        <style>
          .impact-layout {
            display: flex; gap: 2.5rem; align-items: center; justify-content: center; margin-top: 2rem; flex-wrap: wrap; text-align: left;
          }
          .impact-map-col {
            flex: 1; min-width: 320px; max-width: 580px; position: relative;
          }
          .impact-data-col {
            flex: 0 0 380px; max-width: 380px; display: flex; flex-direction: column; gap: 1rem;
          }
          
          /* Pulsing map dots */
          .map-dot {
            position: absolute; width: 18px; height: 18px; border-radius: 50%; background: var(--state-color);
            border: 3px solid white; box-shadow: 0 0 0 0 rgba(255,255,255, 0.7);
            animation: pulse-dot 2s infinite cubic-bezier(0.66, 0, 0, 1); cursor: pointer; transition: transform 0.3s ease;
          }
          .map-dot:hover { transform: scale(1.3); }
          @keyframes pulse-dot {
            to { box-shadow: 0 0 0 18px rgba(255,255,255, 0); }
          }
          
          @media (max-width: 900px) {
            .impact-data-col { flex: 1 1 100%; max-width: 100%; }
          }
        </style>

        <div class="impact-layout">
          <!-- Left: Map -->
          <div class="impact-map-col reveal">
            <div class="map-3d-container" style="margin: 0 auto; width: 100%; height: 440px; position: relative;">
              <div class="map-3d" style="animation: float 6s ease-in-out infinite; width: 100%; height: 100%;">
                <!-- Accurate India Map SVG -->
                <img src="/assets/india-map.svg" alt="Map of India" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; object-fit: contain; filter: drop-shadow(0 20px 30px rgba(0,0,0,0.15));" />
                
                <!-- Pins -->
                <!-- Rajasthan -->
                <div class="map-dot" style="top: 40%; left: 22%; --state-color: #1CA6A0;" title="Rajasthan" onclick="switchStateDeck('rj')"></div>
                <!-- Delhi -->
                <div class="map-dot" style="top: 30%; left: 30%; --state-color: #38B6FF;" title="Delhi" onclick="switchStateDeck('dl')"></div>
                <!-- Bihar -->
                <div class="map-dot" style="top: 40%; left: 56%; --state-color: #FFC72C;" title="Bihar" onclick="switchStateDeck('br')"></div>
              </div>
            </div>
          </div>

          <!-- Right: Interactive Compact Card Deck -->
          <div class="impact-data-col reveal">
            <!-- Deck Tabs -->
            <div class="deck-tabs" style="display: flex; gap: 0.35rem; background: rgba(255,255,255,0.18); padding: 4px; border-radius: 100px; backdrop-filter: blur(10px); width: fit-content; margin-bottom: 0.25rem; border: 1px solid rgba(255,255,255,0.3);">
              <button class="deck-tab active" onclick="switchStateDeck('rj')" id="tab-rj" style="padding: 6px 16px; border-radius: 100px; font-family: var(--font-heading); font-weight: 800; font-size: 0.85rem; border: none; cursor: pointer; transition: all 0.3s ease; background: #1CA6A0; color: white; box-shadow: 0 4px 12px rgba(28,166,160,0.4);">Rajasthan</button>
              <button class="deck-tab" onclick="switchStateDeck('dl')" id="tab-dl" style="padding: 6px 16px; border-radius: 100px; font-family: var(--font-heading); font-weight: 800; font-size: 0.85rem; border: none; cursor: pointer; transition: all 0.3s ease; background: transparent; color: white;">Delhi</button>
              <button class="deck-tab" onclick="switchStateDeck('br')" id="tab-br" style="padding: 6px 16px; border-radius: 100px; font-family: var(--font-heading); font-weight: 800; font-size: 0.85rem; border: none; cursor: pointer; transition: all 0.3s ease; background: transparent; color: white;">Bihar</button>
            </div>

            <!-- Stacked Cards Container -->
            <div class="deck-container" style="position: relative; width: 100%; min-height: 310px;">
              
              <!-- Card 1: Rajasthan -->
              <div class="deck-card active-card" id="deck-card-rj" onclick="switchStateDeck('rj')" style="position: absolute; top: 0; left: 0; width: 100%; background: #ffffff; border-radius: 20px; padding: 1.5rem; box-shadow: 0 16px 40px rgba(0,0,0,0.15); border-top: 5px solid #1CA6A0; transition: all 0.5s cubic-bezier(0.34, 1.56, 0.64, 1); z-index: 3; opacity: 1; transform: translateY(0) scale(1); cursor: pointer;">
                <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 1rem;">
                  <div>
                    <span style="font-size: 0.7rem; font-weight: 800; text-transform: uppercase; letter-spacing: 1.2px; color: #1CA6A0; display: block; margin-bottom: 0.15rem;">ESTABLISHED 2016</span>
                    <h3 style="font-family: var(--font-heading); font-size: 1.65rem; font-weight: 800; color: var(--color-charcoal); margin: 0; line-height: 1.1;">Rajasthan</h3>
                  </div>
                  <span style="background: rgba(28,166,160,0.1); color: #1CA6A0; font-weight: 800; font-size: 0.75rem; padding: 4px 10px; border-radius: 100px;">2016 – Present</span>
                </div>

                <div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 0.6rem; margin-bottom: 1rem;">
                  <div style="background: #F4FBFB; border-radius: 12px; padding: 0.6rem 0.4rem; text-align: center; border: 1px solid rgba(28,166,160,0.15);">
                    <div style="font-family: var(--font-heading); font-size: 1.6rem; font-weight: 800; color: #1CA6A0; line-height: 1;">2</div>
                    <div style="font-size: 0.7rem; font-weight: 700; color: var(--color-text-muted); text-transform: uppercase; margin-top: 0.2rem;">Districts</div>
                  </div>
                  <div style="background: #F4FBFB; border-radius: 12px; padding: 0.6rem 0.4rem; text-align: center; border: 1px solid rgba(28,166,160,0.15);">
                    <div style="font-family: var(--font-heading); font-size: 1.6rem; font-weight: 800; color: #1CA6A0; line-height: 1;">3</div>
                    <div style="font-size: 0.7rem; font-weight: 700; color: var(--color-text-muted); text-transform: uppercase; margin-top: 0.2rem;">Blocks</div>
                  </div>
                  <div style="background: #F4FBFB; border-radius: 12px; padding: 0.6rem 0.4rem; text-align: center; border: 1px solid rgba(28,166,160,0.15);">
                    <div style="font-family: var(--font-heading); font-size: 1.6rem; font-weight: 800; color: #1CA6A0; line-height: 1;">60</div>
                    <div style="font-size: 0.7rem; font-weight: 700; color: var(--color-text-muted); text-transform: uppercase; margin-top: 0.2rem;">Schools</div>
                  </div>
                </div>

                <p style="font-size: 0.85rem; color: #555; line-height: 1.5; margin: 0;">Empowering rural & tribal government schools with community-led learning innovations.</p>
              </div>

              <!-- Card 2: Delhi -->
              <div class="deck-card" id="deck-card-dl" onclick="switchStateDeck('dl')" style="position: absolute; top: 0; left: 0; width: 100%; background: #ffffff; border-radius: 20px; padding: 1.5rem; box-shadow: 0 10px 30px rgba(0,0,0,0.08); border-top: 5px solid #38B6FF; transition: all 0.5s cubic-bezier(0.34, 1.56, 0.64, 1); z-index: 2; opacity: 0.75; transform: translateY(12px) scale(0.96); cursor: pointer;">
                <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 1rem;">
                  <div>
                    <span style="font-size: 0.7rem; font-weight: 800; text-transform: uppercase; letter-spacing: 1.2px; color: #38B6FF; display: block; margin-bottom: 0.15rem;">ESTABLISHED 2018</span>
                    <h3 style="font-family: var(--font-heading); font-size: 1.65rem; font-weight: 800; color: var(--color-charcoal); margin: 0; line-height: 1.1;">Delhi</h3>
                  </div>
                  <span style="background: rgba(56,182,255,0.1); color: #38B6FF; font-weight: 800; font-size: 0.75rem; padding: 4px 10px; border-radius: 100px;">2018 – Present</span>
                </div>

                <div style="background: #F0F9FF; border-radius: 12px; padding: 0.85rem; text-align: center; border: 1px solid rgba(56,182,255,0.15); margin-bottom: 1rem;">
                  <div style="font-family: var(--font-heading); font-size: 1.8rem; font-weight: 800; color: #38B6FF; line-height: 1;">16</div>
                  <div style="font-size: 0.7rem; font-weight: 700; color: var(--color-text-muted); text-transform: uppercase; margin-top: 0.2rem;">MCD Primary Schools</div>
                </div>

                <div style="font-size: 0.7rem; font-weight: 800; text-transform: uppercase; letter-spacing: 1px; color: #777; margin-bottom: 0.4rem;">Institutional Partners</div>
                <div style="display: flex; gap: 0.4rem; flex-wrap: wrap;">
                  <span style="background: white; border: 1.5px solid rgba(56,182,255,0.3); padding: 4px 10px; border-radius: 100px; font-weight: 700; font-size: 0.75rem; color: #38B6FF;">EMC</span>
                  <span style="background: white; border: 1.5px solid rgba(56,182,255,0.3); padding: 4px 10px; border-radius: 100px; font-weight: 700; font-size: 0.75rem; color: #38B6FF;">DIET</span>
                  <span style="background: white; border: 1.5px solid rgba(56,182,255,0.3); padding: 4px 10px; border-radius: 100px; font-weight: 700; font-size: 0.75rem; color: #38B6FF;">SCERT</span>
                  <span style="background: white; border: 1.5px solid rgba(56,182,255,0.3); padding: 4px 10px; border-radius: 100px; font-weight: 700; font-size: 0.75rem; color: #38B6FF;">NCERT</span>
                </div>
              </div>

              <!-- Card 3: Bihar -->
              <div class="deck-card" id="deck-card-br" onclick="switchStateDeck('br')" style="position: absolute; top: 0; left: 0; width: 100%; background: #ffffff; border-radius: 20px; padding: 1.5rem; box-shadow: 0 6px 20px rgba(0,0,0,0.06); border-top: 5px solid #FFC72C; transition: all 0.5s cubic-bezier(0.34, 1.56, 0.64, 1); z-index: 1; opacity: 0.45; transform: translateY(24px) scale(0.92); cursor: pointer;">
                <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 1rem;">
                  <div>
                    <span style="font-size: 0.7rem; font-weight: 800; text-transform: uppercase; letter-spacing: 1.2px; color: #D4A017; display: block; margin-bottom: 0.15rem;">ESTABLISHED 2022</span>
                    <h3 style="font-family: var(--font-heading); font-size: 1.65rem; font-weight: 800; color: var(--color-charcoal); margin: 0; line-height: 1.1;">Bihar</h3>
                  </div>
                  <span style="background: rgba(255,199,44,0.15); color: #B8860B; font-weight: 800; font-size: 0.75rem; padding: 4px 10px; border-radius: 100px;">2022 – Present</span>
                </div>

                <div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 0.6rem; margin-bottom: 1rem;">
                  <div style="background: #FFFDF5; border-radius: 12px; padding: 0.6rem 0.4rem; text-align: center; border: 1px solid rgba(255,199,44,0.25);">
                    <div style="font-family: var(--font-heading); font-size: 1.6rem; font-weight: 800; color: #D4A017; line-height: 1;">2</div>
                    <div style="font-size: 0.7rem; font-weight: 700; color: var(--color-text-muted); text-transform: uppercase; margin-top: 0.2rem;">Districts</div>
                  </div>
                  <div style="background: #FFFDF5; border-radius: 12px; padding: 0.6rem 0.4rem; text-align: center; border: 1px solid rgba(255,199,44,0.25);">
                    <div style="font-family: var(--font-heading); font-size: 1.6rem; font-weight: 800; color: #D4A017; line-height: 1;">13</div>
                    <div style="font-size: 0.7rem; font-weight: 700; color: var(--color-text-muted); text-transform: uppercase; margin-top: 0.2rem;">Blocks</div>
                  </div>
                  <div style="background: #FFFDF5; border-radius: 12px; padding: 0.6rem 0.4rem; text-align: center; border: 1px solid rgba(255,199,44,0.25);">
                    <div style="font-family: var(--font-heading); font-size: 1.6rem; font-weight: 800; color: #D4A017; line-height: 1;">1</div>
                    <div style="font-size: 0.7rem; font-weight: 700; color: var(--color-text-muted); text-transform: uppercase; margin-top: 0.2rem;">SCERT</div>
                  </div>
                </div>

                <p style="font-size: 0.85rem; color: #555; line-height: 1.5; margin: 0;">State-wide systemic transformation and teacher capacity building with SCERT Bihar.</p>
              </div>

            </div>
          </div>

          <script>
            function switchStateDeck(key) {
              const states = ['rj', 'dl', 'br'];
              const colors = { rj: '#1CA6A0', dl: '#38B6FF', br: '#FFC72C' };
              
              states.forEach(s => {
                const tab = document.getElementById('tab-' + s);
                const card = document.getElementById('deck-card-' + s);
                if (tab && card) {
                  if (s === key) {
                    tab.style.background = colors[s];
                    tab.style.color = 'white';
                    tab.style.boxShadow = '0 4px 14px ' + colors[s] + '66';
                    
                    card.style.zIndex = '3';
                    card.style.opacity = '1';
                    card.style.transform = 'translateY(0) scale(1)';
                    card.style.boxShadow = '0 16px 40px rgba(0,0,0,0.15)';
                  } else {
                    tab.style.background = 'transparent';
                    tab.style.color = 'white';
                    tab.style.boxShadow = 'none';
                    
                    const offsetIndex = (states.indexOf(s) - states.indexOf(key) + 3) % 3;
                    if (offsetIndex === 1) {
                      card.style.zIndex = '2';
                      card.style.opacity = '0.75';
                      card.style.transform = 'translateY(12px) scale(0.96)';
                      card.style.boxShadow = '0 10px 30px rgba(0,0,0,0.08)';
                    } else {
                      card.style.zIndex = '1';
                      card.style.opacity = '0.45';
                      card.style.transform = 'translateY(24px) scale(0.92)';
                      card.style.boxShadow = '0 6px 20px rgba(0,0,0,0.06)';
                    }
                  }
                }
              });
            }
          </script>
        </div>
      </div>
    </section>'''

pattern = re.compile(r'<!-- GEOGRAPHICAL REACH 3D MAP.*?<\/section>', re.DOTALL)
new_content = pattern.sub(new_reach_section, content)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(new_content)

print('Successfully made Geographical Reach card deck compact and fitted directly on the right of the map!')
