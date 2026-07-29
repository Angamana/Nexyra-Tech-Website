import os

base_dir = r"C:\Users\angam\Downloads\Nexyra Website"

for root, dirs, files in os.walk(base_dir):
    for file in files:
        if file.endswith(".html"):
            path = os.path.join(root, file)
            try:
                with open(path, "r", encoding="utf-8") as f:
                    html = f.read()
                
                # Replace the margin-bottom
                new_html = html.replace("margin-bottom: 12px;", "margin-bottom: 6px;")
                
                if new_html != html:
                    with open(path, "w", encoding="utf-8") as f:
                        f.write(new_html)
                    print(f"Updated {path}")
                    
            except Exception as e:
                print(f"Error processing {path}: {e}")

print("Done reducing margins.")
