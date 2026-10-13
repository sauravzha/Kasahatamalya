import re

files_to_update = ['index.html', 'story.html']

banner_html = """
        <!-- JOSHILA BANNER -->
        <style>
          .joshila-banner {
            margin-top: 7rem;
            background: linear-gradient(135deg, #08B9DB 0%, #1D4ED8 100%);
            border-radius: 32px;
            position: relative;
            padding: 4rem 4rem 4rem 360px;
            box-shadow: 0 25px 50px rgba(0,0,0,0.25);
            color: #FFFFFF;
            border: 2px solid rgba(255, 255, 255, 0.2);
            overflow: hidden;
          }
          /* Add a glassmorphic decorative shape inside */
          .joshila-banner::after {
            content: '';
            position: absolute;
            top: -50px;
            right: -50px;
            width: 300px;
            height: 300px;
            background: radial-gradient(circle, rgba(255,255,255,0.15) 0%, rgba(255,255,255,0) 70%);
            border-radius: 50%;
            pointer-events: none;
          }
          .joshila-photo {
            position: absolute;
            left: 40px;
            bottom: 0;
            width: 280px;
            height: 280px;
            border-radius: 50% 50% 0 0;
            border: 8px solid rgba(255, 255, 255, 0.1);
            border-bottom: none;
            object-fit: cover;
            object-position: center top;
            box-shadow: 0 -15px 40px rgba(0,0,0,0.2);
            transition: transform 0.4s ease;
          }
          .joshila-banner:hover .joshila-photo {
            transform: translateY(-10px);
          }
          .joshila-tag {
            font-size: 1.1rem;
            font-weight: 800;
            color: #FFC72C;
            text-transform: uppercase;
            letter-spacing: 1.5px;
            margin-bottom: 0.75rem;
          }
          .joshila-title {
            font-family: var(--font-heading);
            font-size: 2.4rem;
            font-weight: 800;
            line-height: 1.25;
            margin-bottom: 1.25rem;
            color: #FFFFFF;
            text-shadow: 0 2px 10px rgba(0,0,0,0.2);
          }
          .joshila-desc {
            font-size: 1.2rem;
            line-height: 1.7;
            color: rgba(255, 255, 255, 0.9);
            max-width: 650px;
            margin-bottom: 2rem;
          }
          .joshila-box {
            padding: 1.5rem;
            border: 2px solid rgba(255, 255, 255, 0.3);
            border-radius: 16px;
            background: rgba(255, 255, 255, 0.1);
            backdrop-filter: blur(10px);
            display: inline-block;
          }
          .joshila-box h5 {
            font-size: 0.9rem;
            text-transform: uppercase;
            letter-spacing: 1.5px;
            margin-bottom: 8px;
            font-weight: 800;
            color: #FFC72C;
          }
          .joshila-box p {
            font-size: 1rem;
            margin: 0;
            color: #FFFFFF;
            font-weight: 500;
            line-height: 1.5;
          }
          @media (max-width: 900px) {
            .joshila-banner {
              margin-top: 8rem;
              padding: 200px 2.5rem 3rem;
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
              border: 6px solid rgba(255, 255, 255, 0.2);
              border-bottom: 6px solid rgba(255, 255, 255, 0.2);
            }
            .joshila-banner:hover .joshila-photo {
              transform: translateX(-50%) scale(1.05);
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
"""

for file in files_to_update:
    try:
        with open(file, 'r', encoding='utf-8') as f:
            text = f.read()

        # Insert banner_html exactly after the closing `</div>` of the `advisory-grid`
        # We need to find the `advisory-grid` div and its closing div
        match = re.search(r'(<div class="advisory-grid"[^>]*>[\s\S]*?</div>\s*</div>)', text)
        if match:
            # We want to replace the match with the match + banner_html
            new_text = text.replace(match.group(1), match.group(1) + '\n' + banner_html)
            
            with open(file, 'w', encoding='utf-8') as f:
                f.write(new_text)
            print(f"Added Joshila banner to {file}")
        else:
            print(f"Could not find advisory-grid in {file}")
    except Exception as e:
        print(f"Failed on {file}: {e}")
