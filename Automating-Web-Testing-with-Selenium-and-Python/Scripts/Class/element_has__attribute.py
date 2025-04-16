class element_has_css_class(object):
    """An expectation for checking that an element has a particular css class.

    locator - used to find the element
    returns the WebElement once it has the particular css class
    """

    def __init__(self, locator, name, classe, Id):
        self.locator = locator
        self.name = name
        self.classe = classe
        self.id = Id

    def __call__(self, driver):
        element = driver.find_element(*self.locator)  # Finding the referenced element
        if self.name == element.get_attribute("name") or self.classe == element.get_attribute("class") or self.id == element.get_attribute("id"):
            return element
        else:
            return False
