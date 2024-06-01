from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def scrollIntoView(browser, element):
    browser.execute_script("return arguments[0].scrollIntoView(true);", element)
    
def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

link = "https://SunInJuly.github.io/execute_script.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    x = browser.find_element(By.ID, "input_value").text
    answer = calc(x)
    
    browser.find_element(By.ID, "answer").send_keys(answer)
    
    checkbox = browser.find_element(By.ID, "robotCheckbox")
    checkbox.click()
    
    radio_button = browser.find_element(By.ID, "robotsRule")
    scrollIntoView(browser, radio_button)
    radio_button.click()
    
    submit_button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    scrollIntoView(browser, submit_button)
    submit_button.click()

finally:
    time.sleep(5)
    browser.quit()