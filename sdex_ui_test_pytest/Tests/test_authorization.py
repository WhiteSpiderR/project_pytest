from CommonConstants.Common import CommonConstants
from selenium import webdriver
import allure
from allure_commons.types import AttachmentType
from Pages.StartPage import StartPage
from Pages.LoginPage import LoginPage
from Pages.ExchangePage import ExchangePage
from Keywords.DefaultKeywords import DefaultKeywords
from Keywords.ResourceAuthorization import ResourceAuthorization as Resource


class TestAuthorization:
    """
    Авторизационные тесты
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

    def setup_method(self):
        self.start_page.open_sdex_site()

    @allure.issue('https://sdexnt.atlassian.net/browse/AUT-271')
    def test_open_authorization_from_header_of_main_page(self):
        """
        2.1 Вызов формы авторизации из хэдера главной страницы
        """
        self.exchange_page.click_button_login()
        self.resource.check_login_forms_inputs()

    @allure.issue('hhttps://sdexnt.atlassian.net/browse/AUT-273')
    def test_authorization_existing_user_verified_profile(self):
        """
        2.3 Авторизация с данными существующего пользователя (профиль верифицирован)
        """
        self.exchange_page.click_button_login()
        self.login_page.site_login(email=CommonConstants.LOGIN_SDEX_2, password=CommonConstants.PASSWORD_SDEX_2,
                                   code_2fa=CommonConstants.DEFAULT_EMAIL_CODE)
        self.default_keywords.check_authorization_page(exp_text=CommonConstants.EXPECTED_TEXT_OF_PAGE_AFTER_LOGIN_ACCOUNT_2)

    def teardown_method(self):
        """
        Возврат системы в исходное состаяние:
        1. Скриншот
        """
        allure.attach(body=self.driver.get_screenshot_as_png(), name='Screenshot', attachment_type=AttachmentType.PNG)

    # def teardown_class(self):
    #     """
    #     Закрыть драйвер
    #     """
    #     self.driver.quit()

