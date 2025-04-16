from selenium import webdriver
from selenium.webdriver.support.abstract_event_listener import AbstractEventListener
from selenium.webdriver.support.event_firing_webdriver import EventFiringWebDriver


class MyListener(AbstractEventListener):
    def before_navigate_to(self, url, driver):
        print("Before navigate to %s" % url)

    def after_navigate_to(self, url, driver):
        print("After navigate to %s" % url)


driver = webdriver.Chrome()
try:
    ef_driver = EventFiringWebDriver(driver, MyListener())
    ef_driver.get("https://www.python.org/")
finally:
    driver.quit()
