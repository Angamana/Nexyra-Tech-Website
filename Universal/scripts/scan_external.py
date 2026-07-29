import os
import re

base_dir = r"C:\Users\angam\Downloads\Nexyra Website"

html_files = []
for root, dirs, files in os.walk(base_dir):
    for f in files:
        if f.endswith(".html") or f.endswith(".css"):
            html_files.append(os.path.join(root, f))

external_urls = set()
pattern = re.compile(r'(?:href|src|url)\s*=\s*[\'"](https?://[^\'"]+)[\'"]')
pattern2 = re.compile(r'url\([\'"]?(https?://[^\'"\)]+)[\'"]?\)')

for file_path in html_files:
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
    
    matches = pattern.findall(content)
    for m in matches:
        external_urls.add(m)
        
    matches2 = pattern2.findall(content)
    for m in matches2:
        external_urls.add(m)

print("External URLs found:")
for url in sorted(external_urls):
    print(url)
