from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure
from typing import Union

class DmPage:
    """
    Класс для работы со страницей Exchange
    """

    input_amount_loc = 'sdex-input[formcontrolname="qty"] input'  # поле Amount
    input_asset_loc = '.sdex-form-field-type-sdex-select [formcontrolname="asset"] ng-select'  # поле Asset
    button_send_money_loc = 'sdex-card-form form button.sdex-button-border'  # кнопка Send money
    button_set_verified_loc = 'button[color="info"]'

    def __init__(self, driver):
        self.driver = driver

    @allure.step('Вводим сумму в поле Amount')
    def input_amount(self, amount: Union[str, int]):
        """
        Ввод в поле Amount
        :arg
            amount: сумма пополнения
        """
        WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, DmPage.input_amount_loc))).clear()
        WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, DmPage.input_amount_loc))).send_keys(str(amount))

    @allure.step('Выбираем валюту пополнения')
    def select_asset_coin(self, coin: Union[str, int]):
        """
        Выбор Asset
        """
        from selenium.webdriver.common.keys import Keys
        asset_coin = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, DmPage.input_asset_loc)))
        asset_coin.click()
        asset_coin.send_keys(str(coin))
        asset_coin.send_keys(Keys.ENTER)

    @allure.step('Нажимаем на кнопку "Send Money"')
    def click_send_money(self):
        """
        Клик на Send Money
        """
        WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, DmPage.button_send_money_loc))).clear()
