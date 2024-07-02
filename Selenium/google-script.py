from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Infra
driver = webdriver.Chrome()

# Infra         #Logic
driver.get("https://www.google.com/")

# Logic
search_input = driver.find_element(By.ID, 'APjFqb')
search_input.send_keys("Python programming")  # Search
search_input.send_keys(Keys.RETURN)  # Enter

# Wait for search results to load and click the first result
wait = WebDriverWait(driver, 10)
first_result = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div.g h3")))
#By.CSS_SELECTOR is a locator strategy in Selenium. It tells Selenium to use CSS selectors to find elements.
# "div.g h3" is the actual CSS selector. It means:
# div.g: Find a <div> element with a class of g
# h3: Within that div, find an <h3> element
first_result.click()

# Infra
driver.quit()