import os
from bs4 import BeautifulSoup

file_path = r"C:\Users\angam\Downloads\Nexyra Website\Contact\Contact Us Page\contact.html"

with open(file_path, "r", encoding="utf-8") as f:
    soup = BeautifulSoup(f, "html.parser")

style_tag = soup.new_tag("style")
style_tag.string = """
  @media screen and (min-width: 992px) {
      .contact-info-wrap {
          justify-content: center !important;
          gap: 6rem !important;
      }
      .contact-info-text-content, .contact-form {
          flex: 0 1 auto !important;
          max-width: 45%;
      }
  }
"""

if soup.head:
    soup.head.append(style_tag)

with open(file_path, "w", encoding="utf-8") as f:
    f.write(str(soup))

print("Spacing updated successfully.")
