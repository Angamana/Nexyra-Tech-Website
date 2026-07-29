import os
import urllib.parse
from bs4 import BeautifulSoup

image_mapping = [
    {"folder": "Blog Sub 1", "filename": "zero-trust-security-why-perimeter-defense-is-no-longer-enough.html", "img": "Blog-USB - Blue.png"},
    {"folder": "Blog Sub 2", "filename": "how-faster-incident-response-limits-security-business-impact.html", "img": "Blog-Scale-Agentic-AI - Blue.png"},
    {"folder": "Blog Sub 3", "filename": "understanding-modern-cyber-threats-in-cloud-environments.html", "img": "Blog-Integration - Blue.png"},
    {"folder": "Blog Sub 4", "filename": "reducing-incident-response-time-with-automation.html", "img": "Blog-Insider-Risk - Blue.png"},
    {"folder": "Blog Sub 5", "filename": "common-security-mistakes-that-lead-to-data-breaches.html", "img": "Blog-FalconCloudSecurity-AI - Blue.png"},
    {"folder": "Blog Sub 6", "filename": "why-continuous-monitoring-beats-periodic-audits-2.html", "img": "Blog-Data-Protection-Day-2026 - Blue.png"},
    {"folder": "Blog Sub 7", "filename": "why-continuous-monitoring-beats-periodic-audits.html", "img": "Blog-DataLeakage - Blue.png"},
    {"folder": "Blog Sub 8", "filename": "detecting-advanced-persistent-threats-before-damage-occurs.html", "img": "Blog-ByteBack - blue.png"},
    {"folder": "Blog Sub 9", "filename": "how-modern-cyber-attacks-bypass-traditional-security-controls.html", "img": "Blog-AdvancedWebShell - Blue.png"}
]

base_dir = r"C:\Users\angam\Downloads\Nexyra Website\Blog - Main Page"

for mapping in image_mapping:
    # 1. Update individual sub-blog HTML files
    html_path = os.path.join(base_dir, mapping["folder"], "sentrixa-template.webflow.io", "blog", mapping["filename"])
    if os.path.exists(html_path):
        with open(html_path, "r", encoding="utf-8") as f:
            soup = BeautifulSoup(f, "html.parser")
            
        img_name_encoded = urllib.parse.quote(mapping["img"])
        rel_path = f"../../cdn.prod.website-files.com/6965d25065d78378ecfa1ae3/{img_name_encoded}"
        
        main_img = soup.find("img", class_="post-main-img")
        if main_img:
            main_img["src"] = rel_path
            # Remove srcset and sizes because new local images don't have variants
            if "srcset" in main_img.attrs:
                del main_img["srcset"]
            if "sizes" in main_img.attrs:
                del main_img["sizes"]
                
        with open(html_path, "w", encoding="utf-8") as f:
            f.write(str(soup))

# 2. Update the main blog.html file
main_blog_path = os.path.join(base_dir, "sentrixa-template.webflow.io", "blog.html")
if os.path.exists(main_blog_path):
    with open(main_blog_path, "r", encoding="utf-8") as f:
        soup = BeautifulSoup(f, "html.parser")
        
    list_bottom = soup.find("div", class_="blog-collection-list-bottom")
    if list_bottom:
        items = list_bottom.find_all("div", role="listitem")
        
        for idx, item in enumerate(items):
            if idx < len(image_mapping):
                mapping = image_mapping[idx]
                img_name_encoded = urllib.parse.quote(mapping["img"])
                rel_path = f"../{mapping['folder']}/cdn.prod.website-files.com/6965d25065d78378ecfa1ae3/{img_name_encoded}"
                
                # In the list item, find the main image
                img_tag = item.find("img")
                if img_tag:
                    img_tag["src"] = rel_path
                    if "srcset" in img_tag.attrs:
                        del img_tag["srcset"]
                    if "sizes" in img_tag.attrs:
                        del img_tag["sizes"]

    with open(main_blog_path, "w", encoding="utf-8") as f:
        f.write(str(soup))
    print("Main blog.html images updated.")
