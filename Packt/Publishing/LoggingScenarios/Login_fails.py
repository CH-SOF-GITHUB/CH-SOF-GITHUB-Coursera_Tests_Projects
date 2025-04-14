import logging
import time

from selenium import webdriver

from PageFactory import LoginPage

# Configuration de base pour logging
logging.basicConfig(
    level=logging.INFO,  # Niveau de log (INFO, DEBUG, WARNING, etc.)
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"  # Format des logs
)

# create a new instance of the Chrome driver
driver = webdriver.Chrome()
log = logging.getLogger(__name__)
if driver:
    # open the login page
    driver.get(
        "http://localhost:63343/Coursera_Intro_Selenium_Project/Packt/Publishing/LoggingScenarios/index.html?_ijt=e02rhfdci6umcul7anto0gqnu8")
    log.info("Login Page opened !")
    # maximize the window
    driver.maximize_window()
    # wait for 3 seconds for the page to load
    time.sleep(3)
    # find the username field
    username = driver.find_element(*LoginPage.usernameField)
    # find the password field
    password = driver.find_element(*LoginPage.passwordField)
    # find the login button
    loginButton = driver.find_element(*LoginPage.loginButton)
    # send credentials authentication
    username.send_keys("User")
    password.send_keys("1234")
    # click the login button
    loginButton.click()
    # wait for 3 seconds for the page to load
    time.sleep(3)
    actual_message = None
    try:
        actual_message = driver.find_element(*LoginPage.message)
        log.info("message auth is displayed")
    except Exception as e:
        log.warning("error auth message: %s", e)
    assert actual_message.text == "Account not found. Please sign up by clicking the link below", "not the same of expected message"
    # close the browser
    driver.quit()
else:
    log.warning("Driver not found")
