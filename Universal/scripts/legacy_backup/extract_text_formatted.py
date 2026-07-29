import os
from bs4 import BeautifulSoup
import re

files_to_extract = [
    ("Index Page", r"C:\Users\angam\Downloads\Nexyra Website\Index\Index Page\index.html"),
    ("About Page", r"C:\Users\angam\Downloads\Nexyra Website\About\About Page\about.html"),
    ("Services Page", r"C:\Users\angam\Downloads\Nexyra Website\Services\Services Page\services.html"),
    ("Contact Us Page", r"C:\Users\angam\Downloads\Nexyra Website\Contact\Contact Us Page\contact.html")
]

output_path = r"C:\Users\angam\Downloads\Nexyra Website\extracted_formatted.txt"

def clean_text(text):
    if not text:
        return ""
    text = re.sub(r'\s+', ' ', text)
    return text.strip()

def html_to_markdown(element):
    markdown = ""
    for child in element.children:
        if child.name in ['script', 'style', 'meta', 'noscript', 'svg', 'nav', 'footer', 'button', 'img']:
            continue
            
        if child.name and child.has_attr('class'):
            classes = ' '.join(child['class']).lower()
            if 'nav' in classes or 'footer' in classes or 'brand-strip' in classes or 'social' in classes:
                continue

        if child.name in ['h1', 'h2', 'h3', 'h4', 'h5', 'h6']:
            heading_level = int(child.name[1])
            text = clean_text(child.get_text())
            if text:
                markdown += f"\n{'#' * heading_level} {text}\n\n"
        elif child.name == 'p':
            text = clean_text(child.get_text())
            if text:
                markdown += f"{text}\n\n"
        elif child.name in ['ul', 'ol']:
            for li in child.find_all('li', recursive=False):
                text = clean_text(li.get_text())
                if text:
                    markdown += f"- {text}\n"
            markdown += "\n"
        elif child.name in ['div', 'section', 'main']:
            markdown += html_to_markdown(child)
        elif child.name is None:
            text = clean_text(child.string)
            if text and len(text) > 2 and not text.isdigit() and text != "%":
                markdown += f"{text}\n\n"
                
    return markdown

with open(output_path, "w", encoding="utf-8") as out:
    out.write("# Nexyra Website Content Review\n\n")
    out.write("This document contains the formatted text from the main pages of the website, with navigation, logos, and footers excluded.\n\n")
    
    for page_name, filepath in files_to_extract:
        out.write(f"---\n\n# {page_name}\n\n")
        
        if not os.path.exists(filepath):
            out.write("*File not found.*\n\n")
            continue
            
        with open(filepath, "r", encoding="utf-8") as f:
            soup = BeautifulSoup(f, "html.parser")
            
        for tag in soup(["nav", "footer", "script", "style", "svg", "img"]):
            tag.extract()
            
        for tag in soup.find_all(attrs={"class": re.compile(r"nav|footer|brand-strip|logo|social", re.I)}):
            tag.extract()

        body = soup.find('body')
        if body:
            md = html_to_markdown(body)
            md = re.sub(r'\n{3,}', '\n\n', md).strip()
            out.write(md)
        out.write("\n\n")

print("Extraction complete.")
