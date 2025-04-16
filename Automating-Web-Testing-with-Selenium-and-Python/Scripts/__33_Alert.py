import time

from selenium import webdriver
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get(
    "http://localhost:63343/Coursera_Intro_Selenium_Project/Automating-Web-Testing-with-Selenium-and-Python/Pages-HTML/section_3/33_prompt_test.html?_ijt=alacpu8rn28m6ajp5cpr5ebrgp&_ij_reload=RELOAD_ON_SAVE")

try:
    # WebDriverWait(driver, 10).until(EC.alert_is_present())
    confirm_alert = Alert(driver)
    confirm_alert.accept()
    time.sleep(2)

    # WebDriverWait(driver, 10).until(EC.alert_is_present())
    prompt_alert = Alert(driver)
    prompt_alert.send_keys("Willian Shakesphere")  # Envoyer le texte
    prompt_alert.accept()
    time.sleep(2)

    # Vérifier le résultat
    result = driver.find_element(By.ID, "result").text
    print(f"Résultat affiché : {result}")
finally:
    driver.quit()
