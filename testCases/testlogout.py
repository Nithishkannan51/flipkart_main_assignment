from pageObjects.Additemcart import Additemcart
from pageObjects.LoginPage import loginpage
from xlrd import open_workbook as rd
from pageObjects.Addaddress import Addaddress
from Locators.locators import locators
from pageObjects.Logout import logout
import allure
import pytest
import pytest_html
from utilities.customLogger import logger
class Test_006_logout:
    r = rd("/Users/nelangovan/PycharmProjects/MainAssignmentFlipkart/TestData/Movielist.xls")
    s = r.sheet_by_name("Login")
    URL = s.cell(1, 4).value


    #logger = LogGen.loggen()

    def testLogout(self,setup):
        self.driver=setup
        self.logger = logger
        self.driver.implicitly_wait(10)
        self.filelocation = "/Users/nelangovan/PycharmProjects/MainAssignmentFlipkart/Screenshot/test_homepage4.jpg"
        #self.options = webdriver.ChromeOptions()
        #self.options.add_experimental_option("detach", True)
        #self.driver=webdriver.Chrome(chrome_options=self.options, executable_path=r'/Users/nelangovan/PycharmProjects/PomAssignment/Driver/chromedriver')
        self.driver.get(self.URL)
        self.driver.maximize_window()
        self.lp = loginpage(self.driver)
        self.lp.Loginpage()
        self.Ad = Addaddress(self.driver)
        self.title=self.Ad.Myprofile()
        self.logout = logout(self.driver)

        if (self.title == self.s.cell(1,5).value):
            self.logger.info("**** My Profile title test passed ****")
            assert True
        else:
            self.driver.get_screenshot_as_file(self.filelocation)
            assert False
        self.Logintext=self.logout.logout()

        if(self.Logintext==self.s.cell(5,5).value):
            self.logger.info("**** Login title test passed ****")
            assert True
        else:
            self.driver.get_screenshot_as_file(self.filelocation)
            assert False
