import json
import os

log_file = r"C:\Users\angam\.gemini\antigravity\brain\a94a3cad-f499-4590-97af-d2d2cacb0fe9\.system_generated\logs\transcript_full.jsonl"
out_dir = r"C:\Users\angam\Downloads\Nexyra Website\Universal\code"

os.makedirs(os.path.join(out_dir, "js"), exist_ok=True)
os.makedirs(os.path.join(out_dir, "css"), exist_ok=True)

def clean_content(raw):
    lines = raw.split('\n')
    cleaned = []
    for line in lines:
        if ':' in line:
            parts = line.split(':', 1)
            if parts[0].strip().isdigit():
                # remove leading space if it exists
                val = parts[1]
                if len(val) > 0 and val[0] == ' ':
                    val = val[1:]
                cleaned.append(val)
            else:
                cleaned.append(line)
        else:
            cleaned.append(line)
    
    # Filter out header/footer text
    out_lines = []
    started = False
    for line in cleaned:
        if line.startswith("The following code has been modified"):
            started = True
            continue
        if line.startswith("The above content shows the entire"):
            break
        if started:
            out_lines.append(line)
    return '\n'.join(out_lines).strip()

with open(log_file, 'r', encoding='utf-8') as f:
    for line in f:
        try:
            data = json.loads(line)
        except:
            continue
            
        if data.get('type') == 'VIEW_FILE':
            content = data.get('content', '')
            # Determine which file this is
            if 'preloader.js' in content:
                print("Extracting preloader.js...")
                with open(os.path.join(out_dir, "js", "preloader.js"), 'w', encoding='utf-8') as outf:
                    outf.write(clean_content(content))
            elif 'preloader.css' in content:
                print("Extracting preloader.css...")
                with open(os.path.join(out_dir, "css", "preloader.css"), 'w', encoding='utf-8') as outf:
                    outf.write(clean_content(content))
            elif 'logo3d.js' in content:
                print("Extracting logo3d.js...")
                with open(os.path.join(out_dir, "js", "logo3d.js"), 'w', encoding='utf-8') as outf:
                    outf.write(clean_content(content))

print("Extraction complete!")
