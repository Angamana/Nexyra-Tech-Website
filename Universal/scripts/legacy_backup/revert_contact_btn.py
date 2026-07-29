import os

workspace_dir = r"c:\Users\angam\Downloads\sentrixa_template.webflow.io"
contact_path = os.path.join(workspace_dir, r"Contact\sentrixa-template.webflow.io\contact.html")

with open(contact_path, "r", encoding="utf-8") as f:
    content = f.read()

# Locate the nav section to restrict replacements
nav_start = content.find('<nav class="nav-menu spark-rounded-corners w-nav-menu" role="navigation">')
nav_end = content.find('<div class="menu-button w-nav-button"')

if nav_start != -1 and nav_end != -1:
    nav_content = content[nav_start:nav_end]
    
    # Revert styling on the buttons
    nav_content = nav_content.replace(
        'style="border-radius: 50px; background-color: #ffffff !important; border: 1px solid #4353ff !important;"',
        'style="border-radius: 50px;"'
    )
    
    # Revert text colors
    nav_content = nav_content.replace(
        '<p class="button-text-01" style="color: #4353ff !important;">Contact Us</p>',
        '<p class="button-text-01">Contact Us</p>'
    )
    nav_content = nav_content.replace(
        '<p class="button-text-02" style="color: #4353ff !important;">Contact Us</p>',
        '<p class="button-text-02">Contact Us</p>'
    )
    nav_content = nav_content.replace(
        '<p class="button-text-01" style="color: #4353ff !important;" text="">Contact Us</p>',
        '<p class="button-text-01" text="">Contact Us</p>'
    )

    # We also need to check the "hide-tab" button which is outside of <nav class="nav-menu">
    # Wait, in the original HTML, the hide-tab button is AFTER </nav> but before <div class="menu-button w-nav-button">.
    # Ah, let's look:
    # <nav class="nav-menu ..."> ... </nav>
    # <div class="nav-button-holder hide-tab"> ... </div>
    # <div class="menu-button w-nav-button">
    # So `nav_start` to `nav_end` covers BOTH buttons because nav_start is <nav...> and nav_end is the menu-button AFTER the hide-tab div.
    
    content = content[:nav_start] + nav_content + content[nav_end:]

with open(contact_path, "w", encoding="utf-8") as f:
    f.write(content)

print("Reverted contact button styling in contact.html")
