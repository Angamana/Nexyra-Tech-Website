import os
import re

base_dir = r"C:\Users\angam\Downloads\Nexyra Website"

def summarize_h1(text):
    text = re.sub(r'<[^>]+>', '', text).strip()
    if "Falcon" in text: return "Falcon AIDR"
    if "Zero Trust" in text: return "Zero Trust Security"
    if "Incident Response Time" in text: return "Automating Incident Response"
    if "Faster Incident Response" in text: return "Faster Incident Response"
    if "Common Security Mistakes" in text: return "Data Breach Causes"
    if "Continuous Monitoring" in text: return "Continuous Monitoring"
    if "Modern Cyber Threats" in text: return "Modern Cyber Threats"
    if "Advanced Persistent Threats" in text: return "Detecting APTs"
    if "Bypass Traditional Security" in text: return "Bypassing Security"
    if "ShinyHunters" in text: return "ShinyHunters Breach"
    if "Mini Shai-Hulud" in text: return "Supply Chain Attacks"
    if "Nitrogen" in text: return "Nitrogen Ransomware"
    if "VECT" in text: return "VECT Ransomware"
    if "Interlock" in text: return "Cisco Zero-Day"
    if "Multi-Extortion" in text: return "Ransomware Extortion"
    if "CoinbaseCartel" in text: return "CoinbaseCartel Extortion"
    if ":" in text: return text.split(":")[0].strip()
    words = text.split()
    if len(words) <= 4: return text
    return " ".join(words[:3])

for root, dirs, files in os.walk(os.path.join(base_dir, "Blog")):
    for f in files:
        if f.endswith(".html") and "Main Page" not in root:
            html_path = os.path.join(root, f)
            with open(html_path, "r", encoding="utf-8") as f_in:
                content = f_in.read()
                
            # Find the main heading
            h3_match = re.search(r'<h[1-4][^>]*class=["\']blog-single-top-title["\'][^>]*>(.*?)</h[1-4]>', content, flags=re.IGNORECASE|re.DOTALL)
            
            if h3_match:
                summary = summarize_h1(h3_match.group(1))
                new_title = f"Nexyra Tech | {summary}"
                content = re.sub(r'<title>.*?</title>', f'<title>{new_title}</title>', content, flags=re.IGNORECASE|re.DOTALL)
                
                with open(html_path, "w", encoding="utf-8") as f_out:
                    f_out.write(content)
                print(f"Updated title for {f} -> {new_title}")
            else:
                print(f"Could not find blog-single-top-title in {f}")
