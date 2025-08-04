from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time, os, requests, json
from urllib.parse import urljoin

# Set up Selenium
options = webdriver.ChromeOptions()
options.add_argument('--headless')
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# Target URL
base_url = "https://www.cbn.gov.ng/Documents/circulars.html"
driver.get(base_url)

# Wait for page to load JS
time.sleep(5)

# Find PDF links
rows = driver.find_elements(By.CSS_SELECTOR, "table tr")
pdfs = []
os.makedirs("cbn_pdfs", exist_ok=True)

for row in rows:
    try:
        link = row.find_element(By.TAG_NAME, "a")
        href = link.get_attribute("href")
        text = link.text.strip()
        
        if href and href.lower().endswith(".pdf"):
            filename = text.replace(" ", "_").replace("/", "_") + ".pdf"
            file_path = os.path.join("cbn_pdfs", filename)
            
            r = requests.get(href)
            with open(file_path, "wb") as f:
                f.write(r.content)

            pdfs.append({
                "title": text,
                "pdf_url": href,
                "local_path": os.path.abspath(file_path)
            })
            print(f"✅ Saved: {filename}")
    except:
        continue

driver.quit()

# Save JSON
with open("cbn_circulars.json", "w", encoding="utf-8") as f:
    json.dump(pdfs, f, indent=2)

print(f"\n📦 Done. {len(pdfs)} PDF(s) saved.")
