from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

# open table in page web
driver.get(
    "http://localhost:63343/Coursera_Intro_Selenium_Project/Automating-Web-Testing-with-Selenium-and-Python/Pages-HTML/section_3/31Demo.html?_ijt=bv835l51jn5qmeampphpde896o&_ij_reload=RELOAD_ON_SAVE")
screenshot_dir = "C:\\Users\\chaker\\PycharmProjects\\Coursera_Intro_Selenium_Project\\Automating-Web-Testing-with-Selenium-and-Python\\Screenshots"
try:
    demo = driver.find_element(By.ID, "demo")
    driver.execute_script("document.body.style.zoom='1.5'")
    driver.execute_script("arguments[0].innerHTML='saisir un texte içi'", demo)
    print("text saisi avec succès")
    driver.save_screenshot(f"{screenshot_dir}/31_inject_js_code.png")
finally:
    driver.quit()
