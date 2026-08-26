import os
import re

dir_path = '.'

# 1. Remove cursor styles from CSS
css_files = [f for f in os.listdir(dir_path) if f.endswith('.css')]
for f in css_files:
    filepath = os.path.join(dir_path, f)
    with open(filepath, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Replace cursor: none with cursor: auto
    content = re.sub(r'cursor:\s*none;?', 'cursor: auto;', content)
    
    # Remove #cur and #ring CSS blocks
    content = re.sub(r'#cur\s*{[^}]*}', '', content)
    content = re.sub(r'#ring\s*{[^}]*}', '', content)
    
    with open(filepath, 'w', encoding='utf-8') as file:
        file.write(content)

# 2. Remove HTML elements and inline JS from HTML files
html_files = [f for f in os.listdir(dir_path) if f.endswith('.html')]
for f in html_files:
    filepath = os.path.join(dir_path, f)
    with open(filepath, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Remove HTML divs
    content = re.sub(r'<div id="cur"></div>\s*', '', content)
    content = re.sub(r'<div id="ring"></div>\s*', '', content)
    
    # Remove inline JS for cursor (found in case study files)
    content = re.sub(r'// Custom Cursor\s*\(function \(\) \{.*?\}\)\(\);', '', content, flags=re.DOTALL)
    
    with open(filepath, 'w', encoding='utf-8') as file:
        file.write(content)

# 3. Remove cursor JS from script.js
if os.path.exists('script.js'):
    with open('script.js', 'r', encoding='utf-8') as f:
        script_content = f.read()
    
    pattern = re.compile(r'/\*.*?CURSOR.*?\*/.*?document\.querySelectorAll.*?\}\);', re.DOTALL)
    script_content = pattern.sub('', script_content)
    
    with open('script.js', 'w', encoding='utf-8') as f:
        f.write(script_content)

print("Cursor removal script complete.")
