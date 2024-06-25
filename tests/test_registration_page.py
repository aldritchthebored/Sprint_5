from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators
import time
from faker import Faker


class TestStellarBurgers:
    fake = Faker()
    def test_registration_new_user(self, driver):
        email = self.fake.email()
        password = self.fake.password(length=6)
        WebDriverWait(driver, 3).until(EC.presence_of_element_located((Locators.LOGIN_IN_ACCOUNT)))
        driver.find_element(*Locators.LOGIN_IN_ACCOUNT).click()
        WebDriverWait(driver, 3).until(EC.presence_of_element_located((Locators.REGISTRATION_BUTTON_ON_LOGIN_PAGE)))
        driver.find_element(*Locators.REGISTRATION_BUTTON_ON_LOGIN_PAGE).click()
        driver.find_element(*Locators.REGISTRATION_NAME_INPUT).send_keys("Тестов")
        driver.find_element(*Locators.REGISTRATION_EMAIL_INPUT).send_keys(email)
        driver.find_element(*Locators.REGISTRATION_PASSWORD_INPUT).send_keys(password)
        driver.find_element(*Locators.REGISTRATION_BUTTON).click()
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((Locators.LOGO_STELLAR_BURGERS)))
        driver.find_element(*Locators.LOGO_STELLAR_BURGERS).click()
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((Locators.LOGIN_IN_ACCOUNT)))
        driver.find_element(*Locators.LOGIN_IN_ACCOUNT).click()
        WebDriverWait(driver, 7).until(EC.presence_of_element_located((Locators.LOGIN_EMAIL_INPUT)))
        driver.find_element(*Locators.LOGIN_EMAIL_INPUT).send_keys(email)
        driver.find_element(*Locators.LOGIN_PASSWORD_INPUT).send_keys(password)
        WebDriverWait(driver, 7).until(EC.presence_of_element_located((Locators.LOGIN_BUTTON)))
        driver.find_element(*Locators.LOGIN_BUTTON).click()
        WebDriverWait(driver, 7).until(EC.element_to_be_clickable((Locators.PERSONAL_ACCOUNT)))
        driver.find_element(*Locators.PERSONAL_ACCOUNT).click()
        WebDriverWait(driver, 7).until(EC.presence_of_element_located((Locators.LOGOUT_BUTTON)))
        assert 'https://stellarburgers.nomoreparties.site/account/profile' == driver.current_url

    def test_registration_invalid_password(self, driver):
        WebDriverWait(driver, 3).until(EC.presence_of_element_located((Locators.LOGIN_IN_ACCOUNT)))
        driver.find_element(*Locators.LOGIN_IN_ACCOUNT).click()
        WebDriverWait(driver, 3).until(EC.presence_of_element_located((Locators.REGISTRATION_BUTTON_ON_LOGIN_PAGE)))
        driver.find_element(*Locators.REGISTRATION_BUTTON_ON_LOGIN_PAGE).click()
        driver.find_element(*Locators.REGISTRATION_NAME_INPUT).send_keys('Елизавета')
        driver.find_element(*Locators.REGISTRATION_EMAIL_INPUT).send_keys('elizavetavinogradova10562@yandex.ru')
        driver.find_element(*Locators.REGISTRATION_PASSWORD_INPUT).send_keys('12345')
        WebDriverWait(driver, 3).until(EC.presence_of_element_located((Locators.REGISTRATION_BUTTON)))
        driver.find_element(*Locators.REGISTRATION_BUTTON).click()
        error_message = driver.find_element(*Locators.ERROR_MESSAGE).text
        assert error_message == 'Некорректный пароль'
