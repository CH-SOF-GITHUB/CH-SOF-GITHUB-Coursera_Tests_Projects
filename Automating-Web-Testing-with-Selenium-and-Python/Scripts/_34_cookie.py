import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from Class.element_has__attribute import element_has_css_class

driver = webdriver.Chrome()

# open the browser
driver.get(
    "http://localhost:63343/Coursera_Intro_Selenium_Project/Automating-Web-Testing-with-Selenium-and-Python/Pages-HTML/section_3/34.html?_ijt=rgruokol97dbi0evcn1tnnfqgc&_ij_reload=RELOAD_ON_SAVE")
screenshot_dir = "C:\\Users\\chaker\\PycharmProjects\\Coursera_Intro_Selenium_Project\\Automating-Web-Testing-with-Selenium-and-Python\\Screenshots"

try:
    # Wait until an element with id='myNewInput' has class 'myCSSClass'
    wait = WebDriverWait(driver, 10)
    btn1 = wait.until(element_has_css_class((By.ID, 'john'), "", "", "john"))
    # btn1 = driver.find_element(By.ID, "john")
    ActionChains(driver).move_to_element(btn1).click().perform()
    time.sleep(2)
    btn2 = wait.until(element_has_css_class((By.ID, 'doe'), "", "", "doe"))
    # btn2 = driver.find_element(By.ID, "doe")
    ActionChains(driver).move_to_element(btn2).click().perform()
    time.sleep(2)
    btnAll = wait.until(element_has_css_class((By.ID, 'display_all'), "", "", "display_all"))
    # btnAll = driver.find_element(By.ID, "display_all")
    ActionChains(driver).move_to_element(btnAll).click().perform()
    time.sleep(2)

    driver.delete_all_cookies()
    time.sleep(2)

    cookies = driver.get_cookies()
    for cookie in cookies:
        print(f"cookie: {cookie['name']}")

except Exception as e:
    print("error found: ", e)
finally:
    driver.quit()
