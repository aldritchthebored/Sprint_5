from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators

class TestStellarBurgers:
    def test_button_bread(self, driver):
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((Locators.SAUCE_BUTTON)))
        driver.find_element(*Locators.SAUCE_BUTTON).click()
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((Locators.BULKI_BUTTON)))
        driver.find_element(*Locators.BULKI_BUTTON).click()
        assert WebDriverWait(driver, 5).until(EC.visibility_of_element_located((Locators.BULKI_TEXT)))

    def test_button_sauces(self, driver):
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((Locators.FILLING_BUTTON)))
        driver.find_element(*Locators.FILLING_BUTTON).click()
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((Locators.SAUCE_BUTTON)))
        driver.find_element(*Locators.SAUCE_BUTTON).click()
        assert WebDriverWait(driver, 5).until(EC.visibility_of_element_located((Locators.SAUCE_TEXT)))
    def test_button_filling(self, driver):
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((Locators.FILLING_BUTTON)))
        driver.find_element(*Locators.FILLING_BUTTON).click()
        assert WebDriverWait(driver, 5).until(EC.visibility_of_element_located((Locators.FILLING_TEXT)))