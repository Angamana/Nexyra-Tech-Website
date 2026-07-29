import os
import shutil
import re
from urllib.parse import urlparse, unquote

base_dir = r"C:\Users\angam\Downloads\Nexyra Website"

# Define the exact target structure for HTML files
# old_path_substring : (target_dir, target_filename)
targets = {
    "Index Page\\index.html": (r"Home\website", "index.html"),
    "About Page\\about.html": (r"About\website", "About.html"),
    "Contact Us Page\\contact.html": (r"Contact\website", "Contact.html"),
    "Nexyra Website - Error\\404.html": (r"Error\website", "Error.html"),
    "Services Page\\services.html": (r"Services\Main Page\website", "Services.html"),
    "sentrixa-template.webflow.io\\blog.html": (r"Blog\Main Page\website", "Blog.html"),
    "Blog 1\\sentrixa-template.webflow.io\\blog": (r"Blog\Blog 1\website", "how-ai-improves-threat-detection-without-increasing-security-team-workload.html"),
    "Blog 2\\sentrixa-template.webflow.io\\blog": (r"Blog\Blog 2\website", "how-ai-is-changing-threat-detection.html"),
    "Blog 3\\sentrixa-template.webflow.io\\blog": (r"Blog\Blog 3\website", "building-a-scalable-security-strategy.html"),
    "Blog 4\\sentrixa-template.webflow.io\\blog": (r"Blog\Blog 4\website", "identity-security-the-new-perimeter.html"),
    "Blog Sub 1\\sentrixa-template.webflow.io\\blog": (r"Blog\Blog Sub 1\website", "zero-trust-security-why-perimeter-defense-is-no-longer-enough.html"),
    "Blog Sub 2\\sentrixa-template.webflow.io\\blog": (r"Blog\Blog Sub 2\website", "how-faster-incident-response-limits-security-business-impact.html"),
    "Blog Sub 3\\sentrixa-template.webflow.io\\blog": (r"Blog\Blog Sub 3\website", "understanding-modern-cyber-threats-in-cloud-environments.html"),
    "Blog Sub 4\\sentrixa-template.webflow.io\\blog": (r"Blog\Blog Sub 4\website", "reducing-incident-response-time-with-automation.html"),
    "Blog Sub 5\\sentrixa-template.webflow.io\\blog": (r"Blog\Blog Sub 5\website", "common-security-mistakes-that-lead-to-data-breaches.html"),
    "Blog Sub 6\\sentrixa-template.webflow.io\\blog": (r"Blog\Blog Sub 6\website", "why-continuous-monitoring-beats-periodic-audits-2.html"),
    "Blog Sub 7\\sentrixa-template.webflow.io\\blog": (r"Blog\Blog Sub 7\website", "why-continuous-monitoring-beats-periodic-audits.html"),
    "Blog Sub 8\\sentrixa-template.webflow.io\\blog": (r"Blog\Blog Sub 8\website", "detecting-advanced-persistent-threats-before-damage-occurs.html"),
    "Blog Sub 9\\sentrixa-template.webflow.io\\blog": (r"Blog\Blog Sub 9\website", "how-modern-cyber-attacks-bypass-traditional-security-controls.html"),
}

# Find all HTML files, identify which is which
html_files = []
for root, dirs, files in os.walk(base_dir):
    if "Universal" in root or "Backend" in root or ".git" in root:
        continue
    for file in files:
        if file.endswith(".html"):
            html_files.append(os.path.join(root, file))

# Map old paths to new paths
move_map = {}
for html_file in html_files:
    for key, (target_dir, target_file) in targets.items():
        # Check if this HTML file matches the old path substring and is NOT already in the new structure
        if key in html_file and "website" not in html_file:
            new_path = os.path.join(base_dir, target_dir, target_file)
            move_map[html_file] = new_path
            break

# Now we need to update the HTML content to point to the new relative paths for other HTML files.
# Wait, what about assets? The assets were rewritten by reorganize_architecture.py in the newly created (but wrongly placed) HTML files.
# We should take the original HTML files (which still exist!), rewrite their asset links to Universal or local based on the asset mapping, and rewrite their HTML links.
