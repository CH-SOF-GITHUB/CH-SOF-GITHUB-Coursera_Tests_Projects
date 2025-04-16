from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from Class.element_has__attribute import element_has_css_class

browser = webdriver.Chrome()

# open the page html
browser.get(
    "http://localhost:63343/Coursera_Intro_Selenium_Project/Automating-Web-Testing-with-Selenium-and-Python/Pages-HTML/25_radio_buttons.html?_ijt=c29r0id9tjtrk8i8cs5iepoq5v&_ij_reload=RELOAD_ON_SAVE")

# verify if the directory of screenshot exist, if not create it
screenshot_dir = "C:\\Users\\chaker\\PycharmProjects\\Coursera_Intro_Selenium_Project\\Automating-Web-Testing-with-Selenium-and-Python\\Screenshots"

# Explicit Wait for locate elements
try:
    # Localisateur et classe CSS
    # Wait until an element with id='myNewInput' has class 'myCSSClass'
    wait = WebDriverWait(browser, 10)
    print("Attente de l'élément avec name='gender' et la classe CSS 'gender'...")
    element = wait.until(element_has_css_class((By.NAME, 'gender'), "gender"))
    print(f"Element trouvé avec la valeur : {element.get_attribute('value')}")
    browser.save_screenshot(f"{screenshot_dir}/explicit_wait_28.png")
except TimeoutException:
    print("Erreur : L'élément n'a pas été trouvé dans le délai imparti.")
finally:
    browser.quit()
