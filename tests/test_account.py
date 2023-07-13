from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import TestLocators
from helpers import login

class TestAccount:
    def test_transition_to_personal_account(self, driver):

        driver.find_element(*TestLocators.BUTTON_PERSONAL_ACCOUNT).click()
        WebDriverWait(driver, 7).until(expected_conditions.visibility_of_element_located(TestLocators.LOGIN_HEADER))

        login(driver)

        WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable(TestLocators.BUTTON_PLACE_AN_ORDER))

        driver.find_element(*TestLocators.BUTTON_PERSONAL_ACCOUNT).click()
        WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable(TestLocators.BUTTON_SAVE))

        assert driver.current_url == "https://stellarburgers.nomoreparties.site/account/profile"

    def test_from_pa_to_contructor_by_button(self, driver):
        driver.find_element(*TestLocators.BUTTON_PERSONAL_ACCOUNT).click()
        WebDriverWait(driver, 7).until(expected_conditions.visibility_of_element_located(TestLocators.LOGIN_HEADER))

        login(driver)

        WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable(TestLocators.BUTTON_PLACE_AN_ORDER))

        driver.find_element(*TestLocators.BUTTON_PERSONAL_ACCOUNT).click()
        WebDriverWait(driver, 5).until(expected_conditions.url_contains("/profile"))

        driver.find_element(*TestLocators.BUTTON_CONSTRUCTOR).click()
        WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable(TestLocators.HEADER_BUNS))

        assert driver.current_url == "https://stellarburgers.nomoreparties.site/"

    def test_from_pa_to_contructor_by_logo(self, driver):
        driver.find_element(*TestLocators.BUTTON_PERSONAL_ACCOUNT).click()
        WebDriverWait(driver, 7).until(expected_conditions.visibility_of_element_located(TestLocators.LOGIN_HEADER))

        login(driver)

        WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable(TestLocators.BUTTON_PLACE_AN_ORDER))

        driver.find_element(*TestLocators.BUTTON_PERSONAL_ACCOUNT).click()
        WebDriverWait(driver, 5).until(expected_conditions.url_contains("/profile"))

        driver.find_element(*TestLocators.LOGO_BUTTON).click()
        WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable(TestLocators.HEADER_BUNS))

        assert driver.current_url == "https://stellarburgers.nomoreparties.site/"
