#! python3
# Note that "ATBS w/ Python" is dated. You have to read the Selenium Docs.
from time import sleep
from selenium import webdriver

browser = webdriver.Chrome()
# browser = webdriver.Firefox()
type(browser)
browser.get('https://inventwithpython.com')

# I read the Selenium Documentation for this
linkElem = browser.find_element(by='link text', value='Read Online for Free')
type(linkElem)
# Follows the "Read Online for Free" link
linkElem.click()

sleep(5)