from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get('https://cnt-a3604b94-3eb8-4c58-95db-3a6c3e88c791.containerhub.tripleten-services.com/')
current_url = driver.current_url
driver.maximize_window()
time.sleep(2)

expand_element = driver.find_element(By.CSS_SELECTOR, 'button[class="gm-control-active gm-fullscreen-control"]')
expand_element.click()
time.sleep(2)

expand_element.click()
time.sleep(2)

input_element_from = driver.find_element(By.CSS_SELECTOR, 'input#from')
input_element_from.send_keys('East')
time.sleep(2)

input_element_to = driver.find_element(By.CSS_SELECTOR, 'input#to')
input_element_to.send_keys('1300')
time.sleep(2)

click_element = driver.find_element(By.CSS_SELECTOR, 'button[class="button round"]')
click_element.click()

print(current_url)
print(input_element_from.get_attribute('class'))
print(input_element_to.get_attribute('class'))

driver.quit()