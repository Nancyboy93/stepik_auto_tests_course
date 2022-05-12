import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture(scope="class")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()

@pytest.mark.parametrize('endpoint', ["lesson/236895/step/1", "lesson/236896/step/1", "lesson/236897/step/1", "lesson/236898/step/1", "lesson/236899/step/1", "lesson/236903/step/1", "lesson/236904/step/1", "lesson/236905/step/1"])
class TestInput():
    def test_correct_answer(self, browser, endpoint):
        link = f"https://stepik.org/{endpoint}/"
        browser.get(link)
        input = WebDriverWait(browser, 5).until(EC.visibility_of_element_located((By.XPATH, "//textarea")))
        input.click()
        answer = str(math.log(int(time.time())))
        input.send_keys(answer)
        button = WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.XPATH, "//button[@class='submit-submission']")))
        button.click()
        result = WebDriverWait(browser, 5).until(EC.visibility_of_element_located((By.XPATH, "//pre[@class='smart-hints__hint']"))).text
        assert result == "Correct!", \
            f"Wrong description, got '{result}' instead of 'Correct!'"