from selenium import webdriver
import time

link = " "   # replace the file path with a valid one

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
    input3 = browser.find_element_by_id("dataEmail")
    input3.send_keys("test@test.ru")
    input4 = browser.find_element_by_id("dataName")
    input4.send_keys("testname1")
    select1 = browser.find_element_by_id("dataGender")
    input4.click()
    select2 = browser.find_element_by_css_selector("#dataGender option:nth-child(2)")
    select2.click()
    option1 = browser.find_element_by_id("dataCheck12")
    option1.click()
    option2 = browser.find_element_by_id("dataSelect21")
    option2.click()
    button = browser.find_element_by_id("dataSend")
    button.click()

finally:
    time.sleep(1)
    browser.quit()
