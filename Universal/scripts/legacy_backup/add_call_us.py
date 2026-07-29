import os
from bs4 import BeautifulSoup

base_dir = r"C:\Users\angam\Downloads\Nexyra Website"

new_html = """
<div class="footer-phone-holder" style="margin-top: 30px;">
  <div class="footer-title">Call Us</div>
  <a class="footer-email-link" href="tel:+27694115473" style="text-decoration: none;">+27 69 411 5473</a>
</div>
"""

for root, dirs, files in os.walk(base_dir):
    for file in files:
        if file.endswith(".html"):
            file_path = os.path.join(root, file)
            try:
                with open(file_path, "r", encoding="utf-8") as f:
                    soup = BeautifulSoup(f, "html.parser")
                
                social_block = soup.find("div", class_="footer-social-block-two")
                if social_block:
                    # check if already inserted
                    next_sibling = social_block.find_next_sibling("div", class_="footer-phone-holder")
                    if not next_sibling:
                        new_tag = BeautifulSoup(new_html, "html.parser").div
                        social_block.insert_after(new_tag)
                        
                        with open(file_path, "w", encoding="utf-8") as f:
                            f.write(str(soup))
                        print(f"Updated {file_path}")
            except Exception as e:
                print(f"Error on {file_path}: {e}")

print("Added Call Us to all footers.")
