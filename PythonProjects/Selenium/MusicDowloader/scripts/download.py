from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class Downloader():
    def __init__(self, driver):
        self.driver = driver

    def openSite(self):
        driver = self.driver
        driver.get('https://ytmp3.cc/youtube-to-mp3/')

    def Converted(self):
        while True:
            try: 
                element = driver.find_element_by_xpath('//*[@id="buttons"]/a[1]')
                return element
            except:
                time.wait(5)
                

    def DownloadItem(self, link):
        driver = self.driver
        #convBtn = driver.find_element_by_id('submit')
        searchField = driver.find_element_by_id('input')
        searchField.send_keys(link)
        searchField.send_keys(Keys.RETURN)
        time.sleep(3)
        element = Converted()
        element.click()
        time.sleep(2)
