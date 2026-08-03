import re

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Extract partners from the current index.html deck
partners = []
matches = re.finditer(r'<img src="([^"]+)" alt="([^"]+)" class="deck-logo"[^>]*>\s*<h3 class="deck-label">([^<]+)</h3>', text)
for m in matches:
    partners.append({"src": m.group(1), "label": m.group(3).strip()})

if not partners:
    print("Could not find partners in index.html to rebuild.")
    exit(1)

# Ensure uniqueness
seen = set()
unique_partners = []
for p in partners:
    if p['src'] not in seen:
        unique_partners.append(p)
        seen.add(p['src'])

new_html = """
    <!-- PARTNERS SECTION -->
    <section class="section" id="partners" aria-label="Our Partners" style="background-color: #0B1120; padding: 6rem 0; position: relative; overflow: hidden;">
      
      <!-- Ambient dark background effects -->
      <div style="position: absolute; top: -20%; left: -10%; width: 50%; height: 60%; background: radial-gradient(circle, rgba(8, 185, 219, 0.1) 0%, transparent 70%); filter: blur(60px); pointer-events: none;"></div>
      <div style="position: absolute; bottom: -20%; right: -10%; width: 50%; height: 60%; background: radial-gradient(circle, rgba(255, 199, 44, 0.08) 0%, transparent 70%); filter: blur(60px); pointer-events: none;"></div>
      
      <div class="container" style="max-width: 1280px; margin: 0 auto; padding: 0 1.5rem; position: relative; z-index: 2;">
        
        <div class="section-header reveal" style="text-align: center; margin-bottom: 4rem;">
          <h2 style="font-family: var(--font-heading); font-size: clamp(2.5rem, 5vw, 3.8rem); font-weight: 800; color: #FFFFFF; margin-bottom: 1rem; line-height: 1.15;">
            Our Partners<br>
            <span style="color: var(--color-teal); font-size: clamp(2rem, 4vw, 3rem);">Partners Along the Way</span>
          </h2>
          <p style="max-width: 850px; margin: 0 auto; font-size: 1.25rem; color: rgba(255,255,255,0.7); line-height: 1.7; font-weight: 400;">
            At Kshamtalaya, we believe that wellbeing is nurtured in relationships — through collaboration, learning, and shared intent. Our collaborations — with knowledge institutions, training organizations, and collective platforms — have helped bring the language of wellbeing into diverse spaces: from classrooms and communities to workplaces and leadership programs.
          </p>
        </div>

        <style>
          .deck-wrapper {
            position: relative;
            width: 100%;
            height: 550px;
            display: flex;
            justify-content: center;
            align-items: center;
            perspective: 2000px;
            transform-style: preserve-3d;
            touch-action: pan-y;
            margin-bottom: 3rem;
          }
          
          .deck-card {
            position: absolute;
            width: 320px;
            height: 450px;
            background: linear-gradient(145deg, rgba(30, 41, 59, 0.95) 0%, rgba(15, 23, 42, 0.95) 100%);
            backdrop-filter: blur(20px);
            border: 1px solid rgba(255, 255, 255, 0.1);
            border-radius: 30px;
            box-shadow: 
              0 30px 60px rgba(0,0,0,0.5),
              inset 0 1px 0 rgba(255,255,255,0.2);
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            padding: 2.5rem;
            text-align: center;
            transition: transform 0.8s cubic-bezier(0.2, 1, 0.3, 1), opacity 0.8s ease;
            transform-origin: center 150%;
            cursor: grab;
            overflow: hidden;
            will-change: transform, opacity;
          }

          /* A nice glowing orb inside the dark card */
          .deck-card::before {
            content: '';
            position: absolute;
            top: -50%;
            left: -50%;
            width: 200%;
            height: 200%;
            background: radial-gradient(circle at 50% 50%, rgba(8, 185, 219, 0.15) 0%, transparent 60%);
            pointer-events: none;
          }

          .deck-card:active {
            cursor: grabbing;
          }
          .deck-card.is-dragging {
            transition: none;
          }
          .deck-card.snap-back {
            transition: transform 0.6s cubic-bezier(0.34, 1.56, 0.64, 1);
          }
          .deck-card.swipe-left {
            transform: translate3d(-150%, 50px, 0) rotateZ(-30deg) !important;
            opacity: 0 !important;
          }
          .deck-card.swipe-right {
            transform: translate3d(150%, 50px, 0) rotateZ(30deg) !important;
            opacity: 0 !important;
          }

          /* Logo container with white background to handle varying partner logos gracefully */
          .deck-logo-wrapper {
            width: 170px;
            height: 170px;
            background: #ffffff;
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            box-shadow: 0 15px 35px rgba(0,0,0,0.3), inset 0 4px 10px rgba(0,0,0,0.05);
            margin-bottom: 2rem;
            padding: 1.5rem;
            position: relative;
            z-index: 2;
            border: 4px solid rgba(255,255,255,0.05);
            transition: transform 0.4s cubic-bezier(0.2, 1, 0.3, 1);
          }

          .deck-logo {
            max-width: 100%;
            max-height: 100%;
            object-fit: contain;
          }

          .deck-card:hover .deck-logo-wrapper {
            transform: scale(1.1) translateY(-10px);
            box-shadow: 0 25px 45px rgba(8, 185, 219, 0.3), inset 0 4px 10px rgba(0,0,0,0.05);
          }

          .deck-label {
            font-family: var(--font-heading);
            font-size: 1.5rem;
            font-weight: 800;
            color: #ffffff;
            line-height: 1.2;
            position: relative;
            z-index: 2;
            letter-spacing: 0.5px;
          }
          
          .deck-badge {
            position: absolute;
            top: 20px;
            left: 50%;
            transform: translateX(-50%);
            background: rgba(255, 255, 255, 0.1);
            color: #FFC72C;
            font-size: 0.75rem;
            font-weight: 800;
            letter-spacing: 2px;
            padding: 6px 16px;
            border-radius: 20px;
            text-transform: uppercase;
            z-index: 2;
            border: 1px solid rgba(255, 255, 255, 0.2);
            backdrop-filter: blur(10px);
          }

          .deck-controls {
            display: flex;
            justify-content: center;
            gap: 1.5rem;
            margin-top: 1rem;
            position: relative;
            z-index: 10;
          }
          .deck-btn {
            width: 64px;
            height: 64px;
            border-radius: 50%;
            border: 1px solid rgba(255, 255, 255, 0.2);
            background: rgba(255, 255, 255, 0.05);
            backdrop-filter: blur(10px);
            color: #FFFFFF;
            display: flex;
            align-items: center;
            justify-content: center;
            cursor: pointer;
            transition: all 0.4s cubic-bezier(0.2, 1, 0.3, 1);
          }
          .deck-btn:hover {
            background: var(--color-teal);
            border-color: var(--color-teal);
            transform: translateY(-5px);
            box-shadow: 0 15px 30px rgba(8, 185, 219, 0.4);
          }
          .deck-btn svg {
            width: 28px;
            height: 28px;
            fill: none;
            stroke: currentColor;
            stroke-width: 2;
            stroke-linecap: round;
            stroke-linejoin: round;
          }
          
          /* The premium quote at the bottom */
          .premium-quote {
            background: linear-gradient(135deg, rgba(8, 185, 219, 0.1) 0%, rgba(30, 41, 59, 0.5) 100%);
            border: 1px solid rgba(8, 185, 219, 0.2);
            border-radius: 24px;
            padding: 3.5rem 2rem;
            text-align: center;
            max-width: 900px;
            margin: 4rem auto 0;
            backdrop-filter: blur(10px);
          }
          .premium-quote p {
            font-family: var(--font-heading);
            font-size: clamp(1.4rem, 3vw, 1.8rem);
            color: #FFFFFF;
            line-height: 1.5;
            margin: 0;
            font-weight: 500;
          }
          .premium-quote strong {
            color: #FFC72C;
            font-weight: 800;
          }
        </style>

        <div class="deck-wrapper" id="partner-deck">
"""

