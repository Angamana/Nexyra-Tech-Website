import os

base_dir = r"C:\Users\angam\Downloads\Nexyra Website"

py_files = []
for root, dirs, files in os.walk(base_dir):
    if "Universal" in root or "Backend" in root:
        continue
    for file in files:
        if file.endswith(".py"):
            py_files.append(os.path.join(root, file))

print(f"Found {len(py_files)} Python files:")
for f in py_files:
    print(os.path.basename(f))
