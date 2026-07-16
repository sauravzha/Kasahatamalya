import re

# We will modify index.html to include the two diagrams

mission_section = '''
    <!-- ════════════════════════════════════════ -->
    <!-- OUR MISSION                              -->
    <!-- ════════════════════════════════════════ -->
    <section class="section section--cream" id="mission" aria-label="Our Mission">
      <div class="container">
        <div class="section-header reveal" style="text-align: center;">
          <div class="section-header__eyebrow">Our Mission</div>
          <h2 class="section-header__title">The Child at the <span class="doodle-highlight" style="color: var(--color-teal);">Center</span></h2>
          <img src="/assets/mission.png" alt="Our Mission Diagram" style="width: 100%; max-width: 900px; height: auto; margin: 3rem auto 0; display: block; border-radius: 16px; box-shadow: 0 10px 30px rgba(0,0,0,0.05);" />
        </div>
      </div>
    </section>
'''

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace pic2.jpg in Our Approach with approach.png
content = content.replace('src="/assets/photos/pic2.jpg"', 'src="/assets/approach.png"')

# Insert Mission section before Approach section
# Approach section starts with <!-- OUR APPROACH --> or <section class="section doodle-bg" id="approach"
content = content.replace('<section class="section doodle-bg" id="approach"', mission_section + '\n    <section class="section doodle-bg" id="approach"')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Added placeholders for approach.png and mission.png")
