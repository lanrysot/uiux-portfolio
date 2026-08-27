import re

with open('project-css.css', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Remove old desktop nav styles
content = re.sub(r'nav\s*\{[^}]*position:\s*fixed;.*?\}\s*\.logo\s*\{.*?\n\.ncta:hover\s*\{[^}]*\}', '', content, flags=re.DOTALL)

# 2. Remove old mobile menu styles
content = re.sub(r'\.mobile-menu-btn\s*\{.*?\n\.mobile-nav-ul \.ncta:hover\s*\{[^}]*\}', '', content, flags=re.DOTALL)
# Also remove any leftover mobile-menu-btn in media queries
content = re.sub(r'\.mobile-menu-btn\s*\{[^}]*\}', '', content, flags=re.DOTALL)

# 3. Remove the block I appended previously
content = re.sub(r'/\* NAV STYLES IMPORTED FROM STYLE\.CSS \*/.*', '', content, flags=re.DOTALL)

# 4. Define the new, unified navigation block
nav_styles = '''
/* Unified Navigation Styles */
nav {
    position: fixed;
    top: 0;
    left: 0;
    right: 0;
    z-index: 200;
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 20px 60px;
    background: rgba(3, 7, 20, .75);
    backdrop-filter: blur(24px);
    border-bottom: 1px solid var(--b);
}

.nav-logo {
    font-size: 16px;
    font-weight: 800;
    letter-spacing: -.01em;
    color: var(--tp);
    text-decoration: none;
    display: flex;
    align-items: center;
    gap: 2px;
}

.nav-logo .dot { color: var(--ac); }

.nav-links {
    display: flex;
    gap: 36px;
    list-style: none;
}

.nav-links a {
    font-size: 13px;
    font-weight: 500;
    color: var(--tm);
    text-decoration: none;
    letter-spacing: .01em;
    transition: color .2s;
    text-transform: none;
}

.nav-links a:hover { color: var(--tp); }

.nav-cta {
    display: inline-flex;
    align-items: center;
    gap: 8px;
    background: var(--ac);
    color: #fff;
    padding: 10px 22px;
    border-radius: 8px;
    font-size: 13px;
    font-weight: 700;
    text-decoration: none;
    transition: opacity .2s, box-shadow .2s;
    box-shadow: 0 0 0 0 var(--acgs);
}

.nav-cta:hover {
    opacity: .9;
    box-shadow: 0 0 24px var(--acgs);
}

/* MOBILE MENU */
.mobile-menu-btn {
    display: none;
    background: none;
    border: none;
    cursor: pointer;
    width: 30px;
    height: 24px;
    position: relative;
    z-index: 1001;
    margin-left: 10px;
}
.mobile-menu-btn span {
    display: block;
    width: 100%;
    height: 2px;
    background: var(--tp);
    position: absolute;
    left: 0;
    transition: 0.3s;
}
.mobile-menu-btn span:nth-child(1) { top: 0; }
.mobile-menu-btn span:nth-child(2) { top: 11px; }
.mobile-menu-btn span:nth-child(3) { top: 22px; }

.mobile-menu-btn.active span:nth-child(1) {
    top: 11px;
    transform: rotate(45deg);
}
.mobile-menu-btn.active span:nth-child(2) {
    opacity: 0;
}
.mobile-menu-btn.active span:nth-child(3) {
    top: 11px;
    transform: rotate(-45deg);
}

.mobile-menu {
    position: fixed;
    inset: 0;
    background: rgba(3, 7, 20, 0.95);
    backdrop-filter: blur(20px);
    z-index: 999;
    display: flex;
    align-items: center;
    justify-content: center;
    opacity: 0;
    pointer-events: none;
    transition: 0.4s;
}
.mobile-menu.active {
    opacity: 1;
    pointer-events: auto;
}
.mobile-nav-ul {
    list-style: none;
    text-align: center;
    display: flex;
    flex-direction: column;
    gap: 24px;
}
.mobile-nav-ul a {
    font-size: 24px;
    color: var(--tp);
    text-decoration: none;
    font-weight: 600;
}
.mobile-nav-ul a.ncta {
    color: var(--ac);
    font-size: 20px;
    border: 1px solid var(--ac);
    padding: 12px 24px;
    border-radius: 8px;
    display: inline-block;
    margin-top: 12px;
    background: transparent !important;
}

@media (max-width: 768px) {
    .nav-links, .nav-cta {
        display: none;
    }
    .mobile-menu-btn {
        display: block;
    }
    nav {
        padding: 20px 24px;
    }
    .nav-logo {
        font-size: 14px;
    }
}
'''

with open('project-css.css', 'w', encoding='utf-8') as f:
    f.write(content + "\n" + nav_styles)

print("Navigation styles updated in project-css.css")
