import unittest
from selenium import webdriver
from Selenium.pom.sauce_demo_ex.logic.logged_in_successfully_page import LoggedInSuccessfullyPage
from Selenium.pom.sauce_demo_ex.logic.practice_test_login_page import PracticeTestLoginPage


class TestLoginPage(unittest.TestCase):
    def test_login_succesfilly(self):
        driver = webdriver.Chrome()
        driver.get("https://www.saucedemo.com/")
        login_page = PracticeTestLoginPage(driver)
        login_page.login_flow("standard_user", "secret_sauce")
        loggred_in_successfully_page = LoggedInSuccessfullyPage(driver)
        result = loggred_in_successfully_page.is_page_loaded()
        print(result)

    def test_login_unsuccessfully(self):
        driver = webdriver.Chrome()
        driver.get("https://www.saucedemo.com/")
        login_page = PracticeTestLoginPage(driver)
        login_page.login_flow("standard_userwww", "secret_sauceaa")