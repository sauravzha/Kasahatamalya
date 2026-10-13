import re

html_path = r"C:\Users\Saurav\Desktop\Kshamatalaya\index.html"
with open(html_path, 'r', encoding='utf-8') as f:
    lines = f.readlines()

# Let's find the closing of the third card in the NEW grid:
# The 3rd card has: <h3 class="approach-title">Building Systemic Excellence</h3>
# Let's find it.
start_delete = -1
end_delete = -1

for i, line in enumerate(lines):
    if '<h3 class="approach-title">Building Systemic Excellence</h3>' in line:
        # Check if it's the FIRST occurrence (the good one inside approach-grid)
        if start_delete == -1:
            # We found the 3rd card in the new grid. Let's trace to its end.
            # We know its ul ends, then approach-content ends, then the card ends.
            # Then the grid ends.
            pass
        else:
            pass

# A safer approach is string replacement:
with open(html_path, 'r', encoding='utf-8') as f:
    content = f.read()

# We know the good grid ends at:
#                 <li>Partnering with state to support Assessment CELL initiatives & Module Development for Teacher Education</li>
#               </ul>
#             </div>
#           </div>
#         </div>

# And the junk starts right after that:
#             <div class="approach-icon-wrap" style="background: linear-gradient(135deg, #38B6FF, #0077B6);">1</div>
#             <div class="approach-content">

junk_start_string = '''                <li>Partnering with state to support Assessment CELL initiatives & Module Development for Teacher Education</li>
              </ul>
            </div>
          </div>
        </div>
            <div class="approach-icon-wrap" style="background: linear-gradient(135deg, #38B6FF, #0077B6);">1</div>'''

if junk_start_string in content:
    print("Found exact junk start!")
    
    # Let's find the end of the junk. It ends right before:
    #       </div>
    #     </section>
    #     <!-- ════════════════════════════════════════ -->
    #     <!-- PROGRAMS AT A GLANCE                     -->
    
    junk_end_pattern = re.compile(r'            <div class="approach-icon-wrap" style="background: linear-gradient\(135deg, #38B6FF, #0077B6\);">1</div>.*?</div>\s*</div>\s*</section>', re.DOTALL)
    
    # Wait, the junk is a bunch of cards, then </div> </div> </section>.
    # Let's just use regex to remove everything from the dangling `<div class="approach-icon-wrap"` up to right before `</div>\n    </section>`
    
    # Let's construct a pattern to match the junk
    # The junk starts with: \s*<div class="approach-icon-wrap" style="background: linear-gradient\(135deg, #38B6FF, #0077B6\);">1</div>
    # The junk ends with: \s*</div>\s*</div>\s*</section>
    
    def remove_junk():
        global content
        # Find the good grid end
        good_grid_end = '''                <li>Partnering with state to support Assessment CELL initiatives & Module Development for Teacher Education</li>
              </ul>
            </div>
          </div>
        </div>'''
        
        idx = content.find(good_grid_end)
        if idx == -1:
            return False
            
        start_junk = idx + len(good_grid_end)
        
        # Find the programs section which is right after the approach section
        programs_start = content.find('<!-- PROGRAMS AT A GLANCE')
        
        if programs_start == -1:
            return False
            
        # The section ends with </div>\n    </section> right before programs
        # So between start_junk and programs_start, we should only have 
        # </div>
        # </section>
        
        # Let's just slice it out:
        new_content = content[:start_junk] + '\n      </div>\n    </section>\n    ' + content[programs_start-49:] # -49 to grab the comment block properly, wait, just use programs_start directly:
        
        new_content = content[:start_junk] + '\n      </div>\n    </section>\n    ' + content[programs_start:]
        content = new_content
        return True

    if remove_junk():
        with open(html_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print("Successfully removed the duplicated junk!")
    else:
        print("Failed to remove junk")
else:
    print("Could not find the exact start string. Maybe it was already fixed or formatted differently.")
