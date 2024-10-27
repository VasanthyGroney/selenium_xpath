from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

# Adjust the path to where your chromedriver is located
service = Service('/usr/local/bin/chromedriver')
driver = webdriver.Chrome(service=service)

# Replace this with your actual HTML file path
driver.get('file:///Users/vasantymarshalgmail.com/Documents/complete flask/Selenium Locators_XPath/sample.html')

# Example actions using CSS selectors
input_field = driver.find_element(By.CSS_SELECTOR, '#inputField')
input_field.send_keys('Hello, Selenium with CSS!')

submit_button = driver.find_element(By.CSS_SELECTOR, 'input[type="submit"]')
submit_button.click()

# Wait for a bit to see the result
time.sleep(3)

# Close the browser
driver.quit()
