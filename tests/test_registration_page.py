from selenium.webdriver.common.by import By
import time

class TestStellarBurgers:
    def test_registration_new_user(self, driver):
        time.sleep(3)
        driver.find_element(By.XPATH, '//*[@id="root"]/div/main/section[2]/div/button').click()

        time.sleep(3)

        driver.find_element(By.XPATH,'//*[@id="root"]/div/main/div/div/p[1]/a').click()  # переходим на страницу авторизации
        # вводим данные для авторизации с неправильным паролем
        driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[1]/div/div/input').send_keys('Елизавета')
        driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[2]/div/div/input').send_keys('elizavetavinogradova10562@yandex.ru')
        driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[3]/div/div/input').send_keys('123456')
         #нажимаем кнопку "Зарегистрироваться"
        driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/form/button').click()
        time.sleep(3)
        assert '/login' in driver.current_url

    def test_registration_invalid_password(self, driver):
        time.sleep(3)

        driver.find_element(By.XPATH, '//*[@id="root"]/div/main/section[2]/div/button').click()
        time.sleep(3)

        driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/div/p[1]/a').click()  # переходим на страницу авторизации
        # вводим данные для авторизации с неправильным паролем
        driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[1]/div/div/input').send_keys('Елизавета')
        driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[2]/div/div/input').send_keys('elizavetavinogradova10562@yandex.ru')
        driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[3]/div/div/input').send_keys('12345')
        # нажимаем кнопку "Зарегистрироваться"
        driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/form/button').click()
        # проверяем, что сообщение об ошибке появилось
        error_message = driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[3]/div/p').text
        assert error_message == 'Некорректный пароль'
        