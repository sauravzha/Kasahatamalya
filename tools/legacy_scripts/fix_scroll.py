import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Extract all the flip cards from the FIRST marquee track.
# The cards look like <div class="flip-card-container"...>...</div></div>
# We can find the first <div class="marquee-track"> and grab everything inside it.
track_match = re.search(r'<div class="marquee-track">(.*?)</div>\s*<div class="marquee-track">', content, re.DOTALL)
if not track_match:
    print("Could not find marquee tracks")
    exit(1)

cards_html = track_match.group(1).strip()

# New section to replace marquee-container
new_scroller = f'''
        <style>
          .interactive-scroller::-webkit-scrollbar {{
            height: 10px;
          }}
          .interactive-scroller::-webkit-scrollbar-track {{
            background: rgba(0,0,0,0.05);
            border-radius: 10px;
          }}
          .interactive-scroller::-webkit-scrollbar-thumb {{
            background: var(--color-teal);
            border-radius: 10px;
          }}
        </style>
        <div class="marquee-container interactive-scroller" id="teamSlider" style="display: flex; overflow-x: auto; scroll-snap-type: x mandatory; gap: 3rem; padding: 2rem 3rem 4rem; scrollbar-width: thin; scrollbar-color: var(--color-teal) rgba(0,0,0,0.05); -webkit-overflow-scrolling: touch;">
            {cards_html}
        </div>
        
        <script>
          const slider = document.getElementById('teamSlider');
          let isInteracting = false;
          
          slider.addEventListener('mouseenter', () => isInteracting = true);
          slider.addEventListener('mouseleave', () => isInteracting = false);
          slider.addEventListener('touchstart', () => isInteracting = true, {{passive: true}});
          slider.addEventListener('touchend', () => {{
              setTimeout(() => isInteracting = false, 1000);
          }});
          
          let scrollTimeout;
          slider.addEventListener('scroll', () => {{
             isInteracting = true;
             window.clearTimeout(scrollTimeout);
             scrollTimeout = setTimeout(() => {{
                 // Check if mouse is still over it, if not resume
                 if (!slider.matches(':hover')) {{
                     isInteracting = false;
                 }}
             }}, 1500); 
          }});

          setInterval(() => {{
            if (!isInteracting) {{
              slider.scrollLeft += 1;
              if (slider.scrollLeft >= (slider.scrollWidth - slider.clientWidth - 1)) {{
                 slider.scrollLeft = 0;
              }}
            }}
          }}, 30);
        </script>
'''

# Replace the entire <div class="marquee-container"> block with our new scroller
# We can regex it
pattern = re.compile(r'<div class="marquee-container">.*?</div>\s*</div>\s*</section>', re.DOTALL)

def repl(m):
    return new_scroller + '\n      </div>\n    </section>'

new_content = pattern.sub(repl, content)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Scroll updated")
