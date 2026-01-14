from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.get('https://cnt-c9490a9d-0d16-4b3f-8bdf-b137b8cfa93e.containerhub.tripleten-services.com/')
current_url = driver.current_url
driver.maximize_window()
time.sleep(2)

from_input = driver.find_element(By.CSS_SELECTOR, 'input#from')
from_input.send_keys('East')
time.sleep(2)

to_input = driver.find_element(By.CSS_SELECTOR, 'input#to')
to_input.send_keys('1300')
time.sleep(2)

taxi_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Call a taxi')]")
taxi_button.click()

WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input#comment"))).send_keys("I am outside waiting for you")

assert driver.find_element(By.ID, "comment").get_attribute("value") == "I am outside waiting for you"

print(current_url)
print(from_input.get_attribute("id"))
print(to_input.get_attribute("id"))
print(driver.find_element(By.ID, "comment").get_attribute("value"))


driver.quit()