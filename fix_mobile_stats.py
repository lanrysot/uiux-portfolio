import glob
import re

files = ['portfolio.html', 'business.html', 'commerce.html', 'finance.html', 'healthcare.html', 'security.html', 'technology.html']

new_style = '''
  <style>
    @media (max-width: 768px) {
      .pstats {
        display: flex !important;
        flex-wrap: nowrap !important;
        overflow: hidden !important;
        width: 100% !important;
        border: 1px solid var(--b) !important;
        border-radius: 8px !important;
        padding-bottom: 0 !important;
        margin-top: 40px !important;
      }
      .pstat {
        flex: 1 1 0 !important;
        min-width: 0 !important;
        padding: 12px 6px !important;
        border-bottom: none !important;
        border-right: 1px solid var(--b) !important;
        display: flex !important;
        flex-direction: column !important;
        justify-content: center !important;
        align-items: center !important;
        text-align: center !important;
      }
      .pstat:last-child {
        border-right: none !important;
      }
      .pstat-n {
        font-size: 18px !important;
        margin-bottom: 4px !important;
        display: block !important;
      }
      .pstat-l {
        font-size: 11px !important;
        line-height: 1.2 !important;
        display: block !important;
      }
    }
  </style>
</head>'''

old_style_pattern = re.compile(r'\s*<style>.*?@media \(max-width: 768px\) \{.*?\.pstats \{.*?</style>\s*</head>', re.DOTALL)
brands_served_pattern = re.compile(r'<div class="pstat"><span class="pstat-n" data-to="6" data-suf="\+">0\+</span><span class="pstat-l">Brands\s*Served</span></div>', re.IGNORECASE)

for file in files:
    with open(file, 'r', encoding='utf-8') as f:
        html = f.read()
    
    # Replace the old inline style block
    html = old_style_pattern.sub(new_style, html)
    
    # Remove the 'Brands Served' stat so we have 4 items just like the screenshot
    html = brands_served_pattern.sub('', html)
    
    with open(file, 'w', encoding='utf-8') as f:
        f.write(html)

print("Updated inline styles and removed 5th stat for 4-column fit")
