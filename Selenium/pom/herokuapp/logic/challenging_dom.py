from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from Selenium.pom.herokuapp.logic.base_page_app_ import BasePageApp

class ChallengingDOM(BasePageApp):
    BUTTONS = ['//a[@class="button"]', '//a[@class="button alert"]', '//a[@class="button success"]']
    TABLE = '//div[@class="large-10 columns"]'
    CANVAS = '//canvas[@id="canvas"]'

    def __init__(self, driver):
        super().__init__(driver)
        self._wait = WebDriverWait(driver, 10)

    def click_button(self, button_index):
        button_locator = self.BUTTONS[button_index]
        button = self._wait.until(EC.presence_of_element_located((By.XPATH, button_locator)))
        button.click()

    def get_table_text(self):
        table = self._wait.until(EC.presence_of_element_located((By.XPATH, self.TABLE)))
        return table.text

    def is_canvas_present(self):
        canvas = self._wait.until(EC.presence_of_element_located((By.XPATH, self.CANVAS)))
        return canvas.is_displayed()