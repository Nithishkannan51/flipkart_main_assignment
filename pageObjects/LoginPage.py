import time

import webdriver_manager
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Locators.locators import locators
from xlrd import open_workbook as rd

from xlutils.copy import copy

class loginpage:
    #Current_temperature="//span[@id='temperature']"
    lp=locators


    def __init__(self,driver):

       #self.driver=webdriver.Chrome(ChromeDriverManager().install())
        self.driver =driver
        self.wait=WebDriverWait(self.driver, 10)

        self.r = rd("/Users/nelangovan/PycharmProjects/MainAssignmentFlipkart/TestData/Movielist.xls")
        self.s = self.r.sheet_by_name("Login")

    def Negativelogin(self):

        size_col = self.s.ncols
        size_row = self.s.nrows
        self.driver.find_element(By.XPATH, self.lp.phone).send_keys(self.s.cell(1,0).value)

        self.Password = self.driver.find_element(By.XPATH, self.lp.Password)
        self.Password.send_keys(self.s.cell(1,1).value)

        self.Login = self.driver.find_element(By.XPATH, self.lp.Login)
        self.Login.click()
        self.wait.until(EC.presence_of_element_located((By.XPATH, self.lp.Invalidlogin)))
        self.invalidlogin=self.driver.find_element(By.XPATH, self.lp.Invalidlogin)
        print(self.invalidlogin.text)
        return self.invalidlogin.text

    def Loginpage(self):
        #self.driver.implicitly_wait(10)
        #self.driver=driver
        self.driver.find_element(By.XPATH, self.lp.phone).clear()
        self.driver.find_element(By.XPATH,self.lp.phone).send_keys(self.s.cell(1,2).value)

        self.driver.find_element(By.XPATH, self.lp.Password).clear()
        self.Password = self.driver.find_element(By.XPATH,self.lp.Password)
        self.Password.send_keys(self.s.cell(1,3).value)

        self.Login=self.driver.find_element(By.XPATH,self.lp.Login)
        self.Login.click()

        self.wait.until(EC.presence_of_element_located((By.XPATH,self.lp.Flipkart)))
        self.flipkartext=self.driver.find_element(By.XPATH,self.lp.Flipkart).text

    def Grocery(self):
        time.sleep(5)
        self.driver.find_element(By.XPATH,self.lp.Grocery).click()
        lst = self.driver.window_handles
        for i in lst:
            self.driver.switch_to.window(i)
        #self.grocerypagetext=self.driver.find_element(By.XPATH, self.lp.Grocerypage).text

