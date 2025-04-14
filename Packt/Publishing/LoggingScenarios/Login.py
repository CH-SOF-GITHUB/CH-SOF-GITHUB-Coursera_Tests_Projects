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
        "http://localhost:63343/Coursera_Intro_Selenium_Project/Packt/Publishing/LoggingScenarios/index.html?_ijt=8a0d8nbb85m7bug0401gldfba")
    log.info("page opened !")
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
    username.send_keys("registeredUser")
    password.send_keys("1234")
    # click the login button
    loginButton.click()
    # wait for 3 seconds for the page to load
    time.sleep(3)
    actual_message = driver.find_element(*LoginPage.message).text
    expected_message = "Welcome back,\nregisteredUser"
    assert expected_message == actual_message, f"Expected : '{expected_message}', but got: '{actual_message}'"
    log.info("login passed with success")
    # close the browser
    driver.quit()
else:
    print("Driver not found")
