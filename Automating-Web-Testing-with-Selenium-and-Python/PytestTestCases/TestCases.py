import logging
import os
import time
import unittest

import pytest
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

logging.basicConfig()
log = logging.getLogger("DummyLogger")


# logging.basicConfig(level=logging.DEBUG)
# mylogger = logging.getLogger()

@pytest.fixture(scope="class")
def setUp(request):
    print("WebDriver initialized")
    driver = webdriver.Chrome()
    request.cls.driver = driver
    yield
    driver.quit()
    print("WebDriver closed")


def is_local_env():
    if os.getenv("ENVIRONMENT") == "local":
        return True
    return False


def get_os_env():
    env = os.getenv("ENVIRONMENT")
    if env is None:
        raise OSError("Local Environment variable ENVIRONMENT not set")
    return env.lower()


class test_ENVIRONMENT(unittest.TestCase):
    # TC000: verify ENVIRONMENT setenv
    def test_environment(self):
        result = is_local_env()
        assert result == True
        env = get_os_env()
        print("Environment Test Passed ===> " + env)


@pytest.mark.usefixtures("setUp")
class test_CasesPythonOrg(unittest.TestCase):
    driver: webdriver.Chrome

    # TC001: Verify Python 3 Docs button
    def test_VerifyPython3DocsButton(self):
        browser = self.driver
        browser.get("http://www.python.org")
        element_to_hover_over = browser.find_element(By.XPATH, "//*[@id='documentation']/a")
        actionChains = ActionChains(browser)
        hover = actionChains.move_to_element(element_to_hover_over)
        hover.perform()
        wait = WebDriverWait(browser, 10)
        wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='documentation']/ul/li[10]/p[2]/a"))).click()
        time.sleep(3)
        assert browser.current_url == "https://docs.python.org/3/"
        print("TC001: redirected to correct page Python 3 Docs passed")

    # TC002: Search - no results found
    def test_SearchNoResultsFound(self):
        browser = self.driver
        browser.get("http://www.python.org")
        search_input = browser.find_element(By.NAME, "q")
        search_input.click()
        search_input.send_keys('blahblah')
        searchBtn = browser.find_element(By.CLASS_NAME, "search-button")
        if searchBtn.is_enabled():
            searchBtn.click()
        time.sleep(3)
        wait = WebDriverWait(browser, 10)
        search_results = wait.until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="content"]/div/section/form/ul')))
        assert search_results.text == "No results found."
        print("TC002: Search - no results found passed")

    def test_UpcomingEventsSectionPresentInAboutPage(self):
        browser = self.driver
        browser.get("http://www.python.org")
        About = browser.find_element(By.XPATH, "//*[@id='about']/a")
        About.click()
        time.sleep(3)
        wait = WebDriverWait(browser, 10)
        UpcomingEventsSection = wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'event-widget')))
        assert "Upcoming Events" in UpcomingEventsSection.text
        print("TC003: Upcoming Events section is present in about page passed")


if __name__ == "__main__":
    unittest.main()
