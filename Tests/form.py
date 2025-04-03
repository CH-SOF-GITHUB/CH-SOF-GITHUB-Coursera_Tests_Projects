import os.path
import time

from selenium import webdriver
from selenium.webdriver.common.by import By


def loginTest():
    # create a new chrome browser instance
    driver = webdriver.Chrome()
    # navigate to the-internet web site login
    driver.get("https://the-internet.herokuapp.com/login")
    # make the browser window full screen
    driver.maximize_window()
    # wait for 3 seconds
    time.sleep(3)
    # Find the usernameField and enter the 'tomsmith'
    usernameField = driver.find_element(By.XPATH, "//*[@id='username']")
    usernameField.send_keys("tomsmith")
    # Find the passwordField and enter the 'SuperSecretPassword!'
    passwordField = driver.find_element(By.XPATH, "//*[@id='password']")
    passwordField.send_keys("SuperSecretPassword!")
    # Find the login button and click it
    LoginBtn = driver.find_element(By.XPATH, "//*[@id='login']/button")
    LoginBtn.click()
    # Log and Check if login was successful
    """
    • Advanced Logging: Use logging libraries to record detailed execution logs.
    • Screenshot Captures: Take screenshots at critical steps or upon errors.
    • Exception Handling: Enhance error handling to make the script more robust.
    """
    try:
        successMessage = driver.find_element(By.CSS_SELECTOR, ".flash.success")
        print("Successfully logged in")
        driver.save_screenshot(os.path.join("Bugs", "login_success.png"))
    except Exception as e:
        print("Failed to log in", e)
        driver.save_screenshot(os.path.join("Bugs", "login_failure.png"))

    # wait for 2 s after clicking to page respond
    time.sleep(2)
    # close the browser
    driver.quit()


if __name__ == '__main__':
    loginTest()
