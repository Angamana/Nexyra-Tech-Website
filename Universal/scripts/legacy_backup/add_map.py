import os
import re
from bs4 import BeautifulSoup

base_dir = r"C:\Users\angam\Downloads\Nexyra Website"
iframe_html = '<iframe src="https://maps.google.com/maps?q=120+11th+St,+Parkmore,+Sandton,+2196&t=&z=13&ie=UTF8&iwloc=&output=embed" width="100%" height="150" style="border:0; border-radius: 8px; margin-top: 1.5rem;" allowfullscreen="" loading="lazy"></iframe>'

for root, dirs, files in os.walk(base_dir):
    for file in files:
        if file.endswith(".html"):
            file_path = os.path.join(root, file)
            with open(file_path, "r", encoding="utf-8") as f:
                soup = BeautifulSoup(f, "html.parser")
            
            changed = False
            footer = soup.find("section", class_="footer")
            if footer:
                text_element = footer.find("p", string=re.compile(r"Securing the next era", re.I))
                if text_element:
                    # check if already added
                    if not text_element.find_next_sibling("iframe"):
                        iframe_tag = BeautifulSoup(iframe_html, "html.parser").iframe
                        text_element.insert_after(iframe_tag)
                        changed = True

            if changed:
                with open(file_path, "w", encoding="utf-8") as f:
                    f.write(str(soup))
                print(f"Updated {file_path}")

print("Maps widget added successfully.")
