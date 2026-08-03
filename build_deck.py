import re

with open('temp_partners.txt', 'r', encoding='utf-8') as f:
    old_html = f.read()

# Extract partners: <img src="...", alt="..."> ... <span class="bento-logo-label">...</span>
partners = []
matches = re.finditer(r'<img\s+src="([^"]+)"\s+alt="([^"]+)"[^>]*>[\s\S]*?<span class="bento-logo-label">([^<]+)</span>', old_html)
for m in matches:
    img_src = m.group(1)
    alt_text = m.group(2)
    label = m.group(3).strip()
    # Check for categories by looking back
    # But it's easier to just list them here since there are 19
    partners.append({"src": img_src, "label": label})

# Ensure uniqueness
seen = set()
unique_partners = []
for p in partners:
    if p['src'] not in seen:
        unique_partners.append(p)
        seen.add(p['src'])

# Build the new HTML
new_html = """
    <!-- PARTNERS SECTION -->
    <section class="section" id="partners" aria-label="Our Partners" style="background-color: #F8FAFC; padding: 6rem 0; position: relative; overflow: hidden;">
      <div class="container" style="max-width: 1280px; margin: 0 auto; padding: 0 1.5rem; position: relative; z-index: 2;">
        
        <div class="section-header reveal" style="text-align: center; margin-bottom: 4rem;">
          <h2 style="font-family: var(--font-heading); font-size: clamp(2.5rem, 5vw, 3.8rem); font-weight: 800; color: var(--color-charcoal); margin-bottom: 1rem; line-height: 1.15;">
            Our Partners<br>
            <span class="doodle-highlight" style="color: var(--color-teal); font-size: clamp(2rem, 4vw, 3rem);">Partners Along the Way</span>
          </h2>
          <p style="max-width: 850px; margin: 0 auto; font-size: 1.25rem; color: var(--color-text-secondary); line-height: 1.7; font-weight: 400;">
            At Kshamtalaya, we believe that wellbeing is nurtured in relationships — through collaboration, learning, and shared intent. Our collaborations — with knowledge institutions, training organizations, and collective platforms — have helped bring the language of wellbeing into diverse spaces: from classrooms and communities to workplaces and leadership programs.
          </p>
        </div>

        <style>
          .deck-wrapper {
            position: relative;
            width: 100%;
            height: 450px;
            display: flex;
            justify-content: center;
            align-items: center;
            perspective: 1200px;
            touch-action: pan-y;
            margin-bottom: 3rem;
          }
          .deck-card {
            position: absolute;
            width: 320px;
            height: 420px;
            background: #FFFFFF;
            border-radius: 24px;
            box-shadow: 0 20px 40px rgba(0,0,0,0.1), 0 0 0 1px rgba(0,0,0,0.05);
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            padding: 2.5rem;
            text-align: center;
            transition: transform 0.6s cubic-bezier(0.2, 0.8, 0.2, 1), opacity 0.6s ease;
            transform-origin: center bottom;
            user-select: none;
            will-change: transform, opacity;
            cursor: grab;
          }
          .deck-card:active {
            cursor: grabbing;
          }
          .deck-card.is-dragging {
            transition: none; /* Instant follow finger */
          }
          .deck-card.swipe-left {
            transform: translate3d(-150%, 0, 0) rotateZ(-30deg) !important;
            opacity: 0 !important;
          }
          .deck-card.swipe-right {
            transform: translate3d(150%, 0, 0) rotateZ(30deg) !important;
            opacity: 0 !important;
          }
          .deck-logo {
            max-width: 180px;
            max-height: 140px;
            object-fit: contain;
            margin-bottom: 2rem;
            filter: grayscale(10%) contrast(1.1);
            transition: filter 0.3s ease, transform 0.3s ease;
          }
          .deck-card:hover .deck-logo {
            filter: grayscale(0%) contrast(1);
            transform: scale(1.05);
          }
          .deck-label {
            font-family: var(--font-heading);
            font-size: 1.4rem;
            font-weight: 800;
            color: var(--color-charcoal);
            line-height: 1.2;
          }
          .deck-controls {
            display: flex;
            justify-content: center;
            gap: 1.5rem;
            margin-top: 2rem;
          }
          .deck-btn {
            width: 56px;
            height: 56px;
            border-radius: 50%;
            border: 2px solid rgba(8, 185, 219, 0.2);
            background: #FFFFFF;
            color: var(--color-teal);
            display: flex;
            align-items: center;
            justify-content: center;
            cursor: pointer;
            transition: all 0.3s ease;
            box-shadow: 0 4px 15px rgba(0,0,0,0.05);
          }
          .deck-btn:hover {
            background: var(--color-teal);
            color: #FFFFFF;
            transform: scale(1.1);
            box-shadow: 0 10px 25px rgba(8, 185, 219, 0.3);
          }
          .deck-btn svg {
            width: 24px;
            height: 24px;
            fill: none;
            stroke: currentColor;
            stroke-width: 2.5;
            stroke-linecap: round;
            stroke-linejoin: round;
          }
          
          /* The premium quote at the bottom */
          .premium-quote {
            background: linear-gradient(135deg, rgba(8, 185, 219, 0.05) 0%, rgba(58, 150, 170, 0.08) 100%);
            border: 1px solid rgba(8, 185, 219, 0.15);
            border-radius: 24px;
            padding: 3rem 2rem;
            text-align: center;
            max-width: 900px;
            margin: 4rem auto 0;
          }
          .premium-quote p {
            font-family: var(--font-heading);
            font-size: clamp(1.4rem, 3vw, 1.8rem);
            color: var(--color-charcoal);
            line-height: 1.5;
            margin: 0;
            font-weight: 600;
          }
          .premium-quote strong {
            color: var(--color-teal-dark);
            font-weight: 800;
          }
        </style>

        <div class="deck-wrapper" id="partner-deck">
"""

