from pageObjects.Additemcart import Additemcart
from pageObjects.LoginPage import loginpage
from xlrd import open_workbook as rd
from utilities.customLogger import logger

class Test_002_Additemcart:
    r = rd("/Users/nelangovan/PycharmProjects/MainAssignmentFlipkart/TestData/Movielist.xls")
    s = r.sheet_by_name("Login")
    URL = s.cell(1, 4).value
    #logger = LogGen.loggen()

    def testAdditemcart(self,setup):
        self.driver=setup
        self.logger = logger
        self.driver.implicitly_wait(10)
        self.filelocation = "/Users/nelangovan/PycharmProjects/MainAssignmentFlipkart/Screenshot/test_homepage4.jpg"
        #self.options = webdriver.ChromeOptions()
        #self.options.add_experimental_option("detach", True)
        #self.driver=webdriver.Chrome(chrome_options=self.options, executable_path=r'/Users/nelangovan/PycharmProjects/PomAssignment/Driver/chromedriver')
        self.driver.get(self.URL)
        self.driver.maximize_window()
        self.itemcart = Additemcart(self.driver)
        self.lp = loginpage(self.driver)
        self.lp.Loginpage()
        self.product1text,self.product1price,self.cartproduct1,self.cartproduct1price=self.itemcart.Additemproduct1()
        self.product2text,self.product2price,self.cartproduct2,self.cartproduct2price=self.itemcart.Additemproduct2()
        self.product3text, self.cartproduct3,self.product3price,self.cartproduct3price=self.itemcart.Additemproduct3()

        if (self.cartproduct1 in self.product1text):
            self.logger.info("**** Product1 name and added Product1 cart name are same ****")
            assert True
        else:
            self.driver.get_screenshot_as_file(self.filelocation)
            assert False

        if (self.cartproduct2 in self.product2text):
            self.logger.info("**** Product2 name and added Product2 cart name are same ****")
            assert True
        else:
            self.driver.get_screenshot_as_file(self.filelocation)
            assert False

        if (self.cartproduct3 in self.product3text):
            self.logger.info("**** Product3 name and added Product3 cart name are same ****")
            assert True
        else:
            self.driver.get_screenshot_as_file(self.filelocation)
            assert False

        if (self.product1price==self.cartproduct1price):
            self.logger.info("**** Product1 price and added Product1 cart price are same ****")
            assert True
        else:
            self.driver.get_screenshot_as_file(self.filelocation)
            assert False

        if (self.product2price==self.cartproduct2price):
            self.logger.info("**** Product2 price and added Product2 cart price are same ****")
            assert True
        else:
            self.driver.get_screenshot_as_file(self.filelocation)
            assert False

        if (self.product3price==self.cartproduct3price):
            self.logger.info("**** Product3 price and added Product3 cart price are same ****")
            assert True
        else:
            self.driver.get_screenshot_as_file(self.filelocation)
            assert False