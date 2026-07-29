import os
from bs4 import BeautifulSoup

base_dir = r"C:\Users\angam\Downloads\Nexyra Website"

css_str = """
.company-footer-pill {
    border-radius: 50px;
    background-color: #3b44ff30;
    border-bottom: 1.5px solid #4a4e98;
    padding: 6px 16px;
    display: flex;
    width: fit-content;
    margin-bottom: 12px;
    align-items: center;
    justify-content: center;
}
"""

for root, dirs, files in os.walk(base_dir):
    for file in files:
        if file.endswith(".html"):
            path = os.path.join(root, file)
            try:
                with open(path, "r", encoding="utf-8") as f:
                    html = f.read()
                
                soup = BeautifulSoup(html, "html.parser")
                changed = False
                
                # Find footer title "Company"
                for title in soup.find_all("div", class_="footer-title"):
                    if title.string and "Company" in title.string:
                        holder = title.find_next_sibling("div", class_="footer-link-two-holder")
                        if holder:
                            wraps = holder.find_all("div", class_="footer-link-two-wrap")
                            for wrap in wraps:
                                # Check if already wrapped
                                if wrap.parent and 'company-footer-pill' in wrap.parent.get('class', []):
                                    continue
                                
                                pill = soup.new_tag("div", attrs={"class": "company-footer-pill"})
                                wrap.wrap(pill)
                                changed = True
                
                # Inject CSS if changed and not already there
                if changed:
                    if ".company-footer-pill {" not in html:
                        head = soup.find("head")
                        if head:
                            style_tag = soup.new_tag("style")
                            style_tag.string = css_str
                            head.append(style_tag)
                            
                    with open(path, "w", encoding="utf-8") as f:
                        f.write(str(soup))
                    print(f"Updated {path}")
                    
            except Exception as e:
                print(f"Error processing {path}: {e}")

print("Done.")
