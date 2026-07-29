import re

def fix_logos_holder_2(file_path):
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

    new_logos_html = '\n'.join([
        f'                                    <div class="logo-wrap" style="margin: 0 30px;"><img alt="Client logo" class="logo" loading="lazy" src="../../brand%20strip/{logo.replace(" ", "%20")}" style="transform: scale(1.5); transform-origin: center;" /></div>'
        for logo in logos
    ])

    new_block = f'<div class="logo-list" id="brand-strip-list">\n{new_logos_html}\n                                </div>'

    # Pattern to match from <div class="logo-holder-2"> to </section>
    pattern = re.compile(r'(<div class="logo-holder-2"[^>]*>).*?(</section>)', re.DOTALL)
    
    replacement = r'\1\n                          <div class="logo3_component" id="brand-strip-track">\n                              ' + new_block + r'\n                          </div>\n                      </div>\n                  \2'
    
    new_content = pattern.sub(replacement, content)

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print(f"Fixed {file_path}")

fix_logos_holder_2(r'c:\Users\angam\Downloads\sentrixa_template.webflow.io\About\sentrixa-template.webflow.io\about.html')
fix_logos_holder_2(r'c:\Users\angam\Downloads\sentrixa_template.webflow.io\Services\sentrixa-template.webflow.io\services.html')
