import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service = Service(executable_path=ChromeDriverManager().install())
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service)

def test1():
    driver.get("https://the-internet.herokuapp.com/")
    time.sleep(5)

def test2():
    locator1 = "a[href='/abtest']"
    locator2 = '/html/body/div[2]/div/ul/li[1]/a'
    driver.get("https://the-internet.herokuapp.com/")
    time.sleep(2)
    driver.find_element('xpath', locator2).click()
    time.sleep(2)
    driver.back()
    print(driver.current_url)
    time.sleep(2)