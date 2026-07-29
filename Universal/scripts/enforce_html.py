import os
import shutil

base_dir = r"C:\Users\angam\Downloads\Nexyra Website"

valid_html_paths = [
    r"Home\website\index.html",
    r"About\website\About.html",
    r"Contact\website\Contact.html",
    r"Error\website\Error.html",
    r"Services\Main Page\website\Services.html",
    r"Blog\Main Page\website\Blog.html",
    r"Blog\Blog 1\website\how-ai-improves-threat-detection-without-increasing-security-team-workload.html",
    r"Blog\Blog 2\website\how-ai-is-changing-threat-detection.html",
    r"Blog\Blog 3\website\building-a-scalable-security-strategy.html",
    r"Blog\Blog 4\website\identity-security-the-new-perimeter.html",
    r"Blog\Blog Sub 1\website\zero-trust-security-why-perimeter-defense-is-no-longer-enough.html",
    r"Blog\Blog Sub 2\website\how-faster-incident-response-limits-security-business-impact.html",
    r"Blog\Blog Sub 3\website\understanding-modern-cyber-threats-in-cloud-environments.html",
    r"Blog\Blog Sub 4\website\reducing-incident-response-time-with-automation.html",
    r"Blog\Blog Sub 5\website\common-security-mistakes-that-lead-to-data-breaches.html",
    r"Blog\Blog Sub 6\website\why-continuous-monitoring-beats-periodic-audits-2.html",
    r"Blog\Blog Sub 7\website\why-continuous-monitoring-beats-periodic-audits.html",
    r"Blog\Blog Sub 8\website\detecting-advanced-persistent-threats-before-damage-occurs.html",
    r"Blog\Blog Sub 9\website\how-modern-cyber-attacks-bypass-traditional-security-controls.html",
]

valid_absolute = [os.path.join(base_dir, p).lower() for p in valid_html_paths]

deleted = 0
for root, dirs, files in os.walk(base_dir):
    if "Universal" in root or "Backend" in root or ".git" in root:
        continue
    for file in files:
        if file.endswith(".html"):
            path = os.path.join(root, file)
            if path.lower() not in valid_absolute:
                try:
                    os.remove(path)
                    deleted += 1
                except Exception as e:
                    print(f"Failed to delete {path}: {e}")

print(f"Deleted {deleted} leftover HTML files.")
