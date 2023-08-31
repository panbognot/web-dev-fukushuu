#! python3
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

browser = webdriver.Chrome()
browser.get('https://nostarch.com')

htmlElem = browser.find_element(by='tag name', value='html')
sleep(3)
htmlElem.send_keys(Keys.END)    # scrolls to bottom
sleep(3)
htmlElem.send_keys(Keys.HOME)   # scrolls to top
sleep(3)
browser.refresh()               # refresh the website
sleep(5)
browser.quit()                  # close the browser window