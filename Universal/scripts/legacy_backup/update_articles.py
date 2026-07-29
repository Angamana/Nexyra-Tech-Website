import os
import re

base_dir = r"c:\Users\angam\Downloads\sentrixa_template.webflow.io\Blog - Main Page"

# Find all HTML files in subdirectories of base_dir
html_files = []
for root, dirs, files in os.walk(base_dir):
    for f in files:
        if f.endswith(".html") and "sentrixa-template.webflow.io" in root:
            # We want to skip the main blog.html
            if f == "blog.html" and root == os.path.join(base_dir, "sentrixa-template.webflow.io"):
                continue
            html_files.append(os.path.join(root, f))

print(f"Found {len(html_files)} article files to process:")
for f in html_files:
    print(f" - {f}")

new_head_styles = """
    <style>
        .w-webflow-badge {
            display: none !important;
        }
    </style>
    <style>
        @media screen and (min-width: 992px) {
            .nav-menu {
                flex: 1;
                display: flex;
                justify-content: flex-end;
                padding-right: 15px;
            }
        }
        @media screen and (max-width: 991px) {
            .navber-v2 {
                height: 60px !important;
                padding-top: 0px !important;
                padding-bottom: 0px !important;
                min-height: 0 !important;
                display: flex !important;
                align-items: center !important;
            }
            .navber-v2 .container {
                height: 60px !important;
                display: flex !important;
                justify-content: space-between !important;
                align-items: center !important;
                max-width: none !important;
                width: 100% !important;
                padding-left: 15px !important;
                padding-right: 15px !important;
                margin: 0 !important;
            }
            .navbar-inner {
                width: auto !important;
                display: flex !important;
                align-items: center !important;
                justify-content: flex-start !important;
                margin: 0 !important;
                padding: 0 !important;
            }
            .menu-button {
                padding: 0 !important;
                margin: 0 !important;
                display: flex !important;
                align-items: center !important;
                justify-content: center !important;
                height: 60px !important;
            }
            .brand-logo {
                display: flex !important;
                align-items: center !important;
                margin: 0 !important;
                padding: 0 !important;
            }
        }
    </style>

    <link href="../../../../logo.png" rel="icon" type="image/png" />
    <link href="../../../../logo.png" rel="shortcut icon" type="image/png" />
    <link href="../../../../logo.png" rel="apple-touch-icon" />
"""

new_navbar = """        <div class="navbar-logo-center">
            <div class="navber-v2 w-nav" data-animation="default" data-collapse="medium" data-duration="400"
                data-easing="ease" data-easing2="ease" role="banner">
                <div class="w-layout-blockcontainer container w-container">
                    <div class="navbar-inner"><a class="brand-logo w-nav-brand"
                            href="../../../../Index/sentrixa-template.webflow.io/index.html" style="text-decoration: none">
                            <div style="display:flex;align-items:center;gap:8px;"><img alt="Nexyra Tech Logo"
                                    src="../../../../logo.png" style="height: 22px; width: auto;" /><span
                                    style="font-family:'Inter', sans-serif; font-size:18px; font-weight:600; color:white; line-height: 1;; text-decoration: none">Nexyra
                                    Tech</span></div>
                        </a>
                        <nav class="nav-menu spark-rounded-corners w-nav-menu" role="navigation">
                            <div class="nav-link-holder" style="margin-left: auto; margin-right: 24px;"><a
                                    class="nav-link w-nav-link"
                                    href="../../../../Index/sentrixa-template.webflow.io/index.html">Home</a><a
                                    class="nav-link w-nav-link"
                                    href="../../../../About/sentrixa-template.webflow.io/about.html">About</a><a class="nav-link w-nav-link" href="../../../../Services/sentrixa-template.webflow.io/services.html">Services</a><a
                                    class="nav-link w-nav-link"
                                    href="../../../../Blog - Main Page/sentrixa-template.webflow.io/blog.html">Blog</a></div>
                            <div class="nav-button-holder hide-desktop">
                                <a class="nav-button w-inline-block"
                                    href="../../../../Contact/sentrixa-template.webflow.io/contact.html"
                                    style="border-radius: 50px;">
                                    <div class="button-text-wrap">
                                        <p class="button-text-01">Contact Us</p>
                                        <p class="button-text-02">Contact Us</p>
                                    </div>
                                </a>
                            </div>
                        </nav>
                        <div class="nav-button-holder hide-tab">
                            <a class="nav-button w-inline-block"
                                href="../../../../Contact/sentrixa-template.webflow.io/contact.html"
                                style="border-radius: 50px;">
                                <div class="button-text-wrap">
                                    <p class="button-text-01" text="">Contact Us</p>
                                </div>
                            </a>
                        </div>
                    </div>
                    <div class="menu-button w-nav-button" data-ix="simple-menu-button">
                        <div class="line-1 nab-line"></div>
                        <div class="spark-line-2 spark-simple-line"></div>
                        <div class="spark-line-3 spark-simple-line"></div>
                    </div>
                </div>
            </div>
        </div>
"""

