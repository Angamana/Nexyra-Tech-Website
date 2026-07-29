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

nav_css = """
    <style>
        .nav-link.w--current {
            color: #4353ff !important;
        }
    </style>
"""

for rel_path in files_to_update:
    file_path = os.path.join(workspace_dir, rel_path)
    if not os.path.exists(file_path):
        print(f"File not found: {file_path}")
        continue
    
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
    
    # 1. Fix missing class on Services link
    # We look for <a href="...services.html">Services</a> that might lack the class.
    # To be safe, we replace any `<a\s+href="[^"]*services\.html">Services</a>`
    # and `<a\n\s*href="[^"]*services\.html">Services</a>` with the classed version.
    
    # Pattern to match <a> tags without classes
    pattern = re.compile(r'<a\s+href="([^"]*services\.html)">Services</a>')
    content = pattern.sub(r'<a class="nav-link w-nav-link" href="\1">Services</a>', content)
    
    # 2. Add the active link color CSS right before </head>
    if '.nav-link.w--current' not in content:
        content = content.replace("</head>", nav_css + "</head>")
    
    # 3. For contact.html ONLY, fix the Contact button in the nav
    if "contact.html" in rel_path.lower():
        # There are two buttons (desktop and tab)
        # Desktop
        content = content.replace(
            '<a class="nav-button w-inline-block"\n                                    href="../../Contact/sentrixa-template.webflow.io/contact.html"\n                                    style="border-radius: 50px;">',
            '<a class="nav-button w-inline-block"\n                                    href="../../Contact/sentrixa-template.webflow.io/contact.html"\n                                    style="border-radius: 50px; background-color: #ffffff !important; border: 1px solid #4353ff !important;">'
        )
        content = content.replace(
            '<a class="nav-button w-inline-block"\n                                href="../../Contact/sentrixa-template.webflow.io/contact.html"\n                                style="border-radius: 50px;">',
            '<a class="nav-button w-inline-block"\n                                href="../../Contact/sentrixa-template.webflow.io/contact.html"\n                                style="border-radius: 50px; background-color: #ffffff !important; border: 1px solid #4353ff !important;">'
        )
        
        # Then change the text color for button-text-01 inside the nav.
        # We need to make sure we don't accidentally change ALL button-text-01 in the page.
        # Actually, let's just do it directly on the nav section text.
        # Let's find the nav section
        nav_start = content.find('<nav class="nav-menu spark-rounded-corners w-nav-menu" role="navigation">')
        nav_end = content.find('<div class="menu-button w-nav-button"')
        if nav_start != -1 and nav_end != -1:
            nav_content = content[nav_start:nav_end]
            nav_content = nav_content.replace('<p class="button-text-01">Contact Us</p>', '<p class="button-text-01" style="color: #4353ff !important;">Contact Us</p>')
            nav_content = nav_content.replace('<p class="button-text-02">Contact Us</p>', '<p class="button-text-02" style="color: #4353ff !important;">Contact Us</p>')
            nav_content = nav_content.replace('<p class="button-text-01" text="">Contact Us</p>', '<p class="button-text-01" style="color: #4353ff !important;" text="">Contact Us</p>')
            
            content = content[:nav_start] + nav_content + content[nav_end:]
            
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)
        
print("Successfully applied updates across all files.")
