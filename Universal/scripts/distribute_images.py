import os
import shutil
import re
from collections import defaultdict

base_dir = r"C:\Users\angam\Downloads\Nexyra Website"
uni_img_dir = os.path.join(base_dir, "Universal", "images")

# Find all universal images
uni_images = set(os.listdir(uni_img_dir))

# Map image -> list of html files using it
image_usage = defaultdict(list)

# Find all HTML files
html_files = []
for root, dirs, files in os.walk(base_dir):
    for f in files:
        if f.endswith(".html"):
            html_files.append(os.path.join(root, f))

for file_path in html_files:
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
        
    for img in uni_images:
        # Check exact usage by making sure it's referenced
        if img in content:
            image_usage[img].append(file_path)

moved_count = 0

for img in list(uni_images):
    users = image_usage[img]
    if len(users) == 0:
        continue
    
    exact_page_folders = set()
    for u in users:
        page_folder = os.path.dirname(os.path.dirname(u))
        exact_page_folders.add(page_folder)
        
    if len(exact_page_folders) == 1:
        # Move image!
        target_page_folder = exact_page_folders.pop()
        target_img_dir = os.path.join(target_page_folder, "images")
        os.makedirs(target_img_dir, exist_ok=True)
        
        src_path = os.path.join(uni_img_dir, img)
        dst_path = os.path.join(target_img_dir, img)
        
        try:
            shutil.move(src_path, dst_path)
            moved_count += 1
            print(f"Moved {img} to {target_img_dir}")
        except Exception as e:
            print(f"Error moving {img}: {e}")
            continue
        
        # Now update the HTML file(s) that use it
        for u in users:
            with open(u, "r", encoding="utf-8") as f:
                content = f.read()
                
            # Pattern: matches anything ending in the filename inside quotes or url()
            pattern = re.compile(r'([\'"])[^\'"]*/Universal/images/' + re.escape(img) + r'\1')
            def replacer(match):
                quote = match.group(1)
                return f'{quote}../images/{img}{quote}'
                
            new_content = pattern.sub(replacer, content)
            
            # Also handle url(path) without quotes
            pattern2 = re.compile(r'url\(([^\'"\)]*/Universal/images/' + re.escape(img) + r')\)')
            def replacer2(match):
                return f'url(../images/{img})'
                
            new_content = pattern2.sub(replacer2, new_content)
            
            with open(u, "w", encoding="utf-8") as f:
                f.write(new_content)
                
print(f"Finished distributing {moved_count} images!")
