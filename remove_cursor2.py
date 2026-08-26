import os
import re

dir_path = '.'

# 1. Clean HTML files
html_files = [f for f in os.listdir(dir_path) if f.endswith('.html')]
for f in html_files:
    filepath = os.path.join(dir_path, f)
    with open(filepath, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Remove HTML divs
    content = re.sub(r'<div id="cd"></div>\s*', '', content)
    content = re.sub(r'<div id="cr"></div>\s*', '', content)
    
    with open(filepath, 'w', encoding='utf-8') as file:
        file.write(content)

# 2. Clean project-css.css
css_file = 'project-css.css'
if os.path.exists(css_file):
    with open(css_file, 'r', encoding='utf-8') as file:
        content = file.read()
    
    content = re.sub(r'#cd\s*{[^}]*}', '', content)
    content = re.sub(r'#cr\s*{[^}]*}', '', content)
    content = re.sub(r'#cr\.big\s*{[^}]*}', '', content)
    
    with open(css_file, 'w', encoding='utf-8') as file:
        file.write(content)

# 3. Clean project-script.js
js_file = 'project-script.js'
if os.path.exists(js_file):
    with open(js_file, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Remove cursor logic
    pattern = re.compile(r'/\*.*?CURSOR.*?\*/.*?/\*.*?PARTICLE CANVAS', re.DOTALL)
    content = pattern.sub('/* PARTICLE CANVAS', content)
    
    with open(js_file, 'w', encoding='utf-8') as file:
        file.write(content)

print("Second cursor removal complete.")
