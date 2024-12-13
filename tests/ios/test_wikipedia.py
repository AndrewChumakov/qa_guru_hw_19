import allure
import pytest
from appium.webdriver.common.appiumby import AppiumBy
from selene import have, browser


def test_search(mobile):
    if mobile == "android":
        pytest.skip("Test android")
    with allure.step("Input text"):
        browser.element((AppiumBy.ACCESSIBILITY_ID, "Text Button")).click()
        browser.element((AppiumBy.ACCESSIBILITY_ID, "Text Input")).send_keys("Algebra\n")
    with allure.step("Verify content found"):
        browser.element((AppiumBy.ACCESSIBILITY_ID, "Text Output")).should(have.text("Algebra"))
