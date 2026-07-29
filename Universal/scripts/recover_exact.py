import json
import re

log_file = r"C:\Users\angam\.gemini\antigravity\brain\a94a3cad-f499-4590-97af-d2d2cacb0fe9\.system_generated\logs\transcript_full.jsonl"

with open(log_file, 'r', encoding='utf-8') as f:
    for line in f:
        try:
            data = json.loads(line)
        except:
            continue
            
        if data.get('type') == 'PLANNER_RESPONSE' and 'tool_calls' in data:
            for tc in data['tool_calls']:
                if tc.get('name') == 'replace_file_content':
                    args = tc.get('args', {})
                    path = args.get('TargetFile', '')
                    if 'preloader.js' in path:
                        print("Found replace_file_content for preloader.js!")
                        print(args.get('TargetContent', '')[:100])
