import allure
import pytest
from appium.webdriver.common.appiumby import AppiumBy
from selene import have, browser


def test_open(mobile):
    if mobile == "ios":
        pytest.skip("Test android")
    with allure.step("Type search"):
        browser.element((AppiumBy.ACCESSIBILITY_ID, "Search Wikipedia")).click()
        browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/search_src_text")).type("Appium")
    with allure.step("Verify content found"):
        results = browser.all((AppiumBy.ID, "org.wikipedia.alpha:id/page_list_item_title"))
        results.first.should(have.text("Appium"))
    with allure.step("Open content"):
        results.first.click()

def test_search(mobile):
    if mobile == "ios":
        pytest.skip("Test android")
    with allure.step("Type search"):
        browser.element((AppiumBy.ACCESSIBILITY_ID, "Search Wikipedia")).click()
        browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/search_src_text")).type("Algebra")
    with allure.step("Verify content found"):
        results = browser.all((AppiumBy.ID, "org.wikipedia.alpha:id/page_list_item_title"))
        results.should(have.size_greater_than(0))
        results.first.should(have.text("Algebra"))
