import re

with open('style.css', 'r', encoding='utf-8') as f:
    content = f.read()

replacement = '''
    .hero-stats {
        flex-direction: row;
    }
    .h-stat {
        border-right: 1px solid var(--b);
        border-bottom: none;
        padding: 12px 6px;
        text-align: center;
    }
    .h-stat:last-child {
        border-right: none;
    }
    .h-stat-num {
        font-size: 18px;
    }
    .h-stat-label {
        font-size: 9px;
    }
'''

pattern = re.compile(r'\.hero-stats\s*\{\s*flex-direction:\s*column\s*\}\s*\.h-stat\s*\{\s*border-right:\s*none;\s*border-bottom:\s*1px solid var\(--b\)\s*\}')

content = pattern.sub(replacement.strip(), content)

with open('style.css', 'w', encoding='utf-8') as f:
    f.write(content)
