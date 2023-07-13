from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import TestLocators
from helpers import login

class TestLogout:
    def test_transition_to_personal_account_logout(self, driver):
        driver.find_element(*TestLocators.BUTTON_PERSONAL_ACCOUNT).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(TestLocators.LOGIN_HEADER))

        login(driver)

        WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable(TestLocators.BUTTON_PLACE_AN_ORDER))

        driver.find_element(*TestLocators.BUTTON_PERSONAL_ACCOUNT).click()
        WebDriverWait(driver, 5).until(expected_conditions.url_contains("/profile"))

        driver.find_element(*TestLocators.BUTTON_LOGOUT).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(TestLocators.LOGIN_HEADER))

        assert driver.current_url == "https://stellarburgers.nomoreparties.site/login"
