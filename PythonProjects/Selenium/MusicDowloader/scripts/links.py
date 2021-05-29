from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time


class Link():
    def __init__(self, driver):
        self.driver = driver

    def saveLinks(self, numOfSongs):
        links = []
        driver = self.driver
        for _ in range(numOfSongs):
            time.sleep(5)
            links.append(driver.current_url)
            action = ActionChains(driver)
            action.key_down(Keys.SHIFT).send_keys(
                'n').key_up(Keys.SHIFT).perform()
        return links
