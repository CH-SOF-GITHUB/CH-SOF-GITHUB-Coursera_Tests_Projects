import time

from selenium import webdriver

driver = webdriver.Chrome()

driver.get(
    "http://localhost:63343/Coursera_Intro_Selenium_Project/Automating-Web-Testing-with-Selenium-and-Python/Pages-HTML/section_3/cookies.html?_ijt=fac0grvlbftq9s1ndpckc0jd05&_ij_reload=RELOAD_ON_SAVE")
screenshot_dir = "C:\\Users\\chaker\\PycharmProjects\\Coursera_Intro_Selenium_Project\\Automating-Web-Testing-with-Selenium-and-Python\\Screenshots"

try:
    cookies = driver.get_cookies()
    print("Cookies avant suppression :")
    for cookie in cookies:
        print("cookie: " + cookie['name'])

    driver.delete_cookie("Pycharm-4bbf0bf2")
    time.sleep(2)

    # refresh
    driver.refresh()
    time.sleep(2)

    cookies = driver.get_cookies()
    print("Cookies aprés suppression :")
    time.sleep(3)
    for cookie in cookies:
        print("cookie: " + cookie['name'])

    driver.save_screenshot(f"{screenshot_dir}/allCookies.png")
finally:
    driver.quit()
