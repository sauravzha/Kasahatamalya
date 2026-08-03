import re

files_to_update = ['index.html', 'story.html']

# The HTML to insert BEFORE the advisory-grid
board_html = """
        <!-- BOARD OF DIRECTORS -->
        <div style="margin-bottom: 5rem;">
          <h3 style="font-family: 'Baloo 2', cursive; font-size: 2.2rem; font-weight: 800; color: #FFC72C; text-align: center; margin-bottom: 2.5rem;">Board of Directors</h3>
          
          <div class="advisory-grid" style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 2rem; align-items: stretch; max-width: 900px; margin: 0 auto;">
            
            <div class="advisory-card reveal" style="background: rgba(255, 255, 255, 0.12); backdrop-filter: blur(16px); -webkit-backdrop-filter: blur(16px); border-radius: 24px; padding: 2rem 1.5rem; border: 1px solid rgba(255, 255, 255, 0.22); box-shadow: 0 15px 35px rgba(0,0,0,0.1); display: flex; flex-direction: column; align-items: center; text-align: center; transition: all 0.4s cubic-bezier(0.16, 1, 0.3, 1);">
              <div style="width: 140px; height: 140px; border-radius: 50%; overflow: hidden; border: 4px solid #FFFFFF; box-shadow: 0 10px 25px rgba(0,0,0,0.2); margin-bottom: 1.25rem; flex-shrink: 0; background: #ffffff; transition: transform 0.4s ease;">
                <img src="/assets/team/soumya_b.jpeg" alt="SOUMYA BHASKARACHARYA" loading="lazy" style="width: 100%; height: 100%; object-fit: cover; object-position: center top;" />
              </div>
              <h3 style="font-family: 'Baloo 2', cursive; font-size: 1.4rem; font-weight: 800; color: #FFFFFF; margin: 0 0 0.25rem 0; letter-spacing: 0.5px;">SOUMYA BHASKARACHARYA</h3>
              <div style="font-size: 0.85rem; font-weight: 700; color: #FFC72C; text-transform: uppercase; letter-spacing: 1px; margin-bottom: 0.25rem;">Director and CEO</div>
              <p style="font-size: 0.95rem; color: rgba(255, 255, 255, 0.92); line-height: 1.65; margin: 0; font-weight: 400; text-align: center;">
                Masters in Applied Sociology. Eight years with the organisation.
              </p>
            </div>

            <div class="advisory-card reveal" style="background: rgba(255, 255, 255, 0.12); backdrop-filter: blur(16px); -webkit-backdrop-filter: blur(16px); border-radius: 24px; padding: 2rem 1.5rem; border: 1px solid rgba(255, 255, 255, 0.22); box-shadow: 0 15px 35px rgba(0,0,0,0.1); display: flex; flex-direction: column; align-items: center; text-align: center; transition: all 0.4s cubic-bezier(0.16, 1, 0.3, 1);">
              <div style="width: 140px; height: 140px; border-radius: 50%; overflow: hidden; border: 4px solid #FFFFFF; box-shadow: 0 10px 25px rgba(0,0,0,0.2); margin-bottom: 1.25rem; flex-shrink: 0; background: #ffffff; transition: transform 0.4s ease;">
                <img src="/assets/team/anjali_gupte.jpeg" alt="ANJALI GUPTE" loading="lazy" style="width: 100%; height: 100%; object-fit: cover; object-position: center top;" />
              </div>
              <h3 style="font-family: 'Baloo 2', cursive; font-size: 1.4rem; font-weight: 800; color: #FFFFFF; margin: 0 0 0.25rem 0; letter-spacing: 0.5px;">ANJALI GUPTE</h3>
              <div style="font-size: 0.85rem; font-weight: 700; color: #FFC72C; text-transform: uppercase; letter-spacing: 1px; margin-bottom: 0.25rem;">Director and founding member</div>
              <p style="font-size: 0.95rem; color: rgba(255, 255, 255, 0.92); line-height: 1.65; margin: 0; font-weight: 400; text-align: center;">
                MSc Statistics, B.Ed. Chairs the Advisory Board.
              </p>
            </div>
            
          </div>
        </div>

        <!-- ADVISORY BOARD HEADER -->
        <h3 style="font-family: 'Baloo 2', cursive; font-size: 2.2rem; font-weight: 800; color: #FFC72C; text-align: center; margin-bottom: 2.5rem;">Advisory Board</h3>
"""

for file in files_to_update:
    try:
        with open(file, 'r', encoding='utf-8') as f:
            text = f.read()

        # Update the main heading and intro text
        # Old:
        #           <h2 style="font-family: 'Baloo 2', cursive; font-size: clamp(2.5rem, 4.5vw, 3.6rem); font-weight: 800; color: #FFFFFF; margin: 0 0 1rem 0; line-height: 1.15; display: flex; align-items: center; justify-content: center; gap: 12px; flex-wrap: wrap;">
        #             Our Advisory Board
        #           </h2>
        #           <p style="max-width: 720px; margin: 0 auto; font-size: 1.2rem; color: rgba(255,255,255,0.9); line-height: 1.6; font-weight: 400;">
        #             Distinguished leaders, researchers, and social entrepreneurs guiding Kshamtalaya's mission to unlock potential across India.
        #           </p>

        # New:
        text = text.replace(
            "            Our Advisory Board\n          </h2>\n          <p style=\"max-width: 720px; margin: 0 auto; font-size: 1.2rem; color: rgba(255,255,255,0.9); line-height: 1.6; font-weight: 400;\">\n            Distinguished leaders, researchers, and social entrepreneurs guiding Kshamtalaya's mission to unlock potential across India.\n          </p>",
            "            Governance\n          </h2>\n          <p style=\"max-width: 800px; margin: 0 auto; font-size: 1.2rem; color: rgba(255,255,255,0.9); line-height: 1.6; font-weight: 400;\">\n            Kshamtalaya Foundation is governed by its Board of Directors under the Companies Act 2013. Our advisors guide strategy and practice and carry no statutory responsibility.\n          </p>"
        )

        # Insert board_html before `<div class="advisory-grid"`
        text = text.replace(
            '        <div class="advisory-grid" style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 2rem; align-items: stretch;">',
            board_html + '\n        <div class="advisory-grid" style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 2rem; align-items: stretch;">'
        )

        with open(file, 'w', encoding='utf-8') as f:
            f.write(text)
        print(f"Successfully added Board of Directors to {file}")
    except Exception as e:
        print(f"Failed on {file}: {e}")
