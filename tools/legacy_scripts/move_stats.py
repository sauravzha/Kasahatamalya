import re

# The new HTML block to insert into story.html
new_stats_html = """
    <!-- ════════════════════════════════════════ -->
    <!-- 10 YEARS IMPACT STATS                    -->
    <!-- ════════════════════════════════════════ -->
    <section class="section section--cream" id="ten-year-impact" style="background: linear-gradient(180deg, #FFFFFF 0%, #F9FAFB 100%); padding: 5rem 0 2rem 0;">
      <div class="container text-center">
        <div class="section-header__eyebrow reveal" style="background: rgba(82, 188, 229, 0.15); color: var(--color-teal-dark); font-weight: 700;">Our Reach Over 10 Years</div>
        <h2 class="reveal" style="margin-bottom: 3rem; font-size: 2.5rem; color: var(--color-charcoal); font-weight: 800;">
          KF Reach in 2025–26 <span style="color: var(--color-teal); font-weight: 600;">(3 States)</span>
        </h2>
        
        <style>
          .impact-grid-10yr {
            display: grid;
            grid-template-columns: repeat(5, 1fr);
            gap: 1.5rem;
          }
          @media (max-width: 1100px) {
            .impact-grid-10yr { grid-template-columns: repeat(3, 1fr); }
          }
          @media (max-width: 768px) {
            .impact-grid-10yr { grid-template-columns: repeat(2, 1fr); }
          }
          @media (max-width: 480px) {
            .impact-grid-10yr { grid-template-columns: 1fr; }
          }
          .impact-card-10yr {
            background: white;
            border-radius: 20px;
            padding: 2rem 1.5rem;
            text-align: center;
            box-shadow: 0 8px 30px rgba(0,0,0,0.04);
            border: 1px solid rgba(0,0,0,0.03);
            transition: all 0.3s ease;
            position: relative;
            overflow: hidden;
          }
          .impact-card-10yr:hover {
            transform: translateY(-8px);
            box-shadow: 0 15px 40px rgba(8,185,219,0.1);
          }
          .impact-card-10yr::before {
            content: ''; position: absolute; top: 0; left: 0; right: 0; height: 5px;
          }
          .impact-icon {
            font-size: 2.5rem;
            margin-bottom: 1rem;
            display: inline-block;
            transition: transform 0.4s ease;
          }
          .impact-card-10yr:hover .impact-icon {
            transform: scale(1.1) rotate(5deg);
          }
          .impact-number {
            font-family: 'Baloo 2', cursive;
            font-size: 2.2rem;
            font-weight: 800;
            line-height: 1.2;
            margin-bottom: 0.5rem;
            color: var(--color-charcoal);
          }
          .impact-label {
            font-size: 0.95rem;
            font-weight: 700;
            color: var(--color-text-secondary);
            text-transform: uppercase;
            letter-spacing: 0.5px;
          }
        </style>

        <div class="impact-grid-10yr reveal">
          <!-- Card 1: Schools -->
          <div class="impact-card-10yr">
            <div style="position:absolute; top:0; left:0; right:0; height:5px; background:linear-gradient(90deg, #08B9DB, #4FB6E8);"></div>
            <div class="impact-icon">🏫</div>
            <div class="impact-number">155</div>
            <div class="impact-label">Schools</div>
          </div>
          <!-- Card 2: Students -->
          <div class="impact-card-10yr">
            <div style="position:absolute; top:0; left:0; right:0; height:5px; background:linear-gradient(90deg, #FF6F59, #FF9080);"></div>
            <div class="impact-icon">👦👧</div>
            <div class="impact-number">3,55,914</div>
            <div class="impact-label">Students Impacted</div>
          </div>
          <!-- Card 3: Fellows -->
          <div class="impact-card-10yr">
            <div style="position:absolute; top:0; left:0; right:0; height:5px; background:linear-gradient(90deg, #1CA6A0, #6DBE45);"></div>
            <div class="impact-icon">🙌</div>
            <div class="impact-number">204</div>
            <div class="impact-label">Fellows</div>
          </div>
          <!-- Card 4: Teachers -->
          <div class="impact-card-10yr">
            <div style="position:absolute; top:0; left:0; right:0; height:5px; background:linear-gradient(90deg, #38B6FF, #08B9DB);"></div>
            <div class="impact-icon">👩‍🏫</div>
            <div class="impact-number">1,59,000</div>
            <div class="impact-label">Teachers Impacted</div>
          </div>
          <!-- Card 5: Parents -->
          <div class="impact-card-10yr">
            <div style="position:absolute; top:0; left:0; right:0; height:5px; background:linear-gradient(90deg, #F2994A, #FFC72C);"></div>
            <div class="impact-icon">👨‍👩‍👧</div>
            <div class="impact-number">79,170</div>
            <div class="impact-label">Parents Impacted</div>
          </div>
        </div>
      </div>
    </section>
"""

def update_files():
    # 1. Remove from index.html
    with open('index.html', 'r', encoding='utf-8') as f:
        idx_text = f.read()

    # We want to remove the PART 1 block.
    # From <!-- ─── PART 1: KF REACH STATS ─── -->
    # up to the closing </div> before <!-- ─── PART 2: ACHIEVEMENT CATEGORIES ─── -->
    pattern = r'\s*<!-- ─── PART 1: KF REACH STATS ─── -->[\s\S]*?(?=<!-- ─── PART 2: ACHIEVEMENT CATEGORIES ─── -->)'
    new_idx_text = re.sub(pattern, '\n        ', idx_text)
    
    if idx_text != new_idx_text:
        with open('index.html', 'w', encoding='utf-8') as f:
            f.write(new_idx_text)
        print("Removed KF Reach Stats from index.html")
    else:
        print("Could not find PART 1 in index.html")

    # 2. Add to story.html
    with open('story.html', 'r', encoding='utf-8') as f:
        story_text = f.read()

    # Find where to insert: right before <!-- OUR APPROACH -->
    insert_target = '    <!-- OUR APPROACH -->'
    if insert_target in story_text and 'KF Reach in 2025–26' not in story_text:
        new_story_text = story_text.replace(insert_target, new_stats_html + '\n' + insert_target)
        with open('story.html', 'w', encoding='utf-8') as f:
            f.write(new_story_text)
        print("Added new consolidated Reach Stats to story.html")
    else:
        print("Target for insertion not found in story.html or already added.")

update_files()
