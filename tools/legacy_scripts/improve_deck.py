import re

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

# 1. Replace the deck styles
old_style = re.search(r'(<style>\s*\.deck-wrapper.*?)(?=<div class="deck-wrapper")', text, re.DOTALL)

new_style = """<style>
          .deck-wrapper {
            position: relative;
            width: 100%;
            height: 550px;
            display: flex;
            justify-content: center;
            align-items: center;
            perspective: 1500px;
            touch-action: pan-y;
            margin-bottom: 3rem;
          }
          /* Ambient glowing backdrop behind the deck */
          .deck-wrapper::before {
            content: '';
            position: absolute;
            width: 400px;
            height: 400px;
            background: radial-gradient(circle, rgba(8, 185, 219, 0.2) 0%, rgba(255,199,44,0.1) 50%, rgba(255,255,255,0) 80%);
            border-radius: 50%;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            z-index: 0;
            pointer-events: none;
            filter: blur(40px);
          }
          
          .deck-card {
            position: absolute;
            width: 340px;
            height: 460px;
            background: linear-gradient(135deg, #ffffff 0%, #f8fafc 100%);
            border-radius: 32px;
            box-shadow: 0 30px 60px -15px rgba(0,0,0,0.15), 0 0 0 1px rgba(8, 185, 219, 0.15);
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            padding: 2.5rem;
            text-align: center;
            transition: transform 0.6s cubic-bezier(0.2, 0.8, 0.2, 1), opacity 0.6s ease, box-shadow 0.3s ease;
            transform-origin: center bottom;
            user-select: none;
            will-change: transform, opacity;
            cursor: grab;
            overflow: hidden;
          }
          
          /* Glassmorphic shine on the card */
          .deck-card::after {
             content: '';
             position: absolute;
             top: 0; left: 0; right: 0; height: 50%;
             background: linear-gradient(180deg, rgba(255,255,255,0.8) 0%, rgba(255,255,255,0) 100%);
             pointer-events: none;
          }

          .deck-card:active {
            cursor: grabbing;
            box-shadow: 0 15px 30px -10px rgba(0,0,0,0.1), 0 0 0 2px rgba(8, 185, 219, 0.3);
          }
          .deck-card.is-dragging {
            transition: none; /* Instant follow finger */
          }
          .deck-card.snap-back {
            transition: transform 0.6s cubic-bezier(0.34, 1.56, 0.64, 1);
          }
          .deck-card.swipe-left {
            transform: translate3d(-150%, 50px, 0) rotateZ(-35deg) !important;
            opacity: 0 !important;
          }
          .deck-card.swipe-right {
            transform: translate3d(150%, 50px, 0) rotateZ(35deg) !important;
            opacity: 0 !important;
          }
          .deck-logo {
            max-width: 200px;
            max-height: 160px;
            object-fit: contain;
            margin-bottom: 2.5rem;
            filter: grayscale(20%) contrast(1.05);
            transition: filter 0.4s ease, transform 0.4s cubic-bezier(0.34, 1.56, 0.64, 1);
            position: relative;
            z-index: 2;
          }
          .deck-card:hover .deck-logo {
            filter: grayscale(0%) contrast(1);
            transform: scale(1.1);
          }
          
          .deck-badge {
            position: absolute;
            top: 20px;
            left: 50%;
            transform: translateX(-50%);
            background: rgba(8, 185, 219, 0.1);
            color: var(--color-teal);
            font-size: 0.75rem;
            font-weight: 800;
            letter-spacing: 1px;
            padding: 4px 12px;
            border-radius: 20px;
            text-transform: uppercase;
            z-index: 2;
          }

          .deck-label {
            font-family: var(--font-heading);
            font-size: 1.5rem;
            font-weight: 800;
            color: var(--color-charcoal);
            line-height: 1.2;
            position: relative;
            z-index: 2;
          }
          .deck-controls {
            display: flex;
            justify-content: center;
            gap: 1.5rem;
            margin-top: 2rem;
            position: relative;
            z-index: 10;
          }
          .deck-btn {
            width: 60px;
            height: 60px;
            border-radius: 50%;
            border: 2px solid rgba(8, 185, 219, 0.2);
            background: rgba(255, 255, 255, 0.8);
            backdrop-filter: blur(10px);
            color: var(--color-teal);
            display: flex;
            align-items: center;
            justify-content: center;
            cursor: pointer;
            transition: all 0.3s cubic-bezier(0.34, 1.56, 0.64, 1);
            box-shadow: 0 8px 25px rgba(0,0,0,0.06);
          }
          .deck-btn:hover {
            background: var(--color-teal);
            color: #FFFFFF;
            transform: translateY(-4px) scale(1.05);
            box-shadow: 0 15px 35px rgba(8, 185, 219, 0.3);
            border-color: var(--color-teal);
          }
          .deck-btn svg {
            width: 26px;
            height: 26px;
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
            padding: 3.5rem 2rem;
            text-align: center;
            max-width: 900px;
            margin: 4rem auto 0;
            box-shadow: inset 0 0 20px rgba(255,255,255,0.5);
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
"""

