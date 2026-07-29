import os
import re

base_dir = r"C:\Users\angam\Downloads\Nexyra Website"

# Regex for .sub-text font-size
pattern_text = re.compile(r"(\.sub-text\s*\{[^\}]*?font-size:\s*)(?:var\(--_typograph---paragraph--paragraph-s\)|21px)(;)", re.MULTILINE | re.DOTALL)
# Regex for .sub-icon width and height
pattern_icon = re.compile(r"(\.sub-icon\s*\{[^\}]*?width:\s*)18px(;[^\}]*?height:\s*)18px(;)", re.MULTILINE | re.DOTALL)

for root, dirs, files in os.walk(base_dir):
    for file in files:
        if file.endswith(".css"):
            file_path = os.path.join(root, file)
            try:
                with open(file_path, "r", encoding="utf-8") as f:
                    content = f.read()
                
                changed = False
                if pattern_text.search(content):
                    content = pattern_text.sub(r"\g<1>28px\g<2>", content)
                    changed = True
                if pattern_icon.search(content):
                    content = pattern_icon.sub(r"\g<1>28px\g<2>28px\g<3>", content)
                    changed = True
                
                if changed:
                    with open(file_path, "w", encoding="utf-8") as f:
                        f.write(content)
                    print(f"Updated {file_path}")
            except Exception as e:
                print(f"Error on {file_path}: {e}")

print("Sub-text and sub-icon sizes updated to 28px.")
