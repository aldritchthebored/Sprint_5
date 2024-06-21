from selenium.webdriver.common.by import By
import time

class TestStellarBurgers:

    def test_login_in_account_button(self, driver):
        time.sleep(3)

        driver.find_element(By.XPATH, '//*[@id="root"]/div/main/section[2]/div/button').click()

        time.sleep(3)

        driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[1]/div/div/input').send_keys('elizavetavinogradova10562@yandex.ru')
        driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[2]/div/div/input').send_keys('123456')

        driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/form/button').click()

        time.sleep(3)

        driver.find_element(By.XPATH, '//*[@id="root"]/div/header/nav/a/p').click()

        time.sleep(3)

        assert 'https://stellarburgers.nomoreparties.site/account/profile' == driver.current_url
    def test_login_personal_account_button(self, driver):
        time.sleep(3)

        driver.find_element(By.XPATH, '//*[@id="root"]/div/header/nav/a/p').click()

        time.sleep(3)

        driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[1]/div/div/input').send_keys('elizavetavinogradova10562@yandex.ru')
        driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[2]/div/div/input').send_keys('123456')

        driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/form/button').click()

        time.sleep(3)

        driver.find_element(By.XPATH, '//*[@id="root"]/div/header/nav/a/p').click()

        time.sleep(3)

        assert 'https://stellarburgers.nomoreparties.site/account/profile' == driver.current_url
    def test_login_button_on_registration_page(self, driver):
        time.sleep(3)

        driver.find_element(By.XPATH, '//*[@id="root"]/div/main/section[2]/div/button').click()

        time.sleep(3)

        driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/div/p[1]/a').click()

        time.sleep(3)

        driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/div/p/a').click()

        time.sleep(3)

        driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[1]/div/div/input').send_keys('elizavetavinogradova10562@yandex.ru')
        driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[2]/div/div/input').send_keys('123456')

        driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/form/button').click()

        time.sleep(3)

        driver.find_element(By.XPATH, '//*[@id="root"]/div/header/nav/a/p').click()

        time.sleep(3)

        assert 'https://stellarburgers.nomoreparties.site/account/profile' == driver.current_url
    def test_login_restore_password_page(self, driver):
        time.sleep(3)
        #переход на страницу входа
        driver.find_element(By.XPATH, '//*[@id="root"]/div/main/section[2]/div/button').click()

        time.sleep(3)

        driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/div/p[2]/a').click()

        time.sleep(3)

        driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/div/p/a').click()

        time.sleep(3)

        driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[1]/div/div/input').send_keys('elizavetavinogradova10562@yandex.ru')
        driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[2]/div/div/input').send_keys('123456')

        driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/form/button').click()

        time.sleep(3)

        driver.find_element(By.XPATH, '//*[@id="root"]/div/header/nav/a/p').click()

        time.sleep(3)

        assert 'https://stellarburgers.nomoreparties.site/account/profile' == driver.current_url
        