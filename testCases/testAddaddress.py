import time

from pageObjects.Addaddress import Addaddress
from pageObjects.LoginPage import loginpage
from selenium.webdriver.common.by import By
from Locators.locators import locators
from xlrd import open_workbook as rd
from utilities.customLogger import logger

class Test_005_testaddaddress:
    r = rd("/Users/nelangovan/PycharmProjects/MainAssignmentFlipkart/TestData/Movielist.xls")
    s = r.sheet_by_name("Login")
    URL = s.cell(1, 4).value
    #logger = LogGen.loggen()

    def testAddaddress(self,setup):
        self.driver=setup
        self.logger = logger
        self.lo = locators
        self.driver.implicitly_wait(10)
        self.filelocation = "/Users/nelangovan/PycharmProjects/MainAssignmentFlipkart/Screenshot/test_homepage4.jpg"
        self.driver.get(self.URL)
        self.driver.maximize_window()
        self.Ad = Addaddress(self.driver)
        self.lp = loginpage(self.driver)
        self.lp.Loginpage()
        self.title=self.Ad.Myprofile()

        if(self.title==self.s.cell(1,5).value):
            self.logger.info("**** My Profile title test passed ****")
            assert True
        else:
            self.driver.get_screenshot_as_file(self.filelocation)
            assert False
        self.statetext=self.Ad.Addaddress()

        self.driver.find_element(By.XPATH, self.lo.save).click()
        time.sleep(10)
        self.SavedName=self.driver.find_element(By.XPATH, self.lo.SavedName).text
        print(self.SavedName)
        #self.SavedPhoneNumber = self.driver.find_element(By.XPATH, self.lo.SavedPhonenumber).text
        time.sleep(4)
        print(self.s.cell(8, 5).value)
        if (self.SavedName == self.s.cell(8, 5).value):

            self.logger.info("**** Saved name and name given are same****")
            assert True
        else:
            self.driver.get_screenshot_as_file(self.filelocation)
            assert False