for i, p in enumerate(unique_partners):
    new_html += f"""
          <div class="deck-card" data-index="{i}">
            <img src="{p['src']}" alt="{p['label']}" class="deck-logo" draggable="false" loading="lazy" />
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
            card.classList.remove('swipe-left', 'swipe-right', 'is-dragging');
            card.style.transform = '';
            
            if (index === 0) {
              card.style.zIndex = cards.length;
              card.style.transform = `translate3d(0, 0, 0) scale(1)`;
              card.style.opacity = '1';
              card.style.pointerEvents = 'auto';
            } else if (index === 1) {
              card.style.zIndex = cards.length - 1;
              card.style.transform = `translate3d(0, 15px, -50px) scale(0.95)`;
              card.style.opacity = '0.9';
              card.style.pointerEvents = 'none';
            } else if (index === 2) {
              card.style.zIndex = cards.length - 2;
              card.style.transform = `translate3d(0, 30px, -100px) scale(0.9)`;
              card.style.opacity = '0.7';
              card.style.pointerEvents = 'none';
            } else {
              card.style.zIndex = 0;
              card.style.transform = `translate3d(0, 45px, -150px) scale(0.85)`;
              card.style.opacity = '0';
              card.style.pointerEvents = 'none';
            }
          });
        }

        function swipeCard(direction) {
          if (cards.length === 0) return;
          const card = cards.shift(); // Remove top card
          card.classList.add(direction === 'left' ? 'swipe-left' : 'swipe-right');
          
          setTimeout(() => {
            cards.push(card); // Move to back
            updateDeck();
          }, 400); // Wait for CSS transition
        }
        
        function swipeCardReverse() {
           if (cards.length === 0) return;
           const card = cards.pop(); // Remove bottom card
           card.style.transition = 'none';
           card.classList.add('swipe-left'); // start off screen
           cards.unshift(card); // Move to front
           
           // force reflow
           void card.offsetWidth;
           
           card.style.transition = 'transform 0.6s cubic-bezier(0.2, 0.8, 0.2, 1), opacity 0.6s ease';
           updateDeck();
        }

        // Pointer Events for Dragging
        deck.addEventListener('pointerdown', (e) => {
          if (e.target.closest('.deck-btn')) return;
          const topCard = cards[0];
          if (!topCard || !topCard.contains(e.target)) return;
          
          isDragging = true;
          startX = e.clientX;
          activeCard = topCard;
          activeCard.classList.add('is-dragging');
          deck.style.cursor = 'grabbing';
          pauseAutoPlay();
        });

        window.addEventListener('pointermove', (e) => {
          if (!isDragging || !activeCard) return;
          currentX = e.clientX - startX;
          const rotate = currentX * 0.05;
          activeCard.style.transform = `translate3d(${currentX}px, 0, 0) rotateZ(${rotate}deg)`;
        });

        window.addEventListener('pointerup', () => {
          if (!isDragging || !activeCard) return;
          isDragging = false;
          activeCard.classList.remove('is-dragging');
          deck.style.cursor = 'default';
          
          const threshold = window.innerWidth > 768 ? 150 : 80;
          if (currentX > threshold) {
            swipeCard('right');
          } else if (currentX < -threshold) {
            swipeCard('left');
          } else {
            // Snap back
            activeCard.style.transform = `translate3d(0, 0, 0) scale(1)`;
          }
          currentX = 0;
          activeCard = null;
          startAutoPlay();
        });
        
        // Touch events explicitly (in case pointer events are flaky on some mobiles)
        deck.addEventListener('touchstart', pauseAutoPlay, {passive: true});
        deck.addEventListener('touchend', startAutoPlay, {passive: true});
        deck.addEventListener('mouseenter', pauseAutoPlay);
        deck.addEventListener('mouseleave', startAutoPlay);

        // Buttons
        document.getElementById('deck-next').addEventListener('click', () => swipeCard('right'));
        document.getElementById('deck-prev').addEventListener('click', () => swipeCardReverse());

        // Auto Play
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

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Replace the old partners section
# We have to find <section class="section" id="partners"...> ... </section>
pattern = r'(<section[^>]*id="partners"[^>]*>[\s\S]*?</section>)'
new_text = re.sub(pattern, new_html, text, flags=re.IGNORECASE)

if new_text != text:
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(new_text)
    print("Successfully replaced partners section in index.html!")
else:
    print("Could not find the partners section in index.html using regex.")
