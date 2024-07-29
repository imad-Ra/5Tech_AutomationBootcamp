from selenium.webdriver.common.by import By
from Selenium.pom.herokuapp.logic.base_page_app_ import BasePageApp


class CheckBoxes(BasePageApp):
    CHECK_BOX_1 = (By.XPATH, '//*[@id="checkboxes"]/input[1]')
    CHECK_BOX_2 = (By.XPATH, '//*[@id="checkboxes"]/input[2]')

    def __init__(self, driver):
        super().__init__(driver)

    def click_check_box_1(self):
        check_box_1 = self._driver.find_element(*self.CHECK_BOX_1)
        check_box_1.click()

    def click_check_box_2(self):
        check_box_2 = self._driver.find_element(*self.CHECK_BOX_2)
        check_box_2.click()

    def double_click_check_box_1(self):
        check_box_1 = self._driver.find_element(*self.CHECK_BOX_1)
        check_box_1.click()
        check_box_1.click()