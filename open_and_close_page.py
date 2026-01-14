from selenium import webdriver

driver = webdriver.Chrome()
driver.maximize_window()

# Open the Urban Routes home page
driver.get('https://google.com/')

# Saving the url in a variable
current_url = driver.current_url

# Printing the saved url to check on command line
print(current_url)

# Check url contains tripleten-services.com
assert 'google.com' in current_url

# Close the browser
driver.quit()