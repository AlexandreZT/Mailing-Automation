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



class GmailManager():

  username = "exemple@name.fr"

  password = "azertyuiop"

  options = Options()

  driver = webdriver.Chrome("chromedriver.exe")

  print ("The version of your selenium: "+selenium.__version__)

  chrome_browser_version = driver.capabilities['browserVersion']
  chrome_driver_version = driver.capabilities['chrome']['chromedriverVersion'].split(' ')[0]

  print("The version of your chrome browser: "+chrome_browser_version[0:2])
  print("The version of your chrome driver: "+chrome_driver_version[0:2])
  if chrome_browser_version[0:2] != chrome_driver_version[0:2]: 
    print("please download correct chromedriver version")

  def gmail_login(self):
    
    time.sleep(random.randint(2, 4))

    self.driver.get("https://www.gmail.com")

    write = self.driver.find_element_by_name("identifier")

    time.sleep(random.randint(2, 4))

    for character in self.username:
        write.send_keys(character)
        time.sleep(random.uniform(0.2, 0.4))
      
    self.driver.find_element_by_class_name("VfPpkd-RLmnJb").click()
      
    time.sleep(random.randint(2, 4))

    write = self.driver.find_element_by_name("password")

    for character in self.password:
        write.send_keys(character)
        time.sleep(random.uniform(0.2, 0.4))

    time.sleep(random.randint(2, 4))

    self.driver.find_element_by_name("signup").click()

  def run_gmail_process(self):
          self.gmail_login()
          # self.gmail_clean_boxes()
          # self.gmail_send_email()
          # self.gmail_logout()
          # self.driver.quit()

if __name__ == "__main__":
    GmailManager().run_gmail_process()