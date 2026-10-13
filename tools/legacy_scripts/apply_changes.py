import re
import sys
import glob

# 1. Update css/components.css for btn--donate
css_file = "css/components.css"
with open(css_file, "r", encoding="utf-8") as f:
    css_content = f.read()

# Replace sunshine with teal for donate button
css_content = css_content.replace(
    ".btn--donate {\n  background: var(--color-sunshine);\n  color: var(--color-charcoal);",
    ".btn--donate {\n  background: var(--color-teal);\n  color: var(--color-white);"
)
css_content = css_content.replace(
    ".btn--donate:hover {\n  background: var(--color-sunshine-dark);",
    ".btn--donate:hover {\n  background: var(--color-teal-dark);"
)
css_content = css_content.replace(
    "box-shadow: 0 6px 20px rgba(255, 199, 44, 0.4);",
    "box-shadow: 0 6px 20px rgba(8, 185, 219, 0.4);"
)
css_content = css_content.replace(
    "color: var(--color-charcoal);\n}",
    "color: var(--color-white);\n}"
)
with open(css_file, "w", encoding="utf-8") as f:
    f.write(css_content)

# 2. Re-write the Timeline section in index.html
html_files = ["index.html", "story.html"] # story might not have timeline but let's check
for file in ["index.html"]:
    with open(file, "r", encoding="utf-8") as f:
        content = f.read()
    
    # Generate new timeline HTML
    timeline_data = [
        ("2016", "The beginning, in Kotra", "Two fellows in a remote tribal block, asking what real education would look like there. Incorporated as a Section 8 company on 27 July 2016.", "#FF6F59"),
        ("2017", "First programmes", "Learning Festivals begin in June. The iDISCOVER Fellowship inducts its first cohort of grassroots education leaders in November.", "#1CA6A0"),
        ("2018", "Into Delhi", "Work begins in MCD government schools in East Delhi.", "#FFC72C"),
        ("2019", "SEE Learning, and a curriculum with the state", "SEE Learning launched with Emory University and the Dalai Lama Trust. Entrepreneurial Mindset Curriculum co-created with SCERT Delhi.", "#38B6FF"),
        ("2020", "The pandemic, and radio", "Relief for families in Kotra and Gogunda. Radio learning launched with Radio Madhuban for children with no internet access.", "#9B51E0"),
        ("2021", "Institutional footing", "CSR registration approved in April 2021, opening the door to corporate partnerships.", "#FF6F59"),
        ("2022", "Into Bihar", "Work begins in Samastipur district, in partnership with SCERT Bihar.", "#1CA6A0"),
        ("2023", "Recognised globally", "The parent engagement model reaches the global Top 10 for the World's Best School Prize for Community Collaboration.", "#FFC72C"),
        ("2025", "Adopted by the system", "The STAR Parents model is adopted by the Municipal Corporation of Delhi from 1 April 2025.", "#38B6FF"),
        ("2026", "The depth decade begins", "Ten years in. An Advisory Board of eight constituted in June 2026. The next decade is about deeper roots and stronger institutions, not more districts.", "#9B51E0")
    ]
    
    timeline_html = '<div class="premium-timeline" data-stagger>\n'
    for year, title, desc, color in timeline_data:
        timeline_html += f'''          <!-- {year} -->
          <div class="pt-item reveal">
            <div class="pt-content-wrap">
              <div class="pt-card">
                <div class="pt-year">{year}</div>
                <h3>{title}</h3>
                <p>{desc}</p>
              </div>
            </div>
            <div class="pt-dot" style="--dot-color: {color};"></div>
            <div style="width: 45%;"></div>
          </div>\n'''
    timeline_html += '        </div>'

    # Replace the old timeline with regex
    content = re.sub(r'<div class="premium-timeline" data-stagger>.*?</div>\s*<div class="text-center', timeline_html + '\n        <div class="text-center', content, flags=re.DOTALL)
    
    # 3. Add "Read our impact report..." in Hero
    # Find </p> in hero__subtitle and add a link below it.
    hero_link = '''<br/><br/><a href="/press.html" style="font-weight:700; color:var(--color-teal); text-decoration:underline;">Read our impact report and see how we work-</a>'''
    if "Read our impact report" not in content:
        content = content.replace(
            "with joyful, whole-school learning.\n        </p>",
            f"with joyful, whole-school learning.{hero_link}\n        </p>"
        )
    
    with open(file, "w", encoding="utf-8") as f:
        f.write(content)

# 4. Remove Vivek from Team & Update Pooja
def update_team(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Remove Vivek's Card
    card_pattern = r'<!-- 2\. Vivek Kumar -->.*?</div>\s*</div>\s*</div>\s*(?=<!-- 3\.|</div>\s*<!-- VIEW 2)'
    content = re.sub(card_pattern, '', content, flags=re.DOTALL)

    # Remove Vivek's row in matrix
    row_pattern = r'<tr>\s*<td>\s*<div class="gov-matrix-user">\s*<div class="gov-matrix-avatar"[^>]*><img src="/assets/team/vivek_kumar\.jpeg"[^>]*></div>\s*<div>Vivek Kumar</div>\s*</div>\s*</td>\s*<td><span class="gov-badge"[^>]*>Co-Founder</span></td>\s*<td>.*?</td>\s*<td>.*?</td>\s*</tr>'
    content = re.sub(row_pattern, '', content, flags=re.DOTALL)

    # Update Pooja's badge
    content = re.sub(r'(<div>Pooja Singh</div>\s*</div>\s*</td>\s*<td><span class="gov-badge" style="[^"]*">)Co-Founder(</span>)', r'\1Co-Founder and Mentor\2', content)
    
    # Also update Pooja's badge in card
    content = re.sub(r'(Pooja Singh\s*</h3>\s*<span class="gov-badge"[^>]*>)\s*Co-Founder\s*(</span>)', r'\1Co-Founder and Mentor\2', content)

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)

update_team("index.html")
update_team("story.html")

print("Finished css and team replacements!")