new_footer = """    <div class="cta-footer">
        <section class="section cta" style="background: #070a1a; position: relative;">
            <div class="w-layout-blockcontainer container w-container">
                <div class="cta-wrap">
                    <div class="cta-top-text-content">
                        <div class="cta-title-wrap">
                            <h2 class="cta-title">Start Protecting Your Business Today</h2>
                        </div>
                        <div class="cta-text-wrap">
                            <p class="cta-text">Start protecting your infrastructure with real-time threat detection and expert-driven security.</p>
                        </div>
                        <div data-w-id="8091e82f-a4bc-f36a-fcb4-2e7ad5600678">
                            <a data-wf--prymary-button--variant="base" href="../../../../Contact/sentrixa-template.webflow.io/contact.html" class="primary-button w-inline-block">
                                <div class="button-text-wrap">
                                    <p text="" class="button-text-01">Contact Us</p>
                                </div>
                            </a>
                        </div>
                    </div>
                </div>
            </div>
            <div class="cta-color"></div>
        </section>
        <section class="footer"
            style="background: radial-gradient(ellipse 80% 120% at 50% 0%, rgba(72, 95, 255, 0.55) 0%, rgba(30, 30, 90, 0.35) 45%, transparent 70%), #070a1a; position: relative;">
            <div class="w-layout-blockcontainer container w-container">
                <div class="footer-wrap">
                    <div class="footer-wrapper-two">
                        <div class="footer-one">
                            <div class="footer-brand-wrap" data-w-id="4e361a89-8bc7-799e-39f1-a7cb844f43ba"><a
                                    class="footer-brand w-inline-block"
                                    href="../../../../Index/sentrixa-template.webflow.io/index.html"
                                    style="text-decoration: none">
                                    <div style="display:flex;align-items:center;gap:8px;text-decoration:none;"><img
                                            alt="Nexyra Tech Logo" class="footer-brand-img" loading="lazy"
                                            src="../../../../logo.png" style="height: 22px; width: auto;" /><span
                                            style="font-family:'Inter', sans-serif; font-size:18px; font-weight:600; color:white; line-height: 1; text-decoration: none;">Nexyra
                                            Tech</span></div>
                                </a>
                                <p class="footer-text">Securing the next era</p>
                            </div>
                        </div>
                        <div class="footer-block-two tab" data-w-id="4e361a89-8bc7-799e-39f1-a7cb844f43cf">
                            <div class="footer-title">Company</div>
                            <div class="footer-link-two-holder">
                                <div class="footer-link-two-wrap" data-w-id="4e361a89-8bc7-799e-39f1-a7cb844f43d3"><a
                                        class="footer-link-one"
                                        href="../../../../Index/sentrixa-template.webflow.io/index.html">Home</a><a
                                        class="footer-link-two"
                                        href="../../../../Index/sentrixa-template.webflow.io/index.html">Home</a></div>
                                <div class="footer-link-two-wrap" data-w-id="4e361a89-8bc7-799e-39f1-a7cb844f43d8"><a
                                        class="footer-link-one"
                                        href="../../../../About/sentrixa-template.webflow.io/about.html">About</a><a
                                        class="footer-link-two"
                                        href="../../../../About/sentrixa-template.webflow.io/about.html">About</a></div>
                                <div class="footer-link-two-wrap" data-w-id="4e361a89-8bc7-799e-39f1-a7cb844f43dd"><a
                                        class="footer-link-one"
                                        href="../../../../Services/sentrixa-template.webflow.io/services.html">Services</a><a
                                        class="footer-link-two"
                                        href="../../../../Services/sentrixa-template.webflow.io/services.html">Services</a>
                                </div>
                                <div class="footer-link-two-wrap" data-w-id="4e361a89-8bc7-799e-39f1-a7cb844f43dd">
                                    <a class="footer-link-one"
                                        href="../../../../Blog - Main Page/sentrixa-template.webflow.io/blog.html">Blog</a><a
                                        class="footer-link-two"
                                        href="../../../../Blog - Main Page/sentrixa-template.webflow.io/blog.html">Blog</a>
                                </div>
                                <div class="footer-link-two-wrap" data-w-id="4e361a89-8bc7-799e-39f1-a7cb844f43f1"><a
                                        class="footer-link-one"
                                        href="../../../../Contact/sentrixa-template.webflow.io/contact.html">Contact</a><a
                                        class="footer-link-two"
                                        href="../../../../Contact/sentrixa-template.webflow.io/contact.html">Contact</a></div>
                            </div>
                        </div>
                        <div class="footer-block">
                            <div class="footer-email-holder" data-w-id="4e361a89-8bc7-799e-39f1-a7cb844f442c">
                                <div class="footer-title">About</div><a class="footer-email-link"
                                    href="mailto:info@thenexyra.com">info@thenexyra.com</a>
                            </div>
                            <div class="footer-social-block-two" data-w-id="4e361a89-8bc7-799e-39f1-a7cb844f431">
                                <div class="footer-title">Social Media</div>
                                <div class="footer-social-link-holder">
                                    <a class="footer-social-link w-inline-block"
                                        data-w-id="4e361a89-8bc7-799e-39f1-a7cb844f435"
                                        href="https://www.facebook.com/">
                                        <div class="footer-social-img-wrap"><img alt="" class="footer-social-img _01"
                                                loading="lazy"
                                                src="https://cdn.prod.website-files.com/6965d25065d78378ecfa1ac9/6965d25065d78378ecfa1ad8_Icon%20(37).svg" />
                                        </div>
                                    </a>
                                    <a class="footer-social-link w-inline-block"
                                        data-w-id="4e361a89-8bc7-799e-39f1-a7cb844f439" href="https://x.com/">
                                        <div class="footer-social-img-wrap"><img alt="" class="footer-social-img _01"
                                                loading="lazy"
                                                src="https://cdn.prod.website-files.com/6965d25065d78378ecfa1ac9/6965d25065d78378ecfa1ad9_Icon%20(35).svg" />
                                        </div>
                                    </a>
                                    <a class="footer-social-link w-inline-block"
                                        data-w-id="4e361a89-8bc7-799e-39f1-a7cb844f43d"
                                        href="https://www.linkedin.com/">
                                        <div class="footer-social-img-wrap"><img alt="" class="footer-social-img _01"
                                                loading="lazy"
                                                src="https://cdn.prod.website-files.com/6965d25065d78378ecfa1ac9/6965d25065d78378ecfa1ada_Icon%20(36).svg" />
                                        </div>
                                    </a>
                                    <a class="footer-social-link w-inline-block"
                                        data-w-id="4e361a89-8bc7-799e-39f1-a7cb844f4441"
                                        href="https://www.instagram.com/flowcubdesign">
                                        <div class="footer-social-img-wrap"><img alt="" class="footer-social-img _01"
                                                loading="lazy"
                                                src="https://cdn.prod.website-files.com/6965d25065d78378ecfa1ac9/6965d25065d78378ecfa1ad6_Icon%20(38).svg" />
                                        </div>
                                    </a>
                                </div>
                            </div>
                        </div>
                    </div>
                    <div class="footer-bottom-two">
                        <div class="footer-divider-two"></div>
                        <div>
                            <div class="footer-bottom" data-w-id="4e361a89-8bc7-799e-39f1-a7cb844f4348"
                                style="opacity:1 !important; visibility:visible !important;">
                                <div class="footer-copyright"
                                    style="text-align:center; display:block; width:100%; color:rgba(255,255,255,0.5); font-size:14px; padding:16px 0;">
                                    © 2026 Nexyra Tech (Pty) Ltd. All rights reserved.</div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </section>
    </div>
"""

