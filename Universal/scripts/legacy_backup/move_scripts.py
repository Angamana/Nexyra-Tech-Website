import os
import shutil

base_dir = r"C:\Users\angam\Downloads\Nexyra Website"
scripts_dir = os.path.join(base_dir, "Universal", "scripts")
os.makedirs(scripts_dir, exist_ok=True)
os.makedirs(os.path.join(scripts_dir, "legacy_backup"), exist_ok=True)

# We will move all Python scripts to legacy backup except for the ones we know we might need.
for root, dirs, files in os.walk(base_dir):
    if "Universal" in root or "Backend" in root or ".git" in root:
        continue
    for file in files:
        if file.endswith(".py") or file.endswith(".txt"):
            src_path = os.path.join(root, file)
            dest_path = os.path.join(scripts_dir, "legacy_backup", file)
            # Handle collision
            counter = 1
            while os.path.exists(dest_path):
                name, ext = os.path.splitext(file)
                dest_path = os.path.join(scripts_dir, "legacy_backup", f"{name}_{counter}{ext}")
                counter += 1
            shutil.move(src_path, dest_path)

print("Python scripts consolidated to Universal/scripts/legacy_backup")
