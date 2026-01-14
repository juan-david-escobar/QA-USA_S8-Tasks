import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get('https://cnt-99abb405-d777-46e3-9e75-06c485de7cf3.containerhub.tripleten-services.com/')
current_url = driver.current_url
time.sleep(2)

