import os
import time
import unittest

from selenium import webdriver

from BasePageObject import AboutPage
from BasePageObject import HomePage
from Locators import AboutPageLocators
from Locators import HomePageLocators
from Locators import SearchPageLocators


class PyOrgFirefoxTestBase(unittest.TestCase):
    def setUp(self):
        # username: Username can be found at automation dashboard
        username = os.getenv("LT_USERNAME")
        # accessToken:  AccessToken can be generated from automation dashboard or profile section
        accessToken = os.getenv("LT_ACCESS_KEY")
        # gridUrl: gridUrl can be found at automation dashboard
        gridUrl = "hub.lambdatest.com/wd/hub"

        # Configuration des options Firefox
        firefox_options = webdriver.FirefoxOptions()
        firefox_options.set_capability('browserName', 'Firefox')
        firefox_options.set_capability('browserVersion', 'latest')
        firefox_options.set_capability('LT:Options', {
            "build": "lambdaTest build firefox with python and selenium 4",
            "name": "firefox python 3 tests",
            "platformName": "Windows 10"
        })

        # URL pour LambdaTest
        url = "https://" + username + ":" + accessToken + "@" + gridUrl
        self.driver = webdriver.Remote(
            command_executor=url,
            options=firefox_options
        )

    def tearDown(self):
        if self.driver is not None:
            self.driver.quit()


class TestCasesFirefox001002003(PyOrgFirefoxTestBase):
    def setUp(self):
        super().setUp()
        self.home = HomePage(self.driver)

    # TC001: Verify Python 3 Docs button
    def test_TC0O1(self, status="failed"):
        self.status = status
        self.home.to_hover(HomePageLocators.DOCUMENTATION_TO_HOVER)
        # verify that Python 3 Docs button is present
        assert self.home.verifyPresentElement(
            HomePageLocators.PYTHON3_BUTTON), "Python 3 Docs button not found on the page"
        self.home.clickBtn(HomePageLocators.PYTHON3_BUTTON)
        # wait for 3 s to load a page response
        time.sleep(3)
        assert self.driver.current_url == "https://docs.python.org/3/"
        status = "passed"
        print("TC001: firefox-Verify Python 3 Docs button with status: " + status)

    # TC002: Search - no results found
    def test_TC002(self, status="failed"):
        self.status = status
        # Utiliser le bon localisateur pour le champ de recherche
        self.home.search_for(HomePageLocators.SEARCH_BAR, HomePageLocators.GO_BUTTON, "blahblah")
        # Attendre 3 secondes pour le chargement de la réponse
        time.sleep(3)
        self.home.assert_elem_text(SearchPageLocators.SEARCH_RESULT, "No results found.")
        status = "passed"
        print("TC002: firefox-Search - no results found with status: " + status)

    # TC003: Verify correct url of page Home
    def test_TC003(self, status="failed"):
        self.status = status
        assert self.driver.current_url == "https://www.python.org/"
        status = "passed"
        print("TC003: firefox-Url Home page with status: " + status)


class TestCasesFirefox004005(PyOrgFirefoxTestBase):
    def setUp(self):
        super().setUp()
        self.about = AboutPage(self.driver)

    # TC004: Upcoming Events section present in About page
    def test_TC004(self, status="failed"):
        self.status = status
        # Attendre 3 secondes pour le chargement de la réponse
        time.sleep(3)
        # Verify Upcoming Events section is present
        assert self.about.verifyPresentElement(
            AboutPageLocators.UPCOMING_EVENTS_SECTION), "Upcoming events section not found in this page"
        self.about.assert_Upcoming_Events_text(AboutPageLocators.UPCOMING_EVENTS_SECTION, "Upcoming Events")
        status = "passed"
        print("TC004: firefox-Upcoming Events section present in About page with status: " + status)

    # TC005: Verify the title  of page home
    def test_TC005(self, status="failed"):
        self.status = status
        self.assertEqual(self.driver.title, "About Python™ | Python.org")
        status = "passed"
        print("TC005: firefox-Title about page with status: " + status)


if __name__ == '__main__':
    unittest.main()
