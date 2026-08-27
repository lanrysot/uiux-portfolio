import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

replacement = '''<div class="rv-strip">
                    <div class="rv-thumb" style="background-image:url('./clients/Winifred.png')"></div>
                    <div class="rv-thumb" style="background-image:url('./clients/Mr-Abraham.png')"></div>
                    <div class="rv-thumb" style="background-image:url('./clients/Mr-olumide.jpg')"></div>
                    <div class="rv-thumb" style="background-image:url('./clients/pol.png')"></div>
                </div>'''

# Regex to match the entire <div class="rv-strip">...</div> block
pattern = re.compile(r'<div class="rv-strip">.*?</div>', re.DOTALL)
content = pattern.sub(replacement, content, count=1)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Images replaced in index.html")
