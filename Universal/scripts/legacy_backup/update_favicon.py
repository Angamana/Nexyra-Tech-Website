import os
from bs4 import BeautifulSoup

base_dir = r'c:\Users\angam\Downloads\sentrixa_template.webflow.io'
files = [
    os.path.join(base_dir, r'Index\sentrixa-template.webflow.io\index.html'),
    os.path.join(base_dir, r'About\sentrixa-template.webflow.io\about.html'),
    os.path.join(base_dir, r'Services\sentrixa-template.webflow.io\services.html'),
    os.path.join(base_dir, r'Contact\sentrixa-template.webflow.io\contact.html'),
    os.path.join(base_dir, r'Error\sentrixa-template.webflow.io\404.html')
]

for file_path in files:
    if os.path.exists(file_path):
        with open(file_path, 'r', encoding='utf-8') as f:
            html_content = f.read()

        soup = BeautifulSoup(html_content, 'lxml')

        # Update <title>
        title_tag = soup.find('title')
        if title_tag:
            title_tag.string = 'Nexyra Tech'

        # Remove all old favicon/touch-icon link tags
        for link in soup.find_all('link'):
            rel = link.get('rel', [])
            if isinstance(rel, list):
                rel = ' '.join(rel).lower()
            else:
                rel = rel.lower()
            if 'icon' in rel or 'apple-touch-icon' in rel:
                link.decompose()

        # Insert fresh favicon tags into <head>
        head = soup.find('head')
        if head:
            head.append(soup.new_tag('link', rel='icon', type='image/png', href='../../logo.png'))
            head.append(soup.new_tag('link', rel='shortcut icon', type='image/png', href='../../logo.png'))
            head.append(soup.new_tag('link', rel='apple-touch-icon', href='../../logo.png'))

        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(str(soup))

        print(f'Updated {os.path.basename(file_path)}')
