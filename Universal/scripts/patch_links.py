import os
import shutil

base_dir = r"C:\Users\angam\Downloads\Nexyra Website"

# Move the PDF file to Universal/documents
docs_dir = os.path.join(base_dir, "Universal", "documents")
os.makedirs(docs_dir, exist_ok=True)
pdf_src = os.path.join(base_dir, "File Resources", "Nexyra Tech Company Profile - V2.pdf")
if os.path.exists(pdf_src):
    shutil.copy2(pdf_src, os.path.join(docs_dir, "Nexyra Tech Company Profile - V2.pdf"))

# Define replacements (old string: new string)
replacements = {
    "../../../Blog - Main Page/images/": "../../../Universal/images/",
    "Financial Services Threat Landscape Report.png": "../../../Universal/images/Financial Services Threat Landscape Report.png",
    "../../Index/code/css/": "../../Universal/code/css/",
    "../../Index/code/js/": "../../Universal/code/js/",
    "../../Index/images/": "../../Universal/images/",
    "../../File%20Resources/Nexyra%20Tech%20Company%20Profile%20-%20V2.pdf": "../../Universal/documents/Nexyra%20Tech%20Company%20Profile%20-%20V2.pdf"
}

for root, dirs, files in os.walk(base_dir):
    if "Universal" in root or "Backend" in root or ".git" in root:
        continue
    for file in files:
        if file.endswith(".html"):
            path = os.path.join(root, file)
            with open(path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            modified = False
            for old, new in replacements.items():
                if old in content:
                    content = content.replace(old, new)
                    modified = True
                    
            if modified:
                with open(path, 'w', encoding='utf-8') as f:
                    f.write(content)

print("Broken links patched.")
