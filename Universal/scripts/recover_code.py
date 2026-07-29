import json
import os
import ast

log_file = r"C:\Users\angam\.gemini\antigravity\brain\a94a3cad-f499-4590-97af-d2d2cacb0fe9\.system_generated\logs\transcript_full.jsonl"
universal_js = r"C:\Users\angam\Downloads\Nexyra Website\Universal\code\js"
universal_css = r"C:\Users\angam\Downloads\Nexyra Website\Universal\code\css"

os.makedirs(universal_js, exist_ok=True)
os.makedirs(universal_css, exist_ok=True)

files_to_recover = {
    "preloader.js": os.path.join(universal_js, "preloader.js"),
    "logo3d.js": os.path.join(universal_js, "logo3d.js"),
    "preloader.css": os.path.join(universal_css, "preloader.css")
}
recovered = {}

with open(log_file, 'r', encoding='utf-8') as f:
    for line in f:
        try:
            data = json.loads(line)
        except:
            continue
            
        # Check tool responses for view_file
        if data.get('type') == 'TOOL_RESPONSE' and 'tool_calls' in data:
            for tc in data['tool_calls']:
                if tc.get('name') == 'view_file':
                    args = tc.get('args', {})
                    if 'AbsolutePath' in args:
                        path = args['AbsolutePath']
                        if 'preloader.js' in path:
                            recovered["preloader.js"] = tc.get('output', '')
                        elif 'logo3d.js' in path:
                            recovered["logo3d.js"] = tc.get('output', '')
                        elif 'preloader.css' in path:
                            recovered["preloader.css"] = tc.get('output', '')

        # Check tool calls for replace_file_content or write_to_file
        if data.get('type') == 'PLANNER_RESPONSE' and 'tool_calls' in data:
            for tc in data['tool_calls']:
                if tc.get('name') in ['replace_file_content', 'write_to_file', 'multi_replace_file_content']:
                    # We might not get full file, but maybe we can? No, replace_file_content just has TargetContent/ReplacementContent.
                    pass

for name, content in recovered.items():
    if content:
        # The output of view_file might have a header like "Created At..."
        # But we can write it and manually clean it up if needed. Or just check for the first { or function.
        # It's better to just write the raw output.
        with open(files_to_recover[name], 'w', encoding='utf-8') as out:
            out.write(content)
        print(f"Recovered {name} from transcript!")

print(f"Recovered {len(recovered)} script/css files.")
