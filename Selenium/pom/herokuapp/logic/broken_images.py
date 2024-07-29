from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from Selenium.pom.herokuapp.logic.base_page_app_ import BasePageApp


class BrokenImages(BasePageApp):
    FIRST_BROKEN_IMAGE = '//img[@src="asdf.jpg"]'
    SECOND_BROKEN_IMAGE = '//img[@src="hjkl.jpg"]'
    AVATAR_BLANK_IMAGE = '//img[@src="img/avatar-blank.jpg"]'

    def __init__(self, driver):
        super().__init__(driver)
        self._wait = WebDriverWait(driver, 10)
        self._first_broken_image = self._wait_for_element((By.XPATH, self.FIRST_BROKEN_IMAGE))
        self._second_broken_image = self._wait_for_element((By.XPATH, self.SECOND_BROKEN_IMAGE))
        self._avatar_blank_image = self._wait_for_element((By.XPATH, self.AVATAR_BLANK_IMAGE))

    def _wait_for_element(self, locator):
        return self._wait.until(EC.presence_of_element_located(locator))

    def is_image_broken(self, image_element):
        return image_element.get_attribute('naturalWidth') == '0'

    def validate_images(self):
        return {
            'first_broken_image': self.is_image_broken(self._first_broken_image),
            'second_broken_image': self.is_image_broken(self._second_broken_image),
            'avatar_blank_image': self.is_image_broken(self._avatar_blank_image)
        }

# if __name__ == "__main__":
#     from selenium import webdriver
#     driver = webdriver.Chrome()
#     driver.get('https://the-internet.herokuapp.com/broken_images')
#
#     # יצירת אובייקט של המחלקה וביצוע הבדיקות
#     broken_images_page = BrokenImages(driver)
#     results = broken_images_page.validate_images()
#
#     # הדפסת התוצאות
#     print(results)
#
#     # סגירת הדפדפן
#     driver.quit()