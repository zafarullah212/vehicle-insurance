import pytest
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from utils.browserUtils import BrowserUtils


class PriceOption(BrowserUtils):
    def __init__(self, driver):
        super().__init__(driver)
        self.silver = (By.ID , "selectsilver")
        self.downloadquote = (By.ID , "downloadquote")
        self.next = (By.ID , "nextsendquote")
        self.LoadingPDF = (By.ID , "LoadingPDF")


    def ChoosePrice(self):

        choose_price = self.driver.find_element(*self.silver)
        self.driver.execute_script("arguments[0].click();", choose_price)

        self.driver.find_element(*self.downloadquote).click()


        wait = WebDriverWait(self.driver, 10)
        wait.until(expected_conditions.invisibility_of_element(self.LoadingPDF))

        next = self.driver.find_element(*self.next)
        self.driver.execute_script("arguments[0].click();", next)



