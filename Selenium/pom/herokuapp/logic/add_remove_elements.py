from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from Selenium.pom.herokuapp.logic.base_page_app_ import BasePageApp

class AddRemoveElements(BasePageApp):
    ADD_ELEMENT = '//button[@onclick="addElement()"]'
    DELETE_ELEMENT = '//button[@onclick="deleteElement()"]'

    def __init__(self, driver):
        super().__init__(driver)
        self._wait = WebDriverWait(driver, 10)
        self._add_element = self._wait.until(EC.presence_of_element_located((By.XPATH, self.ADD_ELEMENT)))
        self._buttons = []

    def add_element(self):
        self._add_element.click()
        self._wait.until(EC.presence_of_element_located((By.XPATH, self.DELETE_ELEMENT)))
        self._update_delete_buttons()

    def _update_delete_buttons(self):
        self._buttons = self._driver.find_elements(By.XPATH, self.DELETE_ELEMENT)

    def delete_element(self, index):
        if index < len(self._buttons):
            self._buttons[index].click()
            self._update_delete_buttons()
