import glob
import re

html_files = glob.glob('*.html')

for file in html_files:
    if 'case-study' in file or file == 'index.html':
        continue
        
    with open(file, 'r', encoding='utf-8') as f:
        html = f.read()

    # Fix closing tags for eversend, plivra, push
    # Look for </a>\s*</div> and replace with </div>\n</a> but only for those cards.
    # Actually, the easier way is to just find:
    # </div>
    # </a>
    # </div>
    # and change it to
    # </div>
    # </div>
    # </a>
    html = html.replace('</div>\n        </a>\n        </div>', '</div>\n        </div>\n        </a>')
    
    with open(file, 'w', encoding='utf-8') as f:
        f.write(html)
