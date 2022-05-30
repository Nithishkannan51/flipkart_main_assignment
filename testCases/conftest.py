from selenium import webdriver
import pytest
from selenium import webdriver
import pytest


@pytest.fixture()
def setup():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    driver=webdriver.Chrome(chrome_options=options, executable_path=r'/Users/nelangovan/PycharmProjects/MainAssignmentFlipkart/Driver/chromedriver')
    return driver

def pytest_configure(config):
    config._metadata['Project Name'] ='Flipkart'
    config._metadata['Module Name']='Customers'
    config._metadata['Tester']='Nithish'
