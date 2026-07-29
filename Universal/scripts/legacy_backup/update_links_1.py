import os
import re

files = [
    r'c:\Users\angam\Downloads\sentrixa_template.webflow.io\Index\sentrixa-template.webflow.io\index.html',
    r'c:\Users\angam\Downloads\sentrixa_template.webflow.io\About\sentrixa-template.webflow.io\about.html',
    r'c:\Users\angam\Downloads\sentrixa_template.webflow.io\Services\sentrixa-template.webflow.io\services.html',
    r'c:\Users\angam\Downloads\sentrixa_template.webflow.io\Contact\sentrixa-template.webflow.io\contact.html'
]

replacements = [
    (r'href="/contact"', r'href="../../Contact/sentrixa-template.webflow.io/contact.html"'),
    (r'href="/services"', r'href="../../Services/sentrixa-template.webflow.io/services.html"'),
    (r'href="/about"', r'href="../../About/sentrixa-template.webflow.io/about.html"'),
    (r'href="/"', r'href="../../Index/sentrixa-template.webflow.io/index.html"')
]

for file_path in files:
    if os.path.exists(file_path):
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        for old, new in replacements:
            content = re.sub(old, new, content)
            
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f'Updated {file_path}')
    else:
        print(f'File not found: {file_path}')
