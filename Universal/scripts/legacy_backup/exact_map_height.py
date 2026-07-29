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
                    # Increase height to fill the space without stretching the footer
                    iframe["height"] = "190"
                    # Decrease margin to be just right under the text
                    iframe["style"] = "border:0; border-radius: 8px; margin-top: 4px;"
                    changed = True

            if changed:
                with open(file_path, "w", encoding="utf-8") as f:
                    f.write(str(soup))
                print(f"Updated {file_path}")

print("Map dimensions updated.")
