import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.maximize_window()
driver.get('https://cnt-4ae5c2b2-2e24-4aa1-acba-42f2d4a2f144.containerhub.tripleten-services.com/')
current_url = driver.current_url
time.sleep(2)

input_from = driver.find_element(By.CSS_SELECTOR, 'input#from')
input_from.send_keys('East')
time.sleep(2)

input_to = driver.find_element(By.CSS_SELECTOR, 'input#to')
input_to.send_keys('1300')
time.sleep(2)

custom_button = WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, "//div[text()='Custom']")))
custom_button.click()
time.sleep(2)

driver.find_element(By.XPATH, '//img[@src="/static/media/scooter.cf9bb57e.svg"]').click()
time.sleep(2)

text_checked = driver.find_element(By.CSS_SELECTOR, 'div.text').text

assert "Scooter" in text_checked

driver.quit()