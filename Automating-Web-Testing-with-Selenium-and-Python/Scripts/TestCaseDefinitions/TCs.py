import logging
import os
import time
import unittest

import xmlrunner
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

logging.basicConfig()
log = logging.getLogger("DummyLogger")


# unittest fournit une classe de base "TestCase" qui peut etre utilisée pour créer des nouveaux scénarios de test.
class TestCasesPythonOrg(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        # log.warning("declare Chrome browser")

    # TC001: Verify Python 3 Docs button
    def test_VerifyPython3DocsButton(self):
        # Go to python.org home page
        browser = self.driver
        browser.get("http://www.python.org")
        element_to_hover_over = browser.find_element(By.XPATH, "//*[@id='documentation']/a")
        # declare an ActionChains to automate low level mouse movements, mouse button actions
        actionChains = ActionChains(browser)
        # Hover the mouse over the Documentation link
        hover = actionChains.move_to_element(element_to_hover_over)
        hover.perform()
        # Verify that Python 3 Docs button is present
        wait = WebDriverWait(browser, 10)
        DocsBtn = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='documentation']/ul/li[10]/p[2]/a")))
        # Click on it and verify that we are redirected to correct page
        DocsBtn.click()
        # wait for 3 s to load a page response
        time.sleep(3)
        assert browser.current_url == "https://docs.python.org/3/"
        print("TC001: redirected to correct page Python 3 Docs passed")

    # TC002: Search - no results found
    def test_SearchNoResultsFound(self):
        browser = self.driver
        # 1. Go to python.org home page
        browser.get("http://www.python.org")
        # 2. Click to the search input text field
        search_input = browser.find_element(By.NAME, "q")
        search_input.click()
        # 3. Enter text 'blahblah'
        search_input.send_keys('blahblah')
        # 4. Click on search button
        searchBtn = browser.find_element(By.CLASS_NAME, "search-button")
        if searchBtn.is_enabled():
            searchBtn.click()
        # wait 3 s to load page response
        time.sleep(3)
        # 5. Verify that the 'No results found.' is displayed in Results section
        wait = WebDriverWait(browser, 10)
        search_results = wait.until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="content"]/div/section/form/ul')))
        assert search_results.text == "No results found."
        print("TC002: Search - no results found passed")

    def test_UpcomingEventsSectionPresentInAboutPage(self):
        browser = self.driver
        # 1. Go to python.org home page
        browser.get("http://www.python.org")
        # 2. Navigate to About page
        About = browser.find_element(By.XPATH, "//*[@id='about']/a")
        About.click()
        # wait for 3 s to load page response
        time.sleep(3)
        # 3. Verify Upcoming Events section is present
        wait = WebDriverWait(browser, 10)
        UpcomingEventsSection = wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'event-widget')))
        assert "Upcoming Events" in UpcomingEventsSection.text
        print("TC003: Upcoming Events section is present in about page passed")

    def tearDown(self):
        if self.driver is not None:
            self.driver.quit()
        # log.warning("driver closed")


if __name__ == "__main__":
    # Vérifiez si le dossier 'test-reports' existe, sinon créez-le
    report_path = 'test-reports'
    os.makedirs(report_path, exist_ok=True)
    print(f"Les rapports seront générés dans : {os.path.abspath(report_path)}")

    try:
        unittest.main(
            testRunner=xmlrunner.XMLTestRunner(output=report_path),
            failfast=False, buffer=False, catchbreak=False
        )
        # Vérifiez si les fichiers XML sont créés
        if os.path.exists(report_path):
            print(f"Le dossier de rapport a été créé : {report_path}")
            print(f"Fichiers générés : {os.listdir(report_path)}")
        else:
            print("Le dossier de rapport n'a pas été créé.")
    except Exception as e:
        print(f"Erreur lors de l'exécution des tests : {e}")

# logging.basicConfig(stream=sys.stderr)
# logging.getLogger("DummyLogger").setLevel(logging.INFO)
# unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='outputFolder', report_title='Dummy report title test'))
