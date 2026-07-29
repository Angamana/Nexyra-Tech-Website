import os
import re

base_dir = r"C:\Users\angam\Downloads\Nexyra Website"

# Find all HTML files
html_files = []
for root, dirs, files in os.walk(base_dir):
    for f in files:
        if f.endswith(".html"):
            html_files.append(os.path.join(root, f))

# We will inject the script src depending on depth
for file_path in html_files:
    rel_dir = os.path.relpath(os.path.dirname(file_path), base_dir)
    if rel_dir == ".":
        prefix = ""
    else:
        depth = len(rel_dir.replace("\\", "/").split("/"))
        prefix = "../" * depth
        
    script_tag = f'\n    <script src="{prefix}Universal/code/js/cookie-policy.js" type="text/javascript"></script>\n</body>'
    
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
        
    # Check if already has a cookie-policy.js
    pattern = r'<script src="[^"]*cookie-policy\.js"[^>]*></script>'
    if re.search(pattern, content):
        new_content = re.sub(pattern, f'<script src="{prefix}Universal/code/js/cookie-policy.js" type="text/javascript"></script>', content)
    else:
        new_content = re.sub(r'</body>', script_tag, content, flags=re.IGNORECASE)
        
    # Also add the border style to footer company links
    style_inject = """
    <style>
        /* Company Footer Links Style */
        .footer-wrapper-three .footer-link {
            border: 2px solid rgba(255, 255, 255, 0.2);
            border-radius: 20px;
            padding: 4px 12px;
            margin-bottom: 6px; /* Halved from original to reduce spacing */
            display: inline-block;
            transition: border-color 0.3s ease;
        }
        .footer-wrapper-three .footer-link:hover {
            border-color: #ffffff;
        }
    </style>
</head>"""
    if "/* Company Footer Links Style */" not in new_content:
        new_content = re.sub(r'</head>', style_inject, new_content, flags=re.IGNORECASE)

    if new_content != content:
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(new_content)
        print(f"Updated {file_path}")

print("Done injecting cookies and styles.")
