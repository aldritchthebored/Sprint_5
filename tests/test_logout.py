from selenium.webdriver.common.by import By
import time

class TestStellarBurgers:
        def test_logout_button(self, logged_user):
            logged_user.find_element(By.XPATH, '//*[@id="root"]/div/main/div/nav/ul/li[3]/button').click()
            time.sleep(3)
            assert '/login' in logged_user.current_url
