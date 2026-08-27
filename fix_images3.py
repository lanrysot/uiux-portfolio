import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace('./clients/Winifred.png', './IMG_0162.WEBP')
content = content.replace('./clients/Mr-Abraham.png', './939a849a-5476-4d8a-b4e6-8e53ff22cce0.webp')
content = content.replace('./clients/Mr-olumide.jpg', './IMG_7060.WEBP')
content = content.replace('./clients/pol.png', './WhatsApp_Image_2026-05-08_at_20_19_24.webp')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)
