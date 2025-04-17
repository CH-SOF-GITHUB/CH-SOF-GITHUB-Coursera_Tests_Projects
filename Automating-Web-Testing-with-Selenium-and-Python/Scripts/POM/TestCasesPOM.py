import time
import unittest

from selenium import webdriver

from BasePageObject import AboutPage
from BasePageObject import HomePage
from Locators import AboutPageLocators
from Locators import HomePageLocators
from Locators import SearchPageLocators


class TestPyOrgBase(unittest.TestCase):
    """
        TBD
    """

    def setUp(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('window-size=1920x1080')
        self.driver = webdriver.Chrome(options=chrome_options)

    def tearDown(self):
        if self.driver is not None:
            self.driver.quit()


class TestCases001And002(TestPyOrgBase):
    """
        TBD
    """

    def setUp(self):
        super().setUp()
        self.home = HomePage(self.driver)

    # TC001: Verify Python 3 Docs button
    def test_TC0O1(self, status="failed"):
        self.status = status
        self.home.to_hover(HomePageLocators.DOCUMENTATION_TO_HOVER)
        self.home.clickBtn(HomePageLocators.PYTHON3_BUTTON)
        # wait for 3 s to load a page response
        time.sleep(3)
        assert self.driver.current_url == "https://docs.python.org/3/"
        status = "passed"
        print("TC001: Verify Python 3 Docs button with status: " + status)

    # TC002: Search - no results found
    def test_TC002(self, status="failed"):
        self.status = status
        # Utiliser le bon localisateur pour le champ de recherche
        self.home.search_for(HomePageLocators.SEARCH_BAR, HomePageLocators.GO_BUTTON, "blahblah")
        # Attendre 3 secondes pour le chargement de la réponse
        time.sleep(3)
        self.home.assert_elem_text(SearchPageLocators.SEARCH_RESULT, "No results found.")
        status = "passed"
        print("TC002: Search - no results found with status: " + status)


class TestTC003(TestPyOrgBase):

    def setUp(self):
        super().setUp()
        self.about = AboutPage(self.driver)

    # TC003: Upcoming Events section present in About page
    def test_TC003(self, status="failed"):
        self.status = status
        # self.about.clickAboutBtn(AboutPageLocators.ABOUT_BUTTON)
        # Attendre 3 secondes pour le chargement de la réponse
        time.sleep(3)
        assert self.driver.current_url == "https://www.python.org/about/"
        self.about.assert_Upcoming_Events_text(AboutPageLocators.UPCOMING_EVENTS_SECTION, "Upcoming Events")
        status = "passed"
        print("TC003: Upcoming Events section present in About page with status: " + status)



if __name__ == '__main__':
    unittest.main()
