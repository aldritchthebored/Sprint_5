from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators

class TestStellarBurgers:
    def test_login(self, driver, logged_user):
        WebDriverWait(driver, 17).until(EC.presence_of_element_located((Locators.PERSONAL_ACCOUNT)))
        driver.find_element(*Locators.PERSONAL_ACCOUNT).click()
        WebDriverWait(driver, 17).until(EC.presence_of_element_located((Locators.LOGOUT_BUTTON)))
        assert 'https://stellarburgers.nomoreparties.site/account/profile' == driver.current_url
