function initCookiePolicy() {
    // Determine the base path dynamically based on where this script is loaded from
    let basePath = "";
    const scripts = document.getElementsByTagName('script');
    for (let i = 0; i < scripts.length; i++) {
        if (scripts[i].src && scripts[i].src.includes("cookie-policy.js")) {
            const src = scripts[i].src;
            basePath = src.substring(0, src.indexOf("cookie-policy.js"));
            break;
        }
    }

    // Inject the CSS if not already present in head
    if (!document.querySelector('link[href*="cookie-policy.css"]')) {
        const link = document.createElement("link");
        link.rel = "stylesheet";
        link.href = basePath.replace('/js/', '/css/') + "cookie-policy.css";
        document.head.appendChild(link);
    }

    // Widget HTML
    const widgetHTML = `
        <style>.cookie-modal-overlay { opacity: 0; pointer-events: none; transition: opacity 0.3s ease; }</style>
        <div class="cookie-widget-btn" id="cookieWidgetBtn" title="Cookie Preferences">
            <svg viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
                <path d="M21.598 11.064a1.006 1.006 0 0 0-.854-.172A2.938 2.938 0 0 1 20 11c-1.654 0-3-1.346-3-3 0-.24.03-.47.086-.69a1.005 1.005 0 0 0-1.261-1.261A2.955 2.955 0 0 1 15 6c-1.654 0-3-1.346-3-3 0-.17.016-.336.043-.5a1.004 1.004 0 0 0-1.127-1.127A9.957 9.957 0 0 0 2 12c0 5.514 4.486 10 10 10s10-4.486 10-10c0-.323-.016-.64-.047-.954a1.006 1.006 0 0 0-.355-.682zM12 20c-4.411 0-8-3.589-8-8a7.962 7.962 0 0 1 6.006-7.75A5.006 5.006 0 0 0 15 9l.101-.001a5.007 5.007 0 0 0 4.837 4C19.444 16.941 16.071 20 12 20z"/>
                <circle cx="7.5" cy="14.5" r="1.5"/>
                <circle cx="12" cy="11" r="1.5"/>
                <circle cx="15.5" cy="16.5" r="1.5"/>
                <circle cx="8" cy="9" r="1"/>
            </svg>
        </div>

        <div class="cookie-modal-overlay" id="cookieModalOverlay">
            <div class="cookie-modal" style="max-width: 600px;">
                <div class="cookie-modal-header">
                    <h3 class="cookie-modal-title">Cookie Preferences</h3>
                    <button class="cookie-modal-close" id="cookieModalClose">&times;</button>
                </div>
                <div class="cookie-modal-body">
                    <p>We use cookies to enhance your browsing experience, serve personalized ads or content, and analyze our traffic. By clicking "Accept All", you consent to our use of cookies.</p>
                    
                    <div class="cookie-toggles">
                        <div class="cookie-toggle-row">
                            <div>
                                <div class="cookie-toggle-label">Essential Cookies</div>
                                <div class="cookie-toggle-desc">Required for the website to function properly. Cannot be disabled.</div>
                            </div>
                            <label class="cookie-switch">
                                <input type="checkbox" checked disabled>
                                <span class="cookie-slider"></span>
                            </label>
                        </div>
                        <div class="cookie-toggle-row">
                            <div>
                                <div class="cookie-toggle-label">Analytics Cookies</div>
                                <div class="cookie-toggle-desc">Help us understand how visitors interact with the website.</div>
                            </div>
                            <label class="cookie-switch">
                                <input type="checkbox" id="cookieAnalytics">
                                <span class="cookie-slider"></span>
                            </label>
                        </div>
                        <div class="cookie-toggle-row">
                            <div>
                                <div class="cookie-toggle-label">Marketing Cookies</div>
                                <div class="cookie-toggle-desc">Used to track visitors across websites to display relevant ads.</div>
                            </div>
                            <label class="cookie-switch">
                                <input type="checkbox" id="cookieMarketing">
                                <span class="cookie-slider"></span>
                            </label>
                        </div>
                    </div>
                </div>
                <div class="cookie-modal-footer">
                    <button class="cookie-btn cookie-btn-secondary" id="cookieSaveBtn">Save Preferences</button>
                    <button class="cookie-btn cookie-btn-primary" id="cookieRejectAllBtn">Reject All</button>
                    <button class="cookie-btn cookie-btn-primary" id="cookieAcceptAllBtn">Accept All</button>
                </div>
            </div>
        </div>
    `;

    const path = window.location.pathname.toLowerCase();
    const isIndexPage = path === "/" || path.includes("/index") || path === "/home";

    const widgetContainer = document.createElement("div");
    widgetContainer.innerHTML = widgetHTML;
    document.body.appendChild(widgetContainer);

    // Elements
    const btn = document.getElementById("cookieWidgetBtn");
    const overlay = document.getElementById("cookieModalOverlay");
    const closeBtn = document.getElementById("cookieModalClose");
    const saveBtn = document.getElementById("cookieSaveBtn");
    const acceptAllBtn = document.getElementById("cookieAcceptAllBtn");
    const rejectAllBtn = document.getElementById("cookieRejectAllBtn");
    const checkAnalytics = document.getElementById("cookieAnalytics");
    const checkMarketing = document.getElementById("cookieMarketing");

    // Inject Google Analytics
    const injectGoogleAnalytics = () => {
        if (window.gaInjected) return;
        window.gaInjected = true;
        
        const script1 = document.createElement("script");
        script1.async = true;
        script1.src = "https://www.googletagmanager.com/gtag/js?id=G-PRCZFZ49RL";
        document.head.appendChild(script1);

        const script2 = document.createElement("script");
        script2.innerHTML = `
          window.dataLayer = window.dataLayer || [];
          function gtag(){dataLayer.push(arguments);}
          gtag('js', new Date());
          gtag('config', 'G-PRCZFZ49RL');
        `;
        document.head.appendChild(script2);
    };

    // Load preferences
    const loadPreferences = () => {
        const prefs = JSON.parse(localStorage.getItem("cookiePreferences"));
        if (prefs) {
            checkAnalytics.checked = prefs.analytics;
            checkMarketing.checked = prefs.marketing;
            
            if (prefs.analytics) {
                injectGoogleAnalytics();
            }
        } else {
            // If no preferences saved, pop up after delay on the index page
            if (isIndexPage) {
                setTimeout(() => {
                    if (overlay) {
                        overlay.classList.add("active");
                    }
                }, 16000); // 16 seconds delay to respect 15s 3D animation
            }
        }
    };

    // Save preferences
    const savePreferences = (analytics, marketing) => {
        localStorage.setItem("cookiePreferences", JSON.stringify({
            essential: true,
            analytics: analytics,
            marketing: marketing
        }));
        
        if (analytics) {
            injectGoogleAnalytics();
        }
        
        overlay.classList.remove("active");
    };

    // Event Listeners
    btn.addEventListener("click", (e) => {
        e.preventDefault();
        e.stopPropagation();
        overlay.classList.add("active");
    });

    closeBtn.addEventListener("click", (e) => {
        e.preventDefault();
        overlay.classList.remove("active");
    });

    overlay.addEventListener("click", (e) => {
        if (e.target === overlay) {
            overlay.classList.remove("active");
        }
    });

    saveBtn.addEventListener("click", (e) => {
        e.preventDefault();
        savePreferences(checkAnalytics.checked, checkMarketing.checked);
    });

    acceptAllBtn.addEventListener("click", (e) => {
        e.preventDefault();
        checkAnalytics.checked = true;
        checkMarketing.checked = true;
        savePreferences(true, true);
    });

    rejectAllBtn.addEventListener("click", (e) => {
        e.preventDefault();
        checkAnalytics.checked = false;
        checkMarketing.checked = false;
        savePreferences(false, false);
    });

    loadPreferences();
}

if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", initCookiePolicy);
} else {
    initCookiePolicy();
}
