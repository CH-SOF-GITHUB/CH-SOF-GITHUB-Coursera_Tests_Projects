from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from Class.element_has__attribute import element_has_css_class

driver = webdriver.Chrome()
# verify if the directory of screenshot exist, if not create it
screenshot_dir = "C:\\Users\\chaker\\PycharmProjects\\Coursera_Intro_Selenium_Project\\Automating-Web-Testing-with-Selenium-and-Python\\Screenshots"

try:
    driver.get(
        "http://localhost:63343/Coursera_Intro_Selenium_Project/Automating-Web-Testing-with-Selenium-and-Python/Pages-HTML/24_clickable_dropdown.html?_ijt=g95t4krj1qoeeh34cic19mpeke&_ij_reload=RELOAD_ON_SAVE")
    # Wait until an element with id='myNewInput' has class 'myCSSClass'
    print("Attente de l'élément avec class='dropbtn'")
    wait = WebDriverWait(driver, 10)
    element = wait.until(element_has_css_class((By.CLASS_NAME, 'dropbtn'), "", "dropbtn"))
    element.click()
    print("button dropdown clicked")
    driver.save_screenshot(f"{screenshot_dir}/24_dropbtn.png")
    driver.execute_script("document.body.style.zoom = '1.5'")
    driver.save_screenshot(f"{screenshot_dir}/24_dropbtn_zoom1.5.png")
finally:
    # close the browser
    driver.quit()
