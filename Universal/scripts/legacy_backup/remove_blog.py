import os
from bs4 import BeautifulSoup

base_dir = r'c:\Users\angam\Downloads\sentrixa_template.webflow.io'
files = [
    os.path.join(base_dir, r'Index\sentrixa-template.webflow.io\index.html'),
    os.path.join(base_dir, r'About\sentrixa-template.webflow.io\about.html'),
    os.path.join(base_dir, r'Services\sentrixa-template.webflow.io\services.html'),
    os.path.join(base_dir, r'Contact\sentrixa-template.webflow.io\contact.html'),
    os.path.join(base_dir, r'Error\sentrixa-template.webflow.io\404.html'),
]

for file_path in files:
    if not os.path.exists(file_path):
        continue

    with open(file_path, 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f.read(), 'lxml')

    # Remove <section class="section blog"> (and any section that contains "blog" as a class)
    removed = 0
    for section in soup.find_all('section'):
        classes = section.get('class', [])
        if 'blog' in classes:
            section.decompose()
            removed += 1

    if removed:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(str(soup))
        print(f'Removed {removed} blog section(s) from {os.path.basename(file_path)}')
    else:
        print(f'No blog section found in {os.path.basename(file_path)}, skipping.')
