from selenium.webdriver.common.by import By

from infra.base_page import BasePage


class BasePageApp(BasePage):
    HOME_HEADER_BUTTON = '//a[text()="Home"]'

    def __init__(self,driver):
        super().__init__(driver)
        self._home_header_button = self._driver.find_element(By.XPATH, self.HOME_HEADER_BUTTON)

    def click_on_home_header_button(self):
        self._home_header_button.click()