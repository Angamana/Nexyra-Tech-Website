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

    # 1. Build the new nav-link-holder with correct w--current
    links = [
        ('Index', '../../Index/sentrixa-template.webflow.io/index.html', 'Home'),
        ('About', '../../About/sentrixa-template.webflow.io/about.html', 'About'),
        ('Services', '../../Services/sentrixa-template.webflow.io/services.html', 'Services'),
        ('Contact', '../../Contact/sentrixa-template.webflow.io/contact.html', 'Contact')
    ]
    
    nav_links_html = '<div class="nav-link-holder">'
    for link_id, href, text in links:
        current_class = ' w--current' if link_id == page_name else ''
        aria = ' aria-current="page"' if link_id == page_name else ''
        nav_links_html += f'<a href="{href}"{aria} class="nav-link w-nav-link{current_class}">{text}</a>'
    nav_links_html += '</div>'

    # The mobile button holder
    mobile_button_html = '''
                            <div class="nav-button-holder hide-desktop">
                                <a href="../../Contact/sentrixa-template.webflow.io/contact.html" class="nav-button w-inline-block">
                                    <div class="button-text-wrap">
                                        <p class="button-text-01">Contact</p>
                                        <p class="button-text-02">Contact</p>
                                    </div>
                                </a>
                            </div>
'''
    
    # Replace nav-link-holder to </nav>
    # Note: re.DOTALL is important. We replace from <div class="nav-link-holder"> up to </nav>
    # but not including </nav>
    pattern_nav_links = re.compile(r'<div class="nav-link-holder">.*?(?=</nav>)', re.DOTALL)
    content = pattern_nav_links.sub(nav_links_html + mobile_button_html, content)

    # 2. Replace the desktop nav and carts
    # From </nav> up to <div data-ix="simple-menu-button"
    desktop_nav_html = '''</nav>
                        <div class="nav-button-holder hide-tab">
                            <a href="../../Contact/sentrixa-template.webflow.io/contact.html" class="nav-button w-inline-block">
                                <div class="button-text-wrap">
                                    <p text="" class="button-text-01">Contact</p>
                                </div>
                            </a>
                        </div>
                    </div>'''
    
    pattern_desktop = re.compile(r'</nav>.*?(?=\s*<div data-ix="simple-menu-button")', re.DOTALL)
    content = pattern_desktop.sub(desktop_nav_html, content)

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
        
    print(f'Successfully updated navigation in {page_name}')
