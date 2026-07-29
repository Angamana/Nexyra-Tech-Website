import os
import shutil
from bs4 import BeautifulSoup
from urllib.parse import urlparse, unquote

base_dir = r"C:\Users\angam\Downloads\Nexyra Website"

# Define mapping for correct HTML locations
html_targets = {
    "index.html": r"Home\website\index.html",
    "about.html": r"About\website\About.html",
    "contact.html": r"Contact\website\Contact.html",
    "404.html": r"Error\website\Error.html",
    "services.html": r"Services\Main Page\website\Services.html",
    "blog.html": r"Blog\Main Page\website\Blog.html",
    "how-ai-improves-threat-detection-without-increasing-security-team-workload.html": r"Blog\Blog 1\website\how-ai-improves-threat-detection-without-increasing-security-team-workload.html",
    "how-ai-is-changing-threat-detection.html": r"Blog\Blog 2\website\how-ai-is-changing-threat-detection.html",
    "building-a-scalable-security-strategy.html": r"Blog\Blog 3\website\building-a-scalable-security-strategy.html",
    "identity-security-the-new-perimeter.html": r"Blog\Blog 4\website\identity-security-the-new-perimeter.html",
    "zero-trust-security-why-perimeter-defense-is-no-longer-enough.html": r"Blog\Blog Sub 1\website\zero-trust-security-why-perimeter-defense-is-no-longer-enough.html",
    "how-faster-incident-response-limits-security-business-impact.html": r"Blog\Blog Sub 2\website\how-faster-incident-response-limits-security-business-impact.html",
    "understanding-modern-cyber-threats-in-cloud-environments.html": r"Blog\Blog Sub 3\website\understanding-modern-cyber-threats-in-cloud-environments.html",
    "reducing-incident-response-time-with-automation.html": r"Blog\Blog Sub 4\website\reducing-incident-response-time-with-automation.html",
    "common-security-mistakes-that-lead-to-data-breaches.html": r"Blog\Blog Sub 5\website\common-security-mistakes-that-lead-to-data-breaches.html",
    "why-continuous-monitoring-beats-periodic-audits-2.html": r"Blog\Blog Sub 6\website\why-continuous-monitoring-beats-periodic-audits-2.html",
    "why-continuous-monitoring-beats-periodic-audits.html": r"Blog\Blog Sub 7\website\why-continuous-monitoring-beats-periodic-audits.html",
    "detecting-advanced-persistent-threats-before-damage-occurs.html": r"Blog\Blog Sub 8\website\detecting-advanced-persistent-threats-before-damage-occurs.html",
    "how-modern-cyber-attacks-bypass-traditional-security-controls.html": r"Blog\Blog Sub 9\website\how-modern-cyber-attacks-bypass-traditional-security-controls.html",
}

all_html_files = []
for root, dirs, files in os.walk(base_dir):
    if "Universal" in root or "Backend" in root or ".git" in root:
        continue
    for file in files:
        if file.endswith(".html") and file not in ["apollo.html", "csrf.html"]:
            all_html_files.append(os.path.join(root, file))

# Find the best version of each HTML file (the ones recently written by reorganize_architecture.py)
# We can just pick the first one that exists, or better, the one inside a 'website' folder.
best_html_files = {}
for hf in all_html_files:
    fname = os.path.basename(hf).lower()
    if fname not in best_html_files:
        best_html_files[fname] = hf
    elif "website" in hf.lower():
        best_html_files[fname] = hf

# Now move them to their correct targets and rewrite links
new_absolute_targets = {}
for fname, source_path in best_html_files.items():
    for orig_name, rel_target in html_targets.items():
        if orig_name.lower() == fname:
            target_path = os.path.join(base_dir, rel_target)
            new_absolute_targets[orig_name] = target_path
            os.makedirs(os.path.dirname(target_path), exist_ok=True)
            if source_path != target_path:
                shutil.copy2(source_path, target_path)
            break

# Rewrite links in the newly placed HTML files
for orig_name, target_path in new_absolute_targets.items():
    try:
        with open(target_path, 'r', encoding='utf-8') as f:
            soup = BeautifulSoup(f, 'html.parser')
    except Exception as e:
        print(f"Error reading {target_path}: {e}")
        continue
        
    target_dir = os.path.dirname(target_path)
    
    # We need to resolve all relative links in the HTML file based on its old path (since it was moved),
    # but since it might have been already rewritten to point to Universal, its links are relative to `source_path`.
    # Actually, it's easier to find the absolute path of the target, and re-relativize.
    source_path = best_html_files[orig_name.lower()]
    source_dir = os.path.dirname(source_path)
    
    def re_relativize(tag, attr):
        val = tag.get(attr)
        if not val: return
        parsed = urlparse(val)
        if parsed.scheme or parsed.netloc or val.startswith('data:'): return
        
        # Absolute path of the asset
        abs_asset_path = os.path.normpath(os.path.join(source_dir, unquote(parsed.path)))
        if os.path.exists(abs_asset_path):
            new_rel = os.path.relpath(abs_asset_path, target_dir).replace('\\', '/')
            tag[attr] = new_rel
            
    for link in soup.find_all('link', rel='stylesheet'): re_relativize(link, 'href')
    for script in soup.find_all('script'): re_relativize(script, 'src')
    for img in soup.find_all('img'): re_relativize(img, 'src')
    
    # Fix HTML links to point to new HTML targets
    for a in soup.find_all('a'):
        href = a.get('href')
        if not href: continue
        parsed = urlparse(href)
        if parsed.scheme or parsed.netloc or href.startswith('#') or href.startswith('mailto:') or href.startswith('tel:'): continue
        
        abs_asset_path = os.path.normpath(os.path.join(source_dir, unquote(parsed.path)))
        # Is this an HTML file?
        filename = os.path.basename(abs_asset_path).lower()
        if filename in [k.lower() for k in html_targets.keys()]:
            for orig, t_path in new_absolute_targets.items():
                if orig.lower() == filename:
                    new_rel = os.path.relpath(t_path, target_dir).replace('\\', '/')
                    a['href'] = new_rel
                    break
    
    with open(target_path, 'w', encoding='utf-8') as f:
        f.write(str(soup))
        
print("HTML files fixed and links re-relativized.")
