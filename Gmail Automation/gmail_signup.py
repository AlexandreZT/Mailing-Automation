# import requests
# from requests.auth import HTTPBasicAuth
import time
import random
import selenium
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
import csv
from pathlib import Path
import os
import re
import copy
# import chromedriver_autoinstaller
# from tools.log_decorator import LogDecorator
# import pickle
# import logging


firstname = "Alphonse"
lastname = "Brown"
username = "alphonse.brown.ab.12@gmail.com"
password = "@lphoneab12"

options = Options()

driver = webdriver.Chrome("chromedriver.exe")

print ("the version of your selenium: "+selenium.__version__)

chrome_browser_version = driver.capabilities['browserVersion']
chrome_driver_version = driver.capabilities['chrome']['chromedriverVersion'].split(' ')[0]

print("The version of your chrome browser: "+chrome_browser_version[0:2])
print("The version of your chrome driver: "+chrome_driver_version[0:2])
if chrome_browser_version[0:2] != chrome_driver_version[0:2]: 
  print("please download correct chromedriver version")

time.sleep(random.randint(2, 4))

driver.get("https://accounts.google.com/signup")

# firstName
write = driver.find_element_by_name("firstName")

for character in firstname:
    write.send_keys(character)
    time.sleep(random.uniform(0.2, 0.4))

# lastName
time.sleep(random.randint(2, 4))
write = driver.find_element_by_name("lastName")

for character in lastname:
    write.send_keys(character)
    time.sleep(random.uniform(0.2, 0.4))

# Username
time.sleep(random.randint(2, 4))
write = driver.find_element_by_name("Username")

for character in username:
    write.send_keys(character)
    time.sleep(random.uniform(0.2, 0.4))
  
# Passwd
time.sleep(random.randint(2, 4))
write = driver.find_element_by_name("Passwd")

for character in password:
    write.send_keys(character)
    time.sleep(random.uniform(0.2, 0.4))
  
# ConfirmPasswd
time.sleep(random.randint(2, 4))
write = driver.find_element_by_name("ConfirmPasswd")

for character in password:
    write.send_keys(character)
    time.sleep(random.uniform(0.2, 0.4))
  
time.sleep(random.randint(2, 4))

# Next
driver.find_element_by_xpath("//*[@id='accountDetailsNext']/span/span").click()
