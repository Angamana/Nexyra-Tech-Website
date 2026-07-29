import os
import shutil
import hashlib
from bs4 import BeautifulSoup
from urllib.parse import urlparse, unquote

base_dir = r"C:\Users\angam\Downloads\Nexyra Website"

def get_file_hash(filepath):
    hasher = hashlib.md5()
    with open(filepath, 'rb') as f:
        buf = f.read()
        hasher.update(buf)
    return hasher.hexdigest()

# 1. Delete old HTML files not in 'website' folders
for root, dirs, files in os.walk(base_dir):
    if "Universal" in root or "Backend" in root or ".git" in root:
        continue
    for file in files:
        if file.endswith(".html"):
            if "website" not in root.split(os.sep):
                os.remove(os.path.join(root, file))

# 2. Gather all assets and move them to Universal
universal_images = os.path.join(base_dir, "Universal", "images")
universal_css = os.path.join(base_dir, "Universal", "code", "css")
universal_js = os.path.join(base_dir, "Universal", "code", "js")

os.makedirs(universal_images, exist_ok=True)
os.makedirs(universal_css, exist_ok=True)
os.makedirs(universal_js, exist_ok=True)

asset_hashes = {} # hash -> absolute path in Universal

for root, dirs, files in os.walk(base_dir):
    if "Backend" in root or ".git" in root:
        continue
    for file in files:
        ext = os.path.splitext(file)[1].lower()
        if ext in ['.css', '.js', '.png', '.jpg', '.jpeg', '.svg', '.gif', '.webp', '.ico']:
            src = os.path.join(root, file)
            fhash = get_file_hash(src)
            
            if ext == '.css': dest_dir = universal_css
            elif ext == '.js': dest_dir = universal_js
            else: dest_dir = universal_images
            
            if fhash not in asset_hashes:
                dest = os.path.join(dest_dir, file)
                counter = 1
                while os.path.exists(dest) and get_file_hash(dest) != fhash:
                    name, e = os.path.splitext(file)
                    dest = os.path.join(dest_dir, f"{name}_{counter}{e}")
                    counter += 1
                
                if src != dest:
                    shutil.copy2(src, dest)
                asset_hashes[fhash] = dest

# 3. Rewrite all HTML files
html_files = []
for root, dirs, files in os.walk(base_dir):
    if "Universal" in root or "Backend" in root or ".git" in root:
        continue
    for file in files:
        if file.endswith(".html"):
            html_files.append(os.path.join(root, file))

for html_path in html_files:
    try:
        with open(html_path, 'r', encoding='utf-8') as f:
            soup = BeautifulSoup(f, 'html.parser')
    except:
        continue
        
    html_dir = os.path.dirname(html_path)
    
    def update_tag(tag, attr):
        val = tag.get(attr)
        if not val: return
        parsed = urlparse(val)
        if parsed.scheme or parsed.netloc or val.startswith('data:') or val.startswith('#') or val.startswith('mailto:') or val.startswith('tel:'):
            return
            
        old_local = os.path.normpath(os.path.join(html_dir, unquote(parsed.path)))
        if os.path.exists(old_local):
            fhash = get_file_hash(old_local)
            if fhash in asset_hashes:
                new_dest = asset_hashes[fhash]
                rel = os.path.relpath(new_dest, html_dir).replace('\\', '/')
                tag[attr] = rel
        else:
            # Maybe it's already broken. Let's try to find it by name in Universal
            basename = os.path.basename(old_local)
            for h, dest in asset_hashes.items():
                if os.path.basename(dest) == basename:
                    rel = os.path.relpath(dest, html_dir).replace('\\', '/')
                    tag[attr] = rel
                    break
                    
    for link in soup.find_all('link', rel='stylesheet'): update_tag(link, 'href')
    for script in soup.find_all('script'): update_tag(script, 'src')
    for img in soup.find_all('img'): update_tag(img, 'src')
    
    with open(html_path, 'w', encoding='utf-8') as f:
        f.write(str(soup))

print("All assets consolidated to Universal and HTML links updated.")
