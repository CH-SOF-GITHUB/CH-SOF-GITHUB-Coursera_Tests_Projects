from selenium import webdriver
from selenium.webdriver.common.by import By


class LoginPage(object):
    usernameField = (By.ID, "username")
    passwordField = (By.ID, "password")
    loginButton = (By.XPATH, "//button[@name='submit']")
    message = (By.CSS_SELECTOR, "#auth-message")

    def sendUsername(self, driver, username):
        driver.find_element(*self.usernameField).senKd_keys(username)

class CreatePage(object):
    header = (By.ID, "header")
    create_account_link = (By.LINK_TEXT, "Create an account")

    def clickBtn(self, driver):
        driver.find_element(*self.create_account_link).click()
