from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

link = "https://suninjuly.github.io/file_input.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    
    browser.find_element(By.NAME, "firstname").send_keys("Ilya")
    browser.find_element(By.NAME, "lastname").send_keys("Ovsyannikov")
    browser.find_element(By.NAME, "email").send_keys("email@example.com")
    
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'file.txt') 
    browser.find_element(By.CSS_SELECTOR, '[type="file"]').send_keys(file_path)
    
    submit_button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    submit_button.click()

finally:
    time.sleep(5)
    browser.quit()