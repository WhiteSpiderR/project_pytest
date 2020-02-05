from Pages.LoginPage import LoginPage
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class ResourceAuthorization:
    """
    класс для методов тспользуемых в тест сьюите 2
    """

    def __init__(self, driver):
        self.driver = driver

    @allure.step('Проверяем формы для ввода пароля и email на кликабельность и видимость')
    def check_login_forms_inputs(self):
        """
        Проверяет формы на кликабельность и видимость
        """
        try:
            WebDriverWait(self.driver, 20).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, LoginPage.input_email_loc)))
            WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, LoginPage.input_email_loc)))
        except TimeoutException:
            print('Element for input email, not visible or not clickable')

        try:
            WebDriverWait(self.driver, 20).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, LoginPage.input_password_loc)))
            WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, LoginPage.input_password_loc)))
        except TimeoutException:
            print('Element for input password, not visible or not clickable')