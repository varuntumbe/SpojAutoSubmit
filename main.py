from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest
from time import sleep
from dotenv import load_dotenv
import sys
import os

#getting chrome browser instance
class Spoj():

    '''constructor which runs chromedriver to start a chromium proxy server
    all the next things that we automate with python is done by chromium server.
    python lang and server is communicate through http json wire proocol'''
    def __init__(self,fname,qcode):
        self.load_env()
        self.username=os.getenv('USER_NAME')
        self.password=os.getenv('PASSWORD')
        self.filename=fname
        self.qcode=qcode
        self.driver=webdriver.Chrome('./chromedriver')
        self.filepath=f'F:/c++(CP)/{self.filename}.cpp'
        # #if html dom doesnt load after 120 secs test will be forcefully closed
        self.driver.set_page_load_timeout(120)
        self.log_in()

    def load_env(self):
        load_dotenv()

    #logging in with email and password
    def log_in(self):
        try:
            driver=self.driver
            driver.get('https://www.spoj.com/problems/classical/')
            sign_in=driver.find_element_by_xpath('//*[@id="menu"]/div/nav/ul/li[6]/a').click()
            login_user=driver.find_element_by_name('login_user')
            login_user.send_keys(self.username)
            login_pass=driver.find_element_by_name('password')
            login_pass.send_keys(self.password)
            driver.find_element_by_xpath('//*[@id="login-form"]/div/div/button').click()
        except Exception as e:
            print(e)
            print('login unsuccesfull')        

    def submit(self):
        #opens a perticular website
        try:
            driver=self.driver
            driver.get(f'https://www.spoj.com/submit/{self.qcode.upper()}/')
            #setting the lang to be cpp
            search_bar=driver.find_element_by_xpath('//*[@id="lang"]/option[15]').click()

            #uploading the file
            fupload=driver.find_element_by_id('subm_file')
            fupload.send_keys(self.filepath)
            
            #submitting the file for compilation
            driver.find_element_by_xpath('//*[@id="submit"]').click()
            sleep(30)

        except Exception as e:
            print(e)

    def dclose(self):
        self.driver.close()

if __name__=="__main__":
    #assuming its there in the mentioned directory
    fname=sys.argv[1]
    #question code
    qcode=sys.argv[2]
    s=Spoj(fname,qcode)
    s.submit()
    s.dclose()


