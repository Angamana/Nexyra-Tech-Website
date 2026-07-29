import os
import re

base_dir = r"c:\Users\angam\Downloads\Nexyra Website"

targets = {
    "index": r"Index\Index Page\index.html",
    "about": r"About\About Page\about.html",
    "services": r"Services\Services Page\services.html",
    "contact": r"Contact\Contact Us Page\contact.html",
    "blog": r"Blog - Main Page\sentrixa-template.webflow.io\blog.html",
    "cookie-js": r"cookie-policy.js",
    "cookie-css": r"cookie-policy.css"
}

def get_target_key(href):
    href_low = href.lower()
    
    if href_low.startswith("http") or href_low.startswith("#") or href_low.startswith("mailto:"):
        return None
        
    if "index.html" in href_low or href_low == "/" or href_low == "../" or href_low == "../../":
        return "index"
    if "about.html" in href_low or href_low == "about":
        return "about"
    if "services.html" in href_low or href_low == "services":
        return "services"
    if "contact.html" in href_low or href_low == "contact" or "/price" in href_low or "price" in href_low:
        return "contact"
    if "blog.html" in href_low or href_low == "blog":
        return "blog"
        
    return None

html_files = []
for root, dirs, files in os.walk(base_dir):
    for f in files:
        if f.endswith(".html"):
            html_files.append(os.path.join(root, f))

updated_count = 0

for file_path in html_files:
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
        continue

    def replace_href(match):
        prefix = match.group(1)
        href = match.group(2)
        suffix = match.group(3)

        key = get_target_key(href)
        if key:
            target_abs = os.path.join(base_dir, targets[key])
            file_dir = os.path.dirname(file_path)
            rel_path = os.path.relpath(target_abs, file_dir).replace("\\", "/")
            return prefix + rel_path + suffix
        return match.group(0)

    # Replace <a href="...">
    new_content = re.sub(r'(href=")([^"]+)(")', replace_href, content)

    if new_content != content:
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(new_content)
        updated_count += 1

print(f"Fixed 'price' links in {updated_count} HTML files.")
