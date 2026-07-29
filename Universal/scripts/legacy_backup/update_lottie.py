import base64

base_dir = r'c:\Users\angam\Downloads\sentrixa_template.webflow.io'
json_path = base_dir + r'\Index\cdn.prod.website-files.com\6965d25065d78378ecfa1ac9\697ca282ec3d6c73fcb77875_integration.json'
html_path = base_dir + r'\Index\sentrixa-template.webflow.io\index.html'

with open(json_path, 'rb') as f:
    json_data = f.read()

b64_str = base64.b64encode(json_data).decode('utf-8')
data_uri = 'data:application/json;base64,' + b64_str

with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

html = html.replace('data-src=\"https://cdn.prod.website-files.com/6965d25065d78378ecfa1ac9/697ca282ec3d6c73fcb77875_integration.json\"', f'data-src=\"{data_uri}\"')

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html)
print('HTML updated with data URI')
