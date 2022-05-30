import time

from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Locators.locators import locators
from xlrd import open_workbook as rd

class Additemcart:
    #Current_temperature="//span[@id='temperature']"
    lp=locators

    def __init__(self,driver):

       #self.driver=webdriver.Chrome(ChromeDriverManager().install())
        self.driver =driver
        self.wait=WebDriverWait(self.driver, 10)
        self.r = rd("/Users/nelangovan/PycharmProjects/MainAssignmentFlipkart/TestData/Movielist.xls")
        self.s = self.r.sheet_by_name("AddItemcart")
    def Additemproduct1(self):

        self.driver.find_element(By.XPATH,self.lp.Search).send_keys(self.s.cell(1,0).value)
        self.driver.find_element(By.XPATH, self.lp.Searchsubmit).click()
        self.product1=self.driver.find_element(By.XPATH, self.lp.laptop)
        #self.product1text=self.product1.text
        self.product1price=self.driver.find_element(By.XPATH, self.lp.pricelaptop).text
        self.product1.click()
        lst = self.driver.window_handles
        for i in lst:
            self.driver.switch_to.window(i)
        self.product1text = self.driver.find_element(By.XPATH, self.lp.producttext).text
        self.wait.until(EC.presence_of_element_located((By.XPATH, self.lp.Addcart)))
        self.driver.find_element(By.XPATH, self.lp.Addcart).click()
        time.sleep(5)
        print(self.product1text)
        print(self.product1price)
        self.cartproduct1 = self.driver.find_element(By.XPATH, self.lp.addcart).text
        print(self.cartproduct1)
        self.cartproduct1price = self.driver.find_element(By.XPATH, self.lp.Cartprice).text
        print(self.cartproduct1price)
        return self.product1text,self.product1price,self.cartproduct1,self.cartproduct1price

    def Additemproduct2(self):
        self.driver.find_element(By.XPATH, self.lp.Search).send_keys(self.s.cell(1,1).value)
        self.driver.find_element(By.XPATH, self.lp.Searchsubmit).click()
        self.product2 = self.driver.find_element(By.XPATH, self.lp.Kitchenstove)
        #self.product2text = self.product2.text
        self.product2price = self.driver.find_element(By.XPATH, self.lp.price).text
        self.product2.click()
        lst = self.driver.window_handles
        for i in lst:
            self.driver.switch_to.window(i)
        self.product2text = self.driver.find_element(By.XPATH, self.lp.producttext).text
        self.wait.until(EC.presence_of_element_located((By.XPATH, self.lp.Addcart)))
        self.driver.find_element(By.XPATH, self.lp.Addcart).click()
        time.sleep(5)
        print(self.product2text)
        print(self.product2price)
        self.cartproduct2 = self.driver.find_element(By.XPATH, self.lp.addcart).text
        print(self.cartproduct2)
        self.cartproduct2price = self.driver.find_element(By.XPATH, self.lp.Cartprice).text
        print(self.cartproduct2price)
        return self.product2text,self.product2price,self.cartproduct2,self.cartproduct2price

    def Additemproduct3(self):
        self.driver.find_element(By.XPATH, self.lp.Search).send_keys(self.s.cell(1,2).value)
        self.driver.find_element(By.XPATH, self.lp.Searchsubmit).click()
        self.product3 = self.driver.find_element(By.XPATH, self.lp.Football)
        #self.product3text = self.product3.text
        self.product3price = self.driver.find_element(By.XPATH, self.lp.price).text
        self.product3.click()
        lst = self.driver.window_handles
        for i in lst:
            self.driver.switch_to.window(i)
        self.product3text = self.driver.find_element(By.XPATH, self.lp.producttext).text
        self.wait.until(EC.presence_of_element_located((By.XPATH, self.lp.Addcart)))
        self.driver.find_element(By.XPATH, self.lp.Addcart).click()
        time.sleep(5)
        print(self.product3text)
        print(self.product3price)
        time.sleep(5)
        self.cartproduct3 = self.driver.find_element(By.XPATH, self.lp.addcart).text
        print(self.cartproduct3)
        self.cartproduct3price = self.driver.find_element(By.XPATH, self.lp.Cartprice).text
        print(self.cartproduct3price)
        self.driver.switch_to.window(lst[0])
        self.wait.until(EC.presence_of_element_located((By.XPATH, self.lp.Cart)))
        self.driver.find_element(By.XPATH, self.lp.Cart).click()

        return self.product3text,self.cartproduct3,self.product3price,self.cartproduct3price
