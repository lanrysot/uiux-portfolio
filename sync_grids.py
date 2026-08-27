import glob
import re

categories = ['business.html', 'commerce.html', 'finance.html', 'healthcare.html', 'security.html', 'technology.html']

with open('grid_block.html', 'r', encoding='utf-8') as f:
    grid_block = f.read()

for file in categories:
    with open(file, 'r', encoding='utf-8') as f:
        html = f.read()

    # Replace the grid block
    new_html = re.sub(r'<div class="grid" id="cardGrid">.*?</div>\s*</div>\s*(?:</div>\s*)?</section>', grid_block, html, flags=re.DOTALL)
    
    with open(file, 'w', encoding='utf-8') as f:
        f.write(new_html)

print("Updates applied to category pages.")
