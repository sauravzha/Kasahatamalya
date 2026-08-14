import re
import shutil
import os

# ── 1. Copy PDFs into public/assets/reports ──────────────────────
src_dir = r"C:\Users\Saurav\Desktop\Kshamatalaya\Annual report from 10 to 26"
dst_dir = r"C:\Users\Saurav\Desktop\Kshamatalaya\public\assets\reports"
os.makedirs(dst_dir, exist_ok=True)

reports = [
    {
        'year': '2016-17',
        'file': '1) Annual Report Kshamtalaya 2016-17.pdf',
        'slug': 'annual-report-2016-17.pdf',
        'highlight': 'Foundation Year',
        'color': '#38B6FF',
        'icon': '🌱',
        'desc': 'The founding year — laying the groundwork for community-led education in rural India.'
    },
    {
        'year': '2017-18',
        'file': '2) Annual Report Kshamtalaya 2017-18.pdf',
        'slug': 'annual-report-2017-18.pdf',
        'highlight': 'Early Growth',
        'color': '#1CA6A0',
        'icon': '🌿',
        'desc': 'Expanding into new communities and building the first cadre of local education leaders.'
    },
    {
        'year': '2018-19',
        'file': '3) Annual Report Kshamtalaya 2018-19.pdf',
        'slug': 'annual-report-2018-19.pdf',
        'highlight': 'Deepening Roots',
        'color': '#6DBE45',
        'icon': '🌳',
        'desc': 'Strengthening program models and deepening partnerships with government schools.'
    },
    {
        'year': '2019-20',
        'file': '4) Annual Report Kshamtalaya 2019-20.pdf',
        'slug': 'annual-report-2019-20.pdf',
        'highlight': 'Resilience & Reach',
        'color': '#F2994A',
        'icon': '🔥',
        'desc': 'Navigating challenges and innovating new approaches for underserved students.'
    },
    {
        'year': '2020-21',
        'file': '5) Annual Report Kshamtalaya 2020-21.pdf',
        'slug': 'annual-report-2020-21.pdf',
        'highlight': 'Pandemic Response',
        'color': '#FF6F59',
        'icon': '💪',
        'desc': 'Pivoting during COVID-19 with community learning hubs and digital outreach.'
    },
    {
        'year': '2021-22',
        'file': 'Annual Report Kshamtalaya All Programs 2021-22.pdf',
        'slug': 'annual-report-2021-22.pdf',
        'highlight': 'Multi-State Impact',
        'color': '#9B51E0',
        'icon': '🗺️',
        'desc': 'Expanding across Rajasthan, Bihar and Delhi with comprehensive program delivery.'
    },
    {
        'year': '2022-23',
        'file': '7) Kshamtalaya Annual Report 2022-23.pdf',
        'slug': 'annual-report-2022-23.pdf',
        'highlight': 'System Strengthening',
        'color': '#01BADE',
        'icon': '⚙️',
        'desc': 'Building systemic excellence through curriculum reform and teacher leadership.'
    },
    {
        'year': '2023-24',
        'file': '8) Kshamtalaya Annual Report 2023-24.pdf',
        'slug': 'annual-report-2023-24.pdf',
        'highlight': 'Scaling Excellence',
        'color': '#E94E77',
        'icon': '🚀',
        'desc': 'Scaling Schools of Excellence and deepening well-being curriculum integration.'
    },
    {
        'year': '2024-25',
        'file': 'Annual Report 2024-25.pdf',
        'slug': 'annual-report-2024-25.pdf',
        'highlight': 'Latest Impact',
        'color': '#FFC72C',
        'icon': '⭐',
        'desc': 'Our most recent year — 100 Schools of Excellence and growing national partnerships.'
    },
]

# Copy files
for r in reports:
    src = os.path.join(src_dir, r['file'])
    dst = os.path.join(dst_dir, r['slug'])
    if os.path.exists(src):
        shutil.copy2(src, dst)
        print(f"  OK Copied {r['file']} -> {r['slug']}")
    else:
        print(f"  MISSING: {r['file']}")


# ── 2. Build HTML section ────────────────────────────────────────

# Build individual book cards
books_html = ''
for i, r in enumerate(reports):
    delay = i * 0.08
    books_html += f'''
              <div class="ar-book" style="--book-color: {r['color']}; animation-delay: {delay:.2f}s;" onclick="openReportModal({i})">
                <div class="ar-book-spine">
                  <span class="ar-book-spine-year">{r['year']}</span>
                </div>
                <div class="ar-book-front">
                  <div class="ar-book-icon">{r['icon']}</div>
                  <div class="ar-book-year">{r['year']}</div>
                  <div class="ar-book-tag" style="background: {r['color']}20; color: {r['color']};">{r['highlight']}</div>
                  <div class="ar-book-label">Annual Report</div>
                </div>
              </div>'''

