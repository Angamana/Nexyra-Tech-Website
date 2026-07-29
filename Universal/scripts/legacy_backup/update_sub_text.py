import os
import re

base_dir = r"C:\Users\angam\Downloads\Nexyra Website"

# We'll use a regex to replace the font-size inside .sub-text { ... }
pattern = re.compile(r"(\.sub-text\s*\{[^\}]*?font-size:\s*)var\(--_typograph---paragraph--paragraph-s\)(;)", re.MULTILINE | re.DOTALL)

for root, dirs, files in os.walk(base_dir):
    for file in files:
        if file.endswith(".css"):
            file_path = os.path.join(root, file)
            try:
                with open(file_path, "r", encoding="utf-8") as f:
                    content = f.read()
                
                if pattern.search(content):
                    content = pattern.sub(r"\g<1>21px\g<2>", content)
                    with open(file_path, "w", encoding="utf-8") as f:
                        f.write(content)
                    print(f"Updated {file_path}")
            except Exception as e:
                print(f"Error on {file_path}: {e}")

print("Sub-text sizes updated by 150% across all CSS.")
