import glob
import re

files = ['portfolio.html', 'business.html', 'commerce.html', 'finance.html', 'healthcare.html', 'security.html', 'technology.html']

target_pattern = re.compile(r'(<div class="pstat"><span class="pstat-n" data-to="3" data-suf="">0</span><span class="pstat-l">Industries)', re.IGNORECASE)

brand_stat = '''<div class="pstat"><span class="pstat-n" data-to="6" data-suf="+">0+</span><span class="pstat-l">Brands
            Served</span></div>
        '''

for file in files:
    with open(file, 'r', encoding='utf-8') as f:
        html = f.read()
    
    # Only insert if it doesn't already exist
    if 'Brands' not in html or 'Brands Served' not in html:
        html = target_pattern.sub(brand_stat + r'\g<1>', html)
        
        with open(file, 'w', encoding='utf-8') as f:
            f.write(html)

print("Re-added the 5th stat for 5-column layout")
