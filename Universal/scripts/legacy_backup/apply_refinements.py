import os
from bs4 import BeautifulSoup
import re

base_dir = r"C:\Users\angam\Downloads\Nexyra Website"

def add_full_stop(text):
    text = text.strip()
    if text and text[-1] not in ['.', '!', '?', ':']:
        text += '.'
    return text

for root, dirs, files in os.walk(base_dir):
    for file in files:
        if file.endswith(".html"):
            file_path = os.path.join(root, file)
            with open(file_path, "r", encoding="utf-8") as f:
                soup = BeautifulSoup(f, "html.parser")
                
            changed = False
            
            # --- 1. Bullets ---
            # Standard lists
            for li in soup.find_all("li"):
                if li.string and li.string.strip():
                    li.string = add_full_stop(li.string)
                    changed = True
                elif li.get_text(strip=True):
                    # If it has child tags but single text node
                    for child in li.children:
                        if isinstance(child, str) and child.strip():
                            new_text = add_full_stop(child)
                            if new_text != child:
                                child.replace_with(new_text)
                                changed = True
            
            # Custom webflow list items (like feature lists)
            item_classes = re.compile(r'item-text|list-text|feature-text', re.I)
            for item in soup.find_all(attrs={"class": item_classes}):
                if item.string and item.string.strip():
                    new_text = add_full_stop(item.string)
                    if new_text != item.string:
                        item.string = new_text
                        changed = True

            # --- 2. Remove CTA ---
            # "Start Protecting Your Business Today" CTA is typically a section with "contact-cta" or similar
            if "index.html" not in file.lower():
                cta_title = soup.find(string=re.compile(r"Start Protecting Your Business Today", re.I))
                if cta_title:
                    cta_section = cta_title.find_parent("section")
                    if cta_section:
                        cta_section.decompose()
                        changed = True
                        
                # --- 3. Footer Background ---
                footer = soup.find("section", class_="footer")
                if footer:
                    footer['style'] = "background: radial-gradient(ellipse 80% 120% at 50% 0%, rgba(72, 95, 255, 0.55) 0%, rgba(30, 30, 90, 0.35) 45%, transparent 70%), #070a1a; position: relative;"
                    changed = True

            # --- 4. About Page Specifics ---
            if "about.html" in file.lower():
                # Reword 1
                adv_text = soup.find(string=re.compile(r"Nexyra Tech approaches every engagement as an advisor first", re.I))
                if adv_text:
                    adv_text.replace_with("As your trusted advisors, we take the time to deeply analyze your infrastructure. Our focus is strictly on identifying genuine vulnerabilities and delivering tailored architectural improvements that serve your long-term success.")
                    changed = True
                
                # Reword 2
                gap_text = soup.find(string=re.compile(r"Old vendors move slowly", re.I))
                if gap_text:
                    gap_text.replace_with("Traditional security models often fail to balance speed with deep technical rigor. Nexyra Tech bridges this divide by delivering rapid, decisive interventions powered by veterans who have engineered defenses at the enterprise level.")
                    changed = True
                    
                # Remove "How We Work With You"
                hww_bg = soup.find("div", class_="vision-center-bg")
                if hww_bg:
                    hww_bg.decompose()
                    changed = True

            # --- 5. Services Page Specifics ---
            if "services.html" in file.lower():
                # Change text
                powering_text = soup.find(string=re.compile(r"POWERING THE WORLD.*S BEST COMPANIES", re.I))
                if powering_text:
                    powering_text.replace_with("Industries we service")
                    changed = True
                    
                # Center and lift 5 pillars
                five_pillars = soup.find(string=re.compile(r"Our Five Service Pillars", re.I))
                if five_pillars:
                    container = five_pillars.find_parent("div", class_="values-text-content")
                    if container:
                        container['style'] = "text-align: center; display: flex; flex-direction: column; align-items: center; margin-top: -3rem; margin-bottom: 2rem;"
                        changed = True

            if changed:
                with open(file_path, "w", encoding="utf-8") as f:
                    f.write(str(soup))
                print(f"Updated {file_path}")

print("Site-wide update complete.")
