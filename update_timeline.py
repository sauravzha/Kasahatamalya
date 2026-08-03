import re

new_timeline_html = """
        <div class="interactive-timeline-container reveal" style="max-width: 1200px; margin: 4rem auto;">
          <style>
            .expanding-timeline {
              display: flex;
              height: 500px;
              gap: 12px;
              width: 100%;
              padding: 0 1rem;
            }
            .et-card {
              flex: 1;
              position: relative;
              background: linear-gradient(145deg, #ffffff 0%, var(--et-bg-color) 100%);
              border-radius: 24px;
              overflow: hidden;
              cursor: pointer;
              transition: all 0.7s cubic-bezier(0.25, 1, 0.3, 1);
              box-shadow: 0 10px 20px rgba(0,0,0,0.04);
              display: flex;
              flex-direction: column;
              border: 1px solid rgba(0,0,0,0.03);
            }
            .et-card:hover, .et-card:focus-within {
              flex: 6;
              box-shadow: 0 20px 40px rgba(0,0,0,0.12);
              transform: translateY(-5px);
            }
            /* The Year Text */
            .et-year {
              position: absolute;
              top: 50%;
              left: 50%;
              transform: translate(-50%, -50%) rotate(-90deg);
              font-family: var(--font-heading);
              font-size: 2rem;
              font-weight: 900;
              color: var(--et-color);
              transition: all 0.7s cubic-bezier(0.25, 1, 0.3, 1);
              white-space: nowrap;
              letter-spacing: 2px;
              opacity: 0.7;
            }
            .et-card:hover .et-year, .et-card:focus-within .et-year {
              transform: translate(0, 0) rotate(0deg);
              top: 2rem;
              left: 2rem;
              font-size: 3.5rem;
              opacity: 1;
            }
            /* The Content */
            .et-content {
              opacity: 0;
              position: absolute;
              bottom: 0;
              left: 0;
              right: 0;
              padding: 2rem;
              padding-top: 4rem;
              background: linear-gradient(0deg, #ffffff 60%, rgba(255,255,255,0) 100%);
              transform: translateY(30px);
              transition: all 0.5s ease;
              transition-delay: 0s;
              pointer-events: none;
            }
            .et-card:hover .et-content, .et-card:focus-within .et-content {
              opacity: 1;
              transform: translateY(0);
              transition-delay: 0.3s;
              pointer-events: auto;
            }
            .et-content h3 {
              font-size: 1.6rem;
              color: var(--color-charcoal);
              margin-bottom: 0.75rem;
              font-weight: 800;
              line-height: 1.2;
            }
            .et-content p {
              font-size: 1.05rem;
              color: var(--color-text-secondary);
              line-height: 1.6;
              margin: 0;
            }
            
            /* Responsive */
            @media (max-width: 900px) {
              .expanding-timeline {
                flex-direction: column;
                height: auto;
              }
              .et-card {
                height: 80px;
                flex: none;
                transition: all 0.5s ease;
              }
              .et-year {
                transform: translate(0, -50%) rotate(0deg);
                top: 50%;
                left: 1.5rem;
                font-size: 2rem;
                opacity: 1;
              }
              .et-card:hover, .et-card:focus-within {
                height: 300px;
                transform: translateX(5px);
              }
              .et-card:hover .et-year, .et-card:focus-within .et-year {
                top: 1.5rem;
                transform: translate(0, 0);
              }
            }
          </style>

          <div class="expanding-timeline">
            <!-- 2016 -->
            <div class="et-card" tabindex="0" style="--et-color: #FF6F59; --et-bg-color: rgba(255,111,89,0.15);">
              <div class="et-year">2016</div>
              <div class="et-content">
                <h3>The beginning, in Kotra</h3>
                <p>Two fellows in a remote tribal block, asking what real education would look like there. Incorporated as a Section 8 company on 27 July 2016.</p>
              </div>
            </div>
            <!-- 2017 -->
            <div class="et-card" tabindex="0" style="--et-color: #1CA6A0; --et-bg-color: rgba(28,166,160,0.15);">
              <div class="et-year">2017</div>
              <div class="et-content">
                <h3>First programmes</h3>
                <p>Learning Festivals begin in June. The iDISCOVER Fellowship inducts its first cohort of grassroots education leaders in November.</p>
              </div>
            </div>
            <!-- 2018 -->
            <div class="et-card" tabindex="0" style="--et-color: #FFC72C; --et-bg-color: rgba(255,199,44,0.2);">
              <div class="et-year">2018</div>
              <div class="et-content">
                <h3>Into Delhi</h3>
                <p>Work begins in MCD government schools in East Delhi, expanding our urban footprint.</p>
              </div>
            </div>
            <!-- 2019 -->
            <div class="et-card" tabindex="0" style="--et-color: #38B6FF; --et-bg-color: rgba(56,182,255,0.15);">
              <div class="et-year">2019</div>
              <div class="et-content">
                <h3>Curriculum with the state</h3>
                <p>SEE Learning launched with Emory University and the Dalai Lama Trust. Entrepreneurial Mindset Curriculum co-created with SCERT Delhi.</p>
              </div>
            </div>
            <!-- 2020 -->
            <div class="et-card" tabindex="0" style="--et-color: #9B51E0; --et-bg-color: rgba(155,81,224,0.15);">
              <div class="et-year">2020</div>
              <div class="et-content">
                <h3>The pandemic & radio</h3>
                <p>Relief for families in Kotra. Radio learning launched with Radio Madhuban for children with no internet access.</p>
              </div>
            </div>
            <!-- 2021 -->
            <div class="et-card" tabindex="0" style="--et-color: #FF6F59; --et-bg-color: rgba(255,111,89,0.15);">
              <div class="et-year">2021</div>
              <div class="et-content">
                <h3>Institutional footing</h3>
                <p>CSR registration approved in April 2021, opening the door to transformative corporate partnerships.</p>
              </div>
            </div>
            <!-- 2022 -->
            <div class="et-card" tabindex="0" style="--et-color: #1CA6A0; --et-bg-color: rgba(28,166,160,0.15);">
              <div class="et-year">2022</div>
              <div class="et-content">
                <h3>Into Bihar</h3>
                <p>Work begins in Samastipur district, scaling impact in partnership with SCERT Bihar.</p>
              </div>
            </div>
            <!-- 2023 -->
            <div class="et-card" tabindex="0" style="--et-color: #FFC72C; --et-bg-color: rgba(255,199,44,0.2);">
              <div class="et-year">2023</div>
              <div class="et-content">
                <h3>Recognised globally</h3>
                <p>The parent engagement model reaches the global Top 10 for the World's Best School Prize for Community Collaboration.</p>
              </div>
            </div>
            <!-- 2025 -->
            <div class="et-card" tabindex="0" style="--et-color: #38B6FF; --et-bg-color: rgba(56,182,255,0.15);">
              <div class="et-year">2025</div>
              <div class="et-content">
                <h3>Adopted by the system</h3>
                <p>The STAR Parents model is officially adopted by the Municipal Corporation of Delhi starting 1 April 2025.</p>
              </div>
            </div>
            <!-- 2026 -->
            <div class="et-card" tabindex="0" style="--et-color: #9B51E0; --et-bg-color: rgba(155,81,224,0.15);">
              <div class="et-year">2026</div>
              <div class="et-content">
                <h3>The depth decade begins</h3>
                <p>Ten years in. An Advisory Board constituted. The next decade is about deeper roots and stronger institutions.</p>
              </div>
            </div>
          </div>
        </div>
"""

def replace_timeline():
    with open('index.html', 'r', encoding='utf-8') as f:
        text = f.read()

    # Pattern to match the existing premium-timeline
    # From: <div class="premium-timeline" data-stagger>
    # Up to: </div> before <div class="text-center reveal" style="margin-top: var(--space-xl);">
    
    pattern = r'<div class="premium-timeline" data-stagger>[\s\S]*?(?=<div class="text-center reveal" style="margin-top: var\(--space-xl\);">)'
    
    new_text = re.sub(pattern, new_timeline_html.strip() + '\n        ', text)
    
    if new_text != text:
        with open('index.html', 'w', encoding='utf-8') as f:
            f.write(new_text)
        print("Successfully replaced vertical timeline with horizontal expanding accordion!")
    else:
        print("Could not find the target timeline block in index.html.")

replace_timeline()