if old_style:
    text = text.replace(old_style.group(1), new_style)

# 2. Add the .deck-badge to every deck-card
# <div class="deck-card" data-index="0">
#   <img src="..." .../>
#   <h3 class="deck-label">...</h3>
# </div>
text = re.sub(
    r'(<div class="deck-card"[^>]*>)\s*(<img)',
    r'\1\n            <div class="deck-badge">Partner</div>\n            \2',
    text
)

# 3. Replace JS for better physics
old_js = re.search(r'(<script>\s*document\.addEventListener\(\'DOMContentLoaded\', \(\) => {[\s\S]*?</script>)', text)

new_js = """<script>
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
            
            if (index === 0) {
              card.style.zIndex = cards.length;
              card.style.transform = `translate3d(0, 0, 0) scale(1) rotateZ(0deg)`;
              card.style.opacity = '1';
              card.style.pointerEvents = 'auto';
              card.style.boxShadow = '0 30px 60px -15px rgba(0,0,0,0.15), 0 0 0 1px rgba(8, 185, 219, 0.15)';
            } else if (index === 1) {
              card.style.zIndex = cards.length - 1;
              card.style.transform = `translate3d(0, 25px, -60px) scale(0.95)`;
              card.style.opacity = '0.9';
              card.style.pointerEvents = 'none';
              card.style.boxShadow = '0 20px 40px -10px rgba(0,0,0,0.1)';
            } else if (index === 2) {
              card.style.zIndex = cards.length - 2;
              card.style.transform = `translate3d(0, 50px, -120px) scale(0.9)`;
              card.style.opacity = '0.7';
              card.style.pointerEvents = 'none';
              card.style.boxShadow = '0 10px 20px -5px rgba(0,0,0,0.05)';
            } else if (index === 3) {
              card.style.zIndex = cards.length - 3;
              card.style.transform = `translate3d(0, 75px, -180px) scale(0.85)`;
              card.style.opacity = '0.4';
              card.style.pointerEvents = 'none';
            } else {
              card.style.zIndex = 0;
              card.style.transform = `translate3d(0, 100px, -240px) scale(0.8)`;
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
           
           card.style.transition = 'transform 0.6s cubic-bezier(0.2, 0.8, 0.2, 1), opacity 0.6s ease';
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
          
          // Slight lift when grabbed
          activeCard.style.transform = `translate3d(0, -10px, 0) scale(1.02)`;
        });

        window.addEventListener('pointermove', (e) => {
          if (!isDragging || !activeCard) return;
          currentX = e.clientX - startX;
          const rotate = currentX * 0.08; 
          activeCard.style.transform = `translate3d(${currentX}px, -10px, 0) rotateZ(${rotate}deg) scale(1.02)`;
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
            // Snap back with spring
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
    </script>"""

if old_js:
    text = text.replace(old_js.group(1), new_js)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(text)

print("Deck improved successfully!")
