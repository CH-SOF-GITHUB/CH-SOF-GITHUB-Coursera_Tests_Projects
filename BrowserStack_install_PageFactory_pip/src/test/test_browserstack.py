import time

from selenium import webdriver

from BrowserStack_PageFactory_pip.src.pages.homepage import Homepage
from BrowserStack_PageFactory_pip.src.pages.sign_in_page import SignInPage


def test_browserstack():
    """
    Test the BrowserStack_install_PageFactory_pip functionality.
    """
    driver = webdriver.Chrome()
    # open the browserstack page
    driver.get("https://www.bstackdemo.com/")
    # create a new instance from classes HomePage and SignInPage
    homePage = Homepage(driver)
    signInPage = SignInPage(driver)
    # maximize the window
    driver.maximize_window()
    # wait for 3 seconds for the page to load
    time.sleep(3)
    homePage.click_sign_in()
    # enter credentials and click the login button
    signInPage.select_username()
    signInPage.select_password()
    signInPage.click_login()
    # wait for 3 seconds for the page to load
    time.sleep(3)
    # check if login the username correct
    homePage.get_username()
    print("Browser Stack Test Passed")
    # close the browser
    driver.quit()


if __name__ == "__main__":
    test_browserstack()
