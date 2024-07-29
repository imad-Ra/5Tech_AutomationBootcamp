from selenium.webdriver.common.by import By
from Selenium.pom.sauce_demo_ex.infra.base_page import BasePage

class ShoppingCartPage(BasePage):

    SHOPPING_CART_BUTTON = "//a[@class='shopping_cart_link']"
    SHOPPING_CART_ITEMS = "//div[@class='cart_item']"
    SHOPPING_CART_TOTAL = "//div[@class='summary_total_label']"
    SHOPPING_CART_ITEM_NAME = "//div[@class='inventory_item_name']"
    SHOPPING_CART_ITEM_PRICE = "//div[@class='summary_subtotal_label']"
    SHOPPING_CART_ITEM_PIC = "//img[@class='inventory_item_img']"
    SHOPPING_CART_ITEM_DESCRIPTION = "//div[@class='inventory_item_desc']"
    SHOPPING_CART_ITEM_REMOVE_BUTTON = "//button[@class='btn btn_secondary btn_small cart_button']"
    SHOPPING_CART_BACK_TO_PRODUCTS_BUTTON = "//button[@id='continue-shopping']"
    SHOPPING_CART_ITEM_QUANTITY = "//div[@class='cart_quantity']"
    SHOPPING_CART_CHECKOUT_BUTTON = "//button[@id='checkout']"
    SHOPPING_CART_CONTINUE_SHOPPING_BUTTON = "//button[@id='continue-shopping']"

    def __init__(self, driver):
        super().__init__(driver)

    def add_item_to_cart(self, item_name):
        items = self._driver.find_elements(By.XPATH, self.SHOPPING_CART_ITEMS)
        for item in items:
            if item.find_element(By.XPATH, self.SHOPPING_CART_ITEM_NAME).text == item_name:
                item.find_element(By.XPATH, self.SHOPPING_CART_ITEM_REMOVE_BUTTON).click()
                break

    def remove_item_from_cart(self, item_name):
        items = self._driver.find_elements(By.XPATH, self.SHOPPING_CART_ITEMS)
        for item in items:
            if item.find_element(By.XPATH, self.SHOPPING_CART_ITEM_NAME).text == item_name:
                item.find_element(By.XPATH, self.SHOPPING_CART_ITEM_REMOVE_BUTTON).click()
                break

    def click_continue_shopping(self):
        self._driver.find_element(By.XPATH, self.SHOPPING_CART_CONTINUE_SHOPPING_BUTTON).click()

    def click_checkout(self):
        self._driver.find_element(By.XPATH, self.SHOPPING_CART_CHECKOUT_BUTTON).click()

    def click_back_to_products(self):
        self._driver.find_element(By.XPATH, self.SHOPPING_CART_BACK_TO_PRODUCTS_BUTTON).click()

    def click_shopping_cart_button(self):
        self._driver.find_element(By.XPATH, self.SHOPPING_CART_BUTTON).click()

    def get_shopping_cart_total(self):
        self._driver.find_element(By.XPATH, self.SHOPPING_CART_TOTAL).text.strip()

    def get_shopping_cart_item_name(self):
        self._driver.find_element(By.XPATH, self.SHOPPING_CART_ITEM_NAME).text

    def get_shopping_cart_item_price(self):
        self._driver.find_element(By.XPATH, self.SHOPPING_CART_ITEM_PRICE).text

    def get_shopping_cart_item_pic(self):
        self._driver.find_element(By.XPATH, self.SHOPPING_CART_ITEM_PIC).get_attribute('src')

    def get_shopping_cart_item_description(self):
        self._driver.find_element(By.XPATH, self.SHOPPING_CART_ITEM_DESCRIPTION).text

    def get_shopping_cart_item_quantity(self):
        self._driver.find_element(By.XPATH, self.SHOPPING_CART_ITEM_QUANTITY).text

    def get_shopping_cart_item_remove_button(self):
        self._driver.find_element(By.XPATH, self.SHOPPING_CART_ITEM_REMOVE_BUTTON).click()

    def get_shopping_cart_back_to_products_button(self):
        self._driver.find_element(By.XPATH, self.SHOPPING_CART_BACK_TO_PRODUCTS_BUTTON).click()