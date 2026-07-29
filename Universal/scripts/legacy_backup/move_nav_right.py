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

        # Replace margin: 0 auto; with margin-left: auto; margin-right: 0;
        new_content = content.replace(
            '<div class="nav-link-holder" style="margin: 0 auto;">',
            '<div class="nav-link-holder" style="margin-left: auto; margin-right: 0;">'
        )

        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        
        print(f'Updated {os.path.basename(file_path)}')
