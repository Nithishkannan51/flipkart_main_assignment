import time

from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Locators.locators import locators
from selenium.webdriver.common.action_chains import ActionChains
from xlrd import open_workbook as rd

class Searchandfilter:
    #Current_temperature="//span[@id='temperature']"
    lp=locators

    def __init__(self,driver):

       #self.driver=webdriver.Chrome(ChromeDriverManager().install())
        self.driver =driver
        self.wait=WebDriverWait(self.driver, 10)
        self.r = rd("/Users/nelangovan/PycharmProjects/MainAssignmentFlipkart/TestData/Movielist.xls")
        self.s = self.r.sheet_by_name("Searchfilter")
    def SearchItem(self):

        self.driver.find_element(By.XPATH,self.lp.Search).send_keys(self.s.cell(1,0).value)
        self.driver.find_element(By.XPATH, self.lp.Searchsubmit).click()
        time.sleep(10)
        self.wait.until(EC.presence_of_element_located((By.XPATH, self.lp.Branditemslist)))
        self.driver.find_element(By.XPATH,self.lp.Branditemslist).click()
        self.elements=self.driver.find_elements(By.XPATH,self.lp.Brand)
        lst=[]
        for i in self.elements:
            self.a=i.text
            lst.append(self.a)
        var=0
        self.brand=self.s.cell(1,1).value
        for i in self.elements:
            self.a = i.text 
            var+=1
            if(self.brand==self.a):
                print(self.a)
                print(i)
                self.brandelement=i
                break
        self.brandfound=self.lp.Brand+"["+str(var)+"]"

        self.wait.until(EC.presence_of_element_located((By.XPATH, self.brandfound)))
        self.driver.find_element(By.XPATH, self.brandfound).click()
        self.driver.find_element(By.XPATH, self.lp.Applyfilters).click()
        print(lst)
        self.wait.until(EC.presence_of_element_located((By.XPATH, self.lp.productfiltered)))
        self.filteredproductbrand=self.driver.find_element(By.XPATH, self.lp.productfiltered).text

        return self.filteredproductbrand,self.brand




