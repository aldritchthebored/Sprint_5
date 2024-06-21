from selenium.webdriver.common.by import By
import time


class TestStellarBurgers:
    def test_button_bread(self, driver):
        time.sleep(3)
        driver.find_element(By.XPATH, '//*[@id="root"]/div/main/section[1]/div[1]/div[2]/span').click()
        time.sleep(3)
        driver.find_element(By.XPATH, '//*[@id="root"]/div/main/section[1]/div[1]/div[1]/span').click()
        time.sleep(3)
        highlight_button = driver.find_element(By.CSS_SELECTOR, '.tab_tab_type_current__2BEPc ')
        assert "tab_tab_type_current__2BEPc" in highlight_button.get_attribute('class')
    def test_button_sauces(self, driver):
        time.sleep(3)
        driver.find_element(By.XPATH, '//*[@id="root"]/div/main/section[1]/div[1]/div[2]/span').click()
        time.sleep(3)
        highlight_button = driver.find_element(By.CSS_SELECTOR, '.tab_tab_type_current__2BEPc ')
        assert "tab_tab_type_current__2BEPc" in highlight_button.get_attribute('class')

    def test_button_filling(self, driver):
        time.sleep(3)
        driver.find_element(By.XPATH, '//*[@id="root"]/div/main/section[1]/div[1]/div[3]/span').click()
        time.sleep(3)
        highlight_button = driver.find_element(By.CSS_SELECTOR, '.tab_tab_type_current__2BEPc ')
        assert "tab_tab_type_current__2BEPc" in highlight_button.get_attribute('class')
