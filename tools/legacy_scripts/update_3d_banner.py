import re

updated_banner = """
    <!-- ════════════════════════════════════════ -->
    <!-- MEANING BANNER                           -->
    <!-- ════════════════════════════════════════ -->
    <style>
      @keyframes float-3d {
        0% { transform: translateY(0) rotateX(0) rotateY(0); }
        50% { transform: translateY(-12px) rotateX(8deg) rotateY(-8deg); }
        100% { transform: translateY(0) rotateX(0) rotateY(0); }
      }
      @keyframes glow-pulse {
        0% { text-shadow: 0 4px 15px rgba(12, 73, 87, 0.2), 0 1px 3px rgba(12,73,87,0.3); }
        50% { text-shadow: 0 12px 30px rgba(12, 73, 87, 0.5), 0 4px 10px rgba(12,73,87,0.6); }
        100% { text-shadow: 0 4px 15px rgba(12, 73, 87, 0.2), 0 1px 3px rgba(12,73,87,0.3); }
      }
      @keyframes symbol-glow {
        0% { text-shadow: 0 0 10px rgba(82, 188, 229, 0.4); transform: translateY(0) scale(1); }
        50% { text-shadow: 0 0 25px rgba(82, 188, 229, 0.8); transform: translateY(-8px) scale(1.15); }
        100% { text-shadow: 0 0 10px rgba(82, 188, 229, 0.4); transform: translateY(0) scale(1); }
      }
      .meaning-card {
        flex: 1;
        min-width: 250px;
        animation: float-3d 6s ease-in-out infinite;
        perspective: 1000px;
        transform-style: preserve-3d;
      }
      .meaning-card:nth-child(3) { animation-delay: 1.5s; }
      .meaning-card:nth-child(5) { animation-delay: 3s; }
      
      .meaning-hindi {
        font-size: 3.8rem; 
        color: #0C4957; 
        margin-bottom: 0.5rem; 
        font-family: var(--font-heading); 
        font-weight: 800;
        animation: glow-pulse 4s ease-in-out infinite;
        transform: translateZ(30px);
        display: inline-block;
      }
      .meaning-symbol {
        font-size: 3.5rem; 
        color: #52BCE5; 
        font-weight: 300;
        animation: symbol-glow 4s ease-in-out infinite;
        display: inline-block;
      }
      .meaning-english {
        font-size: 1rem; 
        font-weight: 800; 
        color: #C5881D; 
        letter-spacing: 3px; 
        margin-bottom: 1rem; 
        text-transform: uppercase;
        transform: translateZ(15px);
        display: block;
      }
      .meaning-desc {
        font-size: 1.1rem; 
        color: #4A5568; 
        line-height: 1.5; 
        margin: 0 auto; 
        max-width: 250px; 
        font-weight: 500;
        transform: translateZ(5px);
      }
    </style>
    <section class="section" aria-label="Meaning of Kshamtalaya" style="background-color: #FFFFFF; padding: 6rem 0; border-bottom: 1px solid rgba(0,0,0,0.05); overflow: hidden;">
      <div class="container" style="max-width: 1200px; margin: 0 auto; perspective: 1500px;">
        <div style="display: flex; align-items: center; justify-content: space-between; text-align: center; gap: 1rem; flex-wrap: wrap; transform-style: preserve-3d;">
          
          <div class="meaning-card">
            <h2 class="meaning-hindi">क्षमता</h2>
            <div class="meaning-english">Kshamta</div>
            <p class="meaning-desc">Potential. What every child already walks in with.</p>
          </div>

          <div class="meaning-symbol">+</div>

          <div class="meaning-card">
            <h2 class="meaning-hindi">आलय</h2>
            <div class="meaning-english">Aalaya</div>
            <p class="meaning-desc">A home. A place that holds you while you grow.</p>
          </div>

          <div class="meaning-symbol">=</div>

          <div class="meaning-card">
            <h2 class="meaning-hindi">क्षमतालय</h2>
            <div class="meaning-english">Kshamtalaya</div>
            <p class="meaning-desc">Where potential finds a home.</p>
          </div>

        </div>
      </div>
    </section>
"""

def update_banner():
    with open('index.html', 'r', encoding='utf-8') as f:
        text = f.read()

    # The current meaning banner starts with:
    # <!-- ════════════════════════════════════════ -->
    # <!-- MEANING BANNER                           -->
    # <!-- ════════════════════════════════════════ -->
    # <section class="section" aria-label="Meaning of Kshamtalaya"
    
    # Let's match from <!-- MEANING BANNER to the end of its <section>
    pattern = r'<!-- ════════════════════════════════════════ -->\s*<!-- MEANING BANNER\s*-->\s*<!-- ════════════════════════════════════════ -->\s*<section class="section" aria-label="Meaning of Kshamtalaya"[\s\S]*?</section>'
    
    new_text = re.sub(pattern, updated_banner.strip(), text)
    
    if text != new_text:
        with open('index.html', 'w', encoding='utf-8') as f:
            f.write(new_text)
        print("Updated the Meaning Banner successfully.")
    else:
        print("Could not find the Meaning Banner to replace.")

update_banner()
