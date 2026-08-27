import glob
import re

files = ['portfolio.html', 'business.html', 'commerce.html', 'finance.html', 'healthcare.html', 'security.html', 'technology.html']

new_style = '''
  <style>
    @media (max-width: 768px) {
      .pstats {
        display: grid !important;
        grid-template-columns: repeat(2, 1fr) !important;
        width: 100% !important;
        border: 1px solid var(--b) !important;
        border-radius: 12px !important;
        margin-top: 40px !important;
        padding: 0 !important;
        overflow: hidden !important;
      }
      .pstat {
        border: none !important;
        border-bottom: 1px solid var(--b) !important;
        border-right: 1px solid var(--b) !important;
        padding: 24px 12px !important;
        display: flex !important;
        flex-direction: column !important;
        justify-content: center !important;
        align-items: center !important;
        text-align: center !important;
      }
      .pstat:nth-child(even) {
        border-right: none !important;
      }
      .pstat:nth-child(5) {
        grid-column: 1 / -1 !important;
        border-bottom: none !important;
        border-right: none !important;
      }
      .pstat-n {
        font-size: 26px !important;
        margin-bottom: 6px !important;
        display: block !important;
      }
      .pstat-l {
        font-size: 12px !important;
        line-height: 1.4 !important;
        display: block !important;
      }
    }
  </style>
</head>'''

# Using regex to find the old <style> block and replace it
old_style_pattern = re.compile(r'\s*<style>.*?@media \(max-width: 768px\) \{.*?\.pstats \{.*?</style>\s*</head>', re.DOTALL)

for file in files:
    with open(file, 'r', encoding='utf-8') as f:
        html = f.read()
    
    html = old_style_pattern.sub(new_style, html)
    
    with open(file, 'w', encoding='utf-8') as f:
        f.write(html)

print("Updated inline styles to a responsive 2x2+1 grid layout")
