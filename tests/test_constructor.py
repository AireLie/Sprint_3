from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import TestLocators
from helpers import login

class TestConstructor:
    def test_buns_block_transition(self, driver):
        driver.find_element(*TestLocators.BUTTON_ENTER_IN_ACCOUNT).click()

        login(driver)

        WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable(TestLocators.BUTTON_PLACE_AN_ORDER))

        driver.find_element(*TestLocators.BLOCK_SAUSES).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(TestLocators.HEADER_BUNS))
        driver.find_element(*TestLocators.BLOCK_BUNS).click()

        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(TestLocators.HEADER_BUNS))

        assert WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(TestLocators.BULKA_NAME))


    def test_sauses_block_transition(self, driver):
        driver.find_element(*TestLocators.BUTTON_ENTER_IN_ACCOUNT).click()

        login(driver)

        WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable(TestLocators.BUTTON_PLACE_AN_ORDER))

        driver.find_element(*TestLocators.BLOCK_SAUSES).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(TestLocators.HEADER_SAUSES))

        assert WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(TestLocators.SAUSE_NAME))


    def test_toppings_block_transition(self, driver):
        driver.find_element(*TestLocators.BUTTON_ENTER_IN_ACCOUNT).click()

        login(driver)

        WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable(TestLocators.BUTTON_PLACE_AN_ORDER))

        driver.find_element(*TestLocators.BLOCK_TOPPINGS).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(TestLocators.HEADER_TOPPINGS))

        assert WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(TestLocators.TOPPING_NAME))
