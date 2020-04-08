from CommonConstants.Common import CommonConstants
from selenium import webdriver
import allure
from allure_commons.types import AttachmentType
from Pages.StartPage import StartPage
from Pages.LoginPage import LoginPage
from Pages.ExchangePage import ExchangePage
from Keywords.DefaultKeywords import DefaultKeywords
from Keywords.ResourceAuthorization import ResourceAuthorization as Resource

@allure.suite('Тест-сьют по работе с открытыми ордерами')
class TestOpenOrders:
    """
    Тесты с открытыми ордерами
    """

    driver = None

    def setup_class(self):
        self.driver = webdriver.Chrome()
        self.driver.set_window_size(1920, 1080)
        self.start_page = StartPage(self.driver)
        self.login_page = LoginPage(self.driver)
        self.exchange_page = ExchangePage(self.driver)
        self.resource = Resource(self.driver)
        self.default_keywords = DefaultKeywords(self.driver)

    @allure.step('')
    def setup_method(self):
        self.start_page.open_sdex_site()
        self.exchange_page.click_button_login()
        self.login_page.site_login(email=CommonConstants.LOGIN_SDEX_2, password=CommonConstants.PASSWORD_SDEX_2,
                                   code_2fa=CommonConstants.DEFAULT_EMAIL_CODE)
        self.default_keywords.check_authorization_page(
            exp_text=CommonConstants.EXPECTED_TEXT_OF_PAGE_AFTER_LOGIN_ACCOUNT_2)

    @allure.issue('')
    def test_buy_or_sell_on_exchange_page_with_check_on_open_order_page(self):
        """
        8.4 Покупка/продажа на бирже с проверкой на странице открытых ордеров и в блоке открытых ордеров на странице биржи
        """
