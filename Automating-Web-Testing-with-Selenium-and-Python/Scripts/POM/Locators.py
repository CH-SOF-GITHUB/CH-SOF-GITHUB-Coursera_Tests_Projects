from selenium.webdriver.common.by import By


class HomePageLocators:
    DOCUMENTATION_TO_HOVER = (By.XPATH, "//*[@id='documentation']/a")
    PYTHON3_BUTTON = (By.XPATH, "//*[@id='documentation']/ul/li[10]/p[2]/a")
    SEARCH_BAR = (By.NAME, "q")
    GO_BUTTON = (By.CLASS_NAME, "search-button")


class SearchPageLocators:
    SEARCH_RESULT = (By.XPATH, "//*[@id='content']/div/section/form/ul")


class AboutPageLocators:
    ABOUT_BUTTON = (By.XPATH, "//*[@id='about']/a")
    UPCOMING_EVENTS_SECTION = (By.CLASS_NAME, 'event-widget')
