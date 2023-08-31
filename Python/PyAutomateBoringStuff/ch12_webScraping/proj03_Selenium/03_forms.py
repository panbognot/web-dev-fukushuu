#! python3
# Filling Out and Submitting Forms
from selenium import webdriver
from time import sleep
import pyinputplus as pyip

browser = webdriver.Chrome()
browser.get('https://nitrotype.com')
sleep(1)

# Click the "log in" button
loginElem = browser.find_element(by='link text', value='Log In')
loginElem.click()
sleep(1)

# Type the username
userElem = browser.find_element(by='id', value='username')
username = pyip.inputStr('Enter your username: ', limit=3)
userElem.send_keys(username)
sleep(0.5)
# Type the password
pwdElem = browser.find_element(by='id', value='password')
password = pyip.inputPassword('Enter your password: ', limit=3)
pwdElem.send_keys(password)
sleep(0.5)
# Submit the form
pwdElem.submit()
sleep(5)