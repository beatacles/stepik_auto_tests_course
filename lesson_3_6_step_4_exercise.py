import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
import time
import math


igotlist = ["236895", "236896", "236897", "236898", "236899", "236903", "236904", "236905" ]

@pytest.fixture(scope="function")
def browser():
    print("\nstart..")
    browser = webdriver.Chrome()
    browser.implicitly_wait(5)
    yield browser
    browser.quit()

@pytest.mark.parametrize('number', igotlist )
def test_authorization(browser, number):
    link = f"https://stepik.org/lesson/{number}/step/1"
    browser.get(link)
    browser.find_element(By.CSS_SELECTOR, "#ember33").click()
    browser.find_element(By.CSS_SELECTOR, "#id_login_email").send_keys("SECRET")
    browser.find_element(By.CSS_SELECTOR, "#id_login_password").send_keys("SECRET")
    browser.find_element(By.CSS_SELECTOR, "[type=submit]").click()
    answer = math.log(int(time.time()))
    time.sleep(2)
    browser.find_element(By.CSS_SELECTOR, "textarea").send_keys(answer)
    WebDriverWait(browser, 5).until(
        EC.element_to_be_clickable((By.CLASS_NAME, "submit-submission"))).click()
    opt_feedback = WebDriverWait(browser, 5).until(
        EC.presence_of_element_located((By.XPATH, "/html/body/main/div[1]/div[2]/div/div[2]/div[1]/div/article/div/div/div[2]/div/div/div/div[2]/div"))).text
    time.sleep(5)
    #opt_feedback = browser.find_element(By.CSS_SELECTOR,"data-showed").text
    time.sleep(10)
    assert 'Correct!' == opt_feedback, opt_feedback

