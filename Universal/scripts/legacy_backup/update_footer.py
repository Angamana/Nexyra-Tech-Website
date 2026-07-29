import os
import re

workspace_dir = r"c:\Users\angam\Downloads\sentrixa_template.webflow.io"

files_to_update = [
    r"Index\sentrixa-template.webflow.io\index.html",
    r"About\sentrixa-template.webflow.io\about.html",
    r"Services\sentrixa-template.webflow.io\services.html",
    r"Contact\sentrixa-template.webflow.io\contact.html",
    r"Blog - Main Page\sentrixa-template.webflow.io\blog.html"
]

# We want to replace:
# Ushering in the next era of technology through innovative and professional means.
# with:
# Securing the next era

pattern = re.compile(r'Ushering\s+in\s+the\s+next\s+era\s+of\s+technology\s+through\s+innovative\s+and\s*[\r\n]*\s*professional\s+means\.', re.IGNORECASE)

for rel_path in files_to_update:
    file_path = os.path.join(workspace_dir, rel_path)
    if not os.path.exists(file_path):
        print(f"File not found: {file_path}")
        continue
    
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
    
    content = pattern.sub('Securing the next era', content)
    
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)
        
print("Updated footer text across all pages.")
