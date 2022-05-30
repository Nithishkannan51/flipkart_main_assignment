from pageObjects.wishlist import Wishlist
from pageObjects.LoginPage import loginpage
from utilities.customLogger import logger
from xlrd import open_workbook as rd

class Test_004_testwishlist:
    r = rd("/Users/nelangovan/PycharmProjects/MainAssignmentFlipkart/TestData/Movielist.xls")
    s = r.sheet_by_name("Login")
    URL = s.cell(1, 4).value
    #logger = LogGen.loggen()

    def testwishlist(self,setup):
        self.driver=setup
        self.logger = logger
        self.driver.implicitly_wait(10)
        self.filelocation = "/Users/nelangovan/PycharmProjects/MainAssignmentFlipkart/Screenshot/test_homepage4.jpg"
        self.driver.get(self.URL)
        self.driver.maximize_window()
        self.wl = Wishlist(self.driver)
        self.lp = loginpage(self.driver)
        self.lp.Loginpage()
        self.section1title=self.wl.Section1()
        if(self.section1title==self.s.cell(6,5).value):
            self.logger.info("**** section1 title and page title are same ****")
            assert True
        else:
            self.driver.get_screenshot_as_file(self.filelocation)
            assert False

        #Topwear - Buy Topwear For Men, Women & Kids Online at Best Prices In India | Flipkart.com
        #KK,Sets,DM,Sarees - Buy KK,Sets,DM,Sarees Online at Low Prices In India | Flipkart.com

        self.product1text,self.product1wishlisttext = self.wl.wishlistproduct1()
        if (self.product1text in self.product1wishlisttext):
            self.logger.info("**** Product1 added before to wishlist and wishlist product1 added after are same ****")
            assert True
        else:
            self.driver.get_screenshot_as_file(self.filelocation)
            assert False

        self.section2title = self.wl.Section2()
        if (self.section2title == self.s.cell(7,5).value):
            self.logger.info("**** section2 title and page title are same ****")
            assert True
        else:
            self.driver.get_screenshot_as_file(self.filelocation)
            assert False

        # Topwear - Buy Topwear For Men, Women & Kids Online at Best Prices In India | Flipkart.com
        # KK,Sets,DM,Sarees - Buy KK,Sets,DM,Sarees Online at Low Prices In India | Flipkart.com

        self.product2text, self.product2wishlisttext = self.wl.wishlistproduct2()
        if (self.product2text == self.product2wishlisttext):
            self.logger.info("**** Product2 added before to wishlist and wishlist product2 added after are same ****")
            assert True
        else:
            self.driver.get_screenshot_as_file(self.filelocation)
            assert False