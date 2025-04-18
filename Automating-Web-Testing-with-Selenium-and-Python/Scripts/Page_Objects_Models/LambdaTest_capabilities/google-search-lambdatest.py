import os

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

"""
    LambdaTest selenium automation sample example
    Configuration
    ----------
    username: Username can be found at automation dashboard
    accessToken:  AccessToken can be generated from automation dashboard or profile section

    Result
    -------
    Execute Test on lambdatest Distributed Grid perform selenium automation based
"""

# google-search-lambdatest.py

# username: Username can be found at automation dashboard
username = os.getenv("LT_USERNAME")
# accessToken:  AccessToken can be generated from automation dashboard or profile section
accessToken = os.getenv("LT_ACCESS_KEY")
# gridUrl: gridUrl can be found at automation dashboard
gridUrl = "hub.lambdatest.com/wd/hub"

# Configuration des options Chrome
chrome_options = webdriver.ChromeOptions()
chrome_options.set_capability('browserName', 'Chrome')
chrome_options.set_capability('browserVersion', 'latest')
chrome_options.set_capability('LT:Options', {
    "build": "lambdaTest with python and selenium 4",
    "name": "Google Search LambdaTest",
    "platformName": "Windows 10"
})

# URL pour LambdaTest
url = "https://" + username + ":" + accessToken + "@" + gridUrl

"""
    ----------
    platformName : Supported platform - (Windows 10, Windows 8.1, Windows 8, Windows 7,  macOS High Sierra, macOS Sierra, OS X El Capitan, OS X Yosemite, OS X Mavericks)
    browserName : Supported platform - (chrome, firefox, Internet Explorer, MicrosoftEdge)
    browserVersion :  Supported list of version can be found at https://www.lambdatest.com/capabilities-generator/

    Result
    -------
"""

driver = webdriver.Remote(
    command_executor=url,
    options=chrome_options
)

"""
	----------
	Execute test:  navigate google.com search LambdaTest
	Result
	----------
	print title
"""
# Attendre que le champ de recherche soit visible et interactif
try:
    driver.get("https://www.bstackdemo.com/")
    print("Searching lambdatest on bstackdemo.com ")
    SignInBtn = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//*[@id='__next']/div/div/div[1]/div/div/div[2]/nav")))
    SignInBtn.click()
    print("Printing title of current page :" + driver.title)
    driver.execute_script("lambda-status=passed")
    print("Requesting to mark test : pass")
except Exception as e:
    print(f"Error: {e}")
    driver.execute_script("lambda-status=failed")
finally:
    # Quitter le driver
    driver.quit()
