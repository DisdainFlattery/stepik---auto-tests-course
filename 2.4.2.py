from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math
import time
def calc(x):
    return str(math.log(abs(12 * math.sin(x))))

link='http://suninjuly.github.io/explicit_wait2.html'

browser=webdriver.Chrome()

browser.get(link)
button=browser.find_element_by_id('book')
price = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"),'$100')
    )

28.968878986066727
button.click()
answer_input=WebDriverWait(browser,15).until(EC.visibility_of_element_located((By.ID,'answer')))
answer_input.click()
x_element = browser.find_element_by_id("input_value")
x = x_element.text
y = calc(int(x))
answer_input = browser.find_element_by_id("answer")
answer_input.send_keys(y)

submit_button = browser.find_element_by_id("solve")
submit_button.click()
