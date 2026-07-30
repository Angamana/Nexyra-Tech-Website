function initCookiePolicy() {
    // Self-contained CSS embedded directly to match the design screenshot perfectly
    const widgetHTML = `
        <style>
            .cookie-widget-btn {
                position: fixed !important;
                bottom: 30px !important;
                left: 30px !important;
                width: 60px !important;
                height: 60px !important;
                background-color: #1d4ed8 !important;
                border-radius: 50% !important;
                display: flex !important;
                justify-content: center !important;
                align-items: center !important;
                cursor: pointer !important;
                box-shadow: 0 4px 16px rgba(0, 0, 0, 0.25) !important;
                z-index: 9999 !important;
                transition: background-color 0.3s ease, transform 0.3s ease !important;
                pointer-events: auto !important;
                visibility: visible !important;
                opacity: 1 !important;
            }
            .cookie-widget-btn:hover {
                background-color: #1e40af !important;
                transform: scale(1.08) !important;
            }
            .cookie-widget-btn svg {
                width: 30px !important;
                height: 30px !important;
                fill: #ffffff !important;
                transition: fill 0.3s ease !important;
                pointer-events: none !important;
            }
            .cookie-modal-overlay {
                position: fixed !important;
                top: 0 !important;
                left: 0 !important;
                width: 100vw !important;
                height: 100vh !important;
                background-color: rgba(0, 0, 0, 0.65) !important;
                z-index: 100000000 !important;
                display: flex !important;
                justify-content: center !important;
                align-items: center !important;
                opacity: 0 !important;
                pointer-events: none !important;
                transition: opacity 0.3s ease !important;
            }
            .cookie-modal-overlay.active {
                opacity: 1 !important;
                pointer-events: auto !important;
            }
            .cookie-modal {
                background-color: #ffffff !important;
                border: none !important;
                color: #0f172a !important;
                border-radius: 16px !important;
                width: 90% !important;
                max-width: 580px !important;
                padding: 36px !important;
                box-shadow: 0 20px 40px rgba(0, 0, 0, 0.35) !important;
                box-sizing: border-box !important;
                font-family: 'Inter', system-ui, -apple-system, sans-serif !important;
            }
            .cookie-modal-header {
                display: flex !important;
                justify-content: space-between !important;
                align-items: center !important;
                margin-bottom: 16px !important;
            }
            .cookie-modal-title {
                font-size: 24px !important;
                font-weight: 700 !important;
                margin: 0 !important;
                color: #0f172a !important;
                letter-spacing: -0.02em !important;
            }
            .cookie-modal-close {
                background: none !important;
                border: none !important;
                font-size: 24px !important;
                color: #94a3b8 !important;
                cursor: pointer !important;
                line-height: 1 !important;
                padding: 0 !important;
            }
            .cookie-modal-close:hover {
                color: #0f172a !important;
            }
            .cookie-modal-body p {
                font-size: 14px !important;
                color: #475569 !important;
                line-height: 1.6 !important;
                margin-top: 0 !important;
                margin-bottom: 24px !important;
            }
            .cookie-toggles {
                display: flex !important;
                flex-direction: column !important;
                gap: 18px !important;
                margin-bottom: 32px !important;
            }
            .cookie-toggle-row {
                display: flex !important;
                justify-content: space-between !important;
                align-items: center !important;
                background: transparent !important;
                border: none !important;
                padding: 0 !important;
                border-bottom: 1px solid #f1f5f9 !important;
                padding-bottom: 14px !important;
            }
            .cookie-toggle-row:last-child {
                border-bottom: none !important;
                padding-bottom: 0 !important;
            }
            .cookie-toggle-label {
                font-weight: 600 !important;
                font-size: 15px !important;
                color: #0f172a !important;
            }
            .cookie-toggle-desc {
                font-size: 12px !important;
                color: #64748b !important;
                margin-top: 3px !important;
            }
            .cookie-switch {
                position: relative !important;
                display: inline-block !important;
                width: 46px !important;
                height: 26px !important;
                flex-shrink: 0 !important;
            }
            .cookie-switch input {
                opacity: 0 !important;
                width: 0 !important;
                height: 0 !important;
            }
            .cookie-slider {
                position: absolute !important;
                cursor: pointer !important;
                top: 0 !important;
                left: 0 !important;
                right: 0 !important;
                bottom: 0 !important;
                background-color: #cbd5e1 !important;
                transition: .3s !important;
                border-radius: 26px !important;
            }
            .cookie-slider:before {
                position: absolute !important;
                content: "" !important;
                height: 20px !important;
                width: 20px !important;
                left: 3px !important;
                bottom: 3px !important;
                background-color: white !important;
                transition: .3s !important;
                border-radius: 50% !important;
                box-shadow: 0 1px 3px rgba(0,0,0,0.15) !important;
            }
            .cookie-switch input:checked + .cookie-slider {
                background-color: #6366f1 !important;
            }
            .cookie-switch input:checked + .cookie-slider:before {
                transform: translateX(20px) !important;
            }
            .cookie-modal-footer {
                display: flex !important;
                justify-content: flex-end !important;
                gap: 12px !important;
            }
            .cookie-btn {
                padding: 11px 22px !important;
                border-radius: 8px !important;
                font-size: 14px !important;
                font-weight: 600 !important;
                cursor: pointer !important;
                border: none !important;
                transition: background-color 0.2s ease, transform 0.1s ease !important;
            }
            .cookie-btn-secondary {
                background-color: #f1f5f9 !important;
                border: none !important;
                color: #334155 !important;
            }
            .cookie-btn-secondary:hover {
                background-color: #e2e8f0 !important;
            }
            .cookie-btn-primary {
                background-color: #1d4ed8 !important;
                color: #ffffff !important;
            }
            .cookie-btn-primary:hover {
                background-color: #1e40af !important;
            }
        </style>

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
                    <button class="cookie-btn cookie-btn-primary" id="cookieRejectAllBtn">Reject All</button>
                    <button class="cookie-btn cookie-btn-primary" id="cookieAcceptAllBtn">Accept All</button>
                </div>
            </div>
        </div>
    `;

    const widgetContainer = document.createElement("div");
    widgetContainer.id = "cookie-policy-system-root";
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
            // Auto popup on index/home pages after 16s delay
            setTimeout(() => {
                if (overlay) {
                    overlay.classList.add("active");
                }
            }, 16000);
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
    if (btn) {
        btn.addEventListener("click", (e) => {
            e.preventDefault();
            e.stopPropagation();
            overlay.classList.add("active");
        });
    }

    if (closeBtn) {
        closeBtn.addEventListener("click", (e) => {
            e.preventDefault();
            overlay.classList.remove("active");
        });
    }

    if (overlay) {
        overlay.addEventListener("click", (e) => {
            if (e.target === overlay) {
                overlay.classList.remove("active");
            }
        });
    }

    if (saveBtn) {
        saveBtn.addEventListener("click", (e) => {
            e.preventDefault();
            savePreferences(checkAnalytics.checked, checkMarketing.checked);
        });
    }

    if (acceptAllBtn) {
        acceptAllBtn.addEventListener("click", (e) => {
            e.preventDefault();
            checkAnalytics.checked = true;
            checkMarketing.checked = true;
            savePreferences(true, true);
        });
    }

    if (rejectAllBtn) {
        rejectAllBtn.addEventListener("click", (e) => {
            e.preventDefault();
            checkAnalytics.checked = false;
            checkMarketing.checked = false;
            savePreferences(false, false);
        });
    }

    loadPreferences();
}

if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", initCookiePolicy);
} else {
    initCookiePolicy();
}

// Disable right-click context menu globally across the website
document.addEventListener("contextmenu", function(e) {
    e.preventDefault();
});
