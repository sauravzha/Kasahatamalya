import re

new_stats_grid = """
        <div class="stats__grid" data-stagger style="display: flex; justify-content: center; gap: 1rem; flex-wrap: wrap;">
          <div class="compact-stat-card reveal">
            <svg width="24" height="24" viewBox="0 0 24 24" fill="#38B6FF" style="margin: 0 auto;"><path d="M12 0L14.59 9.41L24 12L14.59 14.59L12 24L9.41 14.59L0 12L9.41 9.41L12 0Z"/></svg>
            <div class="stat-num-compact" data-count="355914" data-suffix="">3,55,914</div>
            <div class="stat-label-compact">Total Students <span class="stat-verb">Impacted</span></div>
          </div>
          <div class="compact-stat-card reveal">
            <svg width="24" height="24" viewBox="0 0 24 24" fill="#1CA6A0" style="margin: 0 auto;"><path d="M12 0L14.59 9.41L24 12L14.59 14.59L12 24L9.41 14.59L0 12L9.41 9.41L12 0Z"/></svg>
            <div class="stat-num-compact" data-count="1402" data-suffix="">1,402</div>
            <div class="stat-label-compact">iDiscover <span class="stat-verb">Rajasthan</span></div>
          </div>
          <div class="compact-stat-card reveal">
            <svg width="24" height="24" viewBox="0 0 24 24" fill="#FFC72C" style="margin: 0 auto;"><path d="M12 0L14.59 9.41L24 12L14.59 14.59L12 24L9.41 14.59L0 12L9.41 9.41L12 0Z"/></svg>
            <div class="stat-num-compact" data-count="1050" data-suffix="+">1,050+</div>
            <div class="stat-label-compact">iDiscover <span class="stat-verb">Bihar</span></div>
          </div>
          <div class="compact-stat-card reveal">
            <svg width="24" height="24" viewBox="0 0 24 24" fill="#FF6F59" style="margin: 0 auto;"><path d="M12 0L14.59 9.41L24 12L14.59 14.59L12 24L9.41 14.59L0 12L9.41 9.41L12 0Z"/></svg>
            <div class="stat-num-compact" data-count="4053" data-suffix="">4,053</div>
            <div class="stat-label-compact">Delhi Direct <span class="stat-verb">Students</span></div>
          </div>
          <div class="compact-stat-card reveal">
            <svg width="24" height="24" viewBox="0 0 24 24" fill="#38B6FF" style="margin: 0 auto;"><path d="M12 0L14.59 9.41L24 12L14.59 14.59L12 24L9.41 14.59L0 12L9.41 9.41L12 0Z"/></svg>
            <div class="stat-num-compact" data-count="6368" data-suffix="+">6,368+</div>
            <div class="stat-label-compact">Learning Festival <span class="stat-verb">Children</span></div>
          </div>
        </div>
"""

def update_impact_reach():
    with open('index.html', 'r', encoding='utf-8') as f:
        text = f.read()

    # The stats grid starts with:
    # <div class="stats__grid" data-stagger style="display: flex; justify-content: center; gap: 1rem; flex-wrap: wrap;">
    # And ends before:
    #       </div>
    #     </section>
    #     <!-- ════════════════════════════════════════ -->
    #     <!-- OUR APPROACH                             -->
    
    # We can match it cleanly.
    pattern = r'<div class="stats__grid" data-stagger style="display: flex; justify-content: center; gap: 1rem; flex-wrap: wrap;">[\s\S]*?(?=      </div>\n    </section>)'
    
    new_text = re.sub(pattern, new_stats_grid.strip(), text)
    
    if new_text != text:
        with open('index.html', 'w', encoding='utf-8') as f:
            f.write(new_text)
        print("Successfully updated Our Impact & Reach section in index.html!")
    else:
        print("Could not find the stats grid in index.html.")

update_impact_reach()
