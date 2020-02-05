from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure

class ExchangePage:
    """
    Класс для работы со страницей Exchange
    """

    def __init__(self, driver):
        self.driver = driver

    button_login = 'sdex-header [href="/login"]'

    @allure.step('Переходим на страницу для авторизации')
    def click_button_login(self):
        """
        Кликает на кнопку login
        """
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ExchangePage.button_login))).click()
