import re
import glob

def update_logos(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    logos = [
        "FNB Logo.png",
        "Eskom Logo.png",
        "Mutlichoice Logo.png",
        "Old Mutual Logo.png",
        "Sasol Logo.png",
        "Standard Bank Logo.png",
        "Transnet Logo.png",
        "Vodacom Logo.png"
    ]

    # Added inline styling to space out the logos significantly
    new_logos_html = '\n'.join([
        f'                                    <div class="logo-wrap" style="margin: 0 60px;"><img alt="Client logo" class="logo" loading="lazy" src="../../brand%20strip/{logo.replace(" ", "%20")}" style="transform: scale(1.5); transform-origin: center;" /></div>'
        for logo in logos
    ])

    new_block = f'<div class="logo-list" id="brand-strip-list">\n{new_logos_html}\n                                </div>'

    pattern = re.compile(r'<div class="logo-list" id="brand-strip-list">.*?</div>', re.DOTALL)
    new_content = pattern.sub(new_block, content)

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print(f"Updated {file_path}")

update_logos(r'c:\Users\angam\Downloads\sentrixa_template.webflow.io\Index\sentrixa-template.webflow.io\index.html')
update_logos(r'c:\Users\angam\Downloads\sentrixa_template.webflow.io\About\sentrixa-template.webflow.io\about.html')
update_logos(r'c:\Users\angam\Downloads\sentrixa_template.webflow.io\Services\sentrixa-template.webflow.io\services.html')
