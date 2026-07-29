import os

base_dir = r'c:\Users\angam\Downloads\sentrixa_template.webflow.io'
files = [
    os.path.join(base_dir, r'Index\sentrixa-template.webflow.io\index.html'),
    os.path.join(base_dir, r'About\sentrixa-template.webflow.io\about.html'),
    os.path.join(base_dir, r'Services\sentrixa-template.webflow.io\services.html'),
    os.path.join(base_dir, r'Contact\sentrixa-template.webflow.io\contact.html'),
    os.path.join(base_dir, r'Error\sentrixa-template.webflow.io\404.html')
]

old_logo = '<a class="footer-brand w-inline-block" href="../../Index/sentrixa-template.webflow.io/index.html"><img alt="" class="footer-brand-img" loading="lazy" src="../../logo.png"/></a>'
new_logo = '<a class="footer-brand w-inline-block" href="../../Index/sentrixa-template.webflow.io/index.html"><div style="display:flex;align-items:center;gap:8px;"><img alt="Nexyra Tech Logo" class="footer-brand-img" loading="lazy" src="../../logo.png" style="height: 22px; width: auto;"/><span style="font-family:\'Inter\', sans-serif; font-size:18px; font-weight:600; color:white; line-height: 1;">Nexyra Tech</span></div></a>'

for file_path in files:
    if os.path.exists(file_path):
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # Update footer logo
        content = content.replace(old_logo, new_logo)

        # Update email in footer
        content = content.replace('>security@thenexyra.com<', '>info@thenexyra.com<')
        content = content.replace('mailto:security@thenexyra.com', 'mailto:info@thenexyra.com')

        if '404.html' in file_path:
            # Fix "Take me home" link which currently incorrectly points to 404.html
            content = content.replace(
                '<a class="_404-button-wrap w-inline-block" data-w-id="487f872e-d2b8-4372-66f5-98d0227886c5" href="../../Error/sentrixa-template.webflow.io/404.html">',
                '<a class="_404-button-wrap w-inline-block" data-w-id="487f872e-d2b8-4372-66f5-98d0227886c5" href="../../Index/sentrixa-template.webflow.io/index.html">'
            )

        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)

print("Updates to footer and 404 applied successfully.")
