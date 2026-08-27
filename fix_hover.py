import re

# 1. Update index.html
with open('index.html', 'r', encoding='utf-8') as f:
    html_content = f.read()

# Define the overlay HTML
overlay = '''<div class="sc-hover-overlay">
    <span class="sc-hover-btn">CLICK TO SEE MORE PROJECT &rarr;</span>
</div>'''

# We need to insert this right before the closing </a> of the .sc links.
# The .sc links are wrapped as: <a href="..." class="sc ..."> ... </a>
# We can use regex to find these blocks.
def replace_sc(match):
    inner = match.group(1)
    # Ensure we don't insert it multiple times if run twice
    if 'sc-hover-overlay' in inner:
        return match.group(0)
    return f'{inner}\n                        {overlay}\n                    </a>'

html_content = re.sub(r'(<a href="[^"]+\.html"[^>]*class="sc [^"]*"[^>]*>.*?)(</a>)', replace_sc, html_content, flags=re.DOTALL)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

# 2. Update style.css
with open('style.css', 'r', encoding='utf-8') as f:
    css_content = f.read()

if '.sc-hover-overlay' not in css_content:
    hover_css = '''
/* SC Hover Overlay */
.sc .sc-hover-overlay {
    position: absolute;
    inset: 0;
    background: rgba(3, 7, 20, 0.85);
    display: flex;
    align-items: center;
    justify-content: center;
    opacity: 0;
    transition: opacity 0.3s ease;
    z-index: 10;
}
.sc:hover .sc-hover-overlay {
    opacity: 1;
}
.sc-hover-btn {
    background: var(--ac);
    color: #fff;
    padding: 12px 24px;
    font-size: 13px;
    font-weight: 700;
    border-radius: 4px;
    text-transform: uppercase;
    letter-spacing: 0.5px;
    transform: translateY(20px);
    transition: transform 0.3s ease;
}
.sc:hover .sc-hover-btn {
    transform: translateY(0);
}
'''
    css_content += hover_css
    with open('style.css', 'w', encoding='utf-8') as f:
        f.write(css_content)

print("Updated index.html and style.css")
