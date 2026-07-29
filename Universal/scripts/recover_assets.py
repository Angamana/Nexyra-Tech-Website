import os
import json

base_dir = r"C:\Users\angam\Downloads"
nexyra_dir = os.path.join(base_dir, "Nexyra Website")
universal_img = os.path.join(nexyra_dir, "Universal", "images")
universal_js = os.path.join(nexyra_dir, "Universal", "code", "js")
universal_css = os.path.join(nexyra_dir, "Universal", "code", "css")
universal_doc = os.path.join(nexyra_dir, "Universal", "documents")

missing_files = [
    "Falcon AIDR.png",
    "Financial Services Threat Landscape Report.png",
    "Automated Leads.png",
    "May 2026 Patch.png",
    "Blog-USB - Blue.png",
    "Blog-Scale-Agentic-AI - Blue.png",
    "Blog-Integration - Blue.png",
    "Blog-Insider-Risk - Blue.png",
    "Blog-FalconCloudSecurity-AI - Blue.png",
    "Blog-Data-Protection-Day-2026 - Blue.png",
    "Blog-DataLeakage - Blue.png",
    "Blog-ByteBack - blue.png",
    "Blog-AdvancedWebShell - Blue.png",
    "cloud-security.png",
    "Index frame.png",
    "magnifying-glass-removebg-preview.png",
    "hd-white-angle-pencil-icon-png-701751695040455ni7fjxt6ug-removebg-preview.png",
    "Nexyra Tech Company Profile - V2.pdf"
]

found = {}
for root, dirs, files in os.walk(base_dir):
    if "Nexyra Website" in root or "Universal" in root:
        continue # skip the broken project
    for file in files:
        if file in missing_files:
            if file not in found:
                found[file] = os.path.join(root, file)
                print(f"Recovered {file} from {root}")
                import shutil
                if file.endswith(".pdf"):
                    shutil.copy2(found[file], os.path.join(universal_doc, file))
                else:
                    shutil.copy2(found[file], os.path.join(universal_img, file))

print(f"Recovered {len(found)} out of {len(missing_files)} missing assets.")
