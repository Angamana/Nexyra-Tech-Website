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
    if href_low in ["/", "index", "index.html", "../index.html", "../../index.html", "../../../index.html"]: return "index"
    if href_low in ["about", "about.html", "../about.html", "../../about.html", "../../../about.html"]: return "about"
    if href_low in ["services", "services.html", "../services.html", "../../services.html", "../../../services.html"]: return "services"
    if href_low in ["contact", "contact.html", "../contact.html", "../../contact.html", "../../../contact.html"]: return "contact"
    if href_low in ["blog", "blog.html", "../blog.html", "../../blog.html", "../../../blog.html"]: return "blog"
    # match if it contains exactly the word
    if re.search(r'\babout\.html\b', href_low): return "about"
    if re.search(r'\bservices\.html\b', href_low): return "services"
    if re.search(r'\bcontact\.html\b', href_low): return "contact"
    if re.search(r'\bblog\.html\b', href_low): return "blog"
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

        if href.startswith("http") or href.startswith("#") or href.startswith("mailto:"):
            return match.group(0)

        key = get_target_key(href)
        if key:
            target_abs = os.path.join(base_dir, targets[key])
            file_dir = os.path.dirname(file_path)
            rel_path = os.path.relpath(target_abs, file_dir).replace("\\", "/")
            return prefix + rel_path + suffix
        return match.group(0)

    # Replace <a href="...">
    new_content = re.sub(r'(href=")([^"]+)(")', replace_href, content)
    
    # Replace <script src="..."> for cookie-policy.js if it exists
    def replace_script(match):
        prefix = match.group(1)
        src = match.group(2)
        suffix = match.group(3)
        if "cookie-policy.js" in src:
            target_abs = os.path.join(base_dir, targets["cookie-js"])
            file_dir = os.path.dirname(file_path)
            rel_path = os.path.relpath(target_abs, file_dir).replace("\\", "/")
            return prefix + rel_path + suffix
        return match.group(0)
        
    new_content = re.sub(r'(src=")([^"]+)(")', replace_script, new_content)

    if new_content != content:
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(new_content)
        updated_count += 1

print(f"Updated links in {updated_count} HTML files.")
