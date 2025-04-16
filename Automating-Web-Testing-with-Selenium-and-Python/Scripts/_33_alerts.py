import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("http://localhost:63343/Coursera_Intro_Selenium_Project/Automating-Web-Testing-with-Selenium-and-Python/Pages-HTML/section_3/33_alert.html?_ijt=l34c1i82rh4rmrdd0fu1qfsoo1&_ij_reload=RELOAD_ON_SAVE")
screenshot_dir = "C:\\Users\\chaker\\PycharmProjects\\Coursera_Intro_Selenium_Project\\Automating-Web-Testing-with-Selenium-and-Python\\Screenshots"

try:
    alert = driver.find_element(By.TAG_NAME, "button")
    alert.click()
    time.sleep(1)
    driver.switch_to.alert.accept()
    time.sleep(1)
    print("switch to Alert with success")
    driver.save_screenshot(f"{screenshot_dir}/alert.png")
finally:
    driver.quit()
