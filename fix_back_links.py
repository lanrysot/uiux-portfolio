import glob
import re

files = glob.glob('*-case-study.html')

for file in files:
    with open(file, 'r', encoding='utf-8') as f:
        html = f.read()

    # Replace <a href="index.html" ... >Back to Portfolio</a> with portfolio.html
    # This regex looks for href="index.html" inside an anchor tag that has "Back to Portfolio" in its text content
    html = re.sub(r'<a\s+href="index\.html"([^>]*)>(.*?Back to Portfolio.*?)</a>', 
                  r'<a href="portfolio.html"\1>\2</a>', 
                  html, flags=re.IGNORECASE)

    # Replace <a href="index.html" class="back-btn">Back to Portfolio</a> specifically if the previous didn't catch it
    html = html.replace('href="index.html" class="back-btn"', 'href="portfolio.html" class="back-btn"')
    html = html.replace('href="index.html" class="nav-cta">&#8592; Back to Portfolio', 'href="portfolio.html" class="nav-cta">&#8592; Back to Portfolio')
    
    with open(file, 'w', encoding='utf-8') as f:
        f.write(html)

print("Updated links to point to portfolio.html")
