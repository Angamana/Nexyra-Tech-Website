import os
import shutil

base_dir = r"C:\Users\angam\Downloads"
universal_img = os.path.join(base_dir, "Nexyra Website", "Universal", "images")

renames = {
    "Blog-USB.png": "Blog-USB - Blue.png",
    "Blog-Scale-Agentic-AI.png": "Blog-Scale-Agentic-AI - Blue.png",
    "Blog-Integration.png": "Blog-Integration - Blue.png",
    "Blog-Insider-Risk.png": "Blog-Insider-Risk - Blue.png",
    "Blog-FalconCloudSecurity-AI.png": "Blog-FalconCloudSecurity-AI - Blue.png",
    "Blog-Data-Protection-Day-2026.png": "Blog-Data-Protection-Day-2026 - Blue.png",
    "Blog-DataLeakage.png": "Blog-DataLeakage - Blue.png",
    "Blog-ByteBack.png": "Blog-ByteBack - blue.png",
    "Blog-AdvancedWebShell.png": "Blog-AdvancedWebShell - Blue.png",
    "magnifying-glass.png": "magnifying-glass-removebg-preview.png",
    "hd-white-angle-pencil-icon-png-701751695040455ni7fjxt6ug.png": "hd-white-angle-pencil-icon-png-701751695040455ni7fjxt6ug-removebg-preview.png"
}

for src_name, dst_name in renames.items():
    src_path = os.path.join(base_dir, src_name)
    dst_path = os.path.join(universal_img, dst_name)
    if os.path.exists(src_path):
        shutil.copy2(src_path, dst_path)
        print(f"Recovered {dst_name}")

# Also check for cloud-security.png maybe?
for file in os.listdir(base_dir):
    if "cloud" in file.lower() and "security" in file.lower() and file.endswith(".png"):
        shutil.copy2(os.path.join(base_dir, file), os.path.join(universal_img, "cloud-security.png"))
        print(f"Recovered cloud-security.png from {file}")
