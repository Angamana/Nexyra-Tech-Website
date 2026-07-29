import os
from bs4 import BeautifulSoup
from urllib.parse import urlparse, unquote

base_dir = r"C:\Users\angam\Downloads\Nexyra Website"

broken_links = []

for root, dirs, files in os.walk(base_dir):
    if "Universal" in root or "Backend" in root or ".git" in root:
        continue
    for file in files:
        if file.endswith(".html"):
            html_path = os.path.join(root, file)
            with open(html_path, 'r', encoding='utf-8') as f:
                soup = BeautifulSoup(f, 'html.parser')
                
            def check_link(tag, attr):
                val = tag.get(attr)
                if not val: return
                parsed = urlparse(val)
                if parsed.scheme or parsed.netloc or val.startswith('data:') or val.startswith('#') or val.startswith('mailto:') or val.startswith('tel:'):
                    return
                
                local_path = os.path.normpath(os.path.join(root, unquote(parsed.path)))
                if not os.path.exists(local_path):
                    broken_links.append((html_path, tag.name, attr, val))
                    
            for link in soup.find_all('link', rel='stylesheet'): check_link(link, 'href')
            for script in soup.find_all('script'): check_link(script, 'src')
            for img in soup.find_all('img'): check_link(img, 'src')
            for a in soup.find_all('a'): check_link(a, 'href')

if broken_links:
    print(f"Found {len(broken_links)} broken links:")
    # print up to 50
    for link in broken_links[:50]:
        print(f"File: {link[0]} | Tag: {link[1]} | Attr: {link[2]} | Val: {link[3]}")
else:
    print("No broken links found. Everything is perfectly linked!")
