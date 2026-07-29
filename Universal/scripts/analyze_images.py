import os
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
        if img in content:
            image_usage[img].append(file_path)

local_count = 0
global_count = 0
unused_count = 0

for img in uni_images:
    users = image_usage[img]
    if len(users) == 0:
        unused_count += 1
    elif len(users) == 1:
        local_count += 1
    else:
        # Check if they are all in the same top-level folder
        # e.g. all in Blog/
        top_levels = set()
        for u in users:
            rel = os.path.relpath(u, base_dir)
            top_level = rel.split(os.sep)[0]
            top_levels.add(top_level)
            
        if len(top_levels) == 1:
            local_count += 1
        else:
            global_count += 1

print(f"Total images: {len(uni_images)}")
print(f"Globally used (multiple folders): {global_count}")
print(f"Locally used (single folder): {local_count}")
print(f"Unused (or dynamically loaded via JS/CSS): {unused_count}")

