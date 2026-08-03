import re

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

new_js = """
      <script>
        function switchAchieveTab(panelId, btn) {
          document.querySelectorAll('.achieve-panel').forEach(p => p.classList.remove('active'));
          document.querySelectorAll('.achieve-toggle-btn').forEach(b => b.classList.remove('active'));
          
          document.getElementById(panelId).classList.add('active');
          btn.classList.add('active');
          
          const pill = document.getElementById('achievePill');
          pill.style.left = btn.offsetLeft + 'px';
          pill.style.width = btn.offsetWidth + 'px';
          
          // Re-trigger reveal animations in the active panel
          const newReveals = document.getElementById(panelId).querySelectorAll('.reveal');
          newReveals.forEach(r => {
             r.classList.remove('active');
             setTimeout(() => r.classList.add('active'), 50);
          });
        }
        
        // Setup initial pill width
        document.addEventListener('DOMContentLoaded', () => {
           const btn = document.querySelector('.achieve-toggle-btn.active');
           if(btn) {
              const pill = document.getElementById('achievePill');
              if(pill) {
                 pill.style.left = btn.offsetLeft + 'px';
                 pill.style.width = btn.offsetWidth + 'px';
              }
           }
        });
      </script>
"""

# Replace the script block inside the achievements-2025 section
section_pattern = r'(<section[^>]*id="achievements-2025"[^>]*>[\s\S]*?)<script>[\s\S]*?</script>([\s\S]*?</section>)'
new_text = re.sub(section_pattern, r'\1' + new_js + r'\2', text, flags=re.IGNORECASE)

if new_text != text:
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(new_text)
    print("Fixed JS for toggle switch!")
else:
    print("Failed to replace JS.")
