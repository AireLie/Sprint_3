from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import TestLocators

def test_login_from_enter_account_button(driver, get_credentials):
    driver.find_element(*TestLocators.BUTTON_ENTER_IN_ACCOUNT).click()

    driver.find_element(*TestLocators.INPUT_EMAIL).send_keys(get_credentials.email)
    driver.find_element(*TestLocators.INPUT_PASSWORD).send_keys(get_credentials.password)
    driver.find_element(*TestLocators.BUTTON_LOGIN).click()
    WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable(TestLocators.BUTTON_PLACE_AN_ORDER))

    checktxt = driver.find_element(*TestLocators.BUTTON_PLACE_AN_ORDER).text

    assert checktxt == "Оформить заказ"

def test_login_from_personal_account(driver, get_credentials):
    driver.find_element(*TestLocators.BUTTON_PERSONAL_ACCOUNT).click()
    driver.find_element(*TestLocators.INPUT_EMAIL).send_keys(get_credentials.email)
    driver.find_element(*TestLocators.INPUT_PASSWORD).send_keys(get_credentials.password)
    driver.find_element(*TestLocators.BUTTON_LOGIN).click()

    WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable(TestLocators.BUTTON_PLACE_AN_ORDER))

    checktxt = driver.find_element(*TestLocators.BUTTON_PLACE_AN_ORDER).text

    assert checktxt == "Оформить заказ"

def test_login_button_from_registration_form(driver, get_credentials):
    driver.find_element(*TestLocators.BUTTON_PERSONAL_ACCOUNT).click()
    driver.find_element(*TestLocators.LINK_REGISTRATION).click()
    driver.find_element(*TestLocators.LINK_LOGIN_FROM_REGISTRATION).click()
    driver.find_element(*TestLocators.INPUT_EMAIL).send_keys(get_credentials.email)
    driver.find_element(*TestLocators.INPUT_PASSWORD).send_keys(get_credentials.password)
    driver.find_element(*TestLocators.BUTTON_LOGIN).click()
    WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable(TestLocators.BUTTON_PLACE_AN_ORDER))

    checktxt = driver.find_element(*TestLocators.BUTTON_PLACE_AN_ORDER).text

    assert checktxt == "Оформить заказ"

def test_login_from_recovery_link(driver, get_credentials):
    driver.find_element(*TestLocators.BUTTON_PERSONAL_ACCOUNT).click()
    driver.find_element(*TestLocators.LINK_RECOVERY_PASSWORD).click()
    driver.find_element(*TestLocators.LINK_LOGIN_FROM_RECOVERY).click()
    driver.find_element(*TestLocators.INPUT_EMAIL).send_keys(get_credentials.email)
    driver.find_element(*TestLocators.INPUT_PASSWORD).send_keys(get_credentials.password)
    driver.find_element(*TestLocators.BUTTON_LOGIN).click()
    WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable(TestLocators.BUTTON_PLACE_AN_ORDER))

    checktxt = driver.find_element(*TestLocators.BUTTON_PLACE_AN_ORDER).text

    assert checktxt == "Оформить заказ"