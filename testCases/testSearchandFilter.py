from pageObjects.SearchandFilter import Searchandfilter
from pageObjects.LoginPage import loginpage
from utilities.customLogger import logger
from xlrd import open_workbook as rd
class Test_003_SearchandFilter:
    r = rd("/Users/nelangovan/PycharmProjects/MainAssignmentFlipkart/TestData/Movielist.xls")
    s = r.sheet_by_name("Login")
    URL = s.cell(1, 4).value
    #logger = LogGen.loggen()

    def testSearchandFilter(self,setup):
        self.driver=setup
        self.logger = logger
        self.driver.implicitly_wait(10)
        self.filelocation = "/Users/nelangovan/PycharmProjects/MainAssignmentFlipkart/Screenshot/test_homepage4.jpg"
        #self.options = webdriver.ChromeOptions()
        #self.options.add_experimental_option("detach", True)
        #self.driver=webdriver.Chrome(chrome_options=self.options, executable_path=r'/Users/nelangovan/PycharmProjects/PomAssignment/Driver/chromedriver')
        self.driver.get(self.URL)
        self.driver.maximize_window()
        self.Sf = Searchandfilter(self.driver)
        self.lp = loginpage(self.driver)
        self.lp.Loginpage()
        self.filteredproductbrand,self.brand=self.Sf.SearchItem()

        if (self.brand in self.filteredproductbrand):
            self.logger.info("**** Brand and filteredproductbrand are same ****")
            assert True
        else:
            self.driver.get_screenshot_as_file(self.filelocation)
            assert False