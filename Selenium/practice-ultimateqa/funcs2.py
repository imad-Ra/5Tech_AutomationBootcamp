from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


def open_browser():
    driver = webdriver.chrome()
    driver.get("https://ultimateqa.com/complicated-page")
    time.sleep(2)
    return driver


def button_count():
    driver = open_browser()
    time.sleep(2)
    button_list = driver.find_element(By.XPATH, "//div[@class='et_pb_row et_pb_row_2 et_pb_row_4col']")
    time.sleep(2)
    buttons = button_list.find_elements(By.XPATH, "//a[contains(text(), 'Button')]")
    expected = 12
    actual = len(buttons)
    if expected == actual:
        print("TEST PASSED")
    else:
        print("TEST FAILED")
    driver.close()


def social_media_follows():
    driver = open_browser()
    time.sleep(2)
    media_list = driver.find_element(By.XPATH, "//div[@class='et_pb_row et_pb_row_4']")
    time.sleep(2)
    links = media_list.find_elements(By.TAG_NAME, "a")
    twitter_links = [link for link in links if 'twitter' in link.get_attribute('href')]
    facebook_links = [link for link in links if 'facebook' in link.get_attribute('href')]
    if len(twitter_links) == 5 and len(facebook_links) == 5:
        print("TEST PASSED")
    else:
        print("TEST FAILED")
    driver.close()


def fill_name_email_message_captcha():
    driver = open_browser()
    time.sleep(2)
    form_wrap = driver.find_element(By.ID, "et_pb_contact_form_0")
    name = form_wrap.find_element(By.XPATH, "//input[@placeholder='Name']")
    email = form_wrap.find_element(By.XPATH, "//input[@placeholder='Email Address']")
    message = form_wrap.find_element(By.XPATH, "//input[@placeholder='Message']")
    captcha = form_wrap.find_element(By.XPATH, "//input[contains(@class, 'capcha')]")
    submit = form_wrap.find_element(By.XPATH, "//button[@type='submit']")
    time.sleep(2)
    captcha_element = form_wrap.find_element(By.XPATH, "//span[contains(@class, 'et_pb_contact_captcha_question')]")
    time.sleep(2)
    captcha_question = captcha_element.text
    numbers = [int(s) for s in captcha_question.split() if s.isdigit()]
    time.sleep(2)
    captcha_answer = sum(numbers)
    name.send_keys("Ayman")
    email.send_keys("hello@ee.com")
    message.send_keys("hello my name is")
    captcha.send_keys(str(captcha_answer))
    time.sleep(2)
    submit.click()