# Build modal data as JS array
modal_data_js = 'const arReportsData = [\n'
for r in reports:
    modal_data_js += f'  {{ year: "{r["year"]}", highlight: "{r["highlight"]}", color: "{r["color"]}", icon: "{r["icon"]}", desc: "{r["desc"]}", pdf: "/assets/reports/{r["slug"]}" }},\n'
modal_data_js += '];'

section_html = f'''
    <!-- ════════════════════════════════════════ -->
    <!-- ANNUAL REPORTS                           -->
    <!-- ════════════════════════════════════════ -->
    <section class="section" id="annual-reports" aria-label="Annual Reports" style="background: linear-gradient(180deg, #1A1A2E 0%, #16213E 50%, #0F3460 100%); padding: 6rem 0; position: relative; overflow: hidden;">

      <!-- Ambient decorations -->
      <div style="position:absolute; top:0; left:0; width:100%; height:100%; pointer-events:none; overflow:hidden;">
        <div style="position:absolute; top:-80px; right:-80px; width:300px; height:300px; background: radial-gradient(circle, rgba(56,182,255,0.12) 0%, transparent 70%); border-radius:50%;"></div>
        <div style="position:absolute; bottom:-60px; left:-60px; width:250px; height:250px; background: radial-gradient(circle, rgba(255,199,44,0.1) 0%, transparent 70%); border-radius:50%;"></div>
        <!-- Floating particles -->
        <div class="ar-particle" style="top:15%; left:10%; animation-delay:0s;"></div>
        <div class="ar-particle" style="top:25%; right:15%; animation-delay:1.5s;"></div>
        <div class="ar-particle" style="bottom:20%; left:25%; animation-delay:3s;"></div>
        <div class="ar-particle" style="top:60%; right:30%; animation-delay:4.5s;"></div>
        <div class="ar-particle" style="bottom:35%; right:8%; animation-delay:2s;"></div>
      </div>

      <style>
        /* ── Floating particles ── */
        .ar-particle {{
          position: absolute;
          width: 4px; height: 4px;
          background: rgba(255,255,255,0.25);
          border-radius: 50%;
          animation: ar-float 8s infinite ease-in-out;
        }}
        @keyframes ar-float {{
          0%, 100% {{ transform: translateY(0) scale(1); opacity: 0.2; }}
          50% {{ transform: translateY(-40px) scale(1.5); opacity: 0.6; }}
        }}

        /* ── Section header ── */
        .ar-header {{
          text-align: center;
          position: relative;
          z-index: 2;
          margin-bottom: 3.5rem;
        }}
        .ar-eyebrow {{
          display: inline-block;
          padding: 6px 18px;
          background: rgba(255,199,44,0.15);
          border: 1px solid rgba(255,199,44,0.3);
          border-radius: 50px;
          font-size: 0.85rem;
          font-weight: 700;
          color: #FFC72C;
          letter-spacing: 1.5px;
          text-transform: uppercase;
          margin-bottom: 1.25rem;
        }}
        .ar-title {{
          font-family: 'Baloo 2', cursive;
          font-size: clamp(2.2rem, 4.5vw, 3.4rem);
          color: #ffffff;
          line-height: 1.15;
          margin-bottom: 1rem;
        }}
        .ar-title span {{
          background: linear-gradient(135deg, #38B6FF, #FFC72C);
          -webkit-background-clip: text;
          -webkit-text-fill-color: transparent;
          background-clip: text;
        }}
        .ar-subtitle {{
          font-size: 1.15rem;
          color: rgba(255,255,255,0.65);
          max-width: 600px;
          margin: 0 auto;
          line-height: 1.6;
        }}

        /* ── Bookshelf ── */
        .ar-bookshelf-wrapper {{
          position: relative;
          z-index: 2;
          max-width: 1200px;
          margin: 0 auto;
          padding: 0 1.5rem;
        }}
        .ar-shelf {{
          display: flex;
          align-items: flex-end;
          justify-content: center;
          gap: 0;
          padding: 2rem 1rem 0;
          position: relative;
          flex-wrap: wrap;
        }}
        /* Wooden shelf bar */
        .ar-shelf::after {{
          content: '';
          position: absolute;
          bottom: 0;
          left: 0;
          right: 0;
          height: 18px;
          background: linear-gradient(180deg, #8B6914 0%, #6B4F0A 40%, #4A3508 100%);
          border-radius: 0 0 8px 8px;
          box-shadow: 0 6px 20px rgba(0,0,0,0.5), inset 0 2px 4px rgba(255,255,255,0.15);
        }}

        /* ── Book card ── */
        .ar-book {{
          width: 110px;
          height: 260px;
          perspective: 800px;
          cursor: pointer;
          position: relative;
          z-index: 1;
          transition: z-index 0s;
          animation: ar-book-appear 0.6s ease backwards;
          margin: 0 -2px;
        }}
        @keyframes ar-book-appear {{
          from {{ opacity: 0; transform: translateY(30px); }}
          to {{ opacity: 1; transform: translateY(0); }}
        }}
        .ar-book:hover {{
          z-index: 10;
        }}

        /* Spine (visible by default) */
        .ar-book-spine {{
          position: absolute;
          top: 0; left: 0;
          width: 100%;
          height: 100%;
          background: linear-gradient(135deg, var(--book-color), color-mix(in srgb, var(--book-color) 70%, #000));
          border-radius: 4px 8px 8px 4px;
          display: flex;
          align-items: center;
          justify-content: center;
          transition: all 0.5s cubic-bezier(0.34, 1.56, 0.64, 1);
          box-shadow: 2px 4px 12px rgba(0,0,0,0.4), inset -2px 0 4px rgba(0,0,0,0.2), inset 2px 0 4px rgba(255,255,255,0.1);
          transform-origin: left center;
          border-left: 4px solid rgba(0,0,0,0.3);
        }}
        .ar-book-spine-year {{
          writing-mode: vertical-rl;
          text-orientation: mixed;
          color: rgba(255,255,255,0.95);
          font-family: 'Baloo 2', cursive;
          font-size: 1.15rem;
          font-weight: 700;
          letter-spacing: 2px;
          text-shadow: 0 2px 4px rgba(0,0,0,0.4);
        }}

        /* Front face (revealed on hover) */
        .ar-book-front {{
          position: absolute;
          top: 0; left: 0;
          width: 180px;
          height: 100%;
          background: #fff;
          border-radius: 4px 12px 12px 4px;
          padding: 1.5rem 1rem;
          display: flex;
          flex-direction: column;
          align-items: center;
          justify-content: center;
          gap: 0.5rem;
          opacity: 0;
          pointer-events: none;
          transform: rotateY(-30deg);
          transform-origin: left center;
          transition: all 0.5s cubic-bezier(0.34, 1.56, 0.64, 1);
          box-shadow: 8px 8px 25px rgba(0,0,0,0.5);
        }}

        .ar-book:hover .ar-book-spine {{
          transform: rotateY(-50deg);
          box-shadow: 8px 4px 20px rgba(0,0,0,0.5);
        }}
        .ar-book:hover .ar-book-front {{
          opacity: 1;
          pointer-events: auto;
          transform: rotateY(0deg) translateX(5px);
        }}

        .ar-book-icon {{
          font-size: 2.2rem;
          margin-bottom: 0.25rem;
        }}
        .ar-book-year {{
          font-family: 'Baloo 2', cursive;
          font-size: 1.3rem;
          font-weight: 800;
          color: #2D2D2E;
        }}
        .ar-book-tag {{
          font-size: 0.7rem;
          font-weight: 700;
          padding: 3px 10px;
          border-radius: 50px;
          text-align: center;
          white-space: nowrap;
        }}
        .ar-book-label {{
          font-size: 0.7rem;
          font-weight: 600;
          color: #888;
          text-transform: uppercase;
          letter-spacing: 1px;
        }}

        /* ── Timeline dots ── */
        .ar-timeline {{
          display: flex;
          justify-content: center;
          gap: 0;
          margin-top: 2rem;
          position: relative;
          z-index: 2;
          padding: 0 1.5rem;
          flex-wrap: wrap;
        }}
        .ar-timeline-item {{
          display: flex;
          flex-direction: column;
          align-items: center;
          width: 110px;
          margin: 0 -2px;
        }}
        .ar-timeline-line {{
          width: 100%;
          height: 2px;
          background: linear-gradient(90deg, transparent, rgba(255,255,255,0.2), transparent);
          position: relative;
          display: flex;
          align-items: center;
          justify-content: center;
        }}
        .ar-timeline-dot {{
          width: 12px;
          height: 12px;
          border-radius: 50%;
          background: var(--dot-color);
          box-shadow: 0 0 12px var(--dot-color);
          position: absolute;
          transition: all 0.3s ease;
        }}
        .ar-timeline-item:hover .ar-timeline-dot {{
          transform: scale(1.5);
          box-shadow: 0 0 24px var(--dot-color);
        }}
        .ar-timeline-year {{
          font-size: 0.75rem;
          color: rgba(255,255,255,0.5);
          margin-top: 0.75rem;
          font-weight: 600;
        }}

        /* ── Modal ── */
        .ar-modal-overlay {{
          display: none;
          position: fixed;
          top: 0; left: 0;
          width: 100%; height: 100%;
          background: rgba(0,0,0,0.7);
          backdrop-filter: blur(8px);
          -webkit-backdrop-filter: blur(8px);
          z-index: 10000;
          align-items: center;
          justify-content: center;
          padding: 2rem;
          animation: ar-modal-fadein 0.3s ease;
        }}
        .ar-modal-overlay.active {{
          display: flex;
        }}
        @keyframes ar-modal-fadein {{
          from {{ opacity: 0; }}
          to {{ opacity: 1; }}
        }}
        .ar-modal-card {{
          background: #ffffff;
          border-radius: 24px;
          max-width: 480px;
          width: 100%;
          padding: 3rem 2.5rem;
          position: relative;
          text-align: center;
          box-shadow: 0 30px 60px rgba(0,0,0,0.4);
          animation: ar-modal-pop 0.4s cubic-bezier(0.34, 1.56, 0.64, 1);
        }}
        @keyframes ar-modal-pop {{
          from {{ opacity: 0; transform: scale(0.85) translateY(20px); }}
          to {{ opacity: 1; transform: scale(1) translateY(0); }}
        }}
        .ar-modal-close {{
          position: absolute;
          top: 1rem; right: 1rem;
          width: 36px; height: 36px;
          border: none;
          background: #f5f5f7;
          border-radius: 50%;
          cursor: pointer;
          font-size: 1.2rem;
          color: #666;
          display: flex;
          align-items: center;
          justify-content: center;
          transition: all 0.2s;
        }}
        .ar-modal-close:hover {{
          background: #e5e5e7;
          color: #333;
          transform: rotate(90deg);
        }}
        .ar-modal-icon {{
          font-size: 3rem;
          margin-bottom: 0.5rem;
        }}
        .ar-modal-year {{
          font-family: 'Baloo 2', cursive;
          font-size: 2rem;
          font-weight: 800;
          color: #2D2D2E;
          margin-bottom: 0.25rem;
        }}
        .ar-modal-tag {{
          display: inline-block;
          font-size: 0.8rem;
          font-weight: 700;
          padding: 4px 14px;
          border-radius: 50px;
          margin-bottom: 1rem;
        }}
        .ar-modal-desc {{
          font-size: 1rem;
          line-height: 1.6;
          color: #555;
          margin-bottom: 2rem;
        }}
        .ar-modal-download {{
          display: inline-flex;
          align-items: center;
          gap: 8px;
          padding: 14px 32px;
          border-radius: 50px;
          color: #ffffff;
          font-weight: 700;
          font-size: 1rem;
          text-decoration: none;
          box-shadow: 0 8px 24px rgba(0,0,0,0.15);
          transition: all 0.3s ease;
        }}
        .ar-modal-download:hover {{
          transform: translateY(-3px);
          box-shadow: 0 12px 32px rgba(0,0,0,0.25);
        }}
        .ar-modal-size {{
          font-size: 0.8rem;
          color: #999;
          margin-top: 0.75rem;
        }}

        /* ── Responsive ── */
        @media (max-width: 900px) {{
          .ar-shelf {{
            gap: 0;
            flex-wrap: wrap;
            justify-content: center;
          }}
          .ar-book {{
            width: 90px;
            height: 220px;
          }}
          .ar-book-front {{
            width: 150px;
          }}
          .ar-timeline-item {{
            width: 90px;
          }}
        }}
        @media (max-width: 600px) {{
          .ar-book {{
            width: 70px;
            height: 190px;
            margin: 0 -1px;
          }}
          .ar-book-front {{
            width: 140px;
            padding: 1rem 0.75rem;
          }}
          .ar-book-spine-year {{
            font-size: 0.9rem;
          }}
          .ar-timeline-item {{
            width: 70px;
          }}
          .ar-timeline-year {{
            font-size: 0.65rem;
          }}
          .ar-modal-card {{
            padding: 2rem 1.5rem;
          }}
        }}
      </style>

      <div class="ar-bookshelf-wrapper">
        <!-- Header -->
        <div class="ar-header reveal">
          <div class="ar-eyebrow">Transparency & Accountability</div>
          <h2 class="ar-title">Our <span>Annual Reports</span></h2>
          <p class="ar-subtitle">A decade of documenting impact — explore our journey through yearly milestones, from 2016 to 2025.</p>
        </div>

        <!-- Bookshelf -->
        <div class="ar-shelf reveal">
{books_html}
        </div>

        <!-- Timeline dots -->
        <div class="ar-timeline reveal">
''' + ''.join([f'''          <div class="ar-timeline-item">
            <div class="ar-timeline-line"><div class="ar-timeline-dot" style="--dot-color: {r['color']};"></div></div>
            <div class="ar-timeline-year">{r['year']}</div>
          </div>
''' for r in reports]) + '''        </div>
      </div>

      <!-- Modal -->
      <div class="ar-modal-overlay" id="arModal" onclick="if(event.target===this) closeReportModal()">
        <div class="ar-modal-card">
          <button class="ar-modal-close" onclick="closeReportModal()" aria-label="Close">&times;</button>
          <div class="ar-modal-icon" id="arModalIcon"></div>
          <div class="ar-modal-year" id="arModalYear"></div>
          <div class="ar-modal-tag" id="arModalTag"></div>
          <p class="ar-modal-desc" id="arModalDesc"></p>
          <a class="ar-modal-download" id="arModalDownload" href="#" target="_blank" rel="noopener noreferrer">
            <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><path d="M21 15v4a2 2 0 01-2 2H5a2 2 0 01-2-2v-4"/><polyline points="7 10 12 15 17 10"/><line x1="12" y1="15" x2="12" y2="3"/></svg>
            Download Report
          </a>
          <p class="ar-modal-size" id="arModalSize"></p>
        </div>
      </div>

      <script>
        ''' + modal_data_js + '''

        const arFileSizes = {''' + ', '.join([
            f'"{r["slug"]}": "{round(os.path.getsize(os.path.join(src_dir, r["file"])) / (1024*1024), 1)} MB"'
            for r in reports if os.path.exists(os.path.join(src_dir, r['file']))
        ]) + '''};

        function openReportModal(idx) {
          const r = arReportsData[idx];
          document.getElementById('arModalIcon').textContent = r.icon;
          document.getElementById('arModalYear').textContent = 'Annual Report ' + r.year;
          const tag = document.getElementById('arModalTag');
          tag.textContent = r.highlight;
          tag.style.background = r.color + '20';
          tag.style.color = r.color;
          document.getElementById('arModalDesc').textContent = r.desc;
          const dl = document.getElementById('arModalDownload');
          dl.href = r.pdf;
          dl.style.background = r.color;
          const slug = r.pdf.split('/').pop();
          document.getElementById('arModalSize').textContent = arFileSizes[slug] || '';
          document.getElementById('arModal').classList.add('active');
          document.body.style.overflow = 'hidden';
        }
        function closeReportModal() {
          document.getElementById('arModal').classList.remove('active');
          document.body.style.overflow = '';
        }
        document.addEventListener('keydown', function(e) {
          if (e.key === 'Escape') closeReportModal();
        });
      </script>
    </section>
'''

# ── 3. Inject into index.html ────────────────────────────────────
html_path = r"C:\Users\Saurav\Desktop\Kshamatalaya\index.html"
with open(html_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Remove old annual reports section if re-running
content = re.sub(
    r'\n\s*<!-- ════+.*?-->\s*\n\s*<!-- ANNUAL REPORTS.*?-->\s*\n\s*<!-- ════+.*?-->\s*\n.*?</section>\s*\n',
    '\n',
    content,
    flags=re.DOTALL
)

# Insert before the NEWSLETTER & CTA section
marker = '    <!-- ════════════════════════════════════════ -->\n    <!-- NEWSLETTER & CTA                         -->'
if marker in content:
    content = content.replace(marker, section_html + marker)
    print("OK: Annual Reports section inserted before Newsletter & CTA")
else:
    # Try alternate with \r\n
    marker_rn = marker.replace('\n', '\r\n')
    if marker_rn in content:
        content = content.replace(marker_rn, section_html + marker_rn)
        print("OK: Annual Reports section inserted before Newsletter & CTA (CRLF)")
    else:
        print("ERROR: Could not find Newsletter marker")

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Done! Annual Reports section has been added to index.html")
