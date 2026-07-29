import os
import re

files = [
    r'c:\Users\angam\Downloads\sentrixa_template.webflow.io\Index\sentrixa-template.webflow.io\index.html',
    r'c:\Users\angam\Downloads\sentrixa_template.webflow.io\About\sentrixa-template.webflow.io\about.html',
    r'c:\Users\angam\Downloads\sentrixa_template.webflow.io\Services\sentrixa-template.webflow.io\services.html',
    r'c:\Users\angam\Downloads\sentrixa_template.webflow.io\Contact\sentrixa-template.webflow.io\contact.html'
]

navs = []
for file in files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
        match = re.search(r'<div class="navbar-inner">.*?(?:<div data-ix="simple-menu-button"[^>]*>.*?</div>\s*</div>)', content, re.DOTALL)
        if match:
            navs.append(match.group(0))

for i, nav in enumerate(navs):
    print(f'Nav {i} length: {len(nav)}')
