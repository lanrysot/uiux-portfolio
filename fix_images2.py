import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace('./IMG_0162.WEBP', './clients/Winifred.png')
content = content.replace('./939a849a-5476-4d8a-b4e6-8e53ff22cce0.webp', './clients/Mr-Abraham.png')
content = content.replace('./IMG_7060.WEBP', './clients/Mr-olumide.jpg')
content = content.replace('./WhatsApp_Image_2026-05-08_at_20_19_24.webp', './clients/pol.png')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)
