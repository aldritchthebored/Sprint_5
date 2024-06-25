from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators

class TestStellarBurgers:
    def test_login(self, driver):
        WebDriverWait(driver, 7).until(EC.presence_of_element_located((Locators.PERSONAL_ACCOUNT)))
        driver.find_element(*Locators.PERSONAL_ACCOUNT).click()
        WebDriverWait(driver, 3).until(EC.presence_of_element_located((Locators.LOGIN_EMAIL_INPUT)))
        driver.find_element(*Locators.LOGIN_EMAIL_INPUT).send_keys('elizavetavinogradova10562@yandex.ru')
        driver.find_element(*Locators.LOGIN_PASSWORD_INPUT).send_keys('123456')
        driver.find_element(*Locators.LOGIN_BUTTON).click()
        WebDriverWait(driver, 17).until(EC.presence_of_element_located((Locators.PERSONAL_ACCOUNT)))
        driver.find_element(*Locators.PERSONAL_ACCOUNT).click()
        WebDriverWait(driver, 17).until(EC.presence_of_element_located((Locators.LOGOUT_BUTTON)))
        assert 'https://stellarburgers.nomoreparties.site/account/profile' == driver.current_url
