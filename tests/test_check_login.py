from selenium.webdriver.common.by import By
import time

class TestStellarBurgers:
    def test_login(self, driver):
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