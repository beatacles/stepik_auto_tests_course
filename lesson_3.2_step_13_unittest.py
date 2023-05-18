from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest

class TestAbs(unittest.TestCase):
    def test_registration_1(self):
        URL = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.implicitly_wait(1)
        browser.get(URL)
        first_name = browser.find_element(By.CSS_SELECTOR, '[placeholder="Input your first name"]')
        first_name.send_keys("YOUR FIRST NAME")
        last_name = browser.find_element(By.CSS_SELECTOR, '[placeholder="Input your last name"]')
        last_name.send_keys("YOUR LAST NAME")
        email = browser.find_element(By.CSS_SELECTOR, '[placeholder="Input your email"]')
        email.send_keys("YOUR EMAIL")
        button = browser.find_element(By.CSS_SELECTOR, "button")
        button.click()
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        welcome_text = welcome_text_elt.text
        expected_text = "Congratulations! You have successfully registered!"
        self.assertEqual(welcome_text, expected_text, f"{welcome_text} not equal {expected_text}")
        browser.quit()

    def test_registration_2(self):
        URL = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.implicitly_wait(1)
        browser.get(URL)
        first_name = browser.find_element(By.CSS_SELECTOR, '[placeholder="Input your first name"]')
        first_name.send_keys("YOUR FIRST NAME")
        last_name = browser.find_element(By.CSS_SELECTOR, '[placeholder="Input your last name"]')
        last_name.send_keys("YOUR LAST NAME")
        email = browser.find_element(By.CSS_SELECTOR, '[placeholder="Input your email"]')
        email.send_keys("YOUR EMAIL")
        button = browser.find_element(By.CSS_SELECTOR, "button")
        button.click()
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        welcome_text = welcome_text_elt.text
        expected_text = "Congratulations! You have successfully registered!"
        self.assertEqual(welcome_text, expected_text, f"{welcome_text} not equal {expected_text}")
        browser.quit()

if __name__ == "__main__":
    unittest.main()