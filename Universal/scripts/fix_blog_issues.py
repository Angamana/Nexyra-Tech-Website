import os
import re

base_dir = r"C:\Users\angam\Downloads\Nexyra Website"

# 1. Fix the Title for Blog Main Page
blog_main_path = os.path.join(base_dir, "Blog", "Blog Main Page", "website", "Blog Main Page.html")
with open(blog_main_path, "r", encoding="utf-8") as f:
    content = f.read()

content = re.sub(r'<title>.*?</title>', '<title>Nexyra Tech | Blog</title>', content, flags=re.IGNORECASE)

with open(blog_main_path, "w", encoding="utf-8") as f:
    f.write(content)

# 2. Fix the navigation link for Blog across ALL html files
html_files = []
for root, dirs, files in os.walk(base_dir):
    if "Universal" in root: continue
    for f in files:
        if f.endswith(".html"):
            html_files.append(os.path.join(root, f))

for path in html_files:
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()
    
    # We replace any reference to Main Page/website/Blog Main Page.html with Blog Main Page/website/Blog Main Page.html
    new_content = content.replace('/Main Page/website/Blog Main Page.html', '/Blog Main Page/website/Blog Main Page.html')
    
    # Just in case there are single quotes or backslashes
    new_content = new_content.replace('\\Main Page\\website\\Blog Main Page.html', '\\Blog Main Page\\website\\Blog Main Page.html')
    
    if new_content != content:
        with open(path, "w", encoding="utf-8") as f:
            f.write(new_content)

# 3. Update the images for Blog 1, 2, 3, 4
for i in range(1, 5):
    sub_dir = os.path.join(base_dir, "Blog", f"Blog {i}")
    html_path = os.path.join(sub_dir, "website", f"Blog {i}.html")
    images_dir = os.path.join(sub_dir, "images")
    
    if not os.path.exists(html_path):
        continue
        
    with open(html_path, "r", encoding="utf-8") as f:
        html_content = f.read()
        
    # Find the main image for this blog
    match = re.search(r'class=["\']post-main-img["\'][^>]*src=["\']([^"\']+)["\']', html_content)
    if not match:
        continue
        
    old_src = match.group(1)
    old_filename = old_src.split('/')[-1]
    
    # The new filename is 'Blog Page {i}.png'
    new_filename = f"Blog Page {i}.png"
    
    if old_filename == new_filename:
        continue
        
    print(f"Blog {i}: replacing {old_filename} with {new_filename}")
    
    # Update this blog page
    html_content = html_content.replace(old_filename, new_filename)
    
    # Also we should update the src to point to the local images folder if it was pointing to Universal
    # Since the new image is in `Blog {i}/images/`, the relative path from `website/Blog {i}.html` is `../images/Blog Page {i}.png`
    # Let's just blindly replace the whole src for post-main-img
    html_content = re.sub(
        r'(class=["\']post-main-img["\'][^>]*src=["\'])[^"\']+["\']', 
        rf'\g<1>../images/{new_filename}"', 
        html_content
    )
    
    with open(html_path, "w", encoding="utf-8") as f:
        f.write(html_content)
        
    # Update Blog Main Page
    with open(blog_main_path, "r", encoding="utf-8") as f:
        main_content = f.read()
        
    # The Blog Main Page links to the thumbnail, which might be `old_filename`. We replace it.
    main_content = main_content.replace(old_filename, new_filename)
    
    # And make sure it points to `../../Blog {i}/images/` instead of `../../Universal/images/`
    main_content = re.sub(
        r'src=["\'][^"\']*/Universal/images/' + re.escape(new_filename) + r'["\']',
        f'src="../../Blog {i}/images/{new_filename}"',
        main_content
    )
    
    with open(blog_main_path, "w", encoding="utf-8") as f:
        f.write(main_content)

print("Finished fixing blog issues!")
