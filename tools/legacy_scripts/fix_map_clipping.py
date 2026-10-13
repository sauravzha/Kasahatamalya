import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace map container in index.html to fix lower part clipping & move map up
old_map_html = '''          <!-- Left: Map -->
          <div class="impact-map-col reveal">
            <div class="map-3d-container" style="margin: 0 auto; width: 100%; height: 440px; position: relative;">
              <div class="map-3d" style="animation: float 6s ease-in-out infinite; width: 100%; height: 100%;">
                <!-- Accurate India Map SVG -->
                <img src="/assets/india-map.svg" alt="Map of India" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; object-fit: contain; filter: drop-shadow(0 20px 30px rgba(0,0,0,0.15));" />
                
                <!-- Pins -->
                <!-- Rajasthan -->
                <div class="map-dot" style="top: 40%; left: 22%; --state-color: #1CA6A0;" title="Rajasthan" onclick="switchStateDeck('rj')"></div>
                <!-- Delhi -->
                <div class="map-dot" style="top: 30%; left: 30%; --state-color: #38B6FF;" title="Delhi" onclick="switchStateDeck('dl')"></div>
                <!-- Bihar -->
                <div class="map-dot" style="top: 40%; left: 56%; --state-color: #FFC72C;" title="Bihar" onclick="switchStateDeck('br')"></div>
              </div>
            </div>
          </div>'''

new_map_html = '''          <!-- Left: Map -->
          <div class="impact-map-col reveal">
            <div class="map-3d-container" style="margin: 0 auto; width: 100%; height: 480px; position: relative; top: -15px;">
              <div class="map-3d" style="animation: float 6s ease-in-out infinite; width: 100%; height: 100%; position: relative;">
                <!-- Accurate India Map SVG -->
                <img src="/assets/india-map.svg" alt="Map of India" style="position: absolute; top: 0; left: 0; width: 100%; height: 95%; object-fit: contain; object-position: center top; filter: drop-shadow(0 15px 25px rgba(0,0,0,0.12));" />
                
                <!-- Pins -->
                <!-- Rajasthan -->
                <div class="map-dot" style="top: 36%; left: 22%; --state-color: #1CA6A0;" title="Rajasthan" onclick="switchStateDeck('rj')"></div>
                <!-- Delhi -->
                <div class="map-dot" style="top: 26%; left: 30%; --state-color: #38B6FF;" title="Delhi" onclick="switchStateDeck('dl')"></div>
                <!-- Bihar -->
                <div class="map-dot" style="top: 36%; left: 56%; --state-color: #FFC72C;" title="Bihar" onclick="switchStateDeck('br')"></div>
              </div>
            </div>
          </div>'''

content = content.replace(old_map_html, new_map_html)

# Also adjust section padding on #impact-map section
content = content.replace(
    'section class="section" id="impact-map" aria-label="Our Geographical Reach" style="overflow: hidden; background: linear-gradient(135deg, #08B9DB 0%, #0194B1 100%); padding: 5rem 0;"',
    'section class="section" id="impact-map" aria-label="Our Geographical Reach" style="overflow: hidden; background: linear-gradient(135deg, #08B9DB 0%, #0194B1 100%); padding: 4.5rem 0 6rem 0;"'
)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print('Successfully fixed map height, padding & upward position in index.html!')
