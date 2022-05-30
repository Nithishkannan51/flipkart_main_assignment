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

class logout:
    #Current_temperature="//span[@id='temperature']"
    lp=locators

    def __init__(self,driver):

       #self.driver=webdriver.Chrome(ChromeDriverManager().install())
        self.driver =driver

    def logout(self):
        self.Logout = self.driver.find_element(By.XPATH, self.lp.Logout)
        action = ActionChains(self.driver)
        action.move_to_element(self.Logout).perform()
        self.Logout.click()
        time.sleep(5)
        self.Logintext=self.driver.find_element(By.XPATH, self.lp.login).text

        return self.Logintext