import os

base = r'c:\Users\angam\Downloads\sentrixa_template.webflow.io'
files = [
    os.path.join(base, r'Index\sentrixa-template.webflow.io\index.html'),
    os.path.join(base, r'About\sentrixa-template.webflow.io\about.html'),
    os.path.join(base, r'Services\sentrixa-template.webflow.io\services.html'),
    os.path.join(base, r'Contact\sentrixa-template.webflow.io\contact.html'),
    os.path.join(base, r'Error\sentrixa-template.webflow.io\404.html'),
]

OLD_TAGLINE    = "Protecting digital assets and preventing tomorrow’s threats with AI-powered cybersecurity solutions."
NEW_TAGLINE    = "Ushering in the next era of technology through innovative and professional means."

OLD_COPYRIGHT  = "© 2025 Nexyra Tech. All rights reserved."
NEW_COPYRIGHT  = "© 2026 Nexyra Tech (Pty) Ltd. All rights reserved."

for path in files:
    if not os.path.exists(path):
        print(f"SKIP (not found): {path}")
        continue

    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()

    updated = content
    changes = []

    if OLD_TAGLINE in updated:
        updated = updated.replace(OLD_TAGLINE, NEW_TAGLINE)
        changes.append('tagline')

    if OLD_COPYRIGHT in updated:
        updated = updated.replace(OLD_COPYRIGHT, NEW_COPYRIGHT)
        changes.append('copyright')

    if changes:
        with open(path, 'w', encoding='utf-8') as f:
            f.write(updated)
        print(f"Updated {os.path.basename(os.path.dirname(path))}/{os.path.basename(path)}: {', '.join(changes)}")
    else:
        print(f"No matches in {os.path.basename(path)}")
