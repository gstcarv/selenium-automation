from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.options import Options
import json

with open('products.datapool.json', 'r') as f:
    datapool = json.load(f)

with open('config.json', 'r') as f:
    config = json.load(f)

if config["driver"]["firefox"]:
    driver = webdriver.Firefox()
else:
    driver = webdriver.Chrome()

driver.get(datapool["renner_url"])

search_field = driver.find_element(
    by=By.CSS_SELECTOR, value=datapool["selectors"]["search_field"]
)

search_field.send_keys(datapool["query"]["search_query"])

search_field.send_keys(Keys.RETURN)

element = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, datapool["selectors"]["product_box"]))
)

results = driver.find_elements(by=By.CSS_SELECTOR, value=datapool["selectors"]["product_box"])

assert len(results) != 0

# driver.close()