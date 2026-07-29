import os
from bs4 import BeautifulSoup

files_to_extract = [
    ("Index Page", r"C:\Users\angam\Downloads\Nexyra Website\Index\Index Page\index.html"),
    ("About Page", r"C:\Users\angam\Downloads\Nexyra Website\About\About Page\about.html"),
    ("Services Page", r"C:\Users\angam\Downloads\Nexyra Website\Services\Services Page\services.html"),
    ("Contact Us Page", r"C:\Users\angam\Downloads\Nexyra Website\Contact\Contact Us Page\contact.html")
]

output_path = r"C:\Users\angam\Downloads\Nexyra Website\extracted.txt"

def extract_text_from_html(filepath):
    if not os.path.exists(filepath):
        return "File not found."
    
    with open(filepath, "r", encoding="utf-8") as f:
        soup = BeautifulSoup(f, "html.parser")
        
    for element in soup(["script", "style", "meta", "noscript", "svg", "head", "link", "nav"]):
        element.extract()
        
    text = soup.get_text(separator='\n')
    lines = (line.strip() for line in text.splitlines())
    chunks = (line for line in lines if line)
    return '\n\n'.join(chunks)

with open(output_path, "w", encoding="utf-8") as out:
    for page_name, filepath in files_to_extract:
        out.write(f"## {page_name}\n")
        out.write("---\n\n")
        extracted = extract_text_from_html(filepath)
        out.write(extracted)
        out.write("\n\n")

print(f"Extraction complete.")
