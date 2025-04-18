from BasePage import BasePage


class HomePage(BasePage):
    """
        Home page of Python.org
    """

    def __init__(self, driver):
        super().__init__(driver)
        # open the page home
        self.driver.get("https://www.python.org")


class AboutPage(BasePage):
    """
        About page of Python.org
    """

    def __init__(self, driver):
        super().__init__(driver)
        # open the page about
        self.driver.get("https://www.python.org/about/")
