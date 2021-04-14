from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import time
class FirstSelenium:
    """
    Program to open chrome browser and open google webpage
    """
    def __init__(self, url):
        """
        initializing variable
        """
        self.driver = webdriver.Chrome()
        self.url = url

    def openpage(self):
        driver = self.driver
        driver.get(self.url)
        elem = driver.find_element_by_name("q")
        elem.send_keys("My first selenium program", Keys.ENTER)
        time.sleep(5)
        driver.close()


if __name__ == "__main__":
    url = r"https://www.google.co.in"
    run=FirstSelenium(url)
    run.openpage()