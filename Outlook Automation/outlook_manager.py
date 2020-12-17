import pyautogui, sys
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

class OutlookManager():
    
    loop = True
    # LOGIN
    username = "exemple@name.fr"
    # username = input("veuillez saisir votre adresse mail : ")
    password = input(f"""veuillez saisir le mot de passe du compte {username} : """)
    # EMAILING
    sendto = "exemple@name.fr"
    obj_text = "Selenium" 
    obj_used = False
    message = "Salut je t'envoie un message automatisé"
    # SIGN UP
    firstname_signup = "Alphonse"
    lastname_signup = "Brown"
    username_signup = "alphonse.brown.ab.12"
    password_signup = "@lphoneab12"
    
    
    options = Options()

    driver = webdriver.Chrome("..\chromedriver\chromedriver_v86\chromedriver.exe")

    print ("The version of your selenium: "+selenium.__version__)

    chrome_browser_version = driver.capabilities['browserVersion']
    chrome_driver_version = driver.capabilities['chrome']['chromedriverVersion'].split(' ')[0]

    print("The version of your chrome browser: "+chrome_browser_version[0:2])
    print("The version of your chrome driver: "+chrome_driver_version[0:2])
    if chrome_browser_version[0:2] != chrome_driver_version[0:2]: 
        print("please download correct chromedriver version")

    def setUp(self):
        pass
    
    def outlook_login(self):
        time.sleep(random.randint(2, 4))
        self.driver.get("https://login.live.com/")
        # USERNAME
        time.sleep(random.randint(2, 4))
        write = self.driver.find_element_by_xpath("//*[@id='i0116']")
        for character in self.username:
            write.send_keys(character)
            time.sleep(random.uniform(0.2, 0.4))

        # NEXT
        time.sleep(random.randint(2, 4))
        self.driver.find_element_by_xpath("//*[@id='idSIButton9']").click()

        # PASSWORD
        time.sleep(random.randint(2, 4))
        write = self.driver.find_element_by_xpath("//*[@id='i0118']")
        for character in self.password:
            write.send_keys(character)
            time.sleep(random.uniform(0.2, 0.4))

        # NEXT
        time.sleep(random.randint(2, 4))
        self.driver.find_element_by_xpath("//*[@id='idSIButton9']").click()

        # NEXT
        time.sleep(random.randint(2, 4))
        self.driver.find_element_by_xpath("//*[@id='idSIButton9']").click()

        # GOTO OUTLOOK
        time.sleep(random.randint(2, 4))
        self.driver.get("https://outlook.live.com/mail/0/inbox")

    def outlook_send_email(self):
        # NEW EMAIL
        time.sleep(random.randint(2, 4))
        self.driver.find_element_by_xpath("//*[@id='id__3']").click()

        # AT
        time.sleep(random.randint(2, 4))
        write = self.driver.find_element_by_xpath("//*[@id='app']/div/div[2]/div[1]/div[1]/div[3]/div[2]/div/div[3]/div[1]/div/div/div/div[1]/div[1]/div[1]/div/div[1]/div/div/div/div/div[1]/div/div/input")
        for character in self.sendto:
            write.send_keys(character)
            time.sleep(random.uniform(0.2, 0.4))

        # OBJECT
        time.sleep(random.randint(2, 4))
        write = self.driver.find_element_by_xpath("//*[@id='TextField68']")
        for character in self.obj_text:
            write.send_keys(character)
            time.sleep(random.uniform(0.2, 0.4))
        self.obj_used = True

        # MESSAGE
        time.sleep(random.randint(2, 4))
        write = self.driver.find_element_by_xpath("//*[@id='app']/div/div[2]/div[1]/div[1]/div[3]/div[2]/div/div[3]/div[1]/div/div/div/div[1]/div[2]/div[1]")
        for character in self.message:
            write.send_keys(character)
            time.sleep(random.uniform(0.2, 0.4))

        # SEND
        time.sleep(random.randint(2, 4))
        self.driver.find_element_by_xpath("//*[@id='app']/div/div[2]/div[1]/div[1]/div[3]/div[2]/div/div[3]/div[1]/div/div/div/div[1]/div[3]/div[2]/div[1]/div/span/button[1]/span/i").click()

        # CONFIRM MISSING OBJECT
        if not self.obj_used:
            time.sleep(random.randint(2, 4))
            self.driver.find_element_by_xpath("//*[@id='id__200']").click()

    def outlook_logout(self):
        time.sleep(random.randint(2, 4))
        self.driver.find_element_by_xpath("//*[@id='O365_MainLink_MePhoto']/div/div/div/div[2]/img").click()
        time.sleep(random.randint(2, 4))
        self.driver.find_element_by_xpath("//*[@id='meControlSignoutLink']").click()

    def outlook_clean_boxes(self):
        try:
            # SELECT INBOX
            time.sleep(random.randint(2, 4))
            self.driver.find_element_by_xpath("//*[@id='app']/div/div[2]/div[1]/div[1]/div[1]/div[2]/div/div[1]/div/div[1]/div[2]/div/span[1]").click()
            # SELECT ALL
            time.sleep(random.randint(2, 4))
            self.driver.find_element_by_xpath("//*[@id='app']/div/div[2]/div[1]/div[1]/div[3]/div[2]/div/div[1]/div[1]/div/div[1]/div/i[2]").click()
            # CLEAR
            time.sleep(random.randint(2, 4))
            self.driver.find_element_by_xpath("//*[@id='app']/div/div[2]/div[1]/div[1]/div[3]/div[1]/div/div/div/div/div[1]/div[1]/button/span").click()
            # CONFIRM
            xpath_left = "//*[@id='id__"
            xpath_right = "']"
            self.force_id(xpath_left, xpath_right)
        except :
            print("Il n'y a rien dans la boite de reception prioritaire")
        
        try:
            # SELECT INBOX
            time.sleep(random.randint(2, 4))
            self.driver.find_element_by_xpath("//*[@id='app']/div/div[2]/div[1]/div[1]/div[1]/div[2]/div/div[1]/div/div[1]/div[2]/div/span[1]").click()
            # SELECT OTHER 
            xpath_left = "//*[@id='Pivot"
            xpath_right = "-Tab1']/span/div/div/span/span[2]"
            self.force_id(xpath_left, xpath_right)
            # SELECT ALL
            time.sleep(random.randint(2, 4))
            self.driver.find_element_by_xpath("//*[@id='app']/div/div[2]/div[1]/div[1]/div[3]/div[2]/div/div[1]/div[1]/div/div[1]/div/i[2]").click()
            # CLEAR
            time.sleep(random.randint(2, 4))
            self.driver.find_element_by_xpath("//*[@id='app']/div/div[2]/div[1]/div[1]/div[3]/div[1]/div/div/div/div/div[1]/div[1]/button/span").click()
            # CONFIRM
            xpath_left = "//*[@id='id__"
            xpath_right = "']"
            self.force_id(xpath_left, xpath_right)
        except :
            print("Il n'y a rien dans la boite de reception secondaire")

        try:
            # SELECT BIN
            time.sleep(random.randint(2, 4))
            self.driver.find_element_by_xpath("//*[@id='app']/div/div[2]/div[1]/div[1]/div[1]/div[2]/div/div[1]/div/div[2]/div[6]/div/span[1]").click()
            # SELECT ALL
            time.sleep(random.randint(2, 4))
            self.driver.find_element_by_xpath("//*[@id='app']/div/div[2]/div[1]/div[1]/div[3]/div[2]/div/div[1]/div[1]/div[1]/div[1]/div/i[2]").click()
            # CLEAR
            time.sleep(random.randint(2, 4))
            self.driver.find_element_by_xpath("//*[@id='app']/div/div[2]/div[1]/div[1]/div[3]/div[1]/div/div/div/div/div[1]/div[1]/button/span/i").click()
            # CONFIRM
            xpath_left = "//*[@id='id__"
            xpath_right = "']"
            self.force_id(xpath_left, xpath_right)            
        except :
            print("Il n'y a rien dans la corbeille")

    def force_id(self, xpath_left, xpath_right):
        test_id = 0
        while(self.loop):
            try:
                xpath = xpath_left +str(test_id)+ xpath_right
                self.driver.find_element_by_xpath(xpath).click()
                self.loop = False
            except :
                print("test_id: "+str(test_id)+" essai raté")
            test_id+=1
        print("test_id: "+str(test_id-1)+" essai réussi")
        self.loop = True
        
    # NOT FINISHED
    def outlook_signup(self):
        self.driver.get("https://signup.live.com/signup")

        # Switch
        time.sleep(random.randint(2, 4))
        self.driver.find_element_by_xpath("//*[@id='liveSwitch']").click()

        # username
        # Domain default is @outlook.fr
        time.sleep(random.randint(2, 4))
        write = self.driver.find_element_by_xpath("//*[@id='MemberName']")
        for character in self.username_signup:
            write.send_keys(character)
            time.sleep(random.uniform(0.2, 0.4))
            
        # Next
        time.sleep(random.randint(2, 4))
        self.driver.find_element_by_xpath("//*[@id='iSignupAction']").click()
        
        # password
        time.sleep(random.randint(2, 4))
        write = self.driver.find_element_by_xpath("//*[@id='PasswordInput']")

        for character in self.password_signup:
            write.send_keys(character)
            time.sleep(random.uniform(0.2, 0.4))
            
        # Next
        time.sleep(random.randint(2, 4))
        self.driver.find_element_by_xpath("//*[@id='iSignupAction']").click()

        # firstname
        time.sleep(random.randint(2, 4))
        write = self.driver.find_element_by_xpath("//*[@id='FirstName']")

        for character in self.firstname_signup:
            write.send_keys(character)
            time.sleep(random.uniform(0.2, 0.4))

        # lastname
        time.sleep(random.randint(2, 4))
        write = self.driver.find_element_by_xpath("//*[@id='LastName']")

        for character in self.lastname_signup:
            write.send_keys(character)
            time.sleep(random.uniform(0.2, 0.4))
            
        # Next
        time.sleep(random.randint(2, 4))
        self.driver.find_element_by_xpath("//*[@id='iSignupAction']").click()

        # Pays par default = France
        
        # Mois de naissance 
        # January, February, March, April, May, June, July, August, September, October, November, December
        time.sleep(random.randint(2, 4))
        month = random.randint(1, 12)
        if month == 1:
            month = "January"
        elif month == 2:
            month = "February"
        elif month == 3:
            month = "March"
        elif month == 4:
            month = "April"
        elif month == 5:
            month = "May"
        elif month == 6:
            month = "June"
        elif month == 7:
            month = "July"   
        elif month == 8:
            month = "August"
        elif month == 9:
            month = "September"
        elif month == 10:
            month = "October"
        elif month == 11:
            month = "November"
        else:
            month = "December"    
        self.driver.find_element_by_xpath("//*[@id='BirthMonth']").send_keys(month) 
        
        # Jour de naissance 
        # 1 - 31
        time.sleep(random.randint(2, 4))
        self.driver.find_element_by_xpath("//*[@id='BirthDay']").send_keys(random.randint(1, 31)) 
        
        # Année de naissance 
        # 1905 - 2020
        time.sleep(random.randint(2, 4))
        self.driver.find_element_by_xpath("//*[@id='BirthYear']").send_keys(random.randint(1905, 2020)) 

        # Next
        time.sleep(random.randint(2, 4))
        self.driver.find_element_by_xpath("//*[@id='iSignupAction']").click()

        # LAST STEP
        time.sleep(random.randint(2, 4))
        print('Natural Language Processing to solve it ?')
        
    def getWithPosition(self):
        print(pyautogui.size())
        # print(pyautogui.position())
        pyautogui.moveTo(391, 621)
        pyautogui.click(button='right')
        pyautogui.moveTo(512, 662)
        pyautogui.click(button='left')
        pyautogui.press('enter')

    def run_outlook_process(self):
        self.outlook_login()
        self.outlook_clean_boxes()
        # self.outlook_send_email()
        # self.outlook_logout()
        # self.driver.quit()
        # self.outlook_signup()
        # self.getWithPosition()

if __name__ == "__main__":
    OutlookManager().run_outlook_process()