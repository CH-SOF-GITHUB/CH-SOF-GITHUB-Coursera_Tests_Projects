import os

from selenium import webdriver

driver = webdriver.Chrome()

try:
    driver.get("http://localhost/se/page.html")
    assert '404 Not Found' not in driver.page_source
except Exception as e:
    print("Assertion failed: ", e)
    # verify if the directory of screenshot exist, if not create it
    screenshot_dir = "C:\\Users\\chaker\\PycharmProjects\\Coursera_Intro_Selenium_Project\\Automating-Web-Testing-with-Selenium-and-Python\\Screenshots"
    if not os.path.exists(screenshot_dir):
        os.makedirs(screenshot_dir)

    driver.save_screenshot(f"{screenshot_dir}/error.png")
finally:
    # close the browser
    driver.quit()
