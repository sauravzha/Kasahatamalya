import os
import re

new_footer = """  <footer style="background-color: #2D2D2D; color: #ffffff; padding: 5rem 0; font-family: 'Inter', sans-serif;">
    <div class="container" style="display: grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap: 3rem; max-width: 1200px; margin: 0 auto;">
      
      <!-- Column 1: Brand & About -->
      <div>
        <div style="display: flex; align-items: center; gap: 0.75rem; margin-bottom: 1.5rem;">
          <img src="/assets/logo.png" alt="Kshamtalaya Logo" style="height: 60px; width: auto; object-fit: contain;" />
        </div>
        <p style="color: #DDDDDD; font-size: 0.95rem; line-height: 1.8; margin-bottom: 2rem; text-align: left;">
          Kshamta (क्षमता) means Potential.<br>Aalaya (आलय) means Abode or Home.<br>Kshamtalaya is where Potential finds a Home.
        </p>
        <div style="display: flex; gap: 0.75rem;">
          <a href="https://www.facebook.com/kshamtalaya" target="_blank" rel="noopener noreferrer" style="display: flex; align-items: center; justify-content: center; width: 40px; height: 40px; border: 1px solid #555555; border-radius: 50%; color: #fff; text-decoration: none; transition: all 0.3s ease;" onmouseover="this.style.borderColor='#fff'" onmouseout="this.style.borderColor='#555'"><svg width="18" height="18" fill="currentColor" viewBox="0 0 24 24"><path d="M18 2h-3a5 5 0 00-5 5v3H7v4h3v8h4v-8h3l1-4h-4V7a1 1 0 011-1h3z"></path></svg></a>
          <a href="https://twitter.com/kshamtalaya" target="_blank" rel="noopener noreferrer" style="display: flex; align-items: center; justify-content: center; width: 40px; height: 40px; border: 1px solid #555555; border-radius: 50%; color: #fff; text-decoration: none; transition: all 0.3s ease;" onmouseover="this.style.borderColor='#fff'" onmouseout="this.style.borderColor='#555'"><svg width="18" height="18" fill="currentColor" viewBox="0 0 24 24"><path d="M23 3a10.9 10.9 0 01-3.14 1.53 4.48 4.48 0 00-7.86 3v1A10.66 10.66 0 013 4s-4 9 5 13a11.64 11.64 0 01-7 2c9 5 20 0 20-11.5a4.5 4.5 0 00-.08-.83A7.72 7.72 0 0023 3z"></path></svg></a>
          <a href="https://www.instagram.com/kshamtalaya" target="_blank" rel="noopener noreferrer" style="display: flex; align-items: center; justify-content: center; width: 40px; height: 40px; border: 1px solid #555555; border-radius: 50%; color: #fff; text-decoration: none; transition: all 0.3s ease;" onmouseover="this.style.borderColor='#fff'" onmouseout="this.style.borderColor='#555'"><svg width="18" height="18" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" viewBox="0 0 24 24"><rect x="2" y="2" width="20" height="20" rx="5" ry="5"></rect><path d="M16 11.37A4 4 0 1112.63 8 4 4 0 0116 11.37z"></path><line x1="17.5" y1="6.5" x2="17.51" y2="6.5"></line></svg></a>
          <a href="https://www.youtube.com/@kshamtalayafoundation9946" target="_blank" rel="noopener noreferrer" style="display: flex; align-items: center; justify-content: center; width: 40px; height: 40px; border: 1px solid #555555; border-radius: 50%; color: #fff; text-decoration: none; transition: all 0.3s ease;" onmouseover="this.style.borderColor='#fff'" onmouseout="this.style.borderColor='#555'"><svg width="18" height="18" fill="currentColor" viewBox="0 0 24 24"><path d="M22.54 6.42a2.78 2.78 0 00-1.94-1.96C18.88 4 12 4 12 4s-6.88 0-8.6.46a2.78 2.78 0 00-1.94 1.96C1 8.16 1 12 1 12s0 3.84.46 5.58a2.78 2.78 0 001.94 1.96c1.72.46 8.6.46 8.6.46s6.88 0 8.6-.46a2.78 2.78 0 001.94-1.96C23 15.84 23 12 23 12s0-3.84-.46-5.58zM9.54 15.18V8.82l6.26 3.18-6.26 3.18z"></path></svg></a>
          <a href="mailto:info@kshamtalaya.org" style="display: flex; align-items: center; justify-content: center; width: 40px; height: 40px; border: 1px solid #555555; border-radius: 50%; color: #fff; text-decoration: none; transition: all 0.3s ease;" onmouseover="this.style.borderColor='#fff'" onmouseout="this.style.borderColor='#555'"><svg width="18" height="18" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" viewBox="0 0 24 24"><path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"></path><polyline points="22,6 12,13 2,6"></polyline></svg></a>
        </div>
      </div>

      <!-- Column 2: Explore -->
      <div>
        <h4 style="color: #FFC72C; font-size: 1rem; font-weight: 800; margin-bottom: 1.5rem; letter-spacing: 0.5px; text-transform: uppercase;">Explore</h4>
        <ul style="list-style: none; padding: 0; margin: 0; display: flex; flex-direction: column; gap: 1rem;">
          <li><a href="/" style="color: #DDDDDD; text-decoration: none; font-size: 0.95rem; transition: color 0.2s ease;" onmouseover="this.style.color='#fff'" onmouseout="this.style.color='#DDDDDD'">Home</a></li>
          <li><a href="/story.html" style="color: #DDDDDD; text-decoration: none; font-size: 0.95rem; transition: color 0.2s ease;" onmouseover="this.style.color='#fff'" onmouseout="this.style.color='#DDDDDD'">Our Story</a></li>
          <li><a href="/programs.html" style="color: #DDDDDD; text-decoration: none; font-size: 0.95rem; transition: color 0.2s ease;" onmouseover="this.style.color='#fff'" onmouseout="this.style.color='#DDDDDD'">Programs</a></li>
          <li><a href="/press.html" style="color: #DDDDDD; text-decoration: none; font-size: 0.95rem; transition: color 0.2s ease;" onmouseover="this.style.color='#fff'" onmouseout="this.style.color='#DDDDDD'">Press & Media</a></li>
          <li><a href="/resources.html" style="color: #DDDDDD; text-decoration: none; font-size: 0.95rem; transition: color 0.2s ease;" onmouseover="this.style.color='#fff'" onmouseout="this.style.color='#DDDDDD'">Resources</a></li>
          <li><a href="/contact.html" style="color: #DDDDDD; text-decoration: none; font-size: 0.95rem; transition: color 0.2s ease;" onmouseover="this.style.color='#fff'" onmouseout="this.style.color='#DDDDDD'">Contact</a></li>
          <li><a href="/donate.html" style="color: #DDDDDD; text-decoration: none; font-size: 0.95rem; transition: color 0.2s ease;" onmouseover="this.style.color='#fff'" onmouseout="this.style.color='#DDDDDD'">Give India</a></li>
        </ul>
      </div>

      <!-- Column 3: Programs -->
      <div>
        <h4 style="color: #FFC72C; font-size: 1rem; font-weight: 800; margin-bottom: 1.5rem; letter-spacing: 0.5px; text-transform: uppercase;">Programs</h4>
        <ul style="list-style: none; padding: 0; margin: 0; display: flex; flex-direction: column; gap: 1rem;">
          <li><a href="/programs/cell.html" style="color: #DDDDDD; text-decoration: none; font-size: 0.95rem; transition: color 0.2s ease;" onmouseover="this.style.color='#fff'" onmouseout="this.style.color='#DDDDDD'">C.E.L.L.</a></li>
          <li><a href="/programs/learning-festivals.html" style="color: #DDDDDD; text-decoration: none; font-size: 0.95rem; transition: color 0.2s ease;" onmouseover="this.style.color='#fff'" onmouseout="this.style.color='#DDDDDD'">Learning Festivals</a></li>
          <li><a href="/programs/diganth.html" style="color: #DDDDDD; text-decoration: none; font-size: 0.95rem; transition: color 0.2s ease;" onmouseover="this.style.color='#fff'" onmouseout="this.style.color='#DDDDDD'">Project Diganth</a></li>
          <li><a href="/programs/wst.html" style="color: #DDDDDD; text-decoration: none; font-size: 0.95rem; transition: color 0.2s ease;" onmouseover="this.style.color='#fff'" onmouseout="this.style.color='#DDDDDD'">Whole School Transformation</a></li>
          <li><a href="/programs/hausla.html" style="color: #DDDDDD; text-decoration: none; font-size: 0.95rem; transition: color 0.2s ease;" onmouseover="this.style.color='#fff'" onmouseout="this.style.color='#DDDDDD'">Hausla</a></li>
          <li><a href="/programs/fale-fale.html" style="color: #DDDDDD; text-decoration: none; font-size: 0.95rem; transition: color 0.2s ease;" onmouseover="this.style.color='#fff'" onmouseout="this.style.color='#DDDDDD'">Fale Fale Shiksha Muhim</a></li>
          <li><a href="/programs/khushishala.html" style="color: #DDDDDD; text-decoration: none; font-size: 0.95rem; transition: color 0.2s ease;" onmouseover="this.style.color='#fff'" onmouseout="this.style.color='#DDDDDD'">Khushishala</a></li>
          <li><a href="/programs/idiscover.html" style="color: #DDDDDD; text-decoration: none; font-size: 0.95rem; transition: color 0.2s ease;" onmouseover="this.style.color='#fff'" onmouseout="this.style.color='#DDDDDD'">iDiscover Fellowship</a></li>
        </ul>
      </div>

      <!-- Column 4: Policies -->
      <div>
        <h4 style="color: #FFC72C; font-size: 1rem; font-weight: 800; margin-bottom: 1.5rem; letter-spacing: 0.5px; text-transform: uppercase;">Policies</h4>
        <ul style="list-style: none; padding: 0; margin: 0; display: flex; flex-direction: column; gap: 1rem;">
          <li><a href="/Policies/Child%20protection%20policy_%20KF-%202026-27%20(2).pdf" target="_blank" style="color: #DDDDDD; text-decoration: none; font-size: 0.95rem; transition: color 0.2s ease;" onmouseover="this.style.color='#fff'" onmouseout="this.style.color='#DDDDDD'">Child Protection Policy</a></li>
          <li><a href="/Policies/KF_Data_Protection_Policy_v2.1%20(2).pdf" target="_blank" style="color: #DDDDDD; text-decoration: none; font-size: 0.95rem; transition: color 0.2s ease;" onmouseover="this.style.color='#fff'" onmouseout="this.style.color='#DDDDDD'">Data Protection Policy</a></li>
          <li><a href="/Policies/POSH_Policy_26-27_Kshamtalaya_v2.1%20(2)%20(2).pdf" target="_blank" style="color: #DDDDDD; text-decoration: none; font-size: 0.95rem; transition: color 0.2s ease;" onmouseover="this.style.color='#fff'" onmouseout="this.style.color='#DDDDDD'">POSH Policy</a></li>
        </ul>
      </div>

      <!-- Column 5: Stay in Touch -->
      <div>
        <h4 style="color: #FFC72C; font-size: 1rem; font-weight: 800; margin-bottom: 1.5rem; letter-spacing: 0.5px; text-transform: uppercase;">Stay In Touch</h4>
        <p style="color: #DDDDDD; font-size: 0.95rem; line-height: 1.5; margin-bottom: 1.5rem;">
          Get stories of change, learning festival dates, and program updates in your inbox.
        </p>
        <form style="display: flex; gap: 0.5rem; flex-wrap: wrap;">
          <input type="email" placeholder="you@school.org" style="flex: 1; min-width: 150px; padding: 0.75rem 1rem; background-color: #2D2D2D; border: 1px solid #555555; border-radius: 30px; color: #fff; font-family: 'Inter', sans-serif; font-size: 0.9rem; outline: none;" required>
          <button type="submit" style="background-color: #FFC72C; color: #111111; padding: 0.75rem 1.5rem; border: none; border-radius: 30px; font-weight: 600; cursor: pointer; transition: background-color 0.2s ease;" onmouseover="this.style.backgroundColor='#ffdb6b'" onmouseout="this.style.backgroundColor='#FFC72C'">
            Join
          </button>
        </form>
      </div>

    </div>
  </footer>"""

def process_file(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        print(f"Could not read {filepath}: {e}")
        return
        
    pattern = re.compile(r'<footer[^>]*>.*?</footer>', re.DOTALL)
    
    if pattern.search(content):
        new_content = pattern.sub(new_footer, content)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated {filepath}")
    else:
        print(f"Footer not found in {filepath}")

for f in ['index.html', 'contact.html', 'donate.html', 'press.html', 'programs.html', 'story.html']:
    process_file(f)
