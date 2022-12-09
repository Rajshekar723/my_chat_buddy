from selenium import webdriver
from selenium.webdriver import Chrome

import time

driver=Chrome(executable_path="C:\\bin\\chromedriver.exe")
driver.get('https://quotesondesign.com/gonxalo-blanco/')
driver.find_element("id", "get-another-quote-button").click()
driver.implicitly_wait(90000)
quote = driver.find_element("id","quote-content").text
print(quote)
driver.close()