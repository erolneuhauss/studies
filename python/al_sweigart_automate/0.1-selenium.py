#!/usr/bin/env python
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


browser = webdriver.Firefox()
browser.get('https://www.google.de')
try:
    elem = browser.find_element_by_name('q')
    print('Found <%s> element with that name!' % (elem.text))
    elem.send_keys("Automation Step by Step")
    elem.send_keys(Keys.ENTER)
    time.sleep(4)
except:
    print('Was not able to find an element with that name.')
browser.quit()
