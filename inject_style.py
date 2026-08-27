import glob

files = ['portfolio.html', 'business.html', 'commerce.html', 'finance.html', 'healthcare.html', 'security.html', 'technology.html']

style_block = '''
  <style>
    @media (max-width: 768px) {
      .pstats {
        display: flex !important;
        flex-wrap: nowrap !important;
        overflow-x: auto !important;
        -webkit-overflow-scrolling: touch !important;
        padding-bottom: 10px !important;
      }
      .pstats::-webkit-scrollbar {
        display: none !important;
      }
      .pstat {
        flex: 0 0 160px !important;
        min-width: 160px !important;
        border-bottom: none !important;
        border-right: 1px solid var(--b) !important;
      }
      .pstat:last-child {
        border-right: none !important;
      }
    }
  </style>
</head>'''

for file in files:
    with open(file, 'r', encoding='utf-8') as f:
        html = f.read()
        
    if '<style>' not in html:
        html = html.replace('</head>', style_block)
        
        with open(file, 'w', encoding='utf-8') as f:
            f.write(html)

print("Injected inline style block for mobile horizontal scrolling")
