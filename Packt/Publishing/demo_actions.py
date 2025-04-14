import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

# declare a web driver
driver = webdriver.Chrome()
# create a new Chrome browser instance
if driver:
    driver.get("https://www.google.com")
    driver.implicitly_wait(5)
    # wait for 3 seconds for loading page
    time.sleep(3)
    # print the title of the page
    print("Page's Title before search: " + driver.title)
    # locate for search box element
    search_box = driver.find_element(By.NAME, "q")
    # enter the search term
    search_box.send_keys("selenium", Keys.ENTER)
    # print the page's title
    print("Page's Title after search: " + driver.title)
    # wait for time of 10 seconds
    time.sleep(10)
    # close the browser
    driver.quit()
