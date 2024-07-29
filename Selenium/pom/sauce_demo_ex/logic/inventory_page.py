from selenium.webdriver.common.by import By
from Selenium.pom.sauce_demo_ex.infra.base_page import BasePage


class HomePage(BasePage):

    APP_LOGO = '//div[@class="app_logo"]'
    HOME_FOOTER = '//footer[@class="footer"]'
    INVENTORY_CONTAINER = '//div[@class="bm-menu"]'
    SIDE_MENU_BUTTON = '//button[@id="react-burger-menu-btn"]'
    SHOPPING_CART_BUTTON = '//div[@id="shopping_cart_container"]'
    SHOPPING_CART = '//div[@class="cart_contents_container"]'
    ADD_BACK_PACK_BUTTON = '//button[@id="add-to-cart-sauce-labs-backpack"]'
    ADD_BIKE_LIGHTS_BUTTON = '//button[@id="add-to-cart-sauce-labs-bike-light"]'
    REMOVE_BACK_PACK_BUTTON = '//button[@id="remove-sauce-labs-backpack"]'
    REMOVE_BIKE_LIGHTS_BUTTON = '//button[@id="remove-sauce-labs-bike-light"]'

    def __init__(self,driver):
        super().__init__(driver)

        self._app_logo = self._driver.find_element(By.XPATH,self.APP_LOGO)
        self._home_footer = self._driver.find_element(By.XPATH,self.HOME_FOOTER)
        self._inventory_container = self._driver.find_element(By.XPATH,self.INVENTORY_CONTAINER)
        self._side_menu_button = self._driver.find_element(By.XPATH,self.SIDE_MENU_BUTTON)
        self._shopping_cart_button = self._driver.find_element(By.XPATH,self.SHOPPING_CART_BUTTON)
        self._shopping_cart = self._driver.find_element(By.XPATH,self.SHOPPING_CART)
        self._add_back_pack_button = self._driver.find_element(By.XPATH, self.ADD_BACK_PACK_BUTTON)
        self._add_bike_lights_button = self._driver.find_element(By.XPATH,self.ADD_BIKE_LIGHTS_BUTTON)
        self._remove_back_pack_button = self._driver.find_element(By.XPATH,self.REMOVE_BACK_PACK_BUTTON)
        self._remove_bike_lights_button = self._driver.find_element(By.XPATH,self.REMOVE_BIKE_LIGHTS_BUTTON)

    def click_add_back_pack_button(self):
        self._add_back_pack_button.click()

    def click_add_bike_lights_button(self):
        self._add_bike_lights_button.click()

    def click_remove_back_pack_button(self):
        self._remove_back_pack_button.click()

    def click_remove_bike_lights_button(self):
        self._remove_bike_lights_button.click()

    def click_shopping_cart_button(self):
        self._shopping_cart_button.click()
