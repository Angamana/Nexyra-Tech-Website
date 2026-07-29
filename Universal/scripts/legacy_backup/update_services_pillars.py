import os
from bs4 import BeautifulSoup

file_path = r"C:\Users\angam\Downloads\Nexyra Website\Services\Services Page\services.html"

with open(file_path, "r", encoding="utf-8") as f:
    soup = BeautifulSoup(f, "html.parser")

style_tag = soup.new_tag("style")
style_tag.string = """
  /* Enlarge and center text in Five Service Pillars */
  .service-text-content > div:nth-child(2) {
    margin-top: auto;
    margin-bottom: auto;
  }
  .service-text-content p[style*="0.7rem"] {
    font-size: 0.9rem !important;
  }
  .service-text-content .service-card-titel {
    font-size: 1.8rem !important;
    line-height: 1.3 !important;
  }
  .service-text-content .service-card-text {
    font-size: 1.15rem !important;
    line-height: 1.5 !important;
  }
"""

if soup.head:
    soup.head.append(style_tag)

with open(file_path, "w", encoding="utf-8") as f:
    f.write(str(soup))

print("Services pillars text centered and enlarged.")
