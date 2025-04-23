from selenium.webdriver import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class PageFactory:

    def __init__(self, driver):
        self.driver = driver

    def openPage(self, url):
        self.driver.get(url)

    def find(self, by_locator):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.visibility_of_element_located(by_locator))

    def assert_text(self, by_locator, text):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.visibility_of_element_located(by_locator))
        print(f"Texte trouvé : '{element.text}', Texte attendu : '{text}'")  # Débogage
        assert element.text == text, f"Texte attendu '{text}', mais trouvé '{element.text}'"

    def to_type(self, by_locator, text):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.visibility_of_element_located(by_locator))
        element.clear()
        element.send_keys(text)

    def take_screenshot(self, filename):
        self.driver.save_screenshot(f"C:\\Users\\chaker\\PycharmProjects\\Coursera_Intro_Selenium_Project\\Automating-Web-Testing-with-Selenium-and-Python\\orangehrm-testing-suite\\results\\{filename}")

    def exists_element(self, by_locator):
        wait = WebDriverWait(self.driver, 10)
        elem = wait.until(EC.presence_of_element_located(by_locator))
        assert elem.is_enabled()

    def to_click(self, by_locator):
        wait = WebDriverWait(self.driver, 10)
        button = wait.until(EC.element_to_be_clickable(by_locator))
        button.click()

    def get_element_text(self, by_locator):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.visibility_of_element_located(by_locator))
        return element.text

    def getErrorMsg(self, by_locator):
        wait = WebDriverWait(self.driver, 10)
        errorMsg = wait.until(EC.presence_of_element_located(by_locator))
        return errorMsg.text
