import json

log_file = r"C:\Users\angam\.gemini\antigravity\brain\a94a3cad-f499-4590-97af-d2d2cacb0fe9\.system_generated\logs\transcript_full.jsonl"
out_dir = r"C:\Users\angam\Downloads\extracted_files"

import os
os.makedirs(out_dir, exist_ok=True)

pending_target = None
count = 0

with open(log_file, 'r', encoding='utf-8') as f:
    for line in f:
        try:
            data = json.loads(line)
        except:
            continue
            
        if data.get('type') == 'PLANNER_RESPONSE' and 'tool_calls' in data:
            for tc in data['tool_calls']:
                if tc.get('name') == 'view_file':
                    args = tc.get('args', {})
                    path = args.get('AbsolutePath', '')
                    if 'preloader.js' in path or 'preloader.css' in path or 'logo3d.js' in path:
                        pending_target = os.path.basename(path)
                        
        elif data.get('type') == 'TOOL_RESPONSE':
            if pending_target:
                output = data.get('output', '')
                if 'The above content shows the entire' in output or '1:' in output:
                    with open(os.path.join(out_dir, f"{pending_target}_{count}.txt"), 'w', encoding='utf-8') as outf:
                        outf.write(output)
                    print(f"Extracted {pending_target}")
                    count += 1
                pending_target = None

print("Done extracting!")
