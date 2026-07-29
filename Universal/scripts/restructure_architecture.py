import os
import re
import shutil

base_dir = r"C:\Users\angam\Downloads\Nexyra Website"

# 1. Move the logo if it's in the root
root_logo = os.path.join(base_dir, "Nexyra Logo.png")
univ_images = os.path.join(base_dir, "Universal", "images")
os.makedirs(univ_images, exist_ok=True)
univ_logo = os.path.join(univ_images, "Nexyra Logo.png")

if os.path.exists(root_logo):
    shutil.move(root_logo, univ_logo)
    print(f"Moved {root_logo} to {univ_logo}")

# 2. Find all HTML files
html_files = []
for root, dirs, files in os.walk(base_dir):
    if "Universal" in root:
        continue
    for f in files:
        if f.endswith(".html"):
            html_files.append(os.path.join(root, f))

# Calculate new names and map them
rename_map = {} # old_abs_path -> new_abs_path
old_to_new_basename = {} # old_basename -> new_basename

for old_path in html_files:
    website_dir = os.path.dirname(old_path)
    page_dir = os.path.dirname(website_dir)
    page_folder_name = os.path.basename(page_dir)
    
    new_basename = f"{page_folder_name}.html"
    # exception for Index, let's keep it Index.html with capital I to match folder, wait, Windows is case insensitive, but we'll do exactly what user asked
    
    new_path = os.path.join(website_dir, new_basename)
    rename_map[old_path] = new_path
    
    old_to_new_basename[os.path.basename(old_path)] = new_basename

# Rename files on disk
renamed_files = []
for old_path, new_path in rename_map.items():
    if old_path != new_path:
        # If it's just a case change on Windows, we need to do a two-step rename or it might fail
        if old_path.lower() == new_path.lower():
            temp_path = old_path + ".tmp"
            os.rename(old_path, temp_path)
            os.rename(temp_path, new_path)
        else:
            os.rename(old_path, new_path)
        print(f"Renamed {os.path.basename(old_path)} to {os.path.basename(new_path)}")
    renamed_files.append(new_path)

# Helper function to summarize H1
def summarize_h1(text):
    text = re.sub(r'<[^>]+>', '', text).strip()
    if "Falcon AIDR" in text: return "Falcon AIDR"
    if "Zero Trust" in text: return "Zero Trust Security"
    if "Incident Response Time" in text: return "Automating Incident Response"
    if "Faster Incident Response" in text: return "Faster Incident Response"
    if "Common Security Mistakes" in text: return "Data Breach Causes"
    if "Continuous Monitoring" in text: return "Continuous Monitoring"
    if "Modern Cyber Threats" in text: return "Modern Cyber Threats"
    if "Advanced Persistent Threats" in text: return "Detecting APTs"
    if "Bypass Traditional Security" in text: return "Bypassing Security"
    if ":" in text: return text.split(":")[0].strip()
    words = text.split()
    if len(words) <= 4: return text
    return " ".join(words[:3])

# Process each renamed HTML file
for html_path in renamed_files:
    with open(html_path, "r", encoding="utf-8") as f:
        content = f.read()

    # --- A. Update internal links ---
    # We replace any href ending in the old basename with the new basename
    for old_base, new_base in old_to_new_basename.items():
        if old_base == new_base: continue
        # use regex to carefully replace href attribute targets
        # this matches href=".../old_base" or href="old_base"
        pattern = re.compile(r'(href=[\'"](?:[^"\'\>]*?/)?)(%s)([\'"])' % re.escape(old_base), re.IGNORECASE)
        content = pattern.sub(rf'\g<1>{new_base}\g<3>', content)

    # --- B. Update Title ---
    website_dir = os.path.dirname(html_path)
    page_dir = os.path.dirname(website_dir)
    parent_name = os.path.basename(page_dir)
    grandparent_name = os.path.basename(os.path.dirname(page_dir))
    
    new_title = ""
    is_main_page = parent_name in ["Index", "About", "Contact", "Error"] or (parent_name == "Main Page")
    
    if is_main_page:
        if parent_name == "Index":
            new_title = "Nexyra Tech | Home"
        elif parent_name == "About":
            new_title = "Nexyra Tech | About Us"
        elif parent_name == "Contact":
            new_title = "Nexyra Tech | Contact Us"
        elif parent_name == "Main Page":
            if grandparent_name == "Blog":
                new_title = "Nexyra Tech | Blog"
            elif grandparent_name == "Services":
                new_title = "Nexyra Tech | Services"
            else:
                new_title = f"Nexyra Tech | {grandparent_name}"
        else:
            new_title = f"Nexyra Tech | {parent_name}"
    else:
        # Sub Page, extract H1
        h1_match = re.search(r'<h1[^>]*>(.*?)</h1>', content, flags=re.IGNORECASE|re.DOTALL)
        if h1_match:
            summary = summarize_h1(h1_match.group(1))
            new_title = f"Nexyra Tech | {summary}"
        else:
            new_title = f"Nexyra Tech | {parent_name}"
            
    # Replace the <title> tag
    content = re.sub(r'<title>.*?</title>', f'<title>{new_title}</title>', content, flags=re.IGNORECASE|re.DOTALL)

    # --- C. Update Navigation Logo ---
    # The logo in the navbar probably has class="brand-logo" or something, but we can just find the old logo.png and replace it with Nexyra Logo.png
    # The user might have already tried replacing it, so we should look for logo.png, logo.svg, or Nexyra%20Logo.png
    # Actually, we need to calculate the relative path to Universal/images/Nexyra Logo.png
    rel_univ = os.path.relpath(univ_images, website_dir).replace(os.sep, "/")
    new_logo_href = f"{rel_univ}/Nexyra Logo.png"
    
    # Let's replace the src of any img inside the navbar (class="brand" or similar), or just replace all instances of Universal/images/...logo...
    content = re.sub(r'src=["\'][^"\']*?/Universal/images/(?:logo\.png|logo\.svg|Nexyra%20Logo\.png|Nexyra Logo\.png)["\']', f'src="{new_logo_href}"', content, flags=re.IGNORECASE)

    # --- D. Inject Favicon ---
    # Find existing favicon and remove it
    content = re.sub(r'<link[^>]*rel=["\'](?:shortcut )?icon["\'][^>]*>', '', content, flags=re.IGNORECASE)
    # Insert new favicon before </head>
    favicon_tag = f'\n  <link rel="icon" type="image/png" href="{new_logo_href}">\n'
    content = re.sub(r'</head>', f'{favicon_tag}</head>', content, flags=re.IGNORECASE)

    with open(html_path, "w", encoding="utf-8") as f:
        f.write(content)

print("Finished restructuring architecture, links, titles, and favicons!")
