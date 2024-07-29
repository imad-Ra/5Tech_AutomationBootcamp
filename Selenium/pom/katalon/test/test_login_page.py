import unittest
from selenium import webdriver
from Selenium.pom.katalon.logic.logged_in_successfully_page import LoggedInSuccessfullyPage
from Selenium.pom.katalon.logic.practice_test_login_page import PracticeTestLoginPage


class TestLoginPage(unittest.TestCase):

    def test_login_successfully(self):
        driver = webdriver.Chrome()
        driver.get("https://practicetestautomation.com/practice-test-login/")
        login_page = PracticeTestLoginPage(driver)
        login_page.login_flow("student", "Password123")
        logged_in_successfully_page = LoggedInSuccessfullyPage(driver)
        result = logged_in_successfully_page.headre_is_excit()
        print(result)

    def test_login_unsuccessfully(self):
        driver = webdriver.Chrome()
        driver.get("https://practicetestautomation.com/practice-test-login/")
        login_page = PracticeTestLoginPage(driver)
        login_page.login_flow("fff", "ffff")
