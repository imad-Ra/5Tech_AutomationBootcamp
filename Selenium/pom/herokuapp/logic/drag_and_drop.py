from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from Selenium.pom.herokuapp.logic.base_page_app_ import BasePageApp


class DragAndDrop(BasePageApp):
    COLUMN_A = '//div[@id="column-a"]'
    COLUMN_B = '//div[@id="column-b"]'
    def __init__(self, driver):
        super().__init__(driver)
        self._column_a = self._driver.find_element(By.XPATH,self.COLUMN_A)
        self._column_b = self._driver.find_element(By.XPATH,self.COLUMN_B)

    def drag_and_drop(self):
        actions = ActionChains(self._driver)
        actions.click_and_hold(self._column_a).move_to_element(self._column_b).release().perform()