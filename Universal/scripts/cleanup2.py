import os
import shutil

base_dir = r"C:\Users\angam\Downloads\Nexyra Website"
categories = ["Home", "About", "Contact", "Error", "Policies", "Blog", "Services"]

# We only want to keep 'website', 'code', 'images' and any subdirectories (like Blog Sub 1, Main Page, etc that contain 'website', 'code', 'images').
# The old folders like 'About Page', '_DataURI', 'ajax.googleapis.com', etc. must be deleted.

def clean_directory(d):
    for root, dirs, files in os.walk(d, topdown=False):
        for name in dirs:
            dir_path = os.path.join(root, name)
            if name.lower() not in ["website", "code", "images", "css", "js", "main page"] and not name.lower().startswith("blog "):
                # It's an old folder. Let's make sure it has no HTML files in it just in case
                has_html = False
                for r, ds, fs in os.walk(dir_path):
                    for f in fs:
                        if f.endswith('.html'):
                            has_html = True
                            break
                if not has_html:
                    try:
                        shutil.rmtree(dir_path)
                    except:
                        pass
        # also remove empty dirs
        for name in dirs:
            dir_path = os.path.join(root, name)
            try:
                if not os.listdir(dir_path):
                    os.rmdir(dir_path)
            except:
                pass

for cat in categories:
    cat_dir = os.path.join(base_dir, cat)
    if os.path.exists(cat_dir):
        clean_directory(cat_dir)

print("Subdirectory cleanup complete.")
