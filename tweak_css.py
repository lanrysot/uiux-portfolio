import glob
import re

files = ['portfolio.html', 'business.html', 'commerce.html', 'finance.html', 'healthcare.html', 'security.html', 'technology.html']

for file in files:
    with open(file, 'r', encoding='utf-8') as f:
        html = f.read()

    # Modify the font sizes and padding in the inline style for 5 items
    html = html.replace('padding: 12px 6px !important;', 'padding: 10px 2px !important;')
    html = html.replace('font-size: 18px !important;', 'font-size: 16px !important;')
    html = html.replace('font-size: 11px !important;', 'font-size: 9px !important;')

    with open(file, 'w', encoding='utf-8') as f:
        f.write(html)

print("Adjusted CSS to fit 5 items")
