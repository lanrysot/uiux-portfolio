import glob

# The replacement block for PulseHealth
replacement = '''<a href="pulsehealth-case-study.html" style="text-decoration: none; color: inherit; display: block;">
        <div class="pcard rv d2" data-cat="product" data-id="3">
          <div class="pcard-thumb">
            <img src="pulsehealth-hero.jpg" alt="PulseHealth Case Study" style="width: 100%; height: 100%; display: block; object-fit: cover;">
            <span class="pcard-cat">Product Design</span>
            <div class="pcard-overlay">
              <div class="view-btn">View Case Study <svg width="14" height="14" viewBox="0 0 24 24" fill="none"
                  stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">
                  <path d="M5 12h14M12 5l7 7-7 7" />
                </svg></div>
            </div>
          </div>
          <div class="pcard-body">
            <p class="pcard-client">PulseHealth</p>
            <h3 class="pcard-title">PulseHealth - Healthcare Management Platform</h3>
            <p class="pcard-desc">A single connected workspace for appointments, records, imaging, and prescriptions that simplifies daily workflows for healthcare professionals.</p>
            <div class="pcard-result"><svg viewBox="0 0 24 24" width="14" height="14" fill="none" stroke="currentColor"
                stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                <polyline points="22 7 13.5 15.5 8.5 10.5 2 17" />
                <polyline points="16 7 22 7 22 13" />
              </svg><span><strong>Reduced admin time</strong> by connecting fragmented workflows</span></div>
            <div class="pcard-tags"><span class="ptag">Product Design</span><span class="ptag">Healthcare</span><span
                class="ptag">Web App</span></div>
          </div>
        </div>
        </a>'''

html_files = glob.glob('*.html')

for file in html_files:
    if file == 'pulsehealth-case-study.html':
        continue
    
    with open(file, 'r', encoding='utf-8') as f:
        html = f.read()
    
    # Let's find exactly the block for Kajota using its unique start string
    start_str = '<div class="pcard rv d2" data-cat="promo" data-id=\'3\'>'
    end_str = '<div class="pcard rv d3" data-cat="promo" data-id=\'4\'>'
    
    if start_str in html and end_str in html:
        start_idx = html.find(start_str)
        end_idx = html.find(end_str)
        
        # We need to replace html[start_idx:end_idx] with our replacement
        # BUT wait, the whitespace before end_str might be important.
        # Let's just replace from start_str up to the last </div> before end_str.
        
        # Actually it's simpler:
        new_html = html[:start_idx] + replacement + '\n\n        ' + html[end_idx:]
        with open(file, 'w', encoding='utf-8') as f:
            f.write(new_html)
        print(f"Updated {file}")

