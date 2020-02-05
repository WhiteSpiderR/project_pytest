import allure
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class DefaultKeywords:
    """
    Класс для работы с дефолтными кейвордами
    """

    def __init__(self, driver):
        self.driver = driver

    @allure.step('Проверка авторизации')
    def check_authorization_page(self, exp_text, wait_time=30):
        """
        Проверка авторизации
        :param exp_text:
        """
        t_end = time.time() + 1 * wait_time
        while time.time() < t_end:
            try:
                assert exp_text in self.driver.page_source, f'Текст {exp_text} не найден'
                return True
            except AssertionError:
                print('')
