import os
import re

files = [
    r'c:\Users\angam\Downloads\sentrixa_template.webflow.io\Index\sentrixa-template.webflow.io\index.html',
    r'c:\Users\angam\Downloads\sentrixa_template.webflow.io\About\sentrixa-template.webflow.io\about.html',
    r'c:\Users\angam\Downloads\sentrixa_template.webflow.io\Services\sentrixa-template.webflow.io\services.html',
    r'c:\Users\angam\Downloads\sentrixa_template.webflow.io\Contact\sentrixa-template.webflow.io\contact.html'
]

for file_path in files:
    if not os.path.exists(file_path):
        print(f'File not found: {file_path}')
        continue
        
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Remove the comment
    content = re.sub(r'<!-- This site was created in Webflow. https://webflow.com -->\s*', '', content)
    
    # Hide the Webflow badge using CSS safely
    # If not already hidden
    if '.w-webflow-badge { display: none !important; }' not in content:
        content = content.replace('</head>', '    <style>.w-webflow-badge { display: none !important; }</style>\n</head>')

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
        
    print(f'Successfully updated {os.path.basename(file_path)}')
