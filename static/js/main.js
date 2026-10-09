// Initialize GSAP
gsap.registerPlugin(ScrollTrigger);

document.addEventListener("DOMContentLoaded", (event) => {
    // Check if we haven't played intro yet in this session to avoid annoyance on every page load
    if (!sessionStorage.getItem('introPlayed')) {
        const tl = gsap.timeline();

        tl.to(".intro-logo", {
            opacity: 1,
            y: -20,
            duration: 1.2,
            ease: "power3.out"
        })
            .to(".intro-tagline", {
                opacity: 1,
                y: -10,
                duration: 1,
                ease: "power3.out"
            }, "-=0.8")
            .to(".loading-line", {
                width: "200px",
                duration: 1,
                ease: "power2.inOut"
            }, "-=0.4")
            .to(".intro-content", {
                opacity: 0,
                duration: 0.5,
                ease: "power2.in"
            }, "+=0.6")
            .to(".door-left", {
                x: "-100%",
                duration: 1.5,
                ease: "power4.inOut"
            }, "doors")
            .to(".door-right", {
                x: "100%",
                duration: 1.5,
                ease: "power4.inOut"
            }, "doors")
            .set(".intro-overlay", {
                display: "none",
                onComplete: () => {
                    sessionStorage.setItem('introPlayed', 'true');
                    document.dispatchEvent(new CustomEvent('introFinished'));
                }
            })
            .from(".navbar", {
                y: -50,
                opacity: 0,
                duration: 1,
                ease: "power3.out"
            }, "doors+=0.8");
    } else {
        // Intro already played, hide overlay instantly
        document.getElementById('intro-overlay').style.display = 'none';

        // Just animate navbar
        gsap.from(".navbar", {
            y: -50,
            opacity: 0,
            duration: 0.8,
            ease: "power3.out"
        });

        // Dispatch immediately since splash is skipped
        document.dispatchEvent(new CustomEvent('introFinished'));
    }
});

// PWA Installation & Notification Flow
let deferredPrompt;
let introIsDone = false;
let pwaBannerActive = false;

function showBannersIfNeeded() {
    if (!introIsDone) return;

    const pwaBanner = document.getElementById('pwa-banner');
    const notifBanner = document.getElementById('notification-banner');

    // First priority: PWA Install Banner
    if (deferredPrompt && !localStorage.getItem('pwaPromptClosed')) {
        if (pwaBanner) pwaBanner.style.display = 'flex';
        pwaBannerActive = true;
        // Hide notif banner if it was showing
        if (notifBanner) notifBanner.style.display = 'none';
        return;
    }

    // Second priority: Notification Banner
    if (notifBanner && 'Notification' in window) {
        if (Notification.permission === 'default' && !localStorage.getItem('notifPromptClosed')) {
            // Give a small delay for notif banner so it feels less aggressive
            setTimeout(() => {
                if (!pwaBannerActive) {
                    notifBanner.style.display = 'flex';
                }
            }, 3000);
        }
    }
}

window.addEventListener('beforeinstallprompt', (e) => {
    // Prevent the mini-infobar from appearing on mobile
    e.preventDefault();
    // Stash the event so it can be triggered later.
    deferredPrompt = e;
    showBannersIfNeeded();
});

document.addEventListener('introFinished', () => {
    introIsDone = true;
    showBannersIfNeeded();
});

document.addEventListener("DOMContentLoaded", () => {
    // 1. Install App Logic
    const btnInstall = document.getElementById('btn-install-pwa');
    const btnClosePwa = document.getElementById('btn-close-pwa');
    const pwaBanner = document.getElementById('pwa-banner');

    if (btnInstall) {
        btnInstall.addEventListener('click', async () => {
            if (pwaBanner) pwaBanner.style.display = 'none';
            pwaBannerActive = false;
            if (deferredPrompt) {
                deferredPrompt.prompt();
                const { outcome } = await deferredPrompt.userChoice;
                deferredPrompt = null;
            }
            showBannersIfNeeded(); // Check if we should show notif banner
        });
    }

    if (btnClosePwa) {
        btnClosePwa.addEventListener('click', () => {
            if (pwaBanner) pwaBanner.style.display = 'none';
            pwaBannerActive = false;
            localStorage.setItem('pwaPromptClosed', 'true');
            showBannersIfNeeded(); // Check if we should show notif banner
        });
    }

    // 2. Push Notifications Logic
    const notifBanner = document.getElementById('notification-banner');
    const btnEnableNotif = document.getElementById('btn-enable-notif');
    const btnCloseNotif = document.getElementById('btn-close-notif');

    if (btnEnableNotif) {
        btnEnableNotif.addEventListener('click', () => {
            Notification.requestPermission().then(permission => {
                if (notifBanner) notifBanner.style.display = 'none';
                if (permission === 'granted') {
                    console.log('Notification permission granted.');
                    navigator.serviceWorker.ready.then(reg => {
                        reg.showNotification('Olive Cafe', {
                            body: 'Thanks for enabling notifications! You will now receive order updates.',
                            icon: '/static/images/icon-192x192.png',
                            badge: '/static/images/icon-192x192.png'
                        });
                    });
                }
            });
        });
    }

    if (btnCloseNotif) {
        btnCloseNotif.addEventListener('click', () => {
            if (notifBanner) notifBanner.style.display = 'none';
            localStorage.setItem('notifPromptClosed', 'true');
        });
    }

    // 3. Mobile Menu Toggle Logic
    const mobileMenuBtn = document.querySelector('.mobile-menu-btn');
    const navLinks = document.querySelector('.nav-links');
    
    if (mobileMenuBtn && navLinks) {
        mobileMenuBtn.addEventListener('click', () => {
            navLinks.classList.toggle('active');
        });
    }
});
