from selenium.webdriver.common.by import By
from Selenium.pom.sauce_demo_ex.infra.base_page import BasePage


class BasePageAPP(BasePage):
    CART_BUTTON = '//a[@class ="shopping_cart_link"]'
    MENU_BUTTON = '//button[@id="react-burger-menu-btn"]'
    TWITTER_BUTTON = '//a[@data-test="social-twitter"]'
    FACEBOOK_BUTTON = '//a[@data-test="social-facebook"]'
    LINKEDIN_BUTTON = '//a[@data-test="social-linkedin"]'

    def _init_(self, driver):
        super().__init__(driver)
        self._cart_button = self._driver.find_element(By.XPATH, self.CART_BUTTON)
        self._menu_button = self._driver.find_element(By.XPATH, self.MENU_BUTTON)
        self._twitter_button = self._driver.find_element(By.XPATH, self.TWITTER_BUTTON)
        self._facebook_button = self._driver.find_element(By.XPATH, self.FACEBOOK_BUTTON)
        self._linkedin_button = self._driver.find_element(By.XPATH, self.LINKEDIN_BUTTON)

    def click_on_cart_button(self):
        self._cart_button.click()

    def click_on_menu_button(self):
        self._menu_button.click()

    def click_on_twitter_button(self):
        self._twitter_button.click()

    def click_on_facebook_button(self):
        self._facebook_button.click()

    def click_on_linkedin_button(self):
        self._linkedin_button.click()
