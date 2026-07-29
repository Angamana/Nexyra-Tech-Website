import os

pages = [
    r'c:\Users\angam\Downloads\Nexyra Website\Contact\Contact Us Page\contact.html',
    r'c:\Users\angam\Downloads\Nexyra Website\Error\Nexyra Website - Error\404.html',
]

OLD = 'class="footer-bottom" data-w-id="4e361a89-8bc7-799e-39f1-a7cb844f4448"'
NEW = 'class="footer-bottom" data-w-id="4e361a89-8bc7-799e-39f1-a7cb844f4448" style="opacity:1 !important; visibility:visible !important;"'

for p in pages:
    if not os.path.exists(p):
        print(f'NOT FOUND: {p}')
        continue
    with open(p, 'r', encoding='utf-8') as f:
        html = f.read()

    if 'opacity:1 !important' in html:
        print(f'Already fixed: {os.path.basename(p)}')
        continue

    if OLD in html:
        html = html.replace(OLD, NEW)
        with open(p, 'w', encoding='utf-8') as f:
            f.write(html)
        print(f'Fixed: {os.path.basename(p)}')
    else:
        print(f'Pattern not found: {os.path.basename(p)}')
