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
        
        # 1. Remove pricing plan sections
        pricing_sections = soup.find_all('section', class_=lambda c: c and 'pricing' in c.lower())
        for section in pricing_sections:
            section.decompose()
            
        # 2. Update "Start Free" buttons to point to Contact page
        for a in soup.find_all('a'):
            text = a.get_text(strip=True).lower()
            if text == 'start free':
                a['href'] = '../../Contact/sentrixa-template.webflow.io/contact.html'
                
        # 3. Clean up the word "pricing" in contact text
        for text_node in soup.find_all(string=True):
            if text_node.parent and text_node.parent.name in ['script', 'style']:
                continue
            if 'pricing,' in text_node:
                new_text = text_node.replace('pricing, ', '')
                text_node.replace_with(new_text)
            elif 'pricing' in text_node.lower() and ('platform' in text_node.lower() or 'questions' in text_node.lower()):
                new_text = text_node.replace('pricing,', '').replace(' pricing', '')
                text_node.replace_with(new_text)

        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(str(soup))
            
print("Pricing sections removed and CTA buttons updated.")
