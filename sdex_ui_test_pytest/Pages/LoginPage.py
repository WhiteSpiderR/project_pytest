from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure

class LoginPage:
    """
    Класс для работы со страницей Exchange
    """

    # Форма ввода email
    input_email_loc = '[formcontrolname="email"] input'
    # Форма ввода пароля
    input_password_loc = '[formcontrolname="password"] input'
    # Форма ввода кода авторизации, всплывающее окно для двухфакторной авторизации
    input_2fa_code_loc = '[formcontrolname="code"] input'
    # Кнопка отправки логина и пароля
    button_submit_loc = 'div button.sdex-button-border'

    def __init__(self, driver):
        self.driver = driver

    @allure.step('Вводим email в поле авторизации')
    def input_email(self, email):
        """
        Вводим email в поле авторизации
        """
        WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, LoginPage.input_email_loc))).clear()
        WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, LoginPage.input_email_loc))).send_keys(email)

    @allure.step('Вводим email в поле авторизации')
    def input_password(self, password):
        """
        Вводим email в поле авторизации
        """
        WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, LoginPage.input_password_loc))).clear()
        WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, LoginPage.input_password_loc))).send_keys(password)

    @allure.step('кликает на кнопку submit')
    def click_button_login(self):
        """
        Кликает на кнопку submit
        """
        WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, LoginPage.button_submit_loc))).click()

    @allure.step('Авторизация на сайте')
    def site_login(self, email, password, code_2fa=None):
        """
        Логинимся на сайте
        """
        self.input_email(email=email)
        self.input_password(password=password)
        self.click_button_login()
        if code_2fa:
            self.input_2fa_code(code=code_2fa)

    def input_2fa_code(self, code):
        """
        Вводим код для двухфакторной аутентификации
        """
        WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, LoginPage.input_2fa_code_loc))).clear()
        WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, LoginPage.input_2fa_code_loc))).send_keys(code)
