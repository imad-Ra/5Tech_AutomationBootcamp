from selenium.webdriver.common.by import By
from Selenium.pom.herokuapp.logic.base_page_app_ import BasePageApp
from selenium.webdriver.common.action_chains import ActionChains


class ContextMenu(BasePageApp):
    HOT_SPOT = '//div[@id="hot-spot"]'

    def __init__(self, driver):
        super().__init__(driver)

    def right_click_in_hot_spot(self):
        self._hot_spot = self._driver.find_element(By.XPATH, self.HOT_SPOT)
        action = ActionChains(self._driver)
        action.context_click(self._hot_spot).perform()
