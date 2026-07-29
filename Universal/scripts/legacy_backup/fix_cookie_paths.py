import os
import re

base_dir = r"C:\Users\angam\Downloads\Nexyra Website"
script_target_dir = r"Python Code/cookie-policy.js"

# We want to find the <script src="...cookie-policy.js"...></script>
# and replace the src with the correct relative path to Python Code/cookie-policy.js

for root, dirs, files in os.walk(base_dir):
    for file in files:
        if file.endswith(".html"):
            file_path = os.path.join(root, file)
            
            # Calculate depth from base_dir
            # e.g. root = C:\...\Nexyra Website\Folder
            # rel_path = Folder
            # depth = 1
            rel_dir = os.path.relpath(root, base_dir)
            if rel_dir == ".":
                depth = 0
                prefix = ""
            else:
                # normalize path separators
                rel_dir = rel_dir.replace("\\", "/")
                depth = len(rel_dir.split("/"))
                prefix = "../" * depth
                
            new_script_src = f"{prefix}{script_target_dir}"
            
            with open(file_path, "r", encoding="utf-8") as f:
                content = f.read()
                
            # Find the existing cookie-policy script tag
            # It might look like <script src="../../../../cookie-policy.js" type="text/javascript"></script>
            # We'll use a regex to replace the src attribute value if the filename is cookie-policy.js
            
            # Pattern to match src="ANYTHING/cookie-policy.js" or src="cookie-policy.js"
            pattern = r'src="[^"]*cookie-policy\.js"'
            replacement = f'src="{new_script_src}"'
            
            if re.search(pattern, content):
                new_content = re.sub(pattern, replacement, content)
                
                with open(file_path, "w", encoding="utf-8") as f:
                    f.write(new_content)
                print(f"Updated {file_path} with depth {depth}")

print("Cookie paths updated across all HTML files.")
