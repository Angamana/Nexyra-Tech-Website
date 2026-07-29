import os
files = [
    r'c:\Users\angam\Downloads\sentrixa_template.webflow.io\Index\sentrixa-template.webflow.io\index.html',
    r'c:\Users\angam\Downloads\sentrixa_template.webflow.io\About\sentrixa-template.webflow.io\about.html',
    r'c:\Users\angam\Downloads\sentrixa_template.webflow.io\Services\sentrixa-template.webflow.io\services.html',
    r'c:\Users\angam\Downloads\sentrixa_template.webflow.io\Contact\sentrixa-template.webflow.io\contact.html',
    r'c:\Users\angam\Downloads\sentrixa_template.webflow.io\Error\sentrixa-template.webflow.io\404.html'
]
for f in files:
    if os.path.exists(f):
        with open(f, 'r', encoding='utf-8') as file:
            content = file.read()
        
        # We know the href was replaced by the 404 link since it was previously href="#"
        # The line looks like: <a class="footer-email-link" href="../../Error/sentrixa-template.webflow.io/404.html">security@thenexyra.com</a>
        content = content.replace(
            'class="footer-email-link" href="../../Error/sentrixa-template.webflow.io/404.html">security@thenexyra.com',
            'class="footer-email-link" href="mailto:security@thenexyra.com">security@thenexyra.com'
        )
        
        # also check if the 404 link was just `href="404.html"` inside the 404 file itself depending on relative path resolution. Actually I set them all to `../../Error/sentrixa-template.webflow.io/404.html`!
        
        with open(f, 'w', encoding='utf-8') as file:
            file.write(content)
print("Mailto link fixed!")
