import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service


@pytest.fixture()
def browser():
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_experimental_option("detach", True)
    g = Service()
    driver = webdriver.Chrome(options=options, service=g)
    driver.maximize_window()
    return driver


def test_button(browser):
    browser.get("https://www.qa-practice.com/elements/button/simple")
    assert browser.find_element(By.ID, 'submit-id-submit').is_displayed()


def test_button_second(browser):
    browser.get("https://www.qa-practice.com/elements/button/like_a_button")
    assert browser.find_element(By.PARTIAL_LINK_TEXT, 'Click').is_displayed()

