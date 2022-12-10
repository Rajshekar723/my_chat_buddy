from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options

import time
opts = Options()
opts.headless = True
assert opts.headless

driver=Chrome(executable_path="C:\\bin\\chromedriver.exe",options=opts)

def quote():
    driver.get('https://quotesondesign.com/gonxalo-blanco/')
    driver.find_element("id", "get-another-quote-button").click()
    driver.implicitly_wait(9000000)
    quote = driver.find_element("id","quote-content").text
    driver.close()
    return quote

def main():
    motiquote = quote()
    print(motiquote)
    quit()


if __name__ == '__main__':
    main()
