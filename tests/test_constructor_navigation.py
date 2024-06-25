from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators

class TestStellarBurgers:
    def test_button_bread(self, driver):
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((Locators.SAUCE_BUTTON)))
        driver.find_element(*Locators.SAUCE_BUTTON).click()
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((Locators.BULKI_BUTTON)))
        driver.find_element(*Locators.BULKI_BUTTON).click()
        highlight_button = driver.find_element(*Locators.BULKI_BUTTON)
        assert "tab_tab_type_current__2BEPc" in highlight_button.get_attribute('class')
    def test_button_sauces(self, driver):
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((Locators.SAUCE_BUTTON)))
        driver.find_element(*Locators.SAUCE_BUTTON).click()
        highlight_button = driver.find_element(*Locators.SAUCE_BUTTON)
        assert "tab_tab_type_current__2BEPc" in highlight_button.get_attribute('class')
    def test_button_filling(self, driver):
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((Locators.FILLING_BUTTON)))
        driver.find_element(*Locators.FILLING_BUTTON).click()
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((Locators.FILLING_BUTTON)))
        highlight_button = driver.find_element(*Locators.FILLING_BUTTON)
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((Locators.FILLING_BUTTON)))
        assert "tab_tab_type_current__2BEPc" in highlight_button.get_attribute('class')
