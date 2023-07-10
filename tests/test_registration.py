from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import TestLocators

# positive case
def test_registration_with_valid_data(driver, get_valid_user_data):
    driver.find_element(*TestLocators.BUTTON_PERSONAL_ACCOUNT).click()
    driver.find_element(*TestLocators.LINK_REGISTRATION).click()

    driver.find_element(*TestLocators.INPUT_NAME).send_keys(get_valid_user_data.name)
    driver.find_element(*TestLocators.INPUT_EMAIL).send_keys(get_valid_user_data.email)
    driver.find_element(*TestLocators.INPUT_PASSWORD).send_keys(get_valid_user_data.password)
    driver.find_element(*TestLocators.BUTTON_REGISTRATION).click()

    WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(TestLocators.LOGIN_HEADER))

    assert driver.current_url == "https://stellarburgers.nomoreparties.site/login"

# negative case 1
def test_registration_with_empty_user_name(driver, get_empty_username_data):
    driver.find_element(*TestLocators.BUTTON_PERSONAL_ACCOUNT).click()
    driver.find_element(*TestLocators.LINK_REGISTRATION).click()

    driver.find_element(*TestLocators.INPUT_NAME).send_keys(get_empty_username_data.name)
    driver.find_element(*TestLocators.INPUT_EMAIL).send_keys(get_empty_username_data.email)
    driver.find_element(*TestLocators.INPUT_PASSWORD).send_keys(get_empty_username_data.password)
    driver.find_element(*TestLocators.BUTTON_REGISTRATION).click()

    assert driver.current_url == "https://stellarburgers.nomoreparties.site/register"

# negative case 2
def test_registration_with_invalid_password(driver, get_invalid_password_data):
    driver.find_element(*TestLocators.BUTTON_PERSONAL_ACCOUNT).click()
    driver.find_element(*TestLocators.LINK_REGISTRATION).click()

    driver.find_element(*TestLocators.INPUT_NAME).send_keys(get_invalid_password_data.name)
    driver.find_element(*TestLocators.INPUT_EMAIL).send_keys(get_invalid_password_data.email)
    driver.find_element(*TestLocators.INPUT_PASSWORD).send_keys(get_invalid_password_data.password)
    driver.find_element(*TestLocators.BUTTON_REGISTRATION).click()

    WebDriverWait(driver, 5).until(expected_conditions.presence_of_element_located(TestLocators.ERROR_REGISTRATION))

    error_message = driver.find_element(*TestLocators.ERROR_REGISTRATION)

    assert error_message.text == "Некорректный пароль"