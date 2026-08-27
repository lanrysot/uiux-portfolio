import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Healthcare update
# Find the healthcare block and replace its image
# <a href="./healthcare.html"...
# ... background-image: url('./cs-before-after.png');
html = re.sub(
    r'(<a href="\./healthcare\.html"[\s\S]*?background-image:\s*url\(\')(.*?)(\'\))',
    r'\g<1>./pulsehealth-hero.jpg\g<3>',
    html
)

# 2. Swap Technology and Business images
# Tech currently has centa-hero-mockup.png
# Biz currently has cs-imac-mockup.png
# Let's replace them specifically within their anchors

html = re.sub(
    r'(<a href="\./technology\.html"[\s\S]*?background-image:\s*url\(\').*?(\'\))',
    r'\g<1>./cs-imac-mockup.png\g<2>',
    html
)

html = re.sub(
    r'(<a href="\./business\.html"[\s\S]*?background-image:\s*url\(\').*?(\'\))',
    r'\g<1>./centa-hero-mockup.png\g<2>',
    html
)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
