import re

css_update = """
        <!-- JOSHILA BANNER -->
        <style>
          .joshila-banner {
            margin-top: 7rem;
            background: linear-gradient(135deg, #F8FAFC 0%, #E2E8F0 100%);
            border-radius: 32px;
            position: relative;
            padding: 3.5rem 3.5rem 3.5rem 340px;
            box-shadow: 0 25px 50px rgba(0,0,0,0.2);
            color: var(--color-charcoal);
            border: 2px solid rgba(255, 255, 255, 0.5);
          }
          .joshila-photo {
            position: absolute;
            left: 40px;
            bottom: 0;
            width: 260px;
            height: 260px;
            border-radius: 50% 50% 0 0;
            border: 8px solid #F8FAFC;
            border-bottom: none;
            object-fit: cover;
            object-position: center top;
            box-shadow: 0 -15px 40px rgba(0,0,0,0.12);
          }
          .joshila-tag {
            font-size: 1.1rem;
            font-weight: 800;
            color: var(--color-teal);
            text-transform: uppercase;
            letter-spacing: 1px;
            margin-bottom: 0.5rem;
          }
          .joshila-title {
            font-family: var(--font-heading);
            font-size: 2.2rem;
            font-weight: 800;
            line-height: 1.2;
            margin-bottom: 1.2rem;
            color: var(--color-charcoal);
          }
          .joshila-desc {
            font-size: 1.15rem;
            line-height: 1.6;
            color: #4A5568;
            max-width: 650px;
            margin-bottom: 1.5rem;
          }
          .joshila-box {
            padding: 1.2rem;
            border: 2px dashed rgba(58, 150, 170, 0.4);
            border-radius: 16px;
            background: rgba(58, 150, 170, 0.08);
            display: inline-block;
          }
          .joshila-box h5 {
            font-size: 0.85rem;
            text-transform: uppercase;
            letter-spacing: 1.5px;
            margin-bottom: 6px;
            font-weight: 800;
            color: var(--color-teal-dark);
          }
          .joshila-box p {
            font-size: 0.95rem;
            margin: 0;
            color: var(--color-charcoal);
            font-weight: 500;
          }
          @media (max-width: 900px) {
            .joshila-banner {
              margin-top: 8rem;
              padding: 180px 2rem 2.5rem;
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
              border: 6px solid #F8FAFC;
            }
            .joshila-desc {
              margin-left: auto;
              margin-right: auto;
            }
          }
        </style>
"""

def replace_css(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        text = f.read()

    # Find the <style> block directly after <!-- JOSHILA BANNER -->
    pattern = r'<!-- JOSHILA BANNER -->\s*<style>.*?</style>'
    new_text = re.sub(pattern, css_update.strip(), text, flags=re.DOTALL)

    if text != new_text:
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(new_text)
        print(f"Updated Joshila banner styles in {filename}")
    else:
        print(f"Could not find Joshila banner styles to replace in {filename}")

replace_css('story.html')
replace_css('index.html')
