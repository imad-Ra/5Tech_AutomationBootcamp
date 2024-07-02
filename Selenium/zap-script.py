from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


#Infra
driver = webdriver.Chrome()

#Infra         #Logic
driver.get("https://www.youtube.com/")

#Logic
search_input = driver.find_element(By.XPATH, "//input[contains(@id , 'search')]")
search_input.send_keys("Imad") # Search
search_input.send_keys(Keys.RETURN) # Enter

#Infra
driver.quit()