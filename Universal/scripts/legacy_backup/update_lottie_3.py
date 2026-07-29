import json
import base64
import os
import re

base_dir = r'c:\Users\angam\Downloads\sentrixa_template.webflow.io'
cdn_dir = base_dir + r'\Index\cdn.prod.website-files.com\6965d25065d78378ecfa1ac9'
json_path = cdn_dir + r'\697ca282ec3d6c73fcb77875_integration.json'
html_path = base_dir + r'\Index\sentrixa-template.webflow.io\index.html'

with open(json_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

def get_base64_image(path):
    with open(path, 'rb') as img_file:
        return 'data:image/png;base64,' + base64.b64encode(img_file.read()).decode('utf-8')

new_logos = [
    ('img_anglo', r'\Anglo American Logo.png'),
    ('img_sasol', r'\Sasol Logo.png'),
    ('img_transnet', r'\Transnet Logo No BG.png')
]

for l_id, filename in new_logos:
    full_path = cdn_dir + filename
    b64 = get_base64_image(full_path)
    data['assets'].append({
        'id': l_id,
        'w': 800, # Approximate, we will center it
        'h': 800,
        'u': '',
        'p': b64
    })

precomp_ids = []
for layer in data['layers']:
    if layer.get('ty') == 0:
        precomp_ids.append(layer['refId'])

# The first two were 0 and 1. We replace 2, 3, 4.
targets = [
    (precomp_ids[2], 'img_anglo', [5, 5, 100]),
    (precomp_ids[3], 'img_sasol', [5, 5, 100]),
    (precomp_ids[4], 'img_transnet', [5, 5, 100])
]

for asset in data.get('assets', []):
    for pid, img_id, scale in targets:
        if asset.get('id') == pid:
            asset['layers'] = [{
                'ty': 2,
                'refId': img_id,
                'ks': {'o':{'a':0,'k':100},'r':{'a':0,'k':0},'p':{'a':0,'k':[20,20,0]},'a':{'a':0,'k':[400,400,0]},'s':{'a':0,'k':scale}},
                'ao': 0, 'ip': 0, 'op': 301, 'st': 0
            }]

# Save the updated JSON
with open(json_path, 'w', encoding='utf-8') as f:
    json.dump(data, f)

# Generate new Data URI
with open(json_path, 'rb') as f:
    json_data = f.read()

b64_str = base64.b64encode(json_data).decode('utf-8')
data_uri = 'data:application/json;base64,' + b64_str

# Read HTML
with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

# Replace existing data URI
# The data URI starts with data-src="data:application/json;base64,... "
html = re.sub(r'data-src="data:application/json;base64,[^"]+"', f'data-src="{data_uri}"', html)

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html)
print('JSON updated and HTML embedded with new Data URI')
