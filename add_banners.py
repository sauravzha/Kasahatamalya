import re

new_sections = """
    <!-- ════════════════════════════════════════ -->
    <!-- CTA BANNER                               -->
    <!-- ════════════════════════════════════════ -->
    <section class="section" aria-label="Call to Action" style="background-color: #0E4856; padding: 4rem 0;">
      <div class="container" style="display: flex; justify-content: center; gap: 2rem; flex-wrap: wrap;">
        <a href="/press.html" class="btn" style="background-color: white; color: #0E4856; padding: 1rem 2rem; border-radius: 4px; font-weight: 800; font-size: 1.25rem; text-decoration: none; box-shadow: 0 4px 6px rgba(0,0,0,0.1);">Read our Impact Report</a>
        <a href="/story.html" class="btn" style="background-color: transparent; color: white; border: 2px solid rgba(255,255,255,0.5); padding: 1rem 2rem; border-radius: 4px; font-weight: 800; font-size: 1.25rem; text-decoration: none; transition: all 0.3s;" onmouseover="this.style.backgroundColor='rgba(255,255,255,0.1)';" onmouseout="this.style.backgroundColor='transparent';">See how we work</a>
      </div>
    </section>

    <!-- ════════════════════════════════════════ -->
    <!-- MEANING BANNER                           -->
    <!-- ════════════════════════════════════════ -->
    <section class="section" aria-label="Meaning of Kshamtalaya" style="background-color: #EFEDE3; padding: 5rem 0; border-bottom: 1px solid rgba(0,0,0,0.05);">
      <div class="container" style="max-width: 1100px; margin: 0 auto;">
        <div style="display: flex; align-items: center; justify-content: space-between; text-align: center; gap: 1rem; flex-wrap: wrap;">
          
          <div style="flex: 1; min-width: 250px;">
            <h2 style="font-size: 3rem; color: #0C4957; margin-bottom: 0.5rem; font-family: var(--font-heading); font-weight: 800;">क्षमता</h2>
            <div style="font-size: 0.95rem; font-weight: 800; color: #C5881D; letter-spacing: 2px; margin-bottom: 1rem; text-transform: uppercase;">Kshamta</div>
            <p style="font-size: 1.05rem; color: #4A5568; line-height: 1.5; margin: 0 auto; max-width: 250px; font-weight: 500;">Potential. What every child already walks in with.</p>
          </div>

          <div style="font-size: 2.5rem; color: #52BCE5; font-weight: 300;">+</div>

          <div style="flex: 1; min-width: 250px;">
            <h2 style="font-size: 3rem; color: #0C4957; margin-bottom: 0.5rem; font-family: var(--font-heading); font-weight: 800;">आलय</h2>
            <div style="font-size: 0.95rem; font-weight: 800; color: #C5881D; letter-spacing: 2px; margin-bottom: 1rem; text-transform: uppercase;">Aalaya</div>
            <p style="font-size: 1.05rem; color: #4A5568; line-height: 1.5; margin: 0 auto; max-width: 250px; font-weight: 500;">A home. A place that holds you while you grow.</p>
          </div>

          <div style="font-size: 2.5rem; color: #52BCE5; font-weight: 300;">=</div>

          <div style="flex: 1; min-width: 250px;">
            <h2 style="font-size: 3rem; color: #0C4957; margin-bottom: 0.5rem; font-family: var(--font-heading); font-weight: 800;">क्षमतालय</h2>
            <div style="font-size: 0.95rem; font-weight: 800; color: #C5881D; letter-spacing: 2px; margin-bottom: 1rem; text-transform: uppercase;">Kshamtalaya</div>
            <p style="font-size: 1.05rem; color: #4A5568; line-height: 1.5; margin: 0 auto; max-width: 250px; font-weight: 500;">Where potential finds a home.</p>
          </div>

        </div>
      </div>
    </section>

"""

def process_file():
    with open('index.html', 'r', encoding='utf-8') as f:
        text = f.read()

    # 1. Remove the text link from the hero paragraph
    text = text.replace('<br/><br/><a href="/press.html" style="font-weight:700; color:var(--color-teal); text-decoration:underline;">Read our impact report and see how we work-</a>', '')

    # 2. Insert the new sections before <section class="stats section"
    if '<section class="stats section"' in text:
        text = text.replace('<section class="stats section"', new_sections + '    <section class="stats section"')
        with open('index.html', 'w', encoding='utf-8') as f:
            f.write(text)
        print("Updated index.html successfully.")
    else:
        print("Could not find stats section marker.")

process_file()
