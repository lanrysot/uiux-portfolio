import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Pattern to find the exact <a> tag and its contents inside .vshell
pattern = re.compile(r'<a href="quicken-case-study.html" style="display: block;.*?</a>', re.DOTALL)

new_a = '''<a href="quicken-case-study.html" class="cs-preview-link">
                        <img src="quicken-preview-v2.jpg" alt="Quicken Case Study" class="cs-preview-img">
                        <div class="cs-preview-overlay">
                            <h3 class="cs-preview-title">Quicken Financial Platform</h3>
                            <p class="cs-preview-subtitle">Click to view full case study</p>
                        </div>
                    </a>'''

if pattern.search(html):
    html = pattern.sub(new_a, html)
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(html)
    print("Successfully updated HTML.")
else:
    print("Pattern not found!")
