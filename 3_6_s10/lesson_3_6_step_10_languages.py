import time
from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_exist_add_to_cart_button(browser):
    browser.get(link)
    time.sleep(30)
    browser.implicitly_wait(5)
    assert len(browser.find_elements(By.CSS_SELECTOR,".btn.btn-lg.btn-primary.btn-add-to-basket")) == 1, "'Add to basket' button not found!"