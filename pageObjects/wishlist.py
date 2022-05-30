import time

from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Locators.locators import locators
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains

class Wishlist:
    #Current_temperature="//span[@id='temperature']"
    lp=locators

    def __init__(self,driver):

       #self.driver=webdriver.Chrome(ChromeDriverManager().install())
        self.driver =driver
        self.wait=WebDriverWait(self.driver, 10)
    def Section1(self):

        self.fashion=self.driver.find_element(By.XPATH,self.lp.Fashion)
        action = ActionChains(self.driver)
        action.move_to_element(self.fashion).perform()
        time.sleep(5)
        self.x = self.driver.find_element(By.XPATH,self.lp.section1)
        self.x.click()
        time.sleep(5)
        #self.wait.until(EC.title_is(
        print(self.driver.title)
        return self.driver.title
        #My Profile

    def wishlistproduct1(self):
        self.driver.find_element(By.XPATH, self.lp.product).click()
        lst = self.driver.window_handles
        for i in lst:
            self.driver.switch_to.window(i)
        print(self.driver.title)
        self.wait.until(EC.presence_of_element_located((By.XPATH, self.lp.product1text)))
        self.product1text=self.driver.find_element(By.XPATH, self.lp.product1text).text
        #self.wait.until(EC.presence_of_element_located((By.XPATH, self.lp.addproductwishlist)))

        self.driver.find_element(By.XPATH, self.lp.addproductwishlist).click()

        self.profile=self.driver.find_element(By.XPATH, self.lp.Flipkart)
        action = ActionChains(self.driver)
        action.move_to_element(self.profile).perform()
        self.wait.until(EC.presence_of_element_located((By.XPATH, self.lp.Wishlist)))
        self.driver.find_element(By.XPATH, self.lp.Wishlist).click()
        time.sleep(5)
        self.driver.refresh()
        self.driver.find_element(By.XPATH, self.lp.Wishlistproduct1).click()
        lst = self.driver.window_handles
        for i in lst:
            self.driver.switch_to.window(i)


        self.product1wishlisttext = self.driver.find_element(By.XPATH, self.lp.product1text).text
        print(self.product1text)
        print(self.product1wishlisttext)
        return self.product1text,self.product1wishlisttext

    def Section2(self):
        lst = self.driver.window_handles
        self.driver.switch_to.window(lst[0])
        self.driver.back()
        self.wait.until(EC.presence_of_element_located((By.XPATH, self.lp.Fashion)))
        self.fashion=self.driver.find_element(By.XPATH,self.lp.Fashion)
        action = ActionChains(self.driver)
        action.move_to_element(self.fashion).perform()
        time.sleep(5)
        self.x = self.driver.find_element(By.XPATH,self.lp.section2)
        self.x.click()
        time.sleep(5)
        #self.wait.until(EC.title_is(
        print(self.driver.title)
        return self.driver.title
        #My Profile

    def wishlistproduct2(self):

        self.driver.find_element(By.XPATH, self.lp.product).click()
        lst = self.driver.window_handles
        for i in lst:
            self.driver.switch_to.window(i)
        print(self.driver.title)
        self.product2text=self.driver.find_element(By.XPATH, self.lp.product1text).text
        self.driver.find_element(By.XPATH, self.lp.addproductwishlist).click()
        self.profile = self.driver.find_element(By.XPATH, self.lp.Flipkart)
        action = ActionChains(self.driver)
        action.move_to_element(self.profile).perform()
        self.driver.find_element(By.XPATH, self.lp.Wishlist).click()
        time.sleep(5)
        self.driver.refresh()
        self.driver.find_element(By.XPATH, self.lp.Wishlistproduct1).click()
        lst = self.driver.window_handles
        for i in lst:
            self.driver.switch_to.window(i)

        self.product2wishlisttext = self.driver.find_element(By.XPATH, self.lp.product1text).text
        print(self.product2text)
        print(self.product2wishlisttext)
        return self.product2text,self.product2wishlisttext

