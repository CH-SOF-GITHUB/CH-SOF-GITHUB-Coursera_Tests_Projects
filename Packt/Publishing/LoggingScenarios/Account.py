import logging
import time

from selenium import webdriver

from PageFactory import CreatePage

# Configuration de base pour logging
logging.basicConfig(
    level=logging.INFO,  # Niveau de log (INFO, DEBUG, WARNING, etc.)
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"  # Format des logs
)
# create a new instance of logging
log = logging.getLogger(__name__)

# create a new instance of the Chrome driver
driver = webdriver.Chrome()
create_page = CreatePage()
if driver:
    # open the login page
    driver.get(
        "http://localhost:63343/Coursera_Intro_Selenium_Project/Packt/Publishing/LoggingScenarios/index.html?_ijt=qo2m8qd428fg2g0hll0koremhf")
    log.info("page opened !")
    # maximize the window
    driver.maximize_window()
    # wait for 3 seconds for the page to load
    time.sleep(3)
    # click the create account link
    create_page.clickBtn(driver)
    log.info("create account link clicked !")
    # wait for 3 seconds for the page to load
    time.sleep(3)
    # verify the header text with expected value
    header = None
    try:
        header = driver.find_element(*CreatePage.header)
    except Exception as e:
        log.error("Error header : ", e)
    assert header.text == "Create an Account", "Expected Header text does not match"
    log.info("Test link create account passed with success")
    # close the browser
    driver.quit()
else:
    log.error("Web driver not found")
