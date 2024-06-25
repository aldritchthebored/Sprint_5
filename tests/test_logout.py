from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators

class TestStellarBurgers:
        def test_logout_button(self, driver, logged_user):
            WebDriverWait(driver, 7).until(EC.presence_of_element_located((Locators.LOGOUT_BUTTON)))
            driver.find_element(*Locators.LOGOUT_BUTTON).click()
            WebDriverWait(driver, 7).until(EC.presence_of_element_located((Locators.LOGIN_BUTTON)))
            assert '/login' in driver.current_url
