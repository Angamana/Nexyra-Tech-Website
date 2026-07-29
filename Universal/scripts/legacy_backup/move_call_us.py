import os
import re

base_dir = r"C:\Users\angam\Downloads\Nexyra Website"

pattern = re.compile(r'(<div\s+class="footer-phone-holder"\s+style="[^"]*?margin-top:\s*)30px(;">)')

for root, dirs, files in os.walk(base_dir):
    for file in files:
        if file.endswith(".html"):
            file_path = os.path.join(root, file)
            try:
                with open(file_path, "r", encoding="utf-8") as f:
                    content = f.read()
                
                if pattern.search(content):
                    content = pattern.sub(r"\g<1>10px\g<2>", content)
                    with open(file_path, "w", encoding="utf-8") as f:
                        f.write(content)
                    print(f"Updated {file_path}")
            except Exception as e:
                print(f"Error on {file_path}: {e}")

print("Moved Call Us up by changing margin-top to 10px.")
