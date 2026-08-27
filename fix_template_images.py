import re

# Fix Plivra (revert Plivra- back to centa-)
with open('plivra-case-study.html', 'r', encoding='utf-8') as f:
    plivra = f.read()

plivra = re.sub(r'src="Plivra-', 'src="centa-', plivra, flags=re.IGNORECASE)

with open('plivra-case-study.html', 'w', encoding='utf-8') as f:
    f.write(plivra)

# Fix Push (revert Push- back to pulsehealth-)
with open('push-case-study.html', 'r', encoding='utf-8') as f:
    push = f.read()

push = re.sub(r'src="Push-', 'src="pulsehealth-', push, flags=re.IGNORECASE)

with open('push-case-study.html', 'w', encoding='utf-8') as f:
    f.write(push)

print("Restored original image paths for Plivra and Push templates.")
