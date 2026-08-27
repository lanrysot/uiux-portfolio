import re

with open('pulsehealth-case-study.html', 'r', encoding='utf-8') as f:
    html = f.read()

target = '''<div style="display: flex; gap: 16px; flex-wrap: wrap; margin-top: 40px;">
            <a href="portfolio.html" class="back-btn">Back to Portfolio</a>
        </div>'''

replacement = '''<div style="display: flex; gap: 16px; flex-wrap: wrap; margin-top: 40px;">
            <a href="portfolio.html" class="back-btn">Back to Portfolio</a>
            <a href="https://www.figma.com/proto/OKvRbi33FoMc1lxZlJpfVh/PulseHealth---Your-Digital-Health-Companion?node-id=4957-194636&p=f&t=xwvzcon79emuaO46-0&scaling=min-zoom&content-scaling=fixed&page-id=57%3A65743&starting-point-node-id=4957%3A199201" target="_blank" rel="noopener" class="back-btn" style="background: transparent; border: 1px solid var(--ac, #a482fb); color: #fff;">View Prototype</a>
        </div>'''

html = html.replace(target, replacement)

with open('pulsehealth-case-study.html', 'w', encoding='utf-8') as f:
    f.write(html)
