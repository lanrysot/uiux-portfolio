import re

with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Replace the specific repeat(2, 1fr) with repeat(3, 1fr) for .srv-grid
# We only want to replace the first two matches (the desktop ones), leaving the @media one alone.
css = re.sub(r'(\.srv-grid\s*\{\s*display:\s*grid;\s*grid-template-columns:\s*)repeat\(2,\s*1fr\)', r'\g<1>repeat(3, 1fr)', css)

with open('style.css', 'w', encoding='utf-8') as f:
    f.write(css)

print("Updated grid to 3 columns")
