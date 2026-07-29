import os
from bs4 import BeautifulSoup

file_path = r"C:\Users\angam\Downloads\Nexyra Website\About\About Page\about.html"

with open(file_path, "r", encoding="utf-8") as f:
    soup = BeautifulSoup(f, "html.parser")

style_tag = soup.new_tag("style")
style_tag.string = """
  .section.vision {
      padding-bottom: 4rem !important;
  }
"""

if soup.head:
    soup.head.append(style_tag)

with open(file_path, "w", encoding="utf-8") as f:
    f.write(str(soup))

print("Padding removed successfully.")
