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

        # Add CSS to push the nav menu to the right on desktop breakpoints
        css_to_add = "    <style> @media screen and (min-width: 992px) { .nav-menu { flex: 1; display: flex; justify-content: flex-end; padding-right: 15px; } } </style>\n</head>"
        
        if '@media screen and (min-width: 992px) { .nav-menu { flex: 1;' not in content:
            new_content = content.replace('</head>', css_to_add)
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
