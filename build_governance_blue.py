import re

html_content = """
    <!-- GOVERNANCE & ADVISORY -->
    <!-- ════════════════════════════════════════ -->
    <section class="section" id="governance" aria-label="Governance and Advisory Board" style="background: linear-gradient(135deg, #01768d 0%, #08B9DB 100%); color: white; padding: 6rem 0; position: relative; overflow: hidden;">
      
      <!-- Decorative background elements -->
      <div style="position: absolute; top: -150px; right: -100px; width: 600px; height: 600px; background: rgba(255,255,255,0.06); border-radius: 50%; filter: blur(80px); pointer-events: none;"></div>
      <div style="position: absolute; bottom: -100px; left: -150px; width: 500px; height: 500px; background: rgba(255,255,255,0.04); border-radius: 50%; filter: blur(60px); pointer-events: none;"></div>

      <div class="container" style="max-width: 1200px; margin: 0 auto; position: relative; z-index: 2;">
        
        <div style="text-align: center; margin-bottom: 4rem;">
          <h2 style="font-family: var(--font-heading); font-size: clamp(2.5rem, 5vw, 4rem); font-weight: 800; color: #FFFFFF; margin-bottom: 1rem; line-height: 1.1;">Governance</h2>
          <p style="color: rgba(255,255,255,0.9); max-width: 700px; margin: 0 auto; font-size: 1.25rem; line-height: 1.6;">
            Kshamtalaya Foundation is governed by its Board of Directors under the Companies Act 2013. Our advisors guide strategy and practice and carry no statutory responsibility.
          </p>
        </div>

        <style>
          .gov-grid { 
            display: grid; 
            grid-template-columns: repeat(auto-fit, minmax(450px, 1fr)); 
            gap: 2.5rem; 
          }
          .gov-card { 
            display: flex; 
            gap: 1.5rem; 
            background: rgba(255, 255, 255, 0.1); 
            backdrop-filter: blur(16px); 
            -webkit-backdrop-filter: blur(16px);
            border: 1px solid rgba(255, 255, 255, 0.2); 
            border-radius: 24px; 
            padding: 2rem; 
            box-shadow: 0 15px 35px rgba(0,0,0,0.1);
            transition: transform 0.4s cubic-bezier(0.16, 1, 0.3, 1), background 0.4s ease;
          }
          .gov-card:hover {
            transform: translateY(-8px);
            background: rgba(255, 255, 255, 0.15);
            border-color: rgba(255,255,255,0.4);
          }
          .gov-img-wrapper {
            width: 130px; 
            height: 130px; 
            border-radius: 50%; 
            flex-shrink: 0; 
            border: 4px solid rgba(255,255,255,0.8);
            box-shadow: 0 10px 25px rgba(0,0,0,0.15);
            overflow: hidden;
            background: #fff;
          }
          .gov-img { 
            width: 100%; 
            height: 100%; 
            object-fit: cover; 
          }
          .gov-tbc { 
            width: 100%; 
            height: 100%; 
            display: flex; 
            align-items: center; 
            justify-content: center; 
            font-size: 1.5rem; 
            font-weight: 800; 
            color: var(--color-teal); 
            background: rgba(255,255,255,0.9);
          }
          .gov-info { display: flex; flex-direction: column; justify-content: center; }
          .gov-info h4 { 
            font-family: var(--font-heading); 
            font-size: 1.6rem; 
            font-weight: 800;
            color: #FFFFFF; 
            margin-bottom: 0.3rem; 
            letter-spacing: 0.5px;
          }
          .gov-info .gov-role { 
            font-size: 0.85rem; 
            font-weight: 800; 
            text-transform: uppercase; 
            letter-spacing: 1.5px; 
            color: var(--color-sunshine); 
            margin-bottom: 1rem; 
          }
          .gov-info p { 
            font-size: 1.05rem; 
            color: rgba(255,255,255,0.95); 
            line-height: 1.6; 
            margin: 0; 
          }
          
          .gov-divider { 
            display: flex;
            align-items: center;
            gap: 1rem;
            margin: 4rem 0 2.5rem;
          }
          .gov-divider h3 {
            font-family: var(--font-heading);
            font-size: 1.25rem;
            font-weight: 800;
            color: var(--color-sunshine);
            text-transform: uppercase;
            letter-spacing: 3px;
            margin: 0;
            white-space: nowrap;
          }
          .gov-divider::after {
            content: "";
            flex: 1;
            height: 1px;
            background: linear-gradient(90deg, rgba(255,255,255,0.3), transparent);
          }

          @media (max-width: 768px) {
            .gov-grid { grid-template-columns: 1fr; }
            .gov-card { flex-direction: column; align-items: center; text-align: center; padding: 2rem 1.5rem; }
            .gov-info { align-items: center; }
          }
        </style>

        <!-- BOARD OF DIRECTORS -->
        <div class="gov-divider"><h3>Board of Directors</h3></div>
        <div class="gov-grid">
          <div class="gov-card reveal">
            <div class="gov-img-wrapper">
              <img class="gov-img" src="/assets/team/soumya_b.jpeg" alt="Soumya Bhaskaracharya" loading="lazy">
            </div>
            <div class="gov-info">
              <h4>Soumya Bhaskaracharya</h4>
              <div class="gov-role">DIRECTOR AND CEO</div>
              <p>Masters in Applied Sociology. Eight years with the organisation.</p>
            </div>
          </div>
          <div class="gov-card reveal">
            <div class="gov-img-wrapper">
              <img class="gov-img" src="/assets/team/anjali_gupte.jpeg" alt="Anjali Gupte" loading="lazy">
            </div>
            <div class="gov-info">
              <h4>Anjali Gupte</h4>
              <div class="gov-role">DIRECTOR & FOUNDING MEMBER</div>
              <p>MSc Statistics, B.Ed. Chairs the Advisory Board.</p>
            </div>
          </div>
          <div class="gov-card reveal">
            <div class="gov-img-wrapper">
              <div class="gov-tbc">TBC</div>
            </div>
            <div class="gov-info">
              <h4>Further Directors</h4>
              <div class="gov-role" style="color: rgba(255,255,255,0.6);">UNDER REVIEW</div>
              <p>Board composition is under review. Names, roles and DINs to be published once appointments are confirmed and filed.</p>
            </div>
          </div>
        </div>

        <!-- ADVISORY BOARD -->
        <div class="gov-divider"><h3>Advisory Board</h3></div>
        <div class="gov-grid">
          <div class="gov-card reveal">
            <div class="gov-img-wrapper">
              <img class="gov-img" src="/assets/advisory/Ujjawalthakur.png" alt="Ujjwal Thakar" loading="lazy">
            </div>
            <div class="gov-info">
              <h4>Ujjwal Thakar</h4>
              <div class="gov-role">STRATEGY & SECTOR POSITIONING</div>
              <p>Chairperson, Educate Girls. Co-founder, Ujwal Impact Advisers. Over 30 years across the social and corporate sectors.</p>
            </div>
          </div>
          <div class="gov-card reveal">
            <div class="gov-img-wrapper">
              <img class="gov-img" src="/assets/advisory/LaxmiHiranandni.png" alt="Lakshmi Hiranandani" loading="lazy">
            </div>
            <div class="gov-info">
              <h4>Lakshmi Hiranandani</h4>
              <div class="gov-role">COMMUNITY MOBILISATION</div>
              <p>Former CEO of Swara, Voice of Women. Works on women's economic empowerment in rural India.</p>
            </div>
          </div>
          <div class="gov-card reveal">
            <div class="gov-img-wrapper">
              <img class="gov-img" src="/assets/advisory/Reshma Piramal.png" alt="Reshma Piramal" loading="lazy">
            </div>
            <div class="gov-info">
              <h4>Reshma Piramal</h4>
              <div class="gov-role">SOCIAL & EMOTIONAL LEARNING</div>
              <p>Practice Lead at The Karuna Practice. Senior facilitator in social, emotional and ethical learning.</p>
            </div>
          </div>
          <div class="gov-card reveal">
            <div class="gov-img-wrapper">
              <img class="gov-img" src="/assets/advisory/Sadhna Saxsena.png" alt="Prof. Sadhna Saxena" loading="lazy">
            </div>
            <div class="gov-info">
              <h4>Prof. Sadhna Saxena</h4>
              <div class="gov-role">CURRICULUM, LITERACY & EQUITY</div>
              <p>Educationist and teacher educator. Works on literacy, science education and inclusive learning environments.</p>
            </div>
          </div>
          <div class="gov-card reveal">
            <div class="gov-img-wrapper">
              <img class="gov-img" src="/assets/advisory/Dr. Ashok Kumar.png" alt="Dr. Ashok Kumar" loading="lazy">
            </div>
            <div class="gov-info">
              <h4>Dr. Ashok Kumar</h4>
              <div class="gov-role">TEACHER EDUCATION</div>
              <p>Assistant Professor, NCERT. Strengthens teacher education through academic and professional development.</p>
            </div>
          </div>
          <div class="gov-card reveal">
            <div class="gov-img-wrapper">
              <img class="gov-img" src="/assets/advisory/Sanjiv jain.png" alt="Sanjiv Jain" loading="lazy">
            </div>
            <div class="gov-info">
              <h4>Sanjiv Jain</h4>
              <div class="gov-role">FINANCE & GOVERNANCE</div>
              <p>Director Finance at Seva Mandir. Chartered Accountant with over 35 years in financial management.</p>
            </div>
          </div>
          <div class="gov-card reveal">
            <div class="gov-img-wrapper">
              <img class="gov-img" src="/assets/advisory/Avishek Kumar.png" alt="Dr. Avishek Kumar" loading="lazy">
            </div>
            <div class="gov-info">
              <h4>Dr. Avishek Kumar</h4>
              <div class="gov-role">ORGANISATIONAL SYSTEMS</div>
              <p>Co-founder and Board Advisor, VFlowTech. Advises on building systems that hold as an organisation grows.</p>
            </div>
          </div>
          <div class="gov-card reveal">
            <div class="gov-img-wrapper">
              <img class="gov-img" src="/assets/advisory/Joshila Kumari.png" alt="Joshila Kumari" loading="lazy">
            </div>
            <div class="gov-info">
              <h4>Joshila Kumari</h4>
              <div class="gov-role">YOUTH & GIRLS' LEADERSHIP</div>
              <p>From Kotra, Rajasthan. Former iDISCOVER Fellow. PlayQuity Coach and UPAI Fellow.</p>
            </div>
          </div>
        </div>

        <!-- JOSHILA BANNER -->
        <style>
          .joshila-banner {
            margin-top: 7rem;
            background: var(--color-sunshine);
            border-radius: 32px;
            position: relative;
            padding: 3.5rem 3.5rem 3.5rem 340px;
            box-shadow: 0 25px 50px rgba(0,0,0,0.15);
            color: var(--color-charcoal);
            border: 2px solid rgba(255, 255, 255, 0.4);
          }
          .joshila-photo {
            position: absolute;
            left: 40px;
            bottom: 0;
            width: 260px;
            height: 260px;
            border-radius: 50% 50% 0 0;
            border: 8px solid var(--color-white);
            border-bottom: none;
            object-fit: cover;
            object-position: center top;
            box-shadow: 0 -15px 40px rgba(0,0,0,0.12);
          }
          .joshila-tag {
            font-size: 1.1rem;
            font-weight: 700;
            color: var(--color-charcoal);
            opacity: 0.8;
            margin-bottom: 0.5rem;
          }
          .joshila-title {
            font-family: var(--font-heading);
            font-size: 2.2rem;
            font-weight: 800;
            line-height: 1.2;
            margin-bottom: 1.2rem;
            color: var(--color-charcoal);
          }
          .joshila-desc {
            font-size: 1.15rem;
            line-height: 1.6;
            color: var(--color-text-secondary);
            max-width: 650px;
            margin-bottom: 1.5rem;
          }
          .joshila-box {
            padding: 1.2rem;
            border: 2px dashed rgba(49, 50, 52, 0.3);
            border-radius: 16px;
            background: rgba(255,255,255,0.3);
            display: inline-block;
          }
          .joshila-box h5 {
            font-size: 0.85rem;
            text-transform: uppercase;
            letter-spacing: 1.5px;
            margin-bottom: 6px;
            font-weight: 800;
            color: var(--color-teal-dark);
          }
          .joshila-box p {
            font-size: 0.95rem;
            margin: 0;
            color: var(--color-charcoal);
            font-weight: 500;
          }
          @media (max-width: 900px) {
            .joshila-banner {
              margin-top: 8rem;
              padding: 180px 2rem 2.5rem;
              text-align: center;
            }
            .joshila-photo {
              left: 50%;
              transform: translateX(-50%);
              bottom: auto;
              top: -120px;
              width: 220px;
              height: 220px;
              border-radius: 50%;
              border: 6px solid var(--color-white);
            }
            .joshila-desc {
              margin-left: auto;
              margin-right: auto;
            }
          }
        </style>
        <div class="joshila-banner reveal">
          <img src="/assets/advisory/Joshila Kumari.png" alt="Joshila Kumari" class="joshila-photo">
          <div class="joshila-tag">कोटड़ा से</div>
          <div class="joshila-title">Joshila was a girl in Kotra when we started. She now advises our Board.</div>
          <p class="joshila-desc">
            She came through the iDISCOVER Fellowship, coaches with PlayQuity, and represents India as a Women's Ultimate Fellow. If anyone wants a single measure of whether a depth model works, this is the one we would offer.
          </p>
          <div class="joshila-box">
            <h5>CHECK WITH JOSHILA</h5>
            <p>Framing someone's own story publicly needs her consent and her preferred wording.</p>
          </div>
        </div>

      </div>
    </section>
"""

for filename in ['story.html', 'index.html']:
    with open(filename, 'r', encoding='utf-8') as f:
        text = f.read()

    pattern = r'<!-- GOVERNANCE & ADVISORY -->\s*<!-- [═]+ -->\s*<section.*?id="governance".*?</section>'
    new_text = re.sub(pattern, html_content, text, flags=re.DOTALL)
    
    if text != new_text:
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(new_text)
        print(f"Updated governance section in {filename}")
    else:
        print(f"Could not find governance section to replace in {filename}")
