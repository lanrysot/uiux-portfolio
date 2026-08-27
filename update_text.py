with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace Seven steps -> My Seven steps
html = html.replace('Seven steps.<br>Workflow.', 'My Seven steps.<br>Workflow.')
# Also replace in case it's written differently somewhere
html = html.replace('Seven Steps Workflow', 'My Seven Steps Workflow')

# Replace Why Clients Choose Me -> Why Choose Me
html = html.replace('Why Clients Choose Me', 'Why Choose Me')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Updated texts in index.html")
