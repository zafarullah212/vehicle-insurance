import time

from selenium.webdriver.common.by import By

from utils.browserUtils import BrowserUtils


class EnterInsurantData(BrowserUtils):

    def __init__(self, driver):
        super().__init__(driver)
        self.first_name = (By.ID, "firstname")



    def enterInsurantData(self):

        self.driver.find_element(*self.first_name).send_keys("zafar")
        time.sleep(5)


