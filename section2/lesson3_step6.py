from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/redirect_accept.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    
    browser.find_element(By.TAG_NAME, "button").click()
    
    confirm = browser.switch_to.window(browser.window_handles[1])
    
    time.sleep(1)
    
    x = browser.find_element(By.ID, "input_value").text
    answer = calc(x)
    
    browser.find_element(By.ID, "answer").send_keys(answer)

    submit_button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    submit_button.click()

finally:
    time.sleep(5)
    browser.quit()