for f in html_files:
    with open(f, "r", encoding="utf-8") as file:
        content = file.read()

    # 1. Update Head: insert styles and replace Webflow's default tab/shortcut/apple icons
    # First, let's remove any existing logo.png icons if already added, or default ones
    content = re.sub(r'<link[^>]*rel="icon"[^>]*>', '', content)
    content = re.sub(r'<link[^>]*rel="shortcut icon"[^>]*>', '', content)
    content = re.sub(r'<link[^>]*rel="apple-touch-icon"[^>]*>', '', content)
    
    # Insert new head styles right before </head>
    content = content.replace("</head>", new_head_styles + "\n</head>")

    # 2. Update Navbar: everything between <div class="navbar-logo-center"> and <div class="main-content">
    # Note that <div class="main-content"> could have spaces/newlines before it.
    navbar_pattern = re.compile(r'<div class="navbar-logo-center">.*?<div class="main-content">', re.DOTALL)
    if navbar_pattern.search(content):
        content = navbar_pattern.sub(new_navbar + '\n    <div class="main-content">', content)
        print(f"Successfully replaced navbar in {os.path.basename(f)}")
    else:
        print(f"WARNING: navbar pattern not matched in {os.path.basename(f)}")

    # 3. Update Footer: everything from <div class="cta-footer"> to <script src="https://d3e54v103j8qbb.cloudfront.net
    footer_pattern = re.compile(r'<div class="cta-footer">.*?<script src="https://d3e54v103j8qbb.cloudfront.net', re.DOTALL)
    if footer_pattern.search(content):
        content = footer_pattern.sub(new_footer + '\n    <script src="https://d3e54v103j8qbb.cloudfront.net', content)
        print(f"Successfully replaced footer in {os.path.basename(f)}")
    else:
        print(f"WARNING: footer pattern not matched in {os.path.basename(f)}")

    with open(f, "w", encoding="utf-8") as file:
        file.write(content)

print("Done processing all articles!")
