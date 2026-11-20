import time
import os
from selenium import webdriver
from selenium.webdriver.edge.options import Options

def run_checks():
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--window-size=1440,900')
    driver = webdriver.Edge(options=options)

    out_dir = r'C:\Users\Asus\websites-templates\courstal-cards\screenshots'
    os.makedirs(out_dir, exist_ok=True)

    targets = [
        ('next', 'http://localhost:3005'),
        ('html', 'http://localhost:8091/index.html')
    ]

    for prefix, url in targets:
        print(f"Testing {prefix}: {url}...")
        driver.set_window_size(1440, 900)
        driver.get(url)
        # Wait for intro animation (plane + cards rise + icon morph)
        time.sleep(3.5)
        driver.save_screenshot(os.path.join(out_dir, f'{prefix}_desktop_hero.png'))

        # Scroll to Process block (Cards scatter / process reveal)
        driver.execute_script("""
            const story = document.getElementById('story');
            const h = (story.offsetHeight - window.innerHeight);
            window.scrollTo(0, story.offsetTop + h * 0.16);
        """)
        time.sleep(1.0)
        driver.save_screenshot(os.path.join(out_dir, f'{prefix}_desktop_process.png'))

        # Scroll to Wheel
        driver.execute_script("""
            const story = document.getElementById('story');
            const h = (story.offsetHeight - window.innerHeight);
            window.scrollTo(0, story.offsetTop + h * 0.50);
        """)
        time.sleep(1.0)
        driver.save_screenshot(os.path.join(out_dir, f'{prefix}_desktop_wheel.png'))

        # Scroll to Sky panel
        driver.execute_script("""
            const story = document.getElementById('story');
            const h = (story.offsetHeight - window.innerHeight);
            window.scrollTo(0, story.offsetTop + h * 0.78);
        """)
        time.sleep(1.5)
        driver.save_screenshot(os.path.join(out_dir, f'{prefix}_desktop_sky.png'))

        # Scroll to Manifesto
        driver.execute_script("""
            const man = document.getElementById('manifesto');
            window.scrollTo(0, man.offsetTop + 400);
        """)
        time.sleep(1.0)
        driver.save_screenshot(os.path.join(out_dir, f'{prefix}_desktop_manifesto.png'))

        # Mobile Viewport
        driver.set_window_size(390, 844)
        driver.get(url)
        time.sleep(3.5)
        driver.save_screenshot(os.path.join(out_dir, f'{prefix}_mobile_hero.png'))

    driver.quit()
    print("All screenshots captured successfully in", out_dir)

if __name__ == '__main__':
    run_checks()
