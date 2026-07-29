import os
from bs4 import BeautifulSoup

files = [
    r'c:\Users\angam\Downloads\sentrixa_template.webflow.io\Index\sentrixa-template.webflow.io\index.html',
    r'c:\Users\angam\Downloads\sentrixa_template.webflow.io\About\sentrixa-template.webflow.io\about.html',
    r'c:\Users\angam\Downloads\sentrixa_template.webflow.io\Services\sentrixa-template.webflow.io\services.html',
    r'c:\Users\angam\Downloads\sentrixa_template.webflow.io\Contact\sentrixa-template.webflow.io\contact.html',
    r'c:\Users\angam\Downloads\sentrixa_template.webflow.io\Error\sentrixa-template.webflow.io\404.html'
]

for file_path in files:
    if not os.path.exists(file_path):
        continue
        
    with open(file_path, 'r', encoding='utf-8') as f:
        html = f.read()
        
    soup = BeautifulSoup(html, 'lxml')
    
    # 1. Update Dead Links
    valid_pages = ['index.html', 'about.html', 'services.html', 'contact.html', '404.html']
    for a in soup.find_all('a'):
        href = a.get('href', '')
        if href.startswith('http') or href.startswith('mailto') or href.startswith('tel'):
            continue
        if any(valid in href for valid in valid_pages):
            continue
        a['href'] = '../../Error/sentrixa-template.webflow.io/404.html'
        
    # 2. Cleanup Footer
    footer = soup.find('section', class_='footer')
    if footer:
        # Remove newsletter
        newsletter = footer.find('div', class_='footer-one-bottom')
        if newsletter:
            newsletter.decompose()
            
        # Remove unwanted company links
        holders = footer.find_all('div', class_='footer-link-two-holder')
        for holder in holders:
            wraps = holder.find_all('div', class_='footer-link-two-wrap')
            for wrap in wraps:
                a_tag = wrap.find('a')
                if a_tag:
                    text = a_tag.get_text(strip=True).lower()
                    if text not in ['home', 'about', 'services', 'contact']:
                        wrap.decompose()
                        
        # Remove empty footer-block-two
        blocks = footer.find_all('div', class_='footer-block-two')
        for block in blocks:
            holder = block.find('div', class_='footer-link-two-holder')
            if holder:
                wraps = holder.find_all('div', class_='footer-link-two-wrap')
                if len(wraps) == 0:
                    block.decompose()
                    
    # 3. Replace Sentrixa text
    for text_node in soup.find_all(string=True):
        if text_node.parent and text_node.parent.name in ['script', 'style']:
            continue
        if 'Sentrixa' in text_node:
            new_text = text_node.replace('Sentrixa Security', 'Nexyra Tech').replace('Sentrixa', 'Nexyra Tech')
            text_node.replace_with(new_text)
        if 'sentrixa.io' in text_node:
            new_text = text_node.replace('sentrixa.io', 'thenexyra.com')
            text_node.replace_with(new_text)
            
    for meta in soup.find_all('meta'):
        if meta.get('content') and 'Sentrixa' in meta['content']:
            meta['content'] = meta['content'].replace('Sentrixa Security', 'Nexyra Tech').replace('Sentrixa', 'Nexyra Tech')
            
    for img in soup.find_all('img'):
        if img.get('alt') and 'Sentrixa' in img['alt']:
            img['alt'] = img['alt'].replace('Sentrixa Security', 'Nexyra Tech').replace('Sentrixa', 'Nexyra Tech')
            
    for a in soup.find_all('a'):
        href = a.get('href', '')
        if 'sentrixa.io' in href:
            a['href'] = href.replace('sentrixa.io', 'thenexyra.com')

    # 4. Update Old Logos
    for img in soup.find_all('img'):
        src = img.get('src', '')
        if 'Logo.svg' in src:
            img['src'] = '../../logo.png'

    # Save modified HTML
    with open(file_path, 'w', encoding='utf-8') as f:
        # lxml tends to add <html><body> tags if they are missing, but these files have them.
        # We output using html formatter to prevent weird escaping
        f.write(str(soup))
        
print("Modifications complete!")
