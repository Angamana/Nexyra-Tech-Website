import os
import re

files = [
    ('Index', r'c:\Users\angam\Downloads\sentrixa_template.webflow.io\Index\sentrixa-template.webflow.io\index.html'),
    ('About', r'c:\Users\angam\Downloads\sentrixa_template.webflow.io\About\sentrixa-template.webflow.io\about.html'),
    ('Services', r'c:\Users\angam\Downloads\sentrixa_template.webflow.io\Services\sentrixa-template.webflow.io\services.html'),
    ('Contact', r'c:\Users\angam\Downloads\sentrixa_template.webflow.io\Contact\sentrixa-template.webflow.io\contact.html')
]

for page_name, file_path in files:
    if not os.path.exists(file_path):
        print(f'File not found: {file_path}')
        continue
        
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Replace logo
    logo_replacement = '''<div style="display:flex;align-items:center;gap:8px;"><img src="../../logo.png" alt="Nexyra Tech Logo" style="height: 22px; width: auto;" /><span style="font-family:'Inter', sans-serif; font-size:18px; font-weight:600; color:white; line-height: 1;">Nexyra Tech</span></div>'''
    
    # We replace any <img> tag inside .brand-logo that has Logo.svg
    content = re.sub(r'<img loading="lazy" height="23" alt="" src="[^"]*Logo\.svg"/>', logo_replacement, content)

    # 2. Rebuild nav-link-holder WITHOUT Contact, WITH center styling
    links = [
        ('Index', '../../Index/sentrixa-template.webflow.io/index.html', 'Home'),
        ('About', '../../About/sentrixa-template.webflow.io/about.html', 'About'),
        ('Services', '../../Services/sentrixa-template.webflow.io/services.html', 'Services')
    ]
    
    nav_links_html = '<div class="nav-link-holder" style="margin: 0 auto;">'
    for link_id, href, text in links:
        current_class = ' w--current' if link_id == page_name else ''
        aria = ' aria-current="page"' if link_id == page_name else ''
        nav_links_html += f'<a href="{href}"{aria} class="nav-link w-nav-link{current_class}">{text}</a>'
    nav_links_html += '</div>'

    # The mobile button holder
    mobile_button_html = '''
                            <div class="nav-button-holder hide-desktop">
                                <a href="../../Contact/sentrixa-template.webflow.io/contact.html" class="nav-button w-inline-block" style="border-radius: 50px;">
                                    <div class="button-text-wrap">
                                        <p class="button-text-01">Contact Us</p>
                                        <p class="button-text-02">Contact Us</p>
                                    </div>
                                </a>
                            </div>
'''
    
    # Replace from <div class="nav-link-holder"> to </nav>
    # Note: re.DOTALL is important.
    pattern_nav_links = re.compile(r'<div class="nav-link-holder(?:".*?|)>.*?(?=</nav>)', re.DOTALL)
    content = pattern_nav_links.sub(nav_links_html + mobile_button_html, content)

    # 3. Desktop nav replacement
    desktop_nav_html = '''</nav>
                        <div class="nav-button-holder hide-tab">
                            <a href="../../Contact/sentrixa-template.webflow.io/contact.html" class="nav-button w-inline-block" style="border-radius: 50px;">
                                <div class="button-text-wrap">
                                    <p text="" class="button-text-01">Contact Us</p>
                                </div>
                            </a>
                        </div>
                    </div>'''
    
    pattern_desktop = re.compile(r'</nav>\s*<div class="nav-button-holder hide-tab">.*?(?=\s*<div data-ix="simple-menu-button")', re.DOTALL)
    content = pattern_desktop.sub(desktop_nav_html, content)

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
        
    print(f'Successfully updated navigation in {page_name}')
