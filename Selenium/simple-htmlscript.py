from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Infra
driver = webdriver.Chrome()

# Infra         #Logic
driver.get("https://ultimateqa.com/simple-html-elements-for-automation/")

# Logic
search_input = driver.find_element(By.ID, 'APjFqb')
search_input.send_keys("Python programming")  # Search
search_input.send_keys(Keys.RETURN)  # Enter


# Infra
driver.quit()