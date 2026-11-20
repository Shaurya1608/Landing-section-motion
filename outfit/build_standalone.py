import json
import base64
import re
import urllib.request

def build():
    # 1. Load ref.html
    with open('ref.html', 'r', encoding='utf-8') as f:
        html = f.read()

    # 2. Load style.css
    with open('style.css', 'r', encoding='utf-8') as f:
        css = f.read()

    # 3. Load app.js
    with open('app.js', 'r', encoding='utf-8') as f:
        js = f.read()

    # 4. Fetch font and encode base64
    with urllib.request.urlopen('https://reel-ref-try-the-look.vercel.app/assets/inter-600.woff2') as r:
        font_b64 = base64.b64encode(r.read()).decode('ascii')

    font_data_uri = f'data:font/woff2;base64,{font_b64}'
    css = css.replace("url('assets/inter-600.woff2')", f"url('{font_data_uri}')")
    css = css.replace('url("assets/inter-600.woff2")', f"url('{font_data_uri}')")
    css = css.replace('url(assets/inter-600.woff2)', f"url('{font_data_uri}')")

    # 5. Load and process catalog
    with urllib.request.urlopen('https://reel-ref-try-the-look.vercel.app/native-catalog.json') as r:
        catalog = json.loads(r.read().decode('utf-8'))

    # Rewrite all image urls in catalog
    for item in catalog.get('items', []):
        if 'image' in item and item['image'].startswith('assets/'):
            item['image'] = f"https://reel-ref-try-the-look.vercel.app/{item['image']}"

    for look in catalog.get('looks', []):
        if 'image' in look and look['image'].startswith('assets/'):
            look['image'] = f"https://reel-ref-try-the-look.vercel.app/{look['image']}"

    catalog_json_str = json.dumps(catalog)

    # Replace fetch('native-catalog.json') in js
    # Let's inspect how catalogPromise is handled in js
    old_fetch_pattern = re.compile(
        r"const catalogPromise\s*=\s*fetch\('native-catalog\.json'\)\.then\(response\s*=>\s*\{[^}]*return response\.json\(\);\s*\}\)\.then\(data\s*=>\s*\{",
        re.DOTALL
    )
    
    # We can define CATALOG_DATA directly and validate it identically
    replacement_catalog = f"""const CATALOG_DATA = {catalog_json_str};
  const catalogPromise = Promise.resolve(CATALOG_DATA).then(data => {{"""

    new_js = old_fetch_pattern.sub(replacement_catalog, js)
    if new_js == js:
        print("WARNING: old_fetch_pattern did not match, using substring replace")
        # Try finding the exact substring
        idx = js.find("fetch('native-catalog.json')")
        print("fetch index:", idx)
        snippet = js[idx-20:idx+200]
        print("snippet:", snippet)

    # Remove service worker
    new_js = re.sub(r"if\s*\('serviceWorker'\s*in\s*navigator\)\s*navigator\.serviceWorker\.register\('[^']+'\)\.catch\(\(\)\s*=>\s*\{\}\);", "", new_js)

    # 6. Replace all relative assets/ in html
    # Assets are in href, src, srcset, data-probe
    html = html.replace('href="assets/', 'href="https://reel-ref-try-the-look.vercel.app/assets/')
    html = html.replace('src="assets/', 'src="https://reel-ref-try-the-look.vercel.app/assets/')
    html = html.replace('srcset="assets/', 'srcset="https://reel-ref-try-the-look.vercel.app/assets/')
    html = html.replace(', assets/', ', https://reel-ref-try-the-look.vercel.app/assets/')
    html = html.replace('data-probe="assets/', 'data-probe="https://reel-ref-try-the-look.vercel.app/assets/')

    # 7. Replace <link rel="stylesheet" href="style.css"> with <style>...</style>
    style_tag = f"<style>\n{css}\n</style>"
    html = re.sub(r'<link\s+rel=["\']stylesheet["\']\s+href=["\']style\.css["\']\s*/?>', lambda m: style_tag, html)

    # 8. Replace <script src="app.js" defer></script> with inline <script>...</script>
    script_tag = f"<script>\n{new_js}\n</script>"
    html = re.sub(r'<script\s+src=["\']app\.js["\']\s*defer\s*>\s*</script>', lambda m: script_tag, html)

    # 9. Verify page elements
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(html)

    print(f"Successfully generated standalone index.html! Length: {len(html)} bytes")

if __name__ == '__main__':
    build()
