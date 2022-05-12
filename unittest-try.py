import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

class TestRegistration(unittest.TestCase):
    def test_registration1(self):
        browser = webdriver.Chrome()
        browser.get("http://suninjuly.github.io/registration1.html")

        input1 = browser.find_element(By.XPATH, "//input[@placeholder='Input your first name']")
        input1.send_keys("Ivan")
        input2 = browser.find_element(By.XPATH, "//input[@placeholder='Input your last name']")
        input2.send_keys("Petrov")
        input3 = browser.find_element(By.XPATH, "//input[@placeholder='Input your email']")
        input3.send_keys("ivanpetrov@mail.ru")

        button = browser.find_element(By.CSS_SELECTOR, "button.btn")

        button.click()

    def test_registration2(self):
        browser = webdriver.Chrome()
        browser.get("http://suninjuly.github.io/registration2.html")

        input1 = browser.find_element(By.XPATH, "//input[@placeholder='Input your first name']")
        input1.send_keys("Ivan")
        input2 = browser.find_element(By.XPATH, "//input[@placeholder='Input your last name']")
        input2.send_keys("Petrov")
        input3 = browser.find_element(By.XPATH, "//input[@placeholder='Input your email']")
        input3.send_keys("ivanpetrov@mail.ru")

        button = browser.find_element(By.CSS_SELECTOR, "button.btn")

        button.click()

        text = browser.find_element(By.TAG_NAME, "h1").text
        self.assertEqual(text, "Congratulations! You have successfully registered!")

    if __name__ == "__main__": unittest.main()
