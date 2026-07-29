import os
import shutil
import re
from collections import defaultdict

base_dir = r"C:\Users\angam\Downloads\Nexyra Website"
uni_img_dir = os.path.join(base_dir, "Universal", "images")

if not os.path.exists(uni_img_dir):
    print("No Universal images folder.")
    exit(0)

uni_images = set(os.listdir(uni_img_dir))
image_usage = defaultdict(list)

html_files = []
for root, dirs, files in os.walk(base_dir):
    for f in files:
        if f.endswith(".html"):
            html_files.append(os.path.join(root, f))

for file_path in html_files:
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
    for img in uni_images:
        if img in content:
            image_usage[img].append(file_path)

moved_count = 0

aggregation_folders = [
    os.path.join(base_dir, "Index"),
    os.path.join(base_dir, "Blog", "Main Page")
]

for img in list(uni_images):
    users = image_usage[img]
    if len(users) == 0:
        continue
    
    exact_page_folders = set()
    for u in users:
        page_folder = os.path.dirname(os.path.dirname(u))
        exact_page_folders.add(page_folder)
        
    # Check if exactly one non-aggregation folder uses it
    non_agg_folders = [f for f in exact_page_folders if f not in aggregation_folders]
    
    target_page_folder = None
    if len(non_agg_folders) == 1:
        # Move to that non-aggregation folder (e.g. Blog Sub X)
        target_page_folder = non_agg_folders[0]
    elif len(exact_page_folders) == 1:
        # Just in case (e.g. only in Blog/Main Page, and nowhere else)
        target_page_folder = list(exact_page_folders)[0]
    
    if target_page_folder:
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
        
        # Now update ALL HTML files that used it to point to the new location
        for u in users:
            # We need to calculate the relative path from the HTML file's folder to target_img_dir
            html_dir = os.path.dirname(u)
            rel_path_to_img = os.path.relpath(dst_path, html_dir)
            # convert to forward slashes for HTML
            rel_path_to_img = rel_path_to_img.replace(os.sep, '/')
            
            with open(u, "r", encoding="utf-8") as f:
                content = f.read()
                
            # Replace paths ending in /Universal/images/img
            pattern = re.compile(r'([\'"])[^\'"]*/Universal/images/' + re.escape(img) + r'\1')
            def replacer(match):
                quote = match.group(1)
                return f'{quote}{rel_path_to_img}{quote}'
            new_content = pattern.sub(replacer, content)
            
            # Replace url(...) without quotes
            pattern2 = re.compile(r'url\(([^\'"\)]*/Universal/images/' + re.escape(img) + r')\)')
            def replacer2(match):
                return f'url({rel_path_to_img})'
            new_content = pattern2.sub(replacer2, new_content)
            
            if new_content != content:
                with open(u, "w", encoding="utf-8") as f:
                    f.write(new_content)

print(f"Finished distributing {moved_count} blog images!")
