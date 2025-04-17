from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    """
        Base Page class that hold common elements
        and functionalities to all pages in app
    """

    def __init__(self, driver):
        self.driver = driver

    def clickBtn(self, by_locator):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(by_locator)).click()

    # Verify that is present
    def verifyPresentElement(self, by_locator):
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(by_locator))

    def to_hover(self, by_locator):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        ActionChains(self.driver).move_to_element(element).perform()

    def assert_elem_text(self, by_locator, expectedText):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        assert element.text == expectedText

    def search_for(self, by_locator_search, by_locator_go, search_text):
        search_input = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator_search))
        search_input.send_keys(search_text)
        btn_go = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(by_locator_go))
        btn_go.click()
