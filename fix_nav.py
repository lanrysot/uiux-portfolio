import os
import re

new_nav = '''  <!-- NAV -->
  <nav id="nav">
      <a href="./index.html" class="nav-logo">OLANREWAJU SULAIMON<span class="dot">.</span></a>
      <ul class="nav-links">
          <li><a href="./index.html#reel">Case Studies</a></li>
          <li><a href="./index.html#services">Services</a></li>
          <li><a href="./index.html#process">Process</a></li>
          <li><a href="./index.html#about">About</a></li>
          <li><a href="./index.html#reviews">Reviews</a></li>
      </ul>
      <a href="https://cal.com/OLANREWAJU-SULAIMON" class="nav-cta">Start a Project ?</a>
      <button class="mobile-menu-btn" id="mobileMenuBtn">
          <span></span>
          <span></span>
          <span></span>
      </button>
  </nav>

  <!-- MOBILE MENU -->
  <div class="mobile-menu" id="mobileMenu">
      <ul class="mobile-nav-ul">
          <li><a href="./index.html#reel">Case Studies</a></li>
          <li><a href="./index.html#services">Services</a></li>
          <li><a href="./index.html#process">Process</a></li>
          <li><a href="./index.html#about">About</a></li>
          <li><a href="./index.html#reviews">Reviews</a></li>
          <li><a class="ncta" href="https://cal.com/OLANREWAJU-SULAIMON">Start a Project</a></li>
      </ul>
  </div>'''

old_nav_pattern = re.compile(
    r'<!-- NAV -->\s*<nav>\s*<a class=\'logo\'.*?</nav>\s*<!-- MOBILE MENU -->\s*<div class="mobile-menu" id="mobileMenu">.*?</div>\s*</div>',
    re.DOTALL
)

directory = r'.'

for filename in os.listdir(directory):
    if filename.endswith(".html") and filename not in ["index.html", "quicken-case-study.html"]:
        filepath = os.path.join(directory, filename)
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        if old_nav_pattern.search(content):
            new_content = old_nav_pattern.sub(new_nav, content)
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Updated {filename}")
        else:
            print(f"Pattern not found in {filename}")
