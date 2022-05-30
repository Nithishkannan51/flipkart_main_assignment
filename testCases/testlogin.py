from selenium.webdriver.common.by import By
from pageObjects.LoginPage import loginpage
from xlrd import open_workbook as rd
from utilities.customLogger import logger


class Test_001_loginpage:
    r = rd("/Users/nelangovan/PycharmProjects/MainAssignmentFlipkart/TestData/Movielist.xls")
    s = r.sheet_by_name("Login")
    URL=s.cell(1,4).value


    def test_homepage(self,setup):
        self.driver=setup
        self.logger=logger
        self.driver.implicitly_wait(10)
        self.logger.info("*************** Test_001_Login *****************")
        #self.options = webdriver.ChromeOptions()
        #self.options.add_experimental_option("detach", True)
        #self.driver=webdriver.Chrome(chrome_options=self.options, executable_path=r'/Users/nelangovan/PycharmProjects/PomAssignment/Driver/chromedriver')
        self.logger.info("****Opening URL****")
        self.driver.get(self.URL)
        self.driver.maximize_window()
        self.lp = loginpage(self.driver)
        self.invalidmessage=self.lp.Negativelogin()
        self.filelocation="/Users/nelangovan/PycharmProjects/MainAssignmentFlipkart/Screenshot/test_homepage4.jpg"
        if(self.invalidmessage==self.s.cell(2,5).value):
            assert True
        else:
            self.driver.get_screenshot_as_file(self.filelocation)
            assert False
        self.lp.Loginpage()
        print(self.driver.title)

        if(self.driver.title==self.s.cell(3,5).value):
            self.logger.info("**** Home page title test passed ****")
            assert True
        else:
            self.driver.get_screenshot_as_file(self.filelocation)
            assert False

        print(self.lp.flipkartext)

        if(self.lp.flipkartext==self.s.cell(4,5).value):
            self.logger.info("****Login test passed ****")
            assert True
        else:
            self.driver.get_screenshot_as_file(self.filelocation)
            assert False

        self.lp.Grocery()
