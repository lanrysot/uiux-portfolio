import re

with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Remove the old hover styles I added
css = re.sub(r'/\* SC Hover Overlay \*/.*?\.sc:hover \.sc-hover-btn \{\s*transform: translateY\(0\);\s*\}', '', css, flags=re.DOTALL)

# Change .srv-grid from 3 columns to 2 columns on desktop
css = re.sub(r'(\.srv-grid\s*\{\s*display:\s*grid;\s*grid-template-columns:\s*)repeat\(3,\s*1fr\)', r'\g<1>repeat(2, 1fr)', css)

# Add the new .sc-thumb and .sc-overlay styles
new_styles = '''
/* SC Thumb Layout */
.sc-thumb {
    position: relative;
    aspect-ratio: 16/9;
    overflow: hidden;
    background: var(--bg2);
    margin: -50px -40px 30px -40px;
    border-bottom: 1px solid var(--b);
}
@media (max-width: 768px) {
    .sc-thumb {
        margin: -30px -20px 20px -20px;
    }
}
.sc-overlay {
    position: absolute;
    inset: 0;
    background: rgba(3, 7, 20, .85);
    display: flex;
    align-items: center;
    justify-content: center;
    opacity: 0;
    transition: opacity .35s;
    backdrop-filter: blur(4px);
}
.sc:hover .sc-overlay {
    opacity: 1;
}
.sc-view-btn {
    background: var(--ac);
    color: #fff;
    padding: 10px 20px;
    font-size: 13px;
    font-weight: 700;
    border-radius: 6px;
    display: inline-flex;
    align-items: center;
    gap: 8px;
    transform: translateY(16px);
    transition: transform .35s;
}
.sc:hover .sc-view-btn {
    transform: translateY(0);
}
'''

css += new_styles

with open('style.css', 'w', encoding='utf-8') as f:
    f.write(css)

print("Updated style.css")
