import pytest
import selenium
import allure
from CommonConstants.Common import CommonConstants

class StartPage:
    """
    """

    def __init__(self, driver):
        self.driver = driver

    @allure.step('Открываем сайт')
    def open_sdex_site(self):
        """
        Открывает сайт бижи
        """
        self.driver.get(CommonConstants.SITE_HOST)
