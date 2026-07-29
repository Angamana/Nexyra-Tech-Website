import os
import shutil

base_dir = r"C:\Users\angam\Downloads\Nexyra Website"
keep_dirs = ["Universal", "Backend", "Home", "About", "Contact", "Error", "Policies", "Blog", "Services"]

# Remove top-level dirs that are not in keep_dirs
for item in os.listdir(base_dir):
    item_path = os.path.join(base_dir, item)
    if os.path.isdir(item_path):
        if item not in keep_dirs and item != ".git":
            try:
                shutil.rmtree(item_path)
            except Exception as e:
                pass

print("Old directories cleaned up.")
