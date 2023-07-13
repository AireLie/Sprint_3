from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import TestLocators
from helpers import login

class TestLogin:
    def test_login_from_enter_account_button(self, driver):
        driver.find_element(*TestLocators.BUTTON_ENTER_IN_ACCOUNT).click()

        login(driver)

        WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable(TestLocators.BUTTON_PLACE_AN_ORDER))

        check_text = driver.find_element(*TestLocators.BUTTON_PLACE_AN_ORDER).text

        assert check_text == "Оформить заказ"

    def test_login_from_personal_account(self, driver):
        driver.find_element(*TestLocators.BUTTON_PERSONAL_ACCOUNT).click()

        login(driver)

        WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable(TestLocators.BUTTON_PLACE_AN_ORDER))

        check_text = driver.find_element(*TestLocators.BUTTON_PLACE_AN_ORDER).text

        assert check_text == "Оформить заказ"

    def test_login_button_from_registration_form(self, driver):
        driver.find_element(*TestLocators.BUTTON_PERSONAL_ACCOUNT).click()
        driver.find_element(*TestLocators.LINK_REGISTRATION).click()
        driver.find_element(*TestLocators.LINK_LOGIN_FROM_REGISTRATION).click()

        login(driver)

        WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable(TestLocators.BUTTON_PLACE_AN_ORDER))

        check_text = driver.find_element(*TestLocators.BUTTON_PLACE_AN_ORDER).text

        assert check_text == "Оформить заказ"

    def test_login_from_recovery_link(self, driver):
        driver.find_element(*TestLocators.BUTTON_PERSONAL_ACCOUNT).click()
        driver.find_element(*TestLocators.LINK_RECOVERY_PASSWORD).click()
        driver.find_element(*TestLocators.LINK_LOGIN_FROM_RECOVERY).click()

        login(driver)

        WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable(TestLocators.BUTTON_PLACE_AN_ORDER))

        check_text = driver.find_element(*TestLocators.BUTTON_PLACE_AN_ORDER).text

        assert check_text == "Оформить заказ"