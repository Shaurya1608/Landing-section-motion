import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

checks = []

def check(name, condition, details=""):
    checks.append((name, condition, details))
    print(f"[{'PASS' if condition else 'FAIL'}] {name} {details}")

# 1. Page basics
check("lang='en'", '<html lang="en">' in html)
check("meta charset", '<meta charset="utf-8">' in html)
check("viewport", '<meta name="viewport" content="width=device-width,initial-scale=1">' in html)
check("theme-color", '<meta name="theme-color" content="#ffffff">' in html)
check("title", '<title>Try the Look — Runway</title>' in html)
check("meta description", '<meta name="description" content="Six looks, styled head to toe. Explore the runway, isolate a look, and tap a pin to see the piece.">' in html)
check("preload model 1", 'href="https://reel-ref-try-the-look.vercel.app/assets/model-1-640.webp"' in html)

# 1.1 Header
check("header class", 'class="site-header shopify-section-group-header-group"' in html)
check("nike logo absolute url", 'https://reel-ref-try-the-look.vercel.app/assets/nike-logo.svg' in html)
check("nav links: Home", 'Home</a>' in html)
check("nav links: Nike Orbit", 'Nike Orbit</a>' in html)
check("nav links: Hand Rail Pro", 'Hand Rail Pro</a>' in html)
check("nav links: Runway", 'Runway</a>' in html)
check("bag button", 'id="open-bag"' in html)
check("data-cart-count", 'data-cart-count' in html)

# 1.2 Section
check("runway-section tag", '<runway-section' in html)
check("runway id", 'id="Runway-template--28035983671601__the_runway_wdM8BG"' in html)
check("runway classes", 'class="rw rw--add-icon rw--popup rw--list has-dividers has-border"' in html)
check("data-feel", 'data-feel="balanced"' in html)
check("data-blur", 'data-blur="true"' in html)
check("data-style", 'data-style="ring"' in html)
check("data-mstyle", 'data-mstyle="classic"' in html)
check("data-speed", 'data-speed="5000"' in html)

# Dialog & Toast
check("bag-dialog", '<dialog id="bag-dialog"' in html)
check("bag-status toast", '<div id="bag-status" role="status" aria-live="polite">' in html)

# 2. Assets (no relative assets/ left)
relative_assets = re.findall(r'[\'"\s=]assets/[^\'"\s]+', html)
check("no relative assets/ left", len(relative_assets) == 0, f"Found {len(relative_assets)}: {relative_assets[:3]}")

# 3. Font
check("Inter woff2 base64 embedded", 'data:font/woff2;base64,' in html)

# 4. Inlined catalog
check("inlined catalog data", 'CATALOG_DATA' in html)
check("no fetch native-catalog.json", "fetch('native-catalog.json')" not in html)
check("no serviceWorker register", "navigator.serviceWorker.register" not in html)

# 5. Custom element
check("customElements.define", "customElements.define('runway-section', RunwaySection)" in html)

# 6. Syntax validation with Node.js
print("\nTotal checks:", len(checks))
print("Passed:", sum(1 for c in checks if c[1]))
print("Failed:", sum(1 for c in checks if not c[1]))
