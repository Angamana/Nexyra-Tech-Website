import os
import shutil
import re

base_dir = r"C:\Users\angam\Downloads\Nexyra Website"

# 1. Rename Home to Index
home_dir = os.path.join(base_dir, "Home")
index_dir = os.path.join(base_dir, "Index")
if os.path.exists(home_dir) and not os.path.exists(index_dir):
    os.rename(home_dir, index_dir)
    print("Renamed Home to Index")

# 2. Update HTML links pointing to Home/ to Index/
html_files = []
for root, dirs, files in os.walk(base_dir):
    for f in files:
        if f.endswith(".html"):
            html_files.append(os.path.join(root, f))

for file_path in html_files:
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
    
    # We want to replace /Home/ with /Index/
    # And Home/website/index.html with Index/website/index.html
    new_content = content.replace("/Home/", "/Index/")
    new_content = new_content.replace('href="Home/', 'href="Index/')
    new_content = new_content.replace('href="../Home/', 'href="../Index/')
    new_content = new_content.replace('href="../../Home/', 'href="../../Index/')
    new_content = new_content.replace('href="../../../Home/', 'href="../../../Index/')
    
    if new_content != content:
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(new_content)
        print(f"Updated links in {file_path}")

# 3. Clean up and ensure structure in all page folders
# A page folder is defined as a folder that contains 'website' as a direct child.
for root, dirs, files in os.walk(base_dir, topdown=False): # Bottom up to avoid deleting while walking
    if "website" in dirs:
        # It's a page folder!
        # Ensure code/css, code/js, images exist
        code_dir = os.path.join(root, "code")
        css_dir = os.path.join(code_dir, "css")
        js_dir = os.path.join(code_dir, "js")
        img_dir = os.path.join(root, "images")
        
        os.makedirs(css_dir, exist_ok=True)
        os.makedirs(js_dir, exist_ok=True)
        os.makedirs(img_dir, exist_ok=True)
        
        # Remove empty junk folders
        # Expected folders: website, code, images
        expected_folders = {"website", "code", "images"}
        for d in dirs:
            if d.lower() not in expected_folders:
                dir_to_remove = os.path.join(root, d)
                try:
                    # Only remove if it doesn't contain important files (like html/css/js/png)
                    # Let's just do a safe check
                    has_files = False
                    for r2, d2, f2 in os.walk(dir_to_remove):
                        if f2:
                            has_files = True
                            break
                    if not has_files:
                        shutil.rmtree(dir_to_remove)
                        print(f"Removed empty junk folder {dir_to_remove}")
                    else:
                        print(f"Warning: {dir_to_remove} contains files, not deleting.")
                except Exception as e:
                    print(f"Failed to remove {dir_to_remove}: {e}")

# Delete wf_graphql from everywhere as it's definitely junk from Webflow
for root, dirs, files in os.walk(base_dir, topdown=False):
    for d in dirs:
        if "wf_graphql" in d:
            dir_to_remove = os.path.join(root, d)
            try:
                shutil.rmtree(dir_to_remove)
                print(f"Removed junk {dir_to_remove}")
            except:
                pass

print("Structure cleanup complete!")
