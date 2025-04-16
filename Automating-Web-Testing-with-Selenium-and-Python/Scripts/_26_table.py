from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

# open table in page web
driver.get("http://localhost:63343/Coursera_Intro_Selenium_Project/Automating-Web-Testing-with-Selenium-and-Python/Pages-HTML/26_table.html?_ijt=puv4bv9ij492mvenpmtnqev03r&_ij_reload=RELOAD_ON_SAVE")
screenshot_dir = "C:\\Users\\chaker\\PycharmProjects\\Coursera_Intro_Selenium_Project\\Automating-Web-Testing-with-Selenium-and-Python\\Screenshots"
try:
    driver.find_element(By.XPATH, "//*[text()='Apple']/preceding-sibling::td/input").click()
    driver.execute_script("document.body.style.zoom='1.5'")
    driver.save_screenshot(f"{screenshot_dir}/table.png")
finally:
    driver.quit()