import time
import unittest

from selenium import webdriver

from Locators import DashboardPageLocators
from Locators import LoginPageLocators
from Page import LoginPage


class TestBase(unittest.TestCase):
    def setUp(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('window-size=1920x1080')
        self.driver = webdriver.Chrome(options=chrome_options)

    def tearDown(self):
        if self.driver is not None:
            self.driver.quit()


class LoginOrangeHRM(TestBase):

    def setUp(self):
        super().setUp()
        self.loginPage = LoginPage(self.driver)

    def test_TC_L_001_Login_page_loaded(self, status=False):
        self.status = status
        # 1. Verify Login panel exists
        self.loginPage.assert_text(LoginPageLocators.panel_login_locator, "Login")
        # 2. Verify Username input field exists
        self.loginPage.exists_element(LoginPageLocators.username_locator)
        # 3. Verify Password field exists
        self.loginPage.exists_element(LoginPageLocators.password_locator)
        # 4. Verify Login button exists and enabled for clicking
        self.loginPage.exists_element(LoginPageLocators.login_btn_locator)
        # verify the expected results
        status = True
        if status:
            print("TC_L_001: Login page loaded passed")
            self.loginPage.take_screenshot('load-login.png')
            # self.driver.save_screenshot('C:\\Users\\chaker\\PycharmProjects\\Coursera_Intro_Selenium_Project\\Automating-Web-Testing-with-Selenium-and-Python\\orangehrm-testing-suite\\results\\load-login.png')

    def test_TC_L_002_Successful_login(self, status=False):
        self.status = status
        # 1. Enter user name Admin in the username field
        self.loginPage.to_type(LoginPageLocators.username_locator, 'Admin')
        # 2. Enter password admin123 in password field
        self.loginPage.to_type(LoginPageLocators.password_locator, 'admin123')
        # 3. Click on the Login button
        self.loginPage.to_click(LoginPageLocators.login_btn_locator)
        # 4. Verify correct redirection to Dashboard - correct url
        assert self.driver.current_url == "https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index"
        # 5. Verify that Dashboard is loaded
        # Dashboard = self.loginPage.get_element_text(DashboardPageLocators.dashboard_text_locator)
        for i in range(60):
            try:
                if "Dashboard" == self.loginPage.get_element_text(DashboardPageLocators.dashboard_text_locator):
                    status = True
                    break
            except:
                pass
            time.sleep(1)
        else:
            self.fail("time out")
        print("TC_L_002: Successful login with status: ", status)
        self.loginPage.take_screenshot('login-success.png')

    def test_TC_L_003_Failed_login(self, status=True):
        self.status = status
        # 1. Enter user name Admin in the username field
        self.loginPage.to_type(LoginPageLocators.username_locator, 'Admin')
        # 2. Enter passerod password in password field
        self.loginPage.to_type(LoginPageLocators.password_locator, 'admin')
        # 3. Click in Login button
        self.loginPage.to_click(LoginPageLocators.login_btn_locator)
        # 4. Verify the correct message is displayed
        for i in range(60):
            try:
                if "Invalid credentials" in self.loginPage.getErrorMsg(LoginPageLocators.alert_content_error_locator):
                    status = False
                    break
            except:
                pass
            time.sleep(1)
        else:
            self.fail("time out")
        print("TC_L_003	Failed login: ", status)
        self.loginPage.take_screenshot('login-fails.png')


if __name__ == '__main__':
    unittest.main()
