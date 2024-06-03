from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from dotenv import load_dotenv
import time
import pytest
import math
import os

load_dotenv()

link = "https://stepik.org/lesson/236895/step/1"


@pytest.mark.parametrize(
    "link",
    [
        "https://stepik.org/lesson/236895/step/1",
        "https://stepik.org/lesson/236896/step/1",
        "https://stepik.org/lesson/236897/step/1",
        "https://stepik.org/lesson/236898/step/1",
        "https://stepik.org/lesson/236899/step/1",
        "https://stepik.org/lesson/236903/step/1",
        "https://stepik.org/lesson/236904/step/1",
        "https://stepik.org/lesson/236905/step/1",
    ],
)
def test_auth(browser: WebDriver, link):
    browser.get(link)
    WebDriverWait(browser, 12).until(
        EC.element_to_be_clickable((By.ID, "ember459"))
    ).click()

    email = os.getenv("STEPIK_EMAIL")
    password = os.getenv("STEPIK_PASSWORD")

    WebDriverWait(browser, 12).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, 'input[name="login"]'))
    ).send_keys(email)
    browser.find_element(By.CSS_SELECTOR, 'input[name="password"]').send_keys(password)
    browser.find_element(By.CLASS_NAME, "sign-form__btn").click()

    WebDriverWait(browser, 12).until_not(
        EC.presence_of_element_located((By.CLASS_NAME, "auth-widget"))
    )

    if (
        browser.find_element(By.CLASS_NAME, "ember-text-area").get_attribute("disabled")
        == "true"
    ):
        browser.find_element(By.CLASS_NAME, "again-btn").click()

    WebDriverWait(browser, 12).until(
        EC.element_to_be_clickable((By.CLASS_NAME, "ember-text-area"))
    ).send_keys(math.log(int(time.time())))
    WebDriverWait(browser, 12).until(
        EC.element_to_be_clickable((By.CLASS_NAME, "submit-submission"))
    ).click()

    hint = browser.find_element(By.CLASS_NAME, "smart-hints__hint").text
    expectedHint = "Correct!"

    assert (
        hint == expectedHint
    ), f"expected hint to be '{expectedHint}' but got '{hint}'"
