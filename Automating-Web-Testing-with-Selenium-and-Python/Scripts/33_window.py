import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('http://python.org')
time.sleep(1)
driver.maximize_window()
driver.find_element(By.CSS_SELECTOR, 'a[title="Python Package Index"]').click()
time.sleep(1)
driver.back()
time.sleep(1)
driver.close()
