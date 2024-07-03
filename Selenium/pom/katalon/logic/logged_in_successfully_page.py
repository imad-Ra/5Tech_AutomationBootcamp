from selenium.webdriver.common.by import By
from selenium import webdriver

from logic.base_page_app import BasePageApp


class LoggedInSuccessfullyPage(BasePageApp):
    HEADER_LABEL = "//h1"

    def __init__(self, driver):
        super().__init__(driver)
        self._header_label = self._driver.find_element(By.XPATH, self.HEADER_LABEL)

    def headre_is_excit(self):
        return self._header_label.is_displayed()
