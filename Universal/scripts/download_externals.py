import os
import re
import urllib.request
import urllib.parse

base_dir = r"C:\Users\angam\Downloads\Nexyra Website"
uni_js = os.path.join(base_dir, "Universal", "code", "js")
uni_css = os.path.join(base_dir, "Universal", "code", "css")
uni_img = os.path.join(base_dir, "Universal", "images")

os.makedirs(uni_js, exist_ok=True)
os.makedirs(uni_css, exist_ok=True)
os.makedirs(uni_img, exist_ok=True)

html_files = []
for root, dirs, files in os.walk(base_dir):
    for f in files:
        if f.endswith(".html"):
            html_files.append(os.path.join(root, f))

# Pattern to match external URLs
# Matching src="http...", href="http...", url("http...")
pattern = re.compile(r'(?:href|src|url)\s*=\s*[\'"](https?://[^\'"]+)[\'"]')
pattern2 = re.compile(r'url\([\'"]?(https?://[^\'"\)]+)[\'"]?\)')

ignore_domains = [
    'maps.google.com',
    'web.telegram.org',
    'facebook.com',
    'instagram.com',
    'linkedin.com',
    'x.com',
    'fonts.googleapis.com',
    'fonts.gstatic.com'
]

def should_ignore(url):
    for domain in ignore_domains:
        if domain in url:
            return True
    return False

url_to_local = {}

def get_local_path(url):
    if url in url_to_local:
        return url_to_local[url]
        
    parsed = urllib.parse.urlparse(url)
    # Get filename without query params
    filename = os.path.basename(parsed.path)
    if not filename:
        filename = "index.html"
    
    # Check extension
    ext = os.path.splitext(filename)[1].lower()
    
    if ext == '.js':
        target_dir = uni_js
    elif ext == '.css':
        target_dir = uni_css
    else:
        # Default to images for svg, png, webp, json, etc.
        target_dir = uni_img
        
    # Clean filename of weird chars
    filename = re.sub(r'[^a-zA-Z0-9_\-\.]', '_', filename)
    
    # Avoid collisions
    base, e = os.path.splitext(filename)
    counter = 1
    final_path = os.path.join(target_dir, filename)
    while os.path.exists(final_path) and url_to_local.get(url, "") != final_path:
        filename = f"{base}_{counter}{e}"
        final_path = os.path.join(target_dir, filename)
        counter += 1
        
    url_to_local[url] = final_path
    return final_path

# Download headers to mimic a browser to avoid 403s
req_headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
}

downloaded_count = 0
failed_count = 0

for file_path in html_files:
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
    
    matches = pattern.findall(content) + pattern2.findall(content)
    # Deduplicate
    matches = list(set(matches))
    
    new_content = content
    
    for url in matches:
        if should_ignore(url):
            continue
            
        local_path = get_local_path(url)
        
        # Download if not exists
        if not os.path.exists(local_path):
            try:
                print(f"Downloading {url} ...")
                req = urllib.request.Request(url, headers=req_headers)
                with urllib.request.urlopen(req, timeout=15) as response:
                    with open(local_path, 'wb') as out_f:
                        out_f.write(response.read())
                downloaded_count += 1
            except Exception as e:
                print(f"Failed to download {url}: {e}")
                failed_count += 1
                continue # Skip replacing if download failed
                
        # Replace in HTML
        # Calculate relative path from this HTML file to the local downloaded file
        rel_path = os.path.relpath(local_path, os.path.dirname(file_path))
        rel_path = rel_path.replace("\\", "/") # Ensure web-safe slashes
        
        # Replace only exact URL matches in quotes
        new_content = new_content.replace(f'"{url}"', f'"{rel_path}"')
        new_content = new_content.replace(f"'{url}'", f"'{rel_path}'")
        new_content = new_content.replace(f"url({url})", f"url({rel_path})")
        new_content = new_content.replace(f"url('{url}')", f"url('{rel_path}')")
        new_content = new_content.replace(f'url("{url}")', f'url("{rel_path}")')
        
    if new_content != content:
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(new_content)
        print(f"Updated links in {file_path}")

print(f"Finished! Downloaded {downloaded_count} files. Failed {failed_count} files.")
