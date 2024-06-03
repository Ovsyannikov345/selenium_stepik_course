from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest
import time

class TestRegistration(unittest.TestCase):
    def test_required_fields_on_registration1(self):
        link = "https://suninjuly.github.io/registration1.html"
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
        welcome_text = browser.find_element(By.TAG_NAME, "h1").text
        
        self.assertEqual(welcome_text, "Congratulations! You have successfully registered!", "Should display congratulations message after registration")
    
    def test_required_fields_on_registration2(self):
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
        welcome_text = browser.find_element(By.TAG_NAME, "h1").text
        self.assertEqual(welcome_text, "Congratulations! You have successfully registered!", "Should display congratulations message after registration")

if __name__ == "__main__":
    unittest.main()
