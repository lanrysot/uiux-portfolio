import re

with open('portfolio.html', 'r', encoding='utf-8') as f:
    html = f.read()

match = re.search(r'(<div class="grid" id="cardGrid">.*?</div>\s*</div>\s*</section>)', html, re.DOTALL)
if match:
    print("Found the grid block")
    with open('grid_block.html', 'w', encoding='utf-8') as out:
        out.write(match.group(1))
else:
    print("Not found")
