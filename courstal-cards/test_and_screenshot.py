import time
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

chrome_options = Options()
chrome_options.add_argument("--headless=new")
chrome_options.add_argument("--window-size=1600,1000")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--no-sandbox")

driver = webdriver.Chrome(options=chrome_options)
os.makedirs("test_shots", exist_ok=True)

try:
    # 1. Main Home Page
    print("Navigating to http://localhost:3005...")
    driver.get("http://localhost:3005")
    time.sleep(3)
    driver.save_screenshot("test_shots/01_home_hero.png")
    print("Saved 01_home_hero.png")

    # Scroll to works section
    driver.execute_script("document.getElementById('works').scrollIntoView();")
    time.sleep(2)
    driver.save_screenshot("test_shots/02_works_section.png")
    print("Saved 02_works_section.png")

    # Scroll to services section
    driver.execute_script("document.getElementById('services').scrollIntoView();")
    time.sleep(2)
    driver.save_screenshot("test_shots/03_services_section.png")
    print("Saved 03_services_section.png")

    # Scroll to atelier section
    driver.execute_script("document.getElementById('atelier').scrollIntoView();")
    time.sleep(2)
    driver.save_screenshot("test_shots/04_atelier_section.png")
    print("Saved 04_atelier_section.png")

    # Scroll to contact section
    driver.execute_script("document.getElementById('contact').scrollIntoView();")
    time.sleep(2)
    driver.save_screenshot("test_shots/05_contact_section.png")
    print("Saved 05_contact_section.png")

    # 2. Works Page
    print("Navigating to http://localhost:3005/works...")
    driver.get("http://localhost:3005/works")
    time.sleep(2)
    driver.save_screenshot("test_shots/06_works_page.png")
    print("Saved 06_works_page.png")

    # Click first project card to test modal drawer
    cards = driver.find_elements(By.CLASS_NAME, "works-grid-card")
    if cards:
        cards[0].click()
        time.sleep(1)
        driver.save_screenshot("test_shots/07_works_modal.png")
        print("Saved 07_works_modal.png")

    # 3. Services Page
    print("Navigating to http://localhost:3005/services...")
    driver.get("http://localhost:3005/services")
    time.sleep(2)
    driver.save_screenshot("test_shots/08_services_page.png")
    print("Saved 08_services_page.png")

    # 4. Atelier Page
    print("Navigating to http://localhost:3005/atelier...")
    driver.get("http://localhost:3005/atelier")
    time.sleep(2)
    driver.save_screenshot("test_shots/09_atelier_page.png")
    print("Saved 09_atelier_page.png")

    # Check console logs
    logs = driver.get_log('browser')
    print(f"Browser console errors/warnings: {len(logs)}")
    for l in logs:
        if l['level'] in ['SEVERE', 'ERROR']:
            print(f"  [{l['level']}] {l['message']}")

finally:
    driver.quit()
print("Screenshot and verification run complete!")
