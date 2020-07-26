from selenium import webdriver
from selenium.webdriver.common.by import By
import time

TEST_DATA = {
       'single_input': 'My best message here!!',
       'two_input_first': 333,
       'two_input_second': 444
   }
driver = webdriver.Chrome()
driver.get("https://www.seleniumeasy.com/test/basic-first-form-demo.html")
time.sleep(2)

if driver.find_element(By.ID, "at-cv-lightbox-close").size != 0:
   driver.find_element(By.ID, "at-cv-lightbox-close").click()

driver.find_element(By.CSS_SELECTOR, "input#user-message").send_keys(TEST_DATA['single_input'])
driver.find_element(By.CSS_SELECTOR, "form#get-input button").click()

assert driver.find_element(By.ID, "display").text == TEST_DATA['single_input']


driver.find_element_by_css_selector("#sum1").send_keys(TEST_DATA['two_input_first'])
time.sleep(2)

driver.find_element_by_css_selector("#sum2").send_keys(TEST_DATA['two_input_second'])
time.sleep(2)

driver.find_element_by_css_selector('[onclick="return total()"]').click()
time.sleep(2)

assert driver.find_element_by_css_selector("#displayvalue").text == '777'
driver.quit()
