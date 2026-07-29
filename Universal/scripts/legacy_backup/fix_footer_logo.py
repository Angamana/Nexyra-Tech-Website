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
        
        # Fix footer brand
        footer = soup.find('section', class_='footer')
        if footer:
            brand_link = footer.find('a', class_='footer-brand')
            if brand_link:
                brand_link.clear()
                
                # Make sure anchor has text-decoration: none
                existing_style = brand_link.get('style', '')
                if 'text-decoration: none' not in existing_style:
                    brand_link['style'] = (existing_style + '; text-decoration: none;').strip('; ')
                
                div = soup.new_tag('div', style="display:flex;align-items:center;gap:8px;text-decoration:none;")
                img = soup.new_tag('img', alt="Nexyra Tech Logo", loading="lazy", src="../../logo.png", style="height: 22px; width: auto;")
                img['class'] = "footer-brand-img"
                span = soup.new_tag('span', style="font-family:'Inter', sans-serif; font-size:18px; font-weight:600; color:white; line-height: 1; text-decoration: none;")
                span.string = "Nexyra Tech"
                
                div.append(img)
                div.append(span)
                brand_link.append(div)
                
        # Fix navbar brand underline just in case
        navbars = soup.find_all('a', class_='brand-logo')
        for nav in navbars:
            existing_style = nav.get('style', '')
            if 'text-decoration: none' not in existing_style:
                nav['style'] = (existing_style + '; text-decoration: none;').strip('; ')
            span = nav.find('span')
            if span:
                span_style = span.get('style', '')
                if 'text-decoration: none' not in span_style:
                    span['style'] = (span_style + '; text-decoration: none;').strip('; ')
                
        with open(file_path, 'w', encoding='utf-8') as f:
            # We output using html formatter to prevent weird escaping
            f.write(str(soup))
            
print("Footer logo fixed and underlines removed.")
