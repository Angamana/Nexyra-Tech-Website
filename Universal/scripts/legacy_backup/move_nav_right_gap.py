import os

files = [
    r'c:\Users\angam\Downloads\sentrixa_template.webflow.io\Index\sentrixa-template.webflow.io\index.html',
    r'c:\Users\angam\Downloads\sentrixa_template.webflow.io\About\sentrixa-template.webflow.io\about.html',
    r'c:\Users\angam\Downloads\sentrixa_template.webflow.io\Services\sentrixa-template.webflow.io\services.html',
    r'c:\Users\angam\Downloads\sentrixa_template.webflow.io\Contact\sentrixa-template.webflow.io\contact.html'
]

for file_path in files:
    if os.path.exists(file_path):
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # Update the margin to give a small 24px gap between the links and the button
        new_content = content.replace(
            '<div class="nav-link-holder" style="margin-left: auto; margin-right: 0;">',
            '<div class="nav-link-holder" style="margin-left: auto; margin-right: 24px;">'
        )

        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
