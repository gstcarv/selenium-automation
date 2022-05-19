from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://www.lojasrenner.com.br/")

search_field = driver.find_element(
    by=By.CSS_SELECTOR, value="input[placeholder='Buscar produtos']"
)

search_field.send_keys("Moletom")

search_field.send_keys(Keys.RETURN)

element = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, "[class^='ProductBox_']"))
)

results = driver.find_elements(by=By.CSS_SELECTOR, value="[class^='ProductBox_']")

assert len(results) != 0

driver.quit()
