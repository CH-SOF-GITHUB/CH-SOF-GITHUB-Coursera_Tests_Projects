import time

from selenium import webdriver
from selenium.webdriver.common.by import By

from LocatorsPageFactory import WikiPediaHomePage

driver = webdriver.Chrome()
if driver:
    driver.get("https://en.wikipedia.org/")
    driver.maximize_window()
    # Print the title of the page
    print("Wiki Page's Title: " + driver.title)
    # time to wait of 3s for the page to load
    time.sleep(3)
    try:
        # implement locator for button flush
        btn = driver.find_element(By.XPATH, "//input[@id='vector-main-menu-dropdown-checkbox']")
        # click on the button
        btn.click()
        # found a random link locator
        random_link = driver.find_element(*WikiPediaHomePage.Random_Link)
        # click on the random link
        random_link.click()
    except Exception as e:
        print("Error: ", e)
    # print the page's title
    print("Random Page's Title: " + driver.title)
    # wait for 5s to load page response
    time.sleep(5)

    # close th driver
    driver.quit()
else:
    print("error driver not found")
