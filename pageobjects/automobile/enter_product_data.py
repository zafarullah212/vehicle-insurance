import time

from attr.validators import optional
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from utils.browserUtils import BrowserUtils


class ProductData(BrowserUtils):
    def __init__(self , driver):
        super().__init__(driver)

        self.start_date = (By.ID, "startdate")
        self.insurance_sum = (By.ID , "insurancesum")
        self.meritrating = (By.ID , "meritrating")
        self.damageinsurance = (By.ID , "damageinsurance")
        self.Optional_product = (By.CSS_SELECTOR , "input[id='EuroProtection']")
        self.courtesycar = (By.ID , "courtesycar")
        self.next = (By.ID, "nextselectpriceoption")

    def enter_product_data(self):

        self.driver.find_element(*self.start_date).send_keys("08/05/2025")

        insurance_sum = Select(self.driver.find_element(*self.insurance_sum))
        insurance_sum.select_by_visible_text("3.000.000,00")

        merifRating = Select(self.driver.find_element(*self.meritrating))
        merifRating.select_by_index(3)

        damageInsurance = Select(self.driver.find_element(*self.damageinsurance))
        damageInsurance.select_by_visible_text("No Coverage")

        optional_product = self.driver.find_element(*self.Optional_product)
        self.driver.execute_script("arguments[0].click();", optional_product)

        courtesy = Select(self.driver.find_element(*self.courtesycar))
        courtesy.select_by_visible_text("No")


        self.driver.find_element(*self.next).click()


