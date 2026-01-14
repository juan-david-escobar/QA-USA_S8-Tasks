from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.maximize_window()
time.sleep(2)

driver.get('https://cnt-941bbeb5-1f36-468c-80a4-00e2e01a7083.containerhub.tripleten-services.com')
current_url = driver.current_url
time.sleep(2)

input_element_from = driver.find_element(By.CSS_SELECTOR, 'input#from')
input_element_from.send_keys('East')
time.sleep(2)

input_element_to = driver.find_element(By.CSS_SELECTOR, 'input#to')
input_element_to.send_keys('1300')
time.sleep(2)

element_from = input_element_from.get_attribute('id')
element_to = input_element_to.get_attribute('id')

print(current_url)
print(element_from)
print(element_to)

driver.quit()