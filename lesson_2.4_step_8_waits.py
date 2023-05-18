from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math

browser = webdriver.Chrome()

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    browser.get("http://suninjuly.github.io/explicit_wait2.html")
    # Selenium проверяет в течение 12 секунд, пока цена не станет равна $100
    price = WebDriverWait(browser, 12).until(
            EC.text_to_be_present_in_element_attribute((By.CSS_SELECTOR, "#price"),"innerText", "$100")
        )
    button = browser.find_element(By.CSS_SELECTOR, "#book").click()
    x = browser.find_element(By.CSS_SELECTOR, "#input_value").text
    y = calc(int(x))
    input = browser.find_element(By.CSS_SELECTOR, "#answer").send_keys(y)
    submit = browser.find_element(By.CSS_SELECTOR, "[type=submit]").click()
    print(browser.switch_to.alert.text)
finally:
    browser.quit()