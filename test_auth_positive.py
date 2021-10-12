from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import time

link = " " # replace the file path with a valid one

try:
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element_by_id("loginEmail")
    input1.send_keys("test@test.ru")
    input2 = browser.find_element_by_id("loginPassword")
    input2.send_keys("test")
    time.sleep(1)
    button = browser.find_element_by_id("authButton")
    button.click()
    authSuccess = browser.find_element_by_id("inputsPage")
    assert authSuccess != 0, 'OK'

finally:
    time.sleep(1)
    browser.quit()
