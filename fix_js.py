import re

with open('project-script.js', 'r', encoding='utf-8') as file:
    content = file.read()

# Specifically target the block starting with /* emoji CURSOR emoji */
pattern = re.compile(r'/\*.[^\*]*CURSOR.[^\*]*\*/.*?\(function ar\(\).*?\}\)\(\);', re.DOTALL)
content = pattern.sub('', content)

with open('project-script.js', 'w', encoding='utf-8') as file:
    file.write(content)
