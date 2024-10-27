from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

# Automatically download and set up the Chrome WebDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Open the HTML file
driver.get('file:///Users/vasantymarshalgmail.com/Documents/complete flask/Selenium Locators_XPath/sample.html')

# Locate the input field by ID and enter text
input_field = driver.find_element(By.ID, 'inputField')
input_field.send_keys('Hello, Selenium!')

# Locate and click the submit button
submit_button = driver.find_element(By.ID, 'submitButton')
submit_button.click()

# Add delay to see the result
time.sleep(3)

# Close the browser
driver.quit()
