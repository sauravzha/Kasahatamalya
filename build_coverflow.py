import re

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Extract partners from the current index.html deck
partners = []
# Need to match the current HTML structure (it might be the ultra-premium one)
# <img src="..." alt="..." class="deck-logo"...> ... <h3 class="deck-label">...</h3>
matches = re.finditer(r'<img src="([^"]+)" alt="([^"]+)" class="deck-logo"[^>]*>[\s\S]*?<h3 class="deck-label">([^<]+)</h3>', text)
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
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/swiper@10/swiper-bundle.min.css" />
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
          .partners-swiper {
            width: 100%;
            padding-top: 50px;
            padding-bottom: 50px;
          }

          .swiper-slide {
            background-position: center;
            background-size: cover;
            width: 300px;
            height: 400px;
            background: #ffffff;
            border-radius: 24px;
            box-shadow: 0 15px 35px rgba(0,0,0,0.08), 0 5px 15px rgba(0,0,0,0.04);
            border: 1px solid rgba(0,0,0,0.03);
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            padding: 2rem;
            text-align: center;
            transition: box-shadow 0.3s ease;
          }
          
          .swiper-slide-active {
             box-shadow: 0 25px 50px rgba(8, 185, 219, 0.15), 0 10px 20px rgba(0,0,0,0.08);
          }

          .partner-logo {
            width: 100%;
            height: 160px;
            object-fit: contain;
            margin-bottom: 2rem;
            filter: grayscale(100%) opacity(0.6);
            transition: all 0.4s ease;
          }

          .swiper-slide-active .partner-logo {
            filter: grayscale(0%) opacity(1);
            transform: scale(1.05);
          }

          .partner-name {
            font-family: var(--font-heading);
            font-size: 1.4rem;
            font-weight: 800;
            color: var(--color-charcoal);
            line-height: 1.3;
            margin-bottom: 0.5rem;
          }

          .partner-badge {
            background: rgba(8, 185, 219, 0.1);
            color: var(--color-teal);
            font-size: 0.75rem;
            font-weight: 800;
            letter-spacing: 1px;
            padding: 6px 14px;
            border-radius: 20px;
            text-transform: uppercase;
            margin-bottom: auto;
          }

          .swiper-pagination-bullet {
            background: var(--color-teal);
          }
          
          /* Navigation Buttons */
          .swiper-button-next, .swiper-button-prev {
            color: var(--color-teal);
            background: #ffffff;
            width: 50px;
            height: 50px;
            border-radius: 50%;
            box-shadow: 0 5px 15px rgba(0,0,0,0.1);
            transition: all 0.3s ease;
          }
          .swiper-button-next:hover, .swiper-button-prev:hover {
            transform: scale(1.1);
            box-shadow: 0 8px 25px rgba(8, 185, 219, 0.25);
          }
          .swiper-button-next::after, .swiper-button-prev::after {
            font-size: 1.2rem;
            font-weight: bold;
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

        <div class="swiper partners-swiper reveal">
          <div class="swiper-wrapper">
"""

for i, p in enumerate(unique_partners):
    new_html += f"""
            <div class="swiper-slide">
              <div class="partner-badge">Partner</div>
              <img src="{p['src']}" alt="{p['label']}" class="partner-logo" loading="lazy" />
              <h3 class="partner-name">{p['label']}</h3>
            </div>
"""

new_html += """
          </div>
          <!-- Add Pagination -->
          <div class="swiper-pagination"></div>
          <!-- Add Navigation -->
          <div class="swiper-button-prev"></div>
          <div class="swiper-button-next"></div>
        </div>

        <div class="premium-quote reveal">
          <p>Each partnership has been an opportunity to listen, learn, and grow together &#8212; reaffirming that wellbeing is not an individual pursuit, but a <strong>collective responsibility</strong>.</p>
        </div>

      </div>
    </section>

    <!-- Swiper JS -->
    <script src="https://cdn.jsdelivr.net/npm/swiper@10/swiper-bundle.min.js"></script>
    <script>
      document.addEventListener('DOMContentLoaded', () => {
        // We ensure swiper is loaded
        if(typeof Swiper === 'undefined') return;
        
        var swiper = new Swiper('.partners-swiper', {
          effect: 'coverflow',
          grabCursor: true,
          centeredSlides: true,
          slidesPerView: 'auto',
          initialSlide: 2,
          loop: true,
          autoplay: {
            delay: 3500,
            disableOnInteraction: false,
            pauseOnMouseEnter: true,
          },
          coverflowEffect: {
            rotate: 25, /* 3D rotation angle */
            stretch: 0,
            depth: 150, /* Z-depth */
            modifier: 1,
            slideShadows: false,
          },
          pagination: {
            el: '.swiper-pagination',
            clickable: true,
          },
          navigation: {
            nextEl: '.swiper-button-next',
            prevEl: '.swiper-button-prev',
          },
        });
      });
    </script>
"""

pattern = r'(<!-- PARTNERS SECTION -->[\s\S]*?</script>)'
new_text = re.sub(pattern, new_html, text, flags=re.IGNORECASE)

if new_text != text:
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(new_text)
    print("Successfully replaced partners deck with 3D Coverflow Carousel!")
else:
    print("Could not find the partners section in index.html using regex.")
