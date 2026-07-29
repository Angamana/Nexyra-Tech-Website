import os
import re

base_dir = r"c:\Users\angam\Downloads\Nexyra Website"
cookie_js_path = os.path.join(base_dir, "cookie-policy.js")

# 1. Update cookie-policy.js to use dynamic basePath
try:
    with open(cookie_js_path, "r", encoding="utf-8") as f:
        cookie_js = f.read()

    # Replace the old basePath logic
    old_base_path_logic = """    // Determine the base path depending on where we are
    let basePath = "";
    if (window.location.pathname.includes("/Index/") || window.location.pathname.includes("/About/") || window.location.pathname.includes("/Contact/")) {
        basePath = "../../";
    }"""
    
    new_base_path_logic = """    // Determine the base path dynamically based on where this script is loaded from
    let basePath = "";
    const scripts = document.getElementsByTagName('script');
    for (let i = 0; i < scripts.length; i++) {
        if (scripts[i].src && scripts[i].src.includes("cookie-policy.js")) {
            const src = scripts[i].src;
            basePath = src.substring(0, src.indexOf("cookie-policy.js"));
            break;
        }
    }"""
    
    if old_base_path_logic in cookie_js:
        cookie_js = cookie_js.replace(old_base_path_logic, new_base_path_logic)
        with open(cookie_js_path, "w", encoding="utf-8") as f:
            f.write(cookie_js)
        print("Updated cookie-policy.js to use dynamic basePath.")
except Exception as e:
    print(f"Error updating cookie-policy.js: {e}")

# 2. Inject cookie-policy.js into all HTML files
html_files = []
for root, dirs, files in os.walk(base_dir):
    for f in files:
        if f.endswith(".html"):
            html_files.append(os.path.join(root, f))

injected_count = 0

for file_path in html_files:
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()
            
        if "cookie-policy.js" not in content:
            # Need to inject
            file_dir = os.path.dirname(file_path)
            rel_path = os.path.relpath(cookie_js_path, file_dir).replace("\\", "/")
            
            script_tag = f'\n    <script src="{rel_path}" type="text/javascript"></script>\n</body>'
            new_content = re.sub(r'</body>', script_tag, content, flags=re.IGNORECASE)
            
            if new_content != content:
                with open(file_path, "w", encoding="utf-8") as f:
                    f.write(new_content)
                injected_count += 1
    except Exception as e:
        print(f"Error processing {file_path}: {e}")

print(f"Injected cookie-policy.js into {injected_count} HTML files.")
