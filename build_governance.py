import re

html_content = """
    <!-- GOVERNANCE & ADVISORY -->
    <!-- ════════════════════════════════════════ -->
    <section class="section" id="governance" aria-label="Governance and Advisory Board" style="background-color: var(--color-cream-dark); padding: var(--space-4xl) 0;">
      <div class="container" style="max-width: 1000px; margin: 0 auto;">
        
        <div style="margin-bottom: var(--space-3xl);">
          <h2 style="font-family: var(--font-heading); font-size: var(--fs-h2); color: var(--color-teal-dark); margin-bottom: var(--space-sm);">Governance</h2>
          <p style="color: var(--color-text-secondary); max-width: 800px; font-size: var(--fs-body); line-height: 1.6;">
            Kshamtalaya Foundation is governed by its Board of Directors under the Companies Act 2013. Our advisors guide strategy and practice and carry no statutory responsibility.
          </p>
        </div>

        <style>
          .gov-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 0; }
          .gov-card { display: flex; gap: var(--space-lg); padding: var(--space-xl) var(--space-md); border-bottom: 1px solid rgba(0,0,0,0.06); }
          .gov-card:nth-child(odd) { border-right: 1px solid rgba(0,0,0,0.06); }
          .gov-img { width: 72px; height: 72px; border-radius: 50%; object-fit: cover; flex-shrink: 0; background: #eee; }
          .gov-tbc { width: 72px; display: flex; align-items: center; justify-content: center; font-size: 0.75rem; font-weight: bold; color: var(--color-text-muted); flex-shrink: 0; }
          .gov-info h4 { font-family: var(--font-heading); font-size: 1.15rem; color: var(--color-teal-dark); margin-bottom: 2px; }
          .gov-info h4.yellow { color: var(--color-sunshine-dark); }
          .gov-info .gov-role { font-size: 0.75rem; font-weight: bold; text-transform: uppercase; letter-spacing: 1px; color: var(--color-teal); margin-bottom: 10px; }
          .gov-info .gov-role.yellow { color: var(--color-sunshine-dark); }
          .gov-info p { font-size: 0.9rem; color: var(--color-text-secondary); line-height: 1.5; margin: 0; }
          
          .gov-divider { 
            font-size: 0.8rem; font-weight: bold; text-transform: uppercase; letter-spacing: 2px; 
            color: var(--color-teal); border-bottom: 1px solid rgba(0,0,0,0.06); padding-bottom: 8px; margin-top: var(--space-3xl);
          }
          .gov-divider.yellow { color: var(--color-sunshine-dark); }

          @media (max-width: 768px) {
            .gov-grid { grid-template-columns: 1fr; }
            .gov-card:nth-child(odd) { border-right: none; }
          }
        </style>

        <!-- BOARD OF DIRECTORS -->
        <div class="gov-divider">BOARD OF DIRECTORS</div>
        <div class="gov-grid">
          <div class="gov-card">
            <img class="gov-img" src="/assets/team/soumya_b.jpeg" alt="Soumya Bhaskaracharya">
            <div class="gov-info">
              <h4>Soumya Bhaskaracharya</h4>
              <div class="gov-role">DIRECTOR AND CEO</div>
              <p>Masters in Applied Sociology. Eight years with the organisation.</p>
            </div>
          </div>
          <div class="gov-card">
            <img class="gov-img" src="/assets/team/anjali_gupte.jpeg" alt="Anjali Gupte">
            <div class="gov-info">
              <h4>Anjali Gupte</h4>
              <div class="gov-role">DIRECTOR AND FOUNDING MEMBER</div>
              <p>MSc Statistics, B.Ed. Chairs the Advisory Board.</p>
            </div>
          </div>
          <div class="gov-card">
            <div class="gov-tbc">TBC</div>
            <div class="gov-info">
              <h4>Further Directors</h4>
              <p>Board composition is under review. Names, roles and DINs to be published once appointments are confirmed and filed.</p>
            </div>
          </div>
        </div>

        <!-- ADVISORY BOARD -->
        <div class="gov-divider yellow">ADVISORY BOARD</div>
        <div class="gov-grid">
          <div class="gov-card">
            <img class="gov-img" src="/assets/advisory/Ujjawalthakur.png" alt="Ujjwal Thakar">
            <div class="gov-info">
              <h4>Ujjwal Thakar</h4>
              <div class="gov-role yellow">STRATEGY AND SECTOR POSITIONING</div>
              <p>Chairperson, Educate Girls. Co-founder, Ujwal Impact Advisers. Over 30 years across the social and corporate sectors.</p>
            </div>
          </div>
          <div class="gov-card">
            <img class="gov-img" src="/assets/advisory/LaxmiHiranandni.png" alt="Lakshmi Hiranandani">
            <div class="gov-info">
              <h4>Lakshmi Hiranandani</h4>
              <div class="gov-role yellow">COMMUNITY MOBILISATION</div>
              <p>Former CEO of Swara, Voice of Women. Works on women's economic empowerment in rural India.</p>
            </div>
          </div>
          <div class="gov-card">
            <img class="gov-img" src="/assets/advisory/Reshma Piramal.png" alt="Reshma Piramal">
            <div class="gov-info">
              <h4>Reshma Piramal</h4>
              <div class="gov-role yellow">SOCIAL AND EMOTIONAL LEARNING</div>
              <p>Practice Lead at The Karuna Practice. Senior facilitator in social, emotional and ethical learning.</p>
            </div>
          </div>
          <div class="gov-card">
            <img class="gov-img" src="/assets/advisory/Sadhna Saxsena.png" alt="Prof. Sadhna Saxena">
            <div class="gov-info">
              <h4>Prof. Sadhna Saxena</h4>
              <div class="gov-role yellow">CURRICULUM, LITERACY AND EQUITY</div>
              <p>Educationist and teacher educator. Works on literacy, science education and inclusive learning environments.</p>
            </div>
          </div>
          <div class="gov-card">
            <img class="gov-img" src="/assets/advisory/Dr. Ashok Kumar.png" alt="Dr. Ashok Kumar">
            <div class="gov-info">
              <h4>Dr. Ashok Kumar</h4>
              <div class="gov-role yellow">TEACHER EDUCATION</div>
              <p>Assistant Professor, NCERT. Strengthens teacher education through academic and professional development.</p>
            </div>
          </div>
          <div class="gov-card">
            <img class="gov-img" src="/assets/advisory/Sanjiv jain.png" alt="Sanjiv Jain">
            <div class="gov-info">
              <h4>Sanjiv Jain</h4>
              <div class="gov-role yellow">FINANCE AND GOVERNANCE</div>
              <p>Director Finance at Seva Mandir. Chartered Accountant with over 35 years in financial management.</p>
            </div>
          </div>
          <div class="gov-card">
            <img class="gov-img" src="/assets/advisory/Avishek Kumar.png" alt="Dr. Avishek Kumar">
            <div class="gov-info">
              <h4>Dr. Avishek Kumar</h4>
              <div class="gov-role yellow">ORGANISATIONAL SYSTEMS</div>
              <p>Co-founder and Board Advisor, VFlowTech. Advises on building systems that hold as an organisation grows.</p>
            </div>
          </div>
          <div class="gov-card">
            <img class="gov-img" src="/assets/advisory/Joshila Kumari.png" alt="Joshila Kumari">
            <div class="gov-info">
              <h4>Joshila Kumari</h4>
              <div class="gov-role yellow">YOUTH AND GIRLS' LEADERSHIP</div>
              <p>From Kotra, Rajasthan. Former iDISCOVER Fellow. PlayQuity Coach and UPAI Fellow.</p>
            </div>
          </div>
        </div>

        <!-- JOSHILA BANNER -->
        <style>
          .joshila-banner {
            margin-top: var(--space-5xl);
            background: linear-gradient(135deg, var(--color-teal), var(--color-teal-dark));
            border-radius: var(--radius-2xl);
            position: relative;
            padding: var(--space-2xl) var(--space-2xl) var(--space-xl) 280px;
            box-shadow: var(--shadow-xl);
            color: var(--color-white);
          }
          .joshila-photo {
            position: absolute;
            left: 30px;
            bottom: 0;
            width: 220px;
            height: 220px;
            border-radius: 50% 50% 0 0;
            border: 6px solid var(--color-white);
            border-bottom: none;
            object-fit: cover;
            object-position: center top;
            box-shadow: 0 -10px 30px rgba(0,0,0,0.15);
          }
          .joshila-tag {
            font-size: 0.9rem;
            font-weight: 600;
            opacity: 0.9;
            margin-bottom: var(--space-sm);
          }
          .joshila-title {
            font-family: var(--font-heading);
            font-size: 1.8rem;
            font-weight: 800;
            line-height: 1.2;
            margin-bottom: var(--space-md);
          }
          .joshila-desc {
            font-size: 0.95rem;
            line-height: 1.6;
            opacity: 0.9;
            max-width: 600px;
          }
          .joshila-box {
            margin-top: var(--space-md);
            padding: var(--space-md);
            border: 1px dashed rgba(255,255,255,0.4);
            border-radius: var(--radius-md);
            background: rgba(255,255,255,0.05);
          }
          .joshila-box h5 {
            font-size: 0.75rem;
            text-transform: uppercase;
            letter-spacing: 1px;
            margin-bottom: 4px;
            font-weight: bold;
          }
          .joshila-box p {
            font-size: 0.85rem;
            margin: 0;
            opacity: 0.85;
          }
          @media (max-width: 768px) {
            .joshila-banner {
              margin-top: calc(var(--space-5xl) + 60px);
              padding: 120px var(--space-lg) var(--space-lg);
              text-align: center;
            }
            .joshila-photo {
              left: 50%;
              transform: translateX(-50%);
              bottom: auto;
              top: -100px;
              width: 180px;
              height: 180px;
              border-radius: 50%;
              border: 4px solid var(--color-white);
            }
            .joshila-desc {
              margin: 0 auto;
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

with open('story.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Replace the advisory board section
# Find <section class="section" id="advisory-board"... up to </section>
pattern = r'<!-- OUR ADVISORY BOARD -->\s*<!-- [═]+ -->\s*<section.*?id="advisory-board".*?</section>'
new_text = re.sub(pattern, html_content, text, flags=re.DOTALL)

if text != new_text:
    with open('story.html', 'w', encoding='utf-8') as f:
        f.write(new_text)
    print("Replaced advisory-board with governance section in story.html")
else:
    print("Could not find advisory-board section to replace in story.html")
