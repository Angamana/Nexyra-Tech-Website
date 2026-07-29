import os

file_path = r"C:\Users\angam\Downloads\Nexyra Website\Index\Index Page\index.html"

replacements = {
    "Daniel Morris": "Thabo Mokoena",
    "Natalie Brooks": "Lerato Ndlovu",
    "Sarah Whitman": "Nomsa Dlamini",
    "Thomas Fischer": "Sipho Zwane",
    "Laura Bennett": "Zanele Khumalo",
    "William Scott": "Johan van der Merwe",
    "Kevin Patel": "Kgaogelo Mahlangu",
    "Michael Chen": "Pieter Botha",
    "James O’Connor": "Kagiso Nkosi",
    "Robert Klein": "Xolani Mthembu"
}

with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

for old_name, new_name in replacements.items():
    content = content.replace(old_name, new_name)

with open(file_path, "w", encoding="utf-8") as f:
    f.write(content)

print("Names replaced successfully.")
