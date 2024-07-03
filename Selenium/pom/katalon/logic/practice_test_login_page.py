from selenium.webdriver.common.by import By
from logic.base_page_app import BasePageApp


class PracticeTestLoginPage(BasePageApp):
    USER_NAME_INPUT = '//input[@id="username"]'
    PASSWORD_INPUT = '//input[@id="password"]'
    SUBMIT_BUTTON = '//button[@id= "submit"]'

    def __init__(self, driver):
        super().__init__(driver)
        self._user_name_input = self._driver.find_element(By.XPATH, self.USER_NAME_INPUT)
        self._password_input = self._driver.find_element(By.XPATH, self.PASSWORD_INPUT)
        self._submit_button = self._driver.find_element(By.XPATH, self.SUBMIT_BUTTON)

    def fill_user_input(self, username):
        self._user_name_input.send_keys(username)

    def fill_password_input(self, password):
        self._password_input.send_keys(password)

    def click_submit_button(self):
        self._submit_button.click()

    def login_flow(self, username, password):
        self.fill_user_input(username)
        self.fill_password_input(password)
        self.click_submit_button()
