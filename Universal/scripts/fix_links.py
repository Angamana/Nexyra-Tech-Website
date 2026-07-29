import os
import re
import urllib.request
import urllib.parse

base_dir = r"C:\Users\angam\Downloads\Nexyra Website"

# 1. Strip integrity and crossorigin from HTML
html_files = []
for root, dirs, files in os.walk(base_dir):
    for f in files:
        if f.endswith(".html"):
            html_files.append(os.path.join(root, f))

integrity_pattern = re.compile(r'\s+integrity="[^"]*"')
crossorigin_pattern = re.compile(r'\s+crossorigin="[^"]*"')

for file_path in html_files:
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
    
    new_content = integrity_pattern.sub('', content)
    new_content = crossorigin_pattern.sub('', new_content)
    
    if new_content != content:
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(new_content)
        print(f"Stripped integrity from {file_path}")

# 2. Fix CSS file and download its images
css_path = os.path.join(base_dir, "Universal", "code", "css", "sentrixa-template.webflow.shared.51560f5c1.css")
uni_img = os.path.join(base_dir, "Universal", "images")

if os.path.exists(css_path):
    with open(css_path, "r", encoding="utf-8") as f:
        css_content = f.read()

    url_pattern = re.compile(r'url\([\'"]?(https?://[^\'"\)]+)[\'"]?\)')
    matches = list(set(url_pattern.findall(css_content)))

    req_headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
    
    new_css_content = css_content
    for url in matches:
        if 'fonts.googleapis.com' in url or 'fonts.gstatic.com' in url:
            continue
            
        parsed = urllib.parse.urlparse(url)
        filename = os.path.basename(parsed.path)
        filename = urllib.parse.unquote(filename) # decode %20 etc
        filename = re.sub(r'[^a-zA-Z0-9_\-\.]', '_', filename)
        
        local_path = os.path.join(uni_img, filename)
        
        if not os.path.exists(local_path):
            try:
                print(f"Downloading CSS asset: {url} ...")
                req = urllib.request.Request(url, headers=req_headers)
                with urllib.request.urlopen(req, timeout=10) as response:
                    with open(local_path, 'wb') as out_f:
                        out_f.write(response.read())
            except Exception as e:
                print(f"Failed to download {url}: {e}")
                continue
                
        # Rewrite url in CSS
        # from url("https://...") to url("../../images/filename")
        # because css is in Universal/code/css
        new_url = f"../../images/{filename}"
        
        # Replace exact urls
        new_css_content = new_css_content.replace(f'url("{url}")', f'url("{new_url}")')
        new_css_content = new_css_content.replace(f"url('{url}')", f"url('{new_url}')")
        new_css_content = new_css_content.replace(f"url({url})", f"url('{new_url}')")

    if new_css_content != css_content:
        with open(css_path, "w", encoding="utf-8") as f:
            f.write(new_css_content)
        print("Updated CSS with local URLs.")

print("Finished fixing HTML attributes and CSS links!")
