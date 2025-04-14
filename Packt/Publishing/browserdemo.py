import time

from selenium import webdriver

# Create a new Chrome browser instance
driver = webdriver.Chrome()
# Navigate to the Selenium HQ website
driver.get("https://www.seleniumhq.org")
# Print the title of the page
print("Page's Title: " + driver.title)
# time to wait for the page to load
time.sleep(20)
# Close the browser
driver.quit()