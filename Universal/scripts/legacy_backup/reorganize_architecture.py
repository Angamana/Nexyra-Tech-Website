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

def normalize_path(path):
    return os.path.normpath(path).replace('\\', '/')

html_files = []
for root, dirs, files in os.walk(base_dir):
    if "Universal" in root or "Backend" in root or ".git" in root:
        continue
    for file in files:
        if file.endswith(".html"):
            html_files.append(os.path.join(root, file))

# 1. Map assets
# We will track: { hash: {'paths': set(), 'used_in': set()} }
assets = {}

for html_file in html_files:
    try:
        with open(html_file, 'r', encoding='utf-8') as f:
            soup = BeautifulSoup(f, 'html.parser')
    except Exception as e:
        print(f"Error reading {html_file}: {e}")
        continue
        
    html_dir = os.path.dirname(html_file)
    
    def process_tag(tag, attr):
        val = tag.get(attr)
        if not val:
            return
        parsed = urlparse(val)
        if parsed.scheme or parsed.netloc or val.startswith('data:'):
            return # external or inline
            
        local_path = os.path.normpath(os.path.join(html_dir, unquote(parsed.path)))
        if os.path.exists(local_path) and os.path.isfile(local_path):
            file_hash = get_file_hash(local_path)
            if file_hash not in assets:
                assets[file_hash] = {
                    'paths': set(),
                    'used_in_html': set(),
                    'ext': os.path.splitext(local_path)[1].lower(),
                    'basename': os.path.basename(local_path)
                }
            assets[file_hash]['paths'].add(local_path)
            assets[file_hash]['used_in_html'].add(html_file)

    for link in soup.find_all('link', rel='stylesheet'):
        process_tag(link, 'href')
    for script in soup.find_all('script'):
        process_tag(script, 'src')
    for img in soup.find_all('img'):
        process_tag(img, 'src')

# Determine new locations for assets
universal_dir = os.path.join(base_dir, "Universal")
os.makedirs(os.path.join(universal_dir, "code", "css"), exist_ok=True)
os.makedirs(os.path.join(universal_dir, "code", "js"), exist_ok=True)
os.makedirs(os.path.join(universal_dir, "images"), exist_ok=True)

asset_new_locations = {} # { hash: new_absolute_path }

for file_hash, data in assets.items():
    # If used in multiple top-level categories, it's global.
    # What's a category? The first folder under base_dir.
    categories = set()
    for h in data['used_in_html']:
        rel = os.path.relpath(h, base_dir)
        cat = rel.split(os.sep)[0]
        categories.add(cat)
        
    ext = data['ext']
    basename = data['basename']
    
    if len(categories) > 1:
        # Global
        if ext == '.css':
            dest_dir = os.path.join(universal_dir, "code", "css")
        elif ext == '.js':
            dest_dir = os.path.join(universal_dir, "code", "js")
        else:
            dest_dir = os.path.join(universal_dir, "images")
    else:
        # Specific to one category
        cat = list(categories)[0]
        cat_dir = os.path.join(base_dir, cat)
        if ext == '.css':
            dest_dir = os.path.join(cat_dir, "code", "css")
        elif ext == '.js':
            dest_dir = os.path.join(cat_dir, "code", "js")
        else:
            dest_dir = os.path.join(cat_dir, "images")
            
    os.makedirs(dest_dir, exist_ok=True)
    
    # Handle filename collisions
    dest_path = os.path.join(dest_dir, basename)
    counter = 1
    while dest_path in asset_new_locations.values():
        name, extension = os.path.splitext(basename)
        dest_path = os.path.join(dest_dir, f"{name}_{counter}{extension}")
        counter += 1
        
    asset_new_locations[file_hash] = dest_path
    
    # Copy file (using the first available path)
    src_path = list(data['paths'])[0]
    shutil.copy2(src_path, dest_path)

# Now rewrite HTML files and move them
def get_new_html_path(old_html_path):
    rel = os.path.relpath(old_html_path, base_dir)
    parts = rel.split(os.sep)
    cat = parts[0]
    filename = parts[-1]
    
    if cat == "Index":
        return os.path.join(base_dir, "Home", "website", filename)
        
    if cat == "Blog - Main Page":
        if "Blog Sub" in rel or "Blog " in rel:
            sub = parts[1]
            return os.path.join(base_dir, "Blog", sub, "website", filename)
        else:
            return os.path.join(base_dir, "Blog", "Main Page", "website", filename)
            
    # For Services, About, Contact, Error, Policies
    # If there are subpages, group them. Else just website/filename
    if len(parts) > 2:
        return os.path.join(base_dir, cat, parts[-2], "website", filename)
    else:
        return os.path.join(base_dir, cat, "website", filename)

new_html_paths = {}
for html_file in html_files:
    new_html_path = get_new_html_path(html_file)
    new_html_paths[html_file] = new_html_path
    os.makedirs(os.path.dirname(new_html_path), exist_ok=True)

for html_file in html_files:
    try:
        with open(html_file, 'r', encoding='utf-8') as f:
            soup = BeautifulSoup(f, 'html.parser')
    except Exception:
        continue
        
    old_html_dir = os.path.dirname(html_file)
    new_html_path = new_html_paths[html_file]
    new_html_dir = os.path.dirname(new_html_path)
    
    def update_attr(tag, attr):
        val = tag.get(attr)
        if not val: return
        parsed = urlparse(val)
        if parsed.scheme or parsed.netloc or val.startswith('data:'): return
        
        old_local_path = os.path.normpath(os.path.join(old_html_dir, unquote(parsed.path)))
        if os.path.exists(old_local_path) and os.path.isfile(old_local_path):
            file_hash = get_file_hash(old_local_path)
            if file_hash in asset_new_locations:
                new_asset_path = asset_new_locations[file_hash]
                rel_path = os.path.relpath(new_asset_path, new_html_dir)
                tag[attr] = rel_path.replace('\\', '/')
                
    for link in soup.find_all('link', rel='stylesheet'): update_attr(link, 'href')
    for script in soup.find_all('script'): update_attr(script, 'src')
    for img in soup.find_all('img'): update_attr(img, 'src')
    
    # Also update <a> tags to new HTML locations
    for a in soup.find_all('a'):
        href = a.get('href')
        if not href: continue
        parsed = urlparse(href)
        if parsed.scheme or parsed.netloc or href.startswith('#') or href.startswith('mailto:') or href.startswith('tel:'): continue
        
        old_local_path = os.path.normpath(os.path.join(old_html_dir, unquote(parsed.path)))
        # check if this points to an HTML file we know about
        for old_html, new_html in new_html_paths.items():
            if old_local_path == old_html:
                rel_path = os.path.relpath(new_html, new_html_dir)
                a['href'] = rel_path.replace('\\', '/')
                break
                
    with open(new_html_path, 'w', encoding='utf-8') as f:
        f.write(str(soup))

print("Assets and HTML files reorganized successfully.")
