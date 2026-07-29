import os
from bs4 import BeautifulSoup

base_dir = r"C:\Users\angam\Downloads\Nexyra Website"

for root, dirs, files in os.walk(base_dir):
    for file in files:
        if file.endswith(".html"):
            file_path = os.path.join(root, file)
            with open(file_path, "r", encoding="utf-8") as f:
                soup = BeautifulSoup(f, "html.parser")
            
            changed = False
            footer = soup.find("section", class_="footer")
            if footer:
                iframe = footer.find("iframe")
                if iframe and "maps.google.com" in iframe.get("src", ""):
                    # Update height
                    iframe["height"] = "220"
                    # Update margin-top in style
                    iframe["style"] = "border:0; border-radius: 8px; margin-top: 0.5rem;"
                    changed = True

            if changed:
                with open(file_path, "w", encoding="utf-8") as f:
                    f.write(str(soup))
                print(f"Updated {file_path}")

print("Map height updated successfully.")
