import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from utils.browserUtils import BrowserUtils


class EnterInsurantData(BrowserUtils):

    def __init__(self, driver):
        super().__init__(driver)
        self.first_name = (By.ID, "firstname")
        self.last_name = (By.ID, "lastname")
        self.birthdate = (By.ID, "birthdate")
        self.gender = (By.ID, "gendermale")
        self.streetaddress = (By.ID, "streetaddress")
        self.country = (By.ID, "country")
        self.zipcode = (By.ID, "zipcode")
        self.city = (By.ID, "city")
        self.occupation = (By.ID, "occupation")
        self.hobbies = (By.ID, "speeding")
        self.nextenterproductdata = (By.ID, "nextenterproductdata")



    def enterInsurantData(self):

        self.driver.find_element(*self.first_name).send_keys("zafar")

        self.driver.find_element(*self.last_name).send_keys("ullah")
        self.driver.find_element(*self.birthdate).send_keys("10/02/1989")
        element = self.driver.find_element(*self.gender)
        self.driver.execute_script("arguments[0].click();", element)
        self.driver.find_element(*self.streetaddress).send_keys("okrifiteler Strasse")

        country = Select(self.driver.find_element(*self.country))
        country.select_by_visible_text("Germany")

        self.driver.find_element(*self.zipcode).send_keys("64546")
        self.driver.find_element(*self.city).send_keys("Morfelden-walldorf")
        self.driver.find_element(*self.city).send_keys("Morfelden-walldorf")


        occupation = Select(self.driver.find_element(*self.occupation))
        occupation.select_by_value("Employee")
        hobby = self.driver.find_element(*self.hobbies)
        self.driver.execute_script("arguments[0].click();", hobby)

        self.driver.find_element(*self.nextenterproductdata).click()