for i, p in enumerate(unique_partners):
    new_html += f"""
          <div class="deck-card" data-index="{i}">
            <div class="deck-badge">Partner</div>
            <div class="deck-logo-wrapper">
              <img src="{p['src']}" alt="{p['label']}" class="deck-logo" draggable="false" loading="lazy" />
            </div>
            <h3 class="deck-label">{p['label']}</h3>
          </div>
"""

new_html += """
        </div>

        <div class="deck-controls reveal">
          <button class="deck-btn" id="deck-prev" aria-label="Previous Partner">
            <svg viewBox="0 0 24 24"><path d="M19 12H5M12 19l-7-7 7-7"/></svg>
          </button>
          <button class="deck-btn" id="deck-next" aria-label="Next Partner">
            <svg viewBox="0 0 24 24"><path d="M5 12h14M12 5l7 7-7 7"/></svg>
          </button>
        </div>

        <div class="premium-quote reveal">
          <p>Each partnership has been an opportunity to listen, learn, and grow together &#8212; reaffirming that wellbeing is not an individual pursuit, but a <strong>collective responsibility</strong>.</p>
        </div>

      </div>
    </section>

    <script>
      document.addEventListener('DOMContentLoaded', () => {
        const deck = document.getElementById('partner-deck');
        if(!deck) return;
        
        let cards = Array.from(deck.querySelectorAll('.deck-card'));
        let isDragging = false;
        let startX = 0;
        let currentX = 0;
        let activeCard = null;
        let autoPlayInterval = null;

        function updateDeck() {
          cards.forEach((card, index) => {
            card.classList.remove('swipe-left', 'swipe-right', 'is-dragging', 'snap-back');
            card.style.transform = '';
            
            // Scatter the cards slightly for a messy, organic deck look
            if (index === 0) {
              card.style.zIndex = cards.length;
              card.style.transform = `translate3d(0, 0, 0) rotateZ(0deg) scale(1)`;
              card.style.opacity = '1';
              card.style.pointerEvents = 'auto';
            } else if (index === 1) {
              card.style.zIndex = cards.length - 1;
              card.style.transform = `translate3d(15px, 20px, -40px) rotateZ(3deg) scale(0.95)`;
              card.style.opacity = '0.9';
              card.style.pointerEvents = 'none';
            } else if (index === 2) {
              card.style.zIndex = cards.length - 2;
              card.style.transform = `translate3d(-15px, 40px, -80px) rotateZ(-3deg) scale(0.9)`;
              card.style.opacity = '0.75';
              card.style.pointerEvents = 'none';
            } else if (index === 3) {
              card.style.zIndex = cards.length - 3;
              card.style.transform = `translate3d(15px, 60px, -120px) rotateZ(2deg) scale(0.85)`;
              card.style.opacity = '0.5';
              card.style.pointerEvents = 'none';
            } else {
              card.style.zIndex = 0;
              card.style.transform = `translate3d(0, 80px, -160px) rotateZ(0deg) scale(0.8)`;
              card.style.opacity = '0';
              card.style.pointerEvents = 'none';
            }
          });
        }

        function swipeCard(direction) {
          if (cards.length === 0) return;
          const card = cards.shift(); 
          card.classList.add(direction === 'left' ? 'swipe-left' : 'swipe-right');
          
          setTimeout(() => {
            cards.push(card); 
            updateDeck();
          }, 450); 
        }
        
        function swipeCardReverse() {
           if (cards.length === 0) return;
           const card = cards.pop(); 
           card.style.transition = 'none';
           card.classList.add('swipe-left'); 
           cards.unshift(card); 
           
           void card.offsetWidth; 
           
           card.style.transition = 'transform 0.8s cubic-bezier(0.2, 1, 0.3, 1), opacity 0.8s ease';
           updateDeck();
        }

        deck.addEventListener('pointerdown', (e) => {
          if (e.target.closest('.deck-btn')) return;
          const topCard = cards[0];
          if (!topCard || !topCard.contains(e.target)) return;
          
          isDragging = true;
          startX = e.clientX;
          activeCard = topCard;
          activeCard.classList.remove('snap-back');
          activeCard.classList.add('is-dragging');
          deck.style.cursor = 'grabbing';
          pauseAutoPlay();
          
          activeCard.style.transform = `translate3d(0, -10px, 0) scale(1.05)`;
        });

        window.addEventListener('pointermove', (e) => {
          if (!isDragging || !activeCard) return;
          currentX = e.clientX - startX;
          const rotate = currentX * 0.1; 
          activeCard.style.transform = `translate3d(${currentX}px, -10px, 0) rotateZ(${rotate}deg) scale(1.05)`;
        });

        window.addEventListener('pointerup', () => {
          if (!isDragging || !activeCard) return;
          isDragging = false;
          activeCard.classList.remove('is-dragging');
          deck.style.cursor = 'default';
          
          const threshold = window.innerWidth > 768 ? 120 : 80;
          if (currentX > threshold) {
            swipeCard('right');
          } else if (currentX < -threshold) {
            swipeCard('left');
          } else {
            activeCard.classList.add('snap-back');
            activeCard.style.transform = `translate3d(0, 0, 0) scale(1) rotateZ(0deg)`;
          }
          currentX = 0;
          activeCard = null;
          startAutoPlay();
        });
        
        deck.addEventListener('touchstart', pauseAutoPlay, {passive: true});
        deck.addEventListener('touchend', startAutoPlay, {passive: true});
        deck.addEventListener('mouseenter', pauseAutoPlay);
        deck.addEventListener('mouseleave', startAutoPlay);

        document.getElementById('deck-next').addEventListener('click', () => swipeCard('right'));
        document.getElementById('deck-prev').addEventListener('click', () => swipeCardReverse());

        function startAutoPlay() {
          if (autoPlayInterval) clearInterval(autoPlayInterval);
          autoPlayInterval = setInterval(() => {
            swipeCard('left');
          }, 3500);
        }
        function pauseAutoPlay() {
          if (autoPlayInterval) clearInterval(autoPlayInterval);
        }

        updateDeck();
        startAutoPlay();
      });
    </script>
"""

pattern = r'(<section[^>]*id="partners"[^>]*>[\s\S]*?</script>)'
new_text = re.sub(pattern, new_html, text, flags=re.IGNORECASE)

if new_text != text:
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(new_text)
    print("Successfully upgraded partners deck to ULTRA PREMIUM in index.html!")
else:
    print("Could not find the partners section in index.html using regex.")
