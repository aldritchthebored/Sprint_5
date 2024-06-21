from selenium.webdriver.common.by import By
import time

class TestStellarBurgers:
        def test_transition_through_logo(self, logged_user):
            logged_user.find_element(By.XPATH, '//*[@id="root"]/div/header/nav/div').click()
            time.sleep(3)
            title = logged_user.find_element(By.XPATH, '//*[@id="root"]/div/main/section[1]/h1').text
            assert title == "Соберите бургер"
            
        def test_transition_through_constructor(self, logged_user):
            logged_user.find_element(By.XPATH, '//*[@id="root"]/div/header/nav/ul/li[1]/a/p').click()
            time.sleep(3)
            title = logged_user.find_element(By.XPATH, '//*[@id="root"]/div/main/section[1]/h1').text
            assert title == "Соберите бургер"
