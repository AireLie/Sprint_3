from locators import TestLocators
from data import Credentials

def login(driver):

    driver.find_element(*TestLocators.INPUT_EMAIL).send_keys(Credentials.get_credentials().email)
    driver.find_element(*TestLocators.INPUT_PASSWORD).send_keys(Credentials.get_credentials().password)
    driver.find_element(*TestLocators.BUTTON_LOGIN).click()