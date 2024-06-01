from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try: 
    link = "https://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    first_name_input = browser.find_element(By.CSS_SELECTOR, ".first_block input.first")
    first_name_input.send_keys("First name")
    
    last_name_input = browser.find_element(By.CSS_SELECTOR, ".first_block input.second")
    last_name_input.send_keys("Last name")
    
    email_input = browser.find_element(By.CSS_SELECTOR, ".first_block input.third")
    email_input.send_keys("email@example.com")

    submit_button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    submit_button.click()

    time.sleep(1)

    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    welcome_text = welcome_text_elt.text

    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    time.sleep(10)
    browser.quit()