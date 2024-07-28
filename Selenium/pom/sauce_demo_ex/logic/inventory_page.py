from selenium.webdriver.common.by import By
from Selenium.pom.sauce_demo_ex.infra.base_page import BasePage


class HomePage(BasePage):

    APP_LOGO = '//div[@class="app_logo"]'
    HOME_FOOTER = '//footer[@class="footer"]'
    INVENTORY_CONTAINER = '//div[@class="bm-menu"]'
    SHOPPING_CART = '//div[@class="cart_contents_container"]'

    def __init__(self,driver):
        super().__init__(driver)

        self._home_footer = self._driver.find_element(self.HOME_FOOTER)



        self._app_logo = self._app_logo.find_element(self.APP_LOGO)

        self._inventory_container = self._driver.find_element(self.INVENTORY_CONTAINER)
        self._shopping_cart = self._shopping_cart.find_element(self.SHOPPING_CART)