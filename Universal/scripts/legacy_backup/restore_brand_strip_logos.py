import os
from bs4 import BeautifulSoup

base_dir = r'c:\Users\angam\Downloads\sentrixa_template.webflow.io'
files = [
    os.path.join(base_dir, r'Index\sentrixa-template.webflow.io\index.html'),
    os.path.join(base_dir, r'About\sentrixa-template.webflow.io\about.html'),
    os.path.join(base_dir, r'Services\sentrixa-template.webflow.io\services.html'),
    os.path.join(base_dir, r'Contact\sentrixa-template.webflow.io\contact.html'),
    os.path.join(base_dir, r'Error\sentrixa-template.webflow.io\404.html'),
]

CDN = 'https://cdn.prod.website-files.com/6965d25065d78378ecfa1ac9/'

# All 9 logos in display order (matching brand-strip.html reference)
ALL_LOGOS = [
    (CDN + '6965d25065d78378ecfa1b93_Client%20Logo.svg',     'Client logo'),
    (CDN + '6965d25065d78378ecfa1b92_Client%20Logo%20(2).svg', 'Client logo'),
    (CDN + '6965d25065d78378ecfa1b91_Client%20Logo%20(1).svg', 'Client logo'),
    (CDN + '6965d25065d78378ecfa1b90_Client%20Logo%20(3).svg', 'Client logo'),
    (CDN + '6965d25065d78378ecfa1b8f_Client%20Logo%20(4).svg', 'Client logo'),
    (CDN + '6965d25065d78378ecfa1b8d_Client%20Logo%20(5).svg', 'Client logo'),
    (CDN + '6965d25065d78378ecfa1b62_Client%20Logo%20(8).svg', 'Client logo'),
    (CDN + '6965d25065d78378ecfa1b61_Client%20Logo%20(6).svg', 'Client logo'),
    (CDN + '6965d25065d78378ecfa1b60_Client%20Logo%20(7).svg', 'Client logo'),
]

# CSS — targets .logo-holder (the original class name from the template)
MARQUEE_CSS = """
.logo-holder {
    overflow: hidden !important;
    width: 100% !important;
}
.logo3_component {
    display: flex !important;
    width: max-content !important;
    will-change: transform;
}
.logo-list {
    display: flex !important;
    align-items: center !important;
    gap: 48px !important;
    padding-right: 48px !important;
    flex-shrink: 0 !important;
    animation: none !important;
}
.logo-list .logo {
    height: 32px;
    width: auto;
    display: block;
    object-fit: contain;
    flex-shrink: 0;
}
"""

# JS — matches brand-strip.html reference exactly (includes double-init guard)
MARQUEE_JS = """
(function () {
  'use strict';

  var SPEED    = 0.6;
  var SELECTOR = '.logo3_component';

  function initMarquee () {
    var track = document.querySelector(SELECTOR);
    if (!track) return;

    var list = track.querySelector('.logo-list');
    if (!list) return;

    if (track.dataset.marqueeInit) return;
    track.dataset.marqueeInit = '1';

    var clone = list.cloneNode(true);
    track.appendChild(clone);

    var pos         = 0;
    var singleWidth = 0;

    function measure () {
      singleWidth = list.offsetWidth;
    }

    function tick () {
      if (singleWidth === 0) {
        requestAnimationFrame(tick);
        return;
      }
      pos -= SPEED;
      if (pos <= -singleWidth) {
        pos += singleWidth;
      }
      track.style.transform = 'translateX(' + pos + 'px)';
      requestAnimationFrame(tick);
    }

    measure();
    window.addEventListener('load', measure);
    requestAnimationFrame(tick);
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initMarquee);
  } else {
    initMarquee();
  }

})();
"""

for file_path in files:
    if not os.path.exists(file_path):
        continue

    with open(file_path, 'r', encoding='utf-8') as f:
        html_content = f.read()

    soup = BeautifulSoup(html_content, 'lxml')

    brands_section = soup.find('section', class_='brands-logo')
    if not brands_section:
        print(f'No brands section in {os.path.basename(file_path)}, skipping.')
        continue

    # Rebuild the logo3_component with all 9 logos in a single list
    logo_component = brands_section.find('div', class_='logo3_component')
    if logo_component:
        logo_component.clear()
        logo_list = soup.new_tag('div', **{'class': 'logo-list', 'id': 'brand-strip-list'})
        for src, alt in ALL_LOGOS:
            wrap = soup.new_tag('div', **{'class': 'logo-wrap'})
            img = soup.new_tag('img', alt=alt, **{'class': 'logo', 'loading': 'lazy', 'src': src})
            wrap.append(img)
            logo_list.append(wrap)
        logo_component.append(logo_list)

        # Ensure the logo3_component has the correct id
        logo_component['id'] = 'brand-strip-track'

    # Ensure logo-holder wrapper has the right id (use logo-holder, not logo-holder-2)
    logo_holder = brands_section.find('div', class_='logo-holder')
    if logo_holder:
        logo_holder['id'] = 'brand-strip-root'

    # Inject/replace brand strip CSS in <head>
    head = soup.find('head')
    if head:
        for style in head.find_all('style'):
            txt = style.get_text()
            if 'logo3_component' in txt or 'logo-holder' in txt or 'marquee' in txt.lower():
                style.decompose()
        new_style = soup.new_tag('style', id='brand-strip-css')
        new_style.string = MARQUEE_CSS
        head.append(new_style)

    # Inject/replace brand strip JS before </body>
    body = soup.find('body')
    if body:
        for script in body.find_all('script'):
            txt = script.get_text()
            if 'initMarquee' in txt or 'marqueeInit' in txt:
                script.decompose()
        marquee_script = soup.new_tag('script', id='brand-strip-js')
        marquee_script.string = MARQUEE_JS
        body.append(marquee_script)

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(str(soup))

    print(f'Brand strip applied to {os.path.basename(file_path)}')
