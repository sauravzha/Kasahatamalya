import re

new_team_html = """
      <div class="container" style="position: relative; z-index: 2; max-width: 1280px; margin: 0 auto; padding: 0 1.5rem;">
        <!-- Section Header -->
        <div class="section-header reveal" style="text-align: center; margin-bottom: 4rem;">
          <div class="section-header__eyebrow" style="display: inline-block; padding: 6px 18px; background: rgba(8, 185, 219, 0.1); border: 1.5px solid var(--color-teal); border-radius: 30px; font-weight: 800; font-size: 0.85rem; color: var(--color-teal); letter-spacing: 1.5px; margin-bottom: 1rem;">
            GOVERNANCE & LEADERSHIP
          </div>
          <h2 class="section-header__title" style="font-family: 'Baloo 2', cursive; font-size: clamp(2.2rem, 4vw, 3.2rem); color: var(--color-charcoal); margin-bottom: 1rem; font-weight: 800; line-height: 1.2;">
            Core Leadership & <span class="doodle-highlight" style="color: var(--color-teal);">Founding Team</span>
          </h2>
          <p class="section-header__desc" style="max-width: 720px; margin: 0 auto; font-size: 1.15rem; color: var(--color-text-secondary); line-height: 1.6;">
            The founders, directors, and senior leaders steering Kshamtalaya's mission to strengthen learning ecosystems and nurture child potential across India.
          </p>
        </div>

        <style>
          .team-awwwards-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
            gap: 1.5rem;
            margin-top: 3rem;
          }
          .team-pro-card {
            position: relative;
            height: 480px;
            border-radius: 30px;
            overflow: hidden;
            cursor: pointer;
            box-shadow: 0 15px 35px rgba(0,0,0,0.05);
            background: #fff;
          }
          .team-pro-img {
            position: absolute;
            top: 0; left: 0; width: 100%; height: 100%;
            object-fit: cover;
            object-position: center 20%;
            transition: transform 0.8s cubic-bezier(0.25, 1, 0.3, 1), filter 0.8s ease;
            filter: grayscale(80%) contrast(1.1);
          }
          .team-pro-card:hover .team-pro-img {
            transform: scale(1.08);
            filter: grayscale(0%) contrast(1);
          }
          .team-pro-overlay {
            position: absolute;
            inset: 0;
            background: linear-gradient(to top, rgba(0,0,0,0.85) 0%, rgba(0,0,0,0.4) 40%, rgba(0,0,0,0) 100%);
            opacity: 0.7;
            transition: opacity 0.5s ease;
          }
          .team-pro-card:hover .team-pro-overlay {
            opacity: 0.95;
            background: linear-gradient(to top, var(--pro-color) 0%, rgba(0,0,0,0.6) 40%, rgba(0,0,0,0) 100%);
          }
          .team-pro-content {
            position: absolute;
            bottom: 0;
            left: 0;
            right: 0;
            padding: 2rem;
            color: white;
            transform: translateY(60px);
            transition: transform 0.6s cubic-bezier(0.25, 1, 0.3, 1);
          }
          .team-pro-card:hover .team-pro-content {
            transform: translateY(0);
          }
          .team-pro-name {
            font-family: var(--font-heading);
            font-size: 1.8rem;
            font-weight: 800;
            margin: 0 0 0.25rem 0;
            line-height: 1.1;
            text-shadow: 0 2px 10px rgba(0,0,0,0.3);
          }
          .team-pro-role {
            color: #FFC72C;
            font-weight: 700;
            font-size: 0.95rem;
            letter-spacing: 0.5px;
            margin-bottom: 1.5rem;
            display: block;
            text-shadow: 0 2px 5px rgba(0,0,0,0.3);
          }
          .team-pro-card:hover .team-pro-role {
            color: #fff;
          }
          .team-pro-details {
            opacity: 0;
            transition: opacity 0.5s ease;
            transition-delay: 0.1s;
          }
          .team-pro-card:hover .team-pro-details {
            opacity: 1;
          }
          .team-pro-stat {
            display: flex;
            align-items: flex-start;
            gap: 10px;
            font-size: 0.9rem;
            color: rgba(255,255,255,0.85);
            margin-bottom: 0.75rem;
            line-height: 1.4;
          }
          .team-pro-stat strong {
            color: white;
            font-weight: 700;
          }
          .team-pro-badge {
            display: inline-block;
            padding: 4px 10px;
            background: rgba(255,255,255,0.2);
            backdrop-filter: blur(4px);
            border-radius: 20px;
            font-size: 0.8rem;
            font-weight: 700;
            margin-top: 0.5rem;
            border: 1px solid rgba(255,255,255,0.3);
          }
          
          @media (max-width: 768px) {
            .team-pro-content {
              transform: translateY(0);
            }
            .team-pro-details {
              opacity: 1;
            }
            .team-pro-img { filter: grayscale(0%); }
            .team-pro-overlay { opacity: 0.9; }
          }
        </style>

        <div class="team-awwwards-grid reveal" data-stagger>
          <!-- 1. Pooja Singh -->
          <div class="team-pro-card" style="--pro-color: #FF6F59;">
            <img src="/assets/team/pooja_singh.jpeg" alt="Pooja Singh" class="team-pro-img" />
            <div class="team-pro-overlay"></div>
            <div class="team-pro-content">
              <h3 class="team-pro-name">Pooja Singh</h3>
              <span class="team-pro-role">Co-Founder & Mentor</span>
              <div class="team-pro-details">
                <div class="team-pro-stat">
                  <span>🎓</span>
                  <div><strong>Qualifications:</strong><br/>Masters in Mass Comm</div>
                </div>
                <div class="team-pro-badge">🌟 10 Years</div>
              </div>
            </div>
          </div>
          
          <!-- 2. Anjali Gupte -->
          <div class="team-pro-card" style="--pro-color: #9B51E0;">
            <img src="/assets/team/anjali_gupte.jpeg" alt="Anjali Gupte" class="team-pro-img" />
            <div class="team-pro-overlay"></div>
            <div class="team-pro-content">
              <h3 class="team-pro-name">Anjali Gupte</h3>
              <span class="team-pro-role">Director, Founding member</span>
              <div class="team-pro-details">
                <div class="team-pro-stat">
                  <span>🎓</span>
                  <div><strong>Qualifications:</strong><br/>MSc Statistics, B.Ed.</div>
                </div>
                <div class="team-pro-badge">🌟 10 Years</div>
              </div>
            </div>
          </div>
          
          <!-- 3. Soumya B -->
          <div class="team-pro-card" style="--pro-color: #08B9DB;">
            <img src="/assets/team/soumya_b.jpeg" alt="Soumya B" class="team-pro-img" />
            <div class="team-pro-overlay"></div>
            <div class="team-pro-content">
              <h3 class="team-pro-name">Soumya B</h3>
              <span class="team-pro-role">Director, CEO</span>
              <div class="team-pro-details">
                <div class="team-pro-stat">
                  <span>🎓</span>
                  <div><strong>Qualifications:</strong><br/>Masters in Applied Sociology</div>
                </div>
                <div class="team-pro-badge">🌟 10 Years</div>
              </div>
            </div>
          </div>
          
          <!-- 4. Abhishek Tiwari -->
          <div class="team-pro-card" style="--pro-color: #1CA6A0;">
            <img src="/assets/team/abhishek_kumar_tiwari.jpg" alt="Abhishek Tiwari" class="team-pro-img" />
            <div class="team-pro-overlay"></div>
            <div class="team-pro-content">
              <h3 class="team-pro-name">Abhishek Tiwari</h3>
              <span class="team-pro-role">Head of Programs, Bihar</span>
              <div class="team-pro-details">
                <div class="team-pro-stat">
                  <span>🎓</span>
                  <div><strong>Qualifications:</strong><br/>Bachelors of Science</div>
                </div>
                <div class="team-pro-badge">🌟 10 Years</div>
              </div>
            </div>
          </div>
          
          <!-- 5. Tina Aggarwal -->
          <div class="team-pro-card" style="--pro-color: #38B6FF;">
            <img src="/assets/team/tina_aggarwal.jpg" alt="Tina Aggarwal" class="team-pro-img" />
            <div class="team-pro-overlay"></div>
            <div class="team-pro-content">
              <h3 class="team-pro-name">Tina Aggarwal</h3>
              <span class="team-pro-role">Head of Programs, Delhi</span>
              <div class="team-pro-details">
                <div class="team-pro-stat">
                  <span>🎓</span>
                  <div><strong>Qualifications:</strong><br/>D.El Ed, MA- EDUCATION</div>
                </div>
                <div class="team-pro-badge">🌟 10 Years</div>
              </div>
            </div>
          </div>
        </div>
      </div>
"""

def update_team(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        text = f.read()

    # Find the <div class="container" ...> inside #core-governance
    # Pattern to match the container and EVERYTHING inside it until the closing </section>
    pattern = r'<div class="container" style="position: relative; z-index: 2; max-width: 1280px; margin: 0 auto; padding: 0 1\.5rem;">[\s\S]*?(?=    </section>)'
    
    new_text = re.sub(pattern, new_team_html.strip() + '\n', text)
    
    if new_text != text:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_text)
        print(f"Successfully updated team section in {file_path}")
    else:
        print(f"Could not find the target team block in {file_path}")

update_team('index.html')
update_team('story.html')
