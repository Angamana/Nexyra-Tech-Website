import os

base_dir = r"C:\Users\angam\Downloads\Nexyra Website"
main_page_html = os.path.join(base_dir, "Blog", "Main Page", "website", "Blog.html")

with open(main_page_html, "r", encoding="utf-8") as f:
    main_content = f.read()

for i in range(1, 10):
    sub_dir = os.path.join(base_dir, "Blog", f"Blog Sub {i}")
    images_dir = os.path.join(sub_dir, "images")
    
    if not os.path.exists(images_dir):
        continue
        
    old_images = [f for f in os.listdir(images_dir) if f != f"Blog Sub Page {i}.png" and (f.startswith("Blog-") or f.endswith(".png"))]
    
    if not old_images:
        print(f"No old image found for Blog Sub {i}")
        continue
        
    # Exclude Avatar images if they end in .png but don't start with Blog-
    old_images = [f for f in old_images if f.startswith("Blog-")]
    
    if not old_images:
        print(f"No matching Blog- image found for Blog Sub {i}")
        continue
        
    old_img_name = old_images[0]
    new_img_name = f"Blog Sub Page {i}.png"
    
    print(f"Replacing '{old_img_name}' with '{new_img_name}' for Blog Sub {i}")
    
    # Update the sub page HTML
    sub_website_dir = os.path.join(sub_dir, "website")
    for html_file in os.listdir(sub_website_dir):
        if html_file.endswith(".html"):
            html_path = os.path.join(sub_website_dir, html_file)
            with open(html_path, "r", encoding="utf-8") as f:
                content = f.read()
            
            content = content.replace(old_img_name, new_img_name)
            
            with open(html_path, "w", encoding="utf-8") as f:
                f.write(content)
                
    # Update the main page HTML
    # Note: URLs in HTML might be URL-encoded (e.g., %20)
    # But usually literal string replace works because the script `distribute_blog_images` didn't url encode the filenames during replacement.
    main_content = main_content.replace(old_img_name, new_img_name)
    
    # Also delete the old image since it's no longer needed
    try:
        os.remove(os.path.join(images_dir, old_img_name))
    except Exception as e:
        print(f"Could not remove {old_img_name}: {e}")

with open(main_page_html, "w", encoding="utf-8") as f:
    f.write(main_content)

print("Finished updating blog thumbnail links!")
