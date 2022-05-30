import time

from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Locators.locators import locators
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from xlrd import open_workbook as rd

class Addaddress:
    #Current_temperature="//span[@id='temperature']"
    lp=locators

    def __init__(self,driver):

       #self.driver=webdriver.Chrome(ChromeDriverManager().install())
        self.driver =driver
        self.wait=WebDriverWait(self.driver, 10)
        self.r = rd("/Users/nelangovan/PycharmProjects/MainAssignmentFlipkart/TestData/Movielist.xls")
        self.s = self.r.sheet_by_name("Address")
    def Myprofile(self):

        self.fashion=self.driver.find_element(By.XPATH,self.lp.Flipkart)
        action = ActionChains(self.driver)
        action.move_to_element(self.fashion).perform()
        time.sleep(5)

        self.x = self.driver.find_element(By.XPATH,self.lp.Profile)
        self.x.click()
        self.wait.until(EC.title_is("My Profile"))
        print(self.driver.title)
        #My Profile
        return self.driver.title

    def Addaddress(self):
        self.driver.find_element(By.XPATH, self.lp.Flipkart).click()
        self.wait.until(EC.presence_of_element_located((By.XPATH, self.lp.Manageaddress)))
        self.driver.find_element(By.XPATH, self.lp.Manageaddress).click()
        self.wait.until(EC.presence_of_element_located((By.XPATH, self.lp.Addaddress)))
        self.driver.find_element(By.XPATH, self.lp.Addaddress).click()
        self.driver.find_element(By.XPATH, self.lp.Name).send_keys(self.s.cell(1,0).value)
        self.driver.find_element(By.XPATH, self.lp.mobile).send_keys(self.s.cell(1,11).value)
        self.driver.find_element(By.XPATH, self.lp.pincode).send_keys(self.s.cell(1,12).value)
        self.driver.find_element(By.XPATH, self.lp.save).click()
        self.wait.until(EC.presence_of_element_located((By.XPATH, self.lp.Negativephone)))
        self.Negativephonetext= self.driver.find_element(By.XPATH, self.lp.Negativephone).text

        if (self.Negativephonetext == "Not a valid phone number."):
            assert True
        else:
            assert False


        self.wait.until(EC.presence_of_element_located((By.XPATH, self.lp.Negativepincode)))
        self.Negativepincodetext = self.driver.find_element(By.XPATH, self.lp.Negativepincode).text

        if (self.Negativepincodetext == "Not a valid pincode"):
            assert True
        else:
            assert False
        self.driver.find_element(By.XPATH, self.lp.mobile).clear()
        self.driver.find_element(By.XPATH, self.lp.pincode).clear()
        time.sleep(5)
        self.driver.find_element(By.XPATH, self.lp.mobile).send_keys(self.s.cell(1,1).value)

        self.driver.find_element(By.XPATH, self.lp.pincode).send_keys(self.s.cell(1,2).value)
        self.driver.find_element(By.XPATH, self.lp.locality).send_keys(self.s.cell(1,3).value)
        self.address=self.s.cell(1,4).value+self.s.cell(1,5).value+self.s.cell(1,6).value
        self.driver.find_element(By.XPATH, self.lp.addresss).send_keys(self.address)
        self.driver.find_element(By.XPATH, self.lp.city).clear()
        self.driver.find_element(By.XPATH, self.lp.city).send_keys(self.s.cell(1,7).value)
        select = Select(self.driver.find_element(By.XPATH, self.lp.state))
        select.select_by_visible_text(self.s.cell(1,8).value)
        #self.statetext=self.driver.find_element(By.XPATH, self.lp.state).text
        self.driver.find_element(By.XPATH, self.lp.landmark).send_keys(self.s.cell(1,9).value)
        self.driver.find_element(By.XPATH, self.lp.alternatphone).send_keys(self.s.cell(1,10).value)
        self.driver.find_element(By.XPATH, self.lp.Home).click()








