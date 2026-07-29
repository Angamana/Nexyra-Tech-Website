import os
import re

directory = r"C:\Users\angam\Downloads\Nexyra Website"

# Regex patterns to match the avatar and wrighter image wraps including their contents
avatar_pattern = re.compile(r'<div class="avatar-img-wrap">.*?</div>', re.DOTALL)
wrighter_pattern = re.compile(r'<div class="wrighter-img-wrap">.*?</div>', re.DOTALL)

for root, dirs, files in os.walk(directory):
    for file in files:
        if file.endswith(".html"):
            filepath = os.path.join(root, file)
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
                
            new_content = avatar_pattern.sub('', content)
            new_content = wrighter_pattern.sub('', new_content)
            
            if new_content != content:
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                print(f"Removed images from: {filepath}")

print("Done.")
