import pytest
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.options.ios import XCUITestOptions
from dotenv import load_dotenv
from selene import browser
import os

from utils import attach


def pytest_addoption(parser):
    parser.addoption(
        "--platform",
        default="ios"
    )

@pytest.fixture(scope="session", autouse=True)
def load_env():
    load_dotenv()

@pytest.fixture(scope="function", autouse=True)
def mobile(request):
    platform = request.config.getoption("--platform")
    if platform == "android":
        options = android_options()
        browser.config.driver = webdriver.Remote(os.getenv("URL"), options=options)
    elif platform == "ios":
        options = ios_options()
        browser.config.driver = webdriver.Remote(os.getenv("URL"), options=options)
    else:
        return

    browser.config.timeout = float(os.getenv("timeout", "10.0"))

    yield platform

    attach.bstack_screenshot(browser)
    attach.bstack_page_source(browser)
    session_id = browser.driver.session_id
    browser.quit()
    attach.video(session_id)


def android_options():
    options = UiAutomator2Options().load_capabilities({
        "platformVersion": "12.0",
        "deviceName": "Samsung Galaxy S22 Plus",
        "platformName": "android",
        "app": "bs://sample.app",
        "bstack:options": {
            "projectName": "Mobile Project",
            "buildName": "build_android",
            "sessionName": "test_android",
            "userName": os.getenv("USER"),
            "accessKey": os.getenv("KEY")
        }
    })
    return options

def ios_options():
    options = XCUITestOptions().load_capabilities({
        "platformVersion": "14",
        "deviceName": "iPhone 11",
        "platformName": "ios",
        "app": "bs://sample.app",
        "bstack:options": {
            "projectName": "Mobile Project",
            "buildName": "build_ios",
            "sessionName": "test_ios",
            "userName": os.getenv("USER"),
            "accessKey": os.getenv("KEY")
        }
    })
    return options