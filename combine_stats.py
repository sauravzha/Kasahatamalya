import re

# We want to replace the H2 tag and the entire stats__grid div
updated_content = """
          <h2 style="color: white; font-size: 2.2rem; font-family: var(--font-heading); font-weight: 800; margin: 0; text-align: center;">A Decade of Impact: <span style="color: var(--color-sunshine);">10 Years of Reach</span></h2>
        </div>
        <div class="stats__grid" data-stagger style="display: flex; justify-content: center; gap: 1rem; flex-wrap: wrap;">
          
          <!-- NEW 5 CARDS -->
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

          <!-- PREVIOUS 8 CARDS -->
          <div class="compact-stat-card reveal">
            <svg width="24" height="24" viewBox="0 0 24 24" fill="#1CA6A0" style="margin: 0 auto;"><path d="M12 0L14.59 9.41L24 12L14.59 14.59L12 24L9.41 14.59L0 12L9.41 9.41L12 0Z"/></svg>
            <div class="stat-num-compact" data-count="10000" data-suffix="+">10,000+</div>
            <div class="stat-label-compact">Children via direct <span class="stat-verb">engagement</span></div>
          </div>
          <div class="compact-stat-card reveal">
            <svg width="24" height="24" viewBox="0 0 24 24" fill="#FFC72C" style="margin: 0 auto;"><path d="M12 0L14.59 9.41L24 12L14.59 14.59L12 24L9.41 14.59L0 12L9.41 9.41L12 0Z"/></svg>
            <div class="stat-num-compact" data-count="120000" data-suffix="+">1,20,000+</div>
            <div class="stat-label-compact">Children via digital <span class="stat-verb">engagement</span></div>
          </div>
          <div class="compact-stat-card reveal">
            <svg width="24" height="24" viewBox="0 0 24 24" fill="#FF6F59" style="margin: 0 auto;"><path d="M12 0L14.59 9.41L24 12L14.59 14.59L12 24L9.41 14.59L0 12L9.41 9.41L12 0Z"/></svg>
            <div class="stat-num-compact" data-count="1953" data-suffix="">1,953</div>
            <div class="stat-label-compact">Teachers <span class="stat-verb">Supported</span></div>
          </div>
          <div class="compact-stat-card reveal">
            <svg width="24" height="24" viewBox="0 0 24 24" fill="#38B6FF" style="margin: 0 auto;"><path d="M12 0L14.59 9.41L24 12L14.59 14.59L12 24L9.41 14.59L0 12L9.41 9.41L12 0Z"/></svg>
            <div class="stat-num-compact" data-count="10446" data-suffix="">10,446</div>
            <div class="stat-label-compact">Community Members <span class="stat-verb">Engaged</span></div>
          </div>
          <div class="compact-stat-card reveal">
            <svg width="24" height="24" viewBox="0 0 24 24" fill="#1CA6A0" style="margin: 0 auto;"><path d="M12 0L14.59 9.41L24 12L14.59 14.59L12 24L9.41 14.59L0 12L9.41 9.41L12 0Z"/></svg>
            <div class="stat-num-compact" data-count="140" data-suffix="">140</div>
            <div class="stat-label-compact">Facilitators <span class="stat-verb">Trained</span></div>
          </div>
          <div class="compact-stat-card reveal">
            <svg width="24" height="24" viewBox="0 0 24 24" fill="#FFC72C" style="margin: 0 auto;"><path d="M12 0L14.59 9.41L24 12L14.59 14.59L12 24L9.41 14.59L0 12L9.41 9.41L12 0Z"/></svg>
            <div class="stat-num-compact" data-count="519" data-suffix="">519</div>
            <div class="stat-label-compact">Out-of-school Children <span class="stat-verb">Re-enrolled</span></div>
          </div>
          <div class="compact-stat-card reveal">
            <svg width="24" height="24" viewBox="0 0 24 24" fill="#FF6F59" style="margin: 0 auto;"><path d="M12 0L14.59 9.41L24 12L14.59 14.59L12 24L9.41 14.59L0 12L9.41 9.41L12 0Z"/></svg>
            <div class="stat-num-compact" data-count="166" data-suffix="">166</div>
            <div class="stat-label-compact">Learning Festivals <span class="stat-verb">Conducted</span></div>
          </div>
          <div class="compact-stat-card reveal">
            <svg width="24" height="24" viewBox="0 0 24 24" fill="#38B6FF" style="margin: 0 auto;"><path d="M12 0L14.59 9.41L24 12L14.59 14.59L12 24L9.41 14.59L0 12L9.41 9.41L12 0Z"/></svg>
            <div class="stat-num-compact" data-count="28" data-suffix="">28</div>
            <div class="stat-label-compact">Panchayats <span class="stat-verb">Involved</span></div>
          </div>
        </div>
"""

def update_impact_reach():
    with open('index.html', 'r', encoding='utf-8') as f:
        text = f.read()

    # The H2 starts with:
    # <h2 style="color: white; font-size: 2rem; font-family: var(--font-heading); font-weight: 800; margin: 0; text-align: center;">Our Impact & Reach</h2>
    # And the grid ends right before:
    #       </div>
    #     </section>
    
    pattern = r'<h2 style="color: white; font-size: 2rem; font-family: var\(--font-heading\); font-weight: 800; margin: 0; text-align: center;">Our Impact & Reach</h2>[\s\S]*?(?=      </div>\n    </section>)'
    
    new_text = re.sub(pattern, updated_content.strip(), text)
    
    if new_text != text:
        with open('index.html', 'w', encoding='utf-8') as f:
            f.write(new_text)
        print("Successfully combined all stats in index.html!")
    else:
        print("Could not find the target section in index.html.")

update_impact_reach()
