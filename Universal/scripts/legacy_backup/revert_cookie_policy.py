import os

file_path = r'c:\Users\angam\Downloads\sentrixa_template.webflow.io\cookie-policy.js'

js_content = """document.addEventListener("DOMContentLoaded", function() {
    // Determine the base path depending on where we are
    let basePath = "";
    if (window.location.pathname.includes("/Index/") || window.location.pathname.includes("/About/") || window.location.pathname.includes("/Contact/")) {
        basePath = "../../";
    }

    // Inject the CSS
    const link = document.createElement("link");
    link.rel = "stylesheet";
    link.href = basePath + "cookie-policy.css";
    document.head.appendChild(link);

    // Widget HTML
    const widgetHTML = `
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
            <div class="cookie-modal">
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
                    <button class="cookie-btn cookie-btn-primary" id="cookieAcceptAllBtn">Accept All</button>
                </div>
            </div>
        </div>
    `;

    const widgetContainer = document.createElement("div");
    widgetContainer.innerHTML = widgetHTML;
    document.body.appendChild(widgetContainer);

    // Elements
    const btn = document.getElementById("cookieWidgetBtn");
    const overlay = document.getElementById("cookieModalOverlay");
    const closeBtn = document.getElementById("cookieModalClose");
    const saveBtn = document.getElementById("cookieSaveBtn");
    const acceptAllBtn = document.getElementById("cookieAcceptAllBtn");
    const checkAnalytics = document.getElementById("cookieAnalytics");
    const checkMarketing = document.getElementById("cookieMarketing");

    // Load preferences
    const loadPreferences = () => {
        const prefs = JSON.parse(localStorage.getItem("cookiePreferences"));
        if (prefs) {
            checkAnalytics.checked = prefs.analytics;
            checkMarketing.checked = prefs.marketing;
        } else {
            // Auto open if no preferences are set
            setTimeout(() => {
                overlay.classList.add("active");
            }, 1000);
        }
    };

    // Save preferences
    const savePreferences = (analytics, marketing) => {
        localStorage.setItem("cookiePreferences", JSON.stringify({
            essential: true,
            analytics: analytics,
            marketing: marketing
        }));
        overlay.classList.remove("active");
    };

    // Event Listeners
    btn.addEventListener("click", () => {
        overlay.classList.add("active");
    });

    closeBtn.addEventListener("click", () => {
        overlay.classList.remove("active");
    });

    overlay.addEventListener("click", (e) => {
        if (e.target === overlay) {
            overlay.classList.remove("active");
        }
    });

    saveBtn.addEventListener("click", () => {
        savePreferences(checkAnalytics.checked, checkMarketing.checked);
    });

    acceptAllBtn.addEventListener("click", () => {
        checkAnalytics.checked = true;
        checkMarketing.checked = true;
        savePreferences(true, true);
    });

    loadPreferences();
});
"""

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(js_content)

print(f"Reverted {file_path}")
