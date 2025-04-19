import base64
import os

import pytest
import pytest_html
from pytest_metadata.plugin import metadata_key
from selenium import webdriver


@pytest.fixture(scope="class")
def setUp(request):
    driver = webdriver.Chrome()
    request.cls.driver = driver
    yield driver
    driver.quit()


def pytest_html_report_title(report):
    report.title = "Pytest HTML Report Example"


def pytest_configure(config):
    config.stash[metadata_key]["Project"] = "Pytest With Eric"


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, "extras", [])
    if report.when == "call":
        # Assuming your screenshot is saved correctly at the specified path
        screenshot_path = "C:\\Users\\chaker\\PycharmProjects\\Coursera_Intro_Selenium_Project\\Automating-Web-Testing-with-Selenium-and-Python\\PytestTestCases\\SCREENSHOT\\test_screenshot.png"
        if os.path.exists(screenshot_path):
            with open(screenshot_path, "rb") as image_file:
                encoded_string = base64.b64encode(image_file.read()).decode()
            extra.append(pytest_html.extras.png(encoded_string))
        else:
            print(f"Screenshot not found at {screenshot_path}")
        report.extras = extra
