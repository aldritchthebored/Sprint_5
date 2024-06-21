import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

@pytest.fixture
def driver():
    browser = webdriver.Chrome() 
    browser.get('https://stellarburgers.nomoreparties.site')
    yield browser
    browser.quit()

@pytest.fixture
def logged_user():
    browser = webdriver.Chrome() 
    browser.get('https://stellarburgers.nomoreparties.site/login')
    time.sleep(3)
    browser.find_element(By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[1]/div/div/input').send_keys('elizavetavinogradova10562@yandex.ru')
    browser.find_element(By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[2]/div/div/input').send_keys('123456')
    browser.find_element(By.XPATH, '//*[@id="root"]/div/main/div/form/button').click()
    time.sleep(3)
    browser.find_element(By.XPATH, '//*[@id="root"]/div/header/nav/a/p').click()
    time.sleep(3)
    yield browser
    browser.quit()