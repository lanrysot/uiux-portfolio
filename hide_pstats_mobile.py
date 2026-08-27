import glob
import re

files = ['portfolio.html', 'business.html', 'commerce.html', 'finance.html', 'healthcare.html', 'security.html', 'technology.html']

new_style = '''
  <style>
    @media (max-width: 768px) {
      .pstats {
        display: none !important;
      }
    }
  </style>
</head>'''

# Match any inline style we previously added that touches .pstats inside a max-width 768 media query
old_style_pattern = re.compile(r'\s*<style>\s*@media \(max-width: 768px\) \{\s*\.pstats.*?</style>\s*</head>', re.DOTALL)

for file in files:
    with open(file, 'r', encoding='utf-8') as f:
        html = f.read()
    
    html = old_style_pattern.sub(new_style, html)
    
    with open(file, 'w', encoding='utf-8') as f:
        f.write(html)

print("Updated inline styles to hide .pstats on mobile")
