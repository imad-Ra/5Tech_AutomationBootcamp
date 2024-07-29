from selenium.webdriver.common.by import By
from Selenium.pom.sauce_demo_ex.infra.base_page import BasePage


class LoginPage(BasePage):

    USERNAME_INPUT = '//input[@id="user-name"]'
    PASSWORD_INPUT = '//input[@id="password"]'
    LOGIN_BUTTON = '//input[@id="login-button"]'
    LOGIN_LIST = '//div[@class="login_credentials_wrap-inner"]'



    def _init_(self,driver):
        super().__init__(driver)
        self._user_name_input = self._driver.find_element(By.XPATH, self.USERNAME_INPUT)
        self._password_input = self._driver.find_element(By.XPATH, self.PASSWORD_INPUT)
        self._login_button = self._driver.find_element(By.XPATH, self.LOGIN_BUTTON)

    def put_username_input(self,username):
        self._user_name_input.clear()
        self._user_name_input.send_keys(username)

    def put_password_input(self, password):
        self._password_input.clear()
        self._password_input.send_keys(password)

    def click_login_button(self):
        self._login_button.click()