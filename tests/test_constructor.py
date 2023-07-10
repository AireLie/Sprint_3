from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import TestLocators

def test_buns_block_transition(driver, get_credentials):
    driver.find_element(*TestLocators.BLOCK_SAUSES).click()
    WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(TestLocators.HEADER_BUNS))
    driver.find_element(*TestLocators.BLOCK_BUNS).click()
    WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable(TestLocators.HEADER_BUNS))

    assert driver.find_element(*TestLocators.HEADER_BUNS).text == 'Булки'

def test_sauses_block_transition(driver, get_credentials):
    driver.find_element(*TestLocators.BLOCK_SAUSES).click()
    WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(TestLocators.HEADER_SAUSES))

    assert driver.find_element(*TestLocators.HEADER_SAUSES).text == 'Соусы'

def test_toppings_block_transition(driver, get_credentials):
    driver.find_element(*TestLocators.BLOCK_TOPPINGS).click()
    WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(TestLocators.HEADER_TOPPINGS))

    assert driver.find_element(*TestLocators.HEADER_TOPPINGS).text == 'Начинки'
