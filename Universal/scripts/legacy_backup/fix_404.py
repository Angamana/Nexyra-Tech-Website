import re

file_path = r'c:\Users\angam\Downloads\sentrixa_template.webflow.io\Error\sentrixa-template.webflow.io\404.html'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Replace title
content = re.sub(r'<title>.*?</title>', '<title>Nexyra Tech</title>', content, flags=re.DOTALL)

# Replace favicons
content = re.sub(r'<link href="[^"]*fab\.svg" rel="shortcut icon" type="image/x-icon" />', '<link href="../../logo.png" rel="shortcut icon" type="image/png" />', content)
content = re.sub(r'<link href="[^"]*web-clip\.svg" rel="apple-touch-icon" />', '<link href="../../logo.png" rel="apple-touch-icon" />', content)

# Replace navbar
new_navbar = '''<div class="navbar-inner"><a href="../../Index/sentrixa-template.webflow.io/index.html" class="brand-logo w-nav-brand"><div style="display:flex;align-items:center;gap:8px;"><img src="../../logo.png" alt="Nexyra Tech Logo" style="height: 22px; width: auto;" /><span style="font-family:'Inter', sans-serif; font-size:18px; font-weight:600; color:white; line-height: 1;">Nexyra Tech</span></div></a>
                        <nav role="navigation" class="nav-menu spark-rounded-corners w-nav-menu">
                            <div class="nav-link-holder" style="margin-left: auto; margin-right: 24px;"><a href="../../Index/sentrixa-template.webflow.io/index.html" class="nav-link w-nav-link">Home</a><a href="../../About/sentrixa-template.webflow.io/about.html" class="nav-link w-nav-link">About</a><a href="../../Services/sentrixa-template.webflow.io/services.html" class="nav-link w-nav-link">Services</a></div>
                            <div class="nav-button-holder hide-desktop">
                                <a href="../../Contact/sentrixa-template.webflow.io/contact.html" class="nav-button w-inline-block" style="border-radius: 50px;">
                                    <div class="button-text-wrap">
                                        <p class="button-text-01">Contact Us</p>
                                        <p class="button-text-02">Contact Us</p>
                                    </div>
                                </a>
                            </div>
                        </nav>
                        <div class="nav-button-holder hide-tab">
                            <a href="../../Contact/sentrixa-template.webflow.io/contact.html" class="nav-button w-inline-block" style="border-radius: 50px;">
                                <div class="button-text-wrap">
                                    <p text="" class="button-text-01">Contact Us</p>
                                </div>
                            </a>
                        </div>
                    </div>'''

# Find the start and end to replace
start_str = '<div class="navbar-inner">'
end_str = '<div data-ix="simple-menu-button"'

start_idx = content.find(start_str)
end_idx = content.find(end_str)

if start_idx != -1 and end_idx != -1:
    content = content[:start_idx] + new_navbar + '\n                    ' + content[end_idx:]

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("404.html updated successfully!")
