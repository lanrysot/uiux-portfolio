import glob
import re

html_files = glob.glob('*.html')

for file in html_files:
    if 'case-study' in file or file == 'index.html':
        continue
        
    with open(file, 'r', encoding='utf-8') as f:
        html = f.read()

    # 1. EVERSEND
    # Wrap in anchor and replace iframe with quicken image
    # Note: data-id='4' is Eversend
    eversend_pattern = re.compile(r'(<div class="pcard rv [^"]+" data-cat="[^"]+" data-id=\'4\'>\s*<div class="pcard-thumb">\s*)<iframe[^>]+></iframe>', re.DOTALL)
    if 'Eversend' in html and not 'eversend-case-study.html' in html:
        html = eversend_pattern.sub(r'<a href="eversend-case-study.html" style="text-decoration: none; color: inherit; display: block;">\n          \g<1><img src="quicken-preview-v2.jpg" alt="Eversend Case Study" style="width: 100%; height: 100%; display: block; object-fit: cover;">', html)
        # Close the anchor after the pcard block
        # The block ends before the next <!-- CARD 5 --> or the end of the container
        # Better yet, since we know it ends with </div> just before CARD 5:
        html = re.sub(r'(<p class="pcard-client">Eversend</p>.*?</div>\s*</div>)', r'\g<1>\n        </a>', html, flags=re.DOTALL)

    # 2. PLIVRA (data-id='5')
    plivra_pattern = re.compile(r'(<div class="pcard rv [^"]+" data-cat="[^"]+" data-id=\'5\'>\s*<div class="pcard-thumb">\s*)<iframe[^>]+></iframe>', re.DOTALL)
    if 'Plivra' in html and not 'plivra-case-study.html' in html:
        html = plivra_pattern.sub(r'<a href="plivra-case-study.html" style="text-decoration: none; color: inherit; display: block;">\n          \g<1><img src="centa-hero-mockup.png" alt="Plivra Case Study" style="width: 100%; height: 100%; display: block; object-fit: cover;">', html)
        html = re.sub(r'(<p class="pcard-client">Plivra</p>.*?</div>\s*</div>)', r'\g<1>\n        </a>', html, flags=re.DOTALL)

    # 3. PUSH (data-id='6')
    push_pattern = re.compile(r'(<div class="pcard rv [^"]+" data-cat="[^"]+" data-id=\'6\'>\s*<div class="pcard-thumb">\s*)<iframe[^>]+></iframe>', re.DOTALL)
    if 'Push' in html and not 'push-case-study.html' in html:
        html = push_pattern.sub(r'<a href="push-case-study.html" style="text-decoration: none; color: inherit; display: block;">\n          \g<1><img src="pulsehealth-hero.jpg" alt="Push Case Study" style="width: 100%; height: 100%; display: block; object-fit: cover;">', html)
        html = re.sub(r'(<p class="pcard-client">Push</p>.*?</div>\s*</div>)', r'\g<1>\n        </a>', html, flags=re.DOTALL)

    with open(file, 'w', encoding='utf-8') as f:
        f.write(html)

print("Updates completed.")
