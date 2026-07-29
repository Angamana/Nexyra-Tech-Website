import re

def fix_logos(file_path):
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
        f'                                    <div class="logo-wrap" style="margin: 0 60px;"><img alt="Client logo" class="logo" loading="lazy" src="../../brand%20strip/{logo.replace(" ", "%20")}" style="transform: scale(1.5); transform-origin: center;" /></div>'
        for logo in logos
    ])

    new_block = f'<div class="logo-list" id="brand-strip-list">\n{new_logos_html}\n                                </div>'

    # Find <div class="logo3_component" id="brand-strip-track"> and replace everything inside it until its closing div
    # Actually, we can just replace the whole track component to be safe since it just wraps the list.
    new_track_block = f'<div class="logo3_component" id="brand-strip-track">\n                                {new_block}\n                            </div>'

    # We will use regex to find the logo3_component and replace it entirely.
    pattern = re.compile(r'<div class="logo3_component" id="brand-strip-track">.*?</div>\s*</div>\s*</div>\s*</section>', re.DOTALL)
    
    # Wait, the closing tags after brand-strip-track are:
    # </div> (closes brand-strip-track)
    # </div> (closes logo-holder)
    # </div> (closes container)
    # </section>
    
    # Let's just do a string replacement if possible, or use a simpler regex that matches up to a known following element.
    # We know the element right after logo-holder is <div class="line-hero-bg" or </section>.
    
    # Let's replace the content between <div class="logo-holder"...> and </section>
    pattern = re.compile(r'(<div class="logo-holder"[^>]*>).*?(</section>)', re.DOTALL)
    
    replacement = r'\1\n                            <div class="logo3_component" id="brand-strip-track">\n                                ' + new_block + r'\n                            </div>\n                        </div>\n                    \2'
    
    new_content = pattern.sub(replacement, content)

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print(f"Fixed {file_path}")

fix_logos(r'c:\Users\angam\Downloads\sentrixa_template.webflow.io\Index\sentrixa-template.webflow.io\index.html')
fix_logos(r'c:\Users\angam\Downloads\sentrixa_template.webflow.io\About\sentrixa-template.webflow.io\about.html')
fix_logos(r'c:\Users\angam\Downloads\sentrixa_template.webflow.io\Services\sentrixa-template.webflow.io\services.html')
