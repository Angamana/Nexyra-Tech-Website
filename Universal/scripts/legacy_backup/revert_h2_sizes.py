import os

base_dir = r"C:\Users\angam\Downloads\Nexyra Website"

replacements = {
    "--_typograph---h2-style--font-size: 78px;": "--_typograph---h2-style--font-size: 52px;",
    "--_typograph---h2-style--font-size: 66px;": "--_typograph---h2-style--font-size: 44px;",
    "--_typograph---h2-style--font-size: 60px;": "--_typograph---h2-style--font-size: 40px;",
    "--_typograph---h2-style--font-size: 48px;": "--_typograph---h2-style--font-size: 32px;"
}

for root, dirs, files in os.walk(base_dir):
    for file in files:
        if file.endswith(".css"):
            file_path = os.path.join(root, file)
            try:
                with open(file_path, "r", encoding="utf-8") as f:
                    content = f.read()
                
                changed = False
                for old_str, new_str in replacements.items():
                    if old_str in content:
                        content = content.replace(old_str, new_str)
                        changed = True
                        
                if changed:
                    with open(file_path, "w", encoding="utf-8") as f:
                        f.write(content)
                    print(f"Updated {file_path}")
            except Exception as e:
                print(f"Error on {file_path}: {e}")

print("CSS variable sizes reverted.")
