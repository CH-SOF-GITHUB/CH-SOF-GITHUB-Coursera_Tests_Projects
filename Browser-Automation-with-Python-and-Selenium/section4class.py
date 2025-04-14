from selenium.webdriver.common.by import By


class Training_ground:
    def __init__(self, driver, url):
        self.name = "Section 4"
        self.description = "This section covers advanced browser automation techniques."
        self.driver = driver
        self.url = url

    def open(self):
        if not self.url.startswith(("http://", "https://")):
            raise ValueError(f"L'URL fournie est invalide : {self.url}")
        self.driver.get(self.url)
        print(f"Page opened with browser: {self.driver.name}")

    def execute_script(self, script):
        # execute a JavaScript script in the context of the currently selected frame or window
        self.driver.execute_script(script)
        print("new tab opened with browser: " + self.driver.name)

    def saisir_text_input(self, text):
        # locate the input field and enter text
        input_field = self.driver.find_element(By.ID, 'ipt1')
        input_field.send_keys(text)

    def get_input_value(self):
        # get the value of the input field
        input_field = self.driver.find_element(By.ID, 'ipt1')
        return input_field.get_attribute('value')

    def click_button1(self):
        # locate and click the button
        button = self.driver.find_element(By.ID, 'b1')
        button.click()
