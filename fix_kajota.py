import re
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
    
    # We need to find the <div class="pcard ..."> that contains Kajota, and replace the WHOLE block.
    # Since HTML can be tricky, let's use a regex that matches from <div class="pcard to the end of its </div>
    # Usually it's:
    # <div class="pcard rv d2" data-cat="promo" data-id='3'>
    # ...
    # </div>
    
    # Let's find the starting index of the pcard that contains Kajota
    if 'Kajota' in html:
        # regex to match the pcard block
        # Look for <div class="pcard" ... up to the end of the tags div and its closing div
        pattern = re.compile(r'<div class="pcard[^>]*>.*?<p class="pcard-client">Kajota</p>.*?</div>\s*</div>\s*</div>', re.DOTALL)
        
        # Test if it matches
        new_html = pattern.sub(replacement, html)
        
        if new_html != html:
            with open(file, 'w', encoding='utf-8') as f:
                f.write(new_html)
            print(f"Updated {file}")
        else:
            print(f"Could not replace in {file}")

