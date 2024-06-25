from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators


class TestStellarBurgers:
    def test_transition_through_logo(self, driver, logged_user):
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((Locators.LOGO_STELLAR_BURGERS)))
        driver.find_element(*Locators.LOGO_STELLAR_BURGERS).click()
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((Locators.CREATE_BURGER)))
        title = driver.find_element(*Locators.CREATE_BURGER).text
        assert title == "Соберите бургер"

    def test_transition_through_constructor(self, driver, logged_user):
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((Locators.CONSTRUCTOR_BUTTON)))
        driver.find_element(*Locators.CONSTRUCTOR_BUTTON).click()
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((Locators.CREATE_BURGER)))
        title = driver.find_element(*Locators.CREATE_BURGER).text
        assert title == "Соберите бургер"
