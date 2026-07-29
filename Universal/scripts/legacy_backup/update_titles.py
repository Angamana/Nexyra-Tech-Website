import os
from bs4 import BeautifulSoup
import re

base_dir = r"C:\Users\angam\Downloads\Nexyra Website"

def replace_text(text):
    if not text:
        return text
    text = re.sub(r'Sentrixa\s*-\s*Webflow Ecommerce Website Template', 'Nexyra Tech', text, flags=re.IGNORECASE)
    text = re.sub(r'Sentrixa', 'Nexyra Tech', text, flags=re.IGNORECASE)
    return text

for root, dirs, files in os.walk(base_dir):
    for file in files:
        if file.endswith(".html"):
            file_path = os.path.join(root, file)
            with open(file_path, "r", encoding="utf-8") as f:
                soup = BeautifulSoup(f, "html.parser")
                
            changed = False
            
            if soup.title and soup.title.string:
                new_title = replace_text(soup.title.string)
                if new_title != soup.title.string:
                    soup.title.string = new_title
                    changed = True
                    
            for meta in soup.find_all("meta"):
                if "content" in meta.attrs:
                    name_attr = meta.get("name", "").lower()
                    prop_attr = meta.get("property", "").lower()
                    
                    if name_attr in ["description"] or prop_attr in ["og:title", "og:description", "twitter:title", "twitter:description"]:
                        new_content = replace_text(meta["content"])
                        if new_content != meta["content"]:
                            meta["content"] = new_content
                            changed = True
                            
            if changed:
                with open(file_path, "w", encoding="utf-8") as f:
                    f.write(str(soup))
                print(f"Updated titles/meta in {file_path}")

print("Update complete.")
