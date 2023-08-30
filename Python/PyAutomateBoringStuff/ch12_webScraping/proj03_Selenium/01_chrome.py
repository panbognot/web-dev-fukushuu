#! python3
# Note that "ATBS w/ Python" is dated. You have to read the Selenium Docs.
from selenium import webdriver

browser = webdriver.Chrome()
# browser = webdriver.Firefox()
type(browser)
browser.get('https://inventwithpython.com')

try:
  # I read the Selenium Documentation for this
  elem = browser.find_element(by="class name", value="cover-thumb")
  print('Found <%s> element with that class name!' % (elem.tag_name))
except:
  print('Was not able to find an element with that name.')