from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import TestLocators
from data import Registration

class TestRegistration_positive:
    def test_registration_with_valid_data(self, driver):
        driver.find_element(*TestLocators.BUTTON_PERSONAL_ACCOUNT).click()
        driver.find_element(*TestLocators.LINK_REGISTRATION).click()

        reg_email = Registration.get_valid_user_data().email
        driver.find_element(*TestLocators.INPUT_NAME).send_keys(Registration.get_valid_user_data().name)
        driver.find_element(*TestLocators.INPUT_EMAIL).send_keys(reg_email)
        driver.find_element(*TestLocators.INPUT_PASSWORD).send_keys(Registration.get_valid_user_data().password)
        driver.find_element(*TestLocators.BUTTON_REGISTRATION).click()

        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(TestLocators.LOGIN_HEADER))

        driver.find_element(*TestLocators.INPUT_EMAIL).send_keys(reg_email)
        driver.find_element(*TestLocators.INPUT_PASSWORD).send_keys("736540")
        driver.find_element(*TestLocators.BUTTON_LOGIN).click()
        WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable(TestLocators.BUTTON_PLACE_AN_ORDER))

        check_text = driver.find_element(*TestLocators.BUTTON_PLACE_AN_ORDER).text

        assert check_text == "Оформить заказ"


class TestRegistration_negative:
    def test_registration_with_empty_user_name(self, driver):
        driver.find_element(*TestLocators.BUTTON_PERSONAL_ACCOUNT).click()
        driver.find_element(*TestLocators.LINK_REGISTRATION).click()

        driver.find_element(*TestLocators.INPUT_NAME).send_keys(Registration.get_empty_username_data().name)
        driver.find_element(*TestLocators.INPUT_EMAIL).send_keys(Registration.get_empty_username_data().email)
        driver.find_element(*TestLocators.INPUT_PASSWORD).send_keys(Registration.get_empty_username_data().password)
        driver.find_element(*TestLocators.BUTTON_REGISTRATION).click()

        assert driver.current_url == "https://stellarburgers.nomoreparties.site/register"

    def test_registration_with_invalid_password(self, driver):
        driver.find_element(*TestLocators.BUTTON_PERSONAL_ACCOUNT).click()
        driver.find_element(*TestLocators.LINK_REGISTRATION).click()

        driver.find_element(*TestLocators.INPUT_NAME).send_keys(Registration.get_invalid_password_data().name)
        driver.find_element(*TestLocators.INPUT_EMAIL).send_keys(Registration.get_invalid_password_data().email)
        driver.find_element(*TestLocators.INPUT_PASSWORD).send_keys(Registration.get_invalid_password_data().password)
        driver.find_element(*TestLocators.BUTTON_REGISTRATION).click()

        WebDriverWait(driver, 5).until(expected_conditions.presence_of_element_located(TestLocators.ERROR_REGISTRATION))

        error_message = driver.find_element(*TestLocators.ERROR_REGISTRATION)

        assert error_message.text == "Некорректный пароль"