import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from utils.browserUtils import BrowserUtils


class Automobile(BrowserUtils):

    def __init__(self, driver):

        super().__init__(driver) #inheriting and calling parent Class instructor

        self.driver = driver
        self.nav_click = (By.ID, "nav_automobile")
        self.make = (By.XPATH, "//select[@name='Make']")
        self.engine_performance = (By.XPATH, "//input[@name='[kW]']")
        self.date_of_manufacture = (By.XPATH, "//input[@id='dateofmanufacture']")
        self.number_of_seats = (By.ID, "numberofseats")
        self.fuel_type = (By.ID, "fuel")
        self.list_price = (By.ID, "listprice")
        self.annual_milage = (By.ID , "annualmileage")
        self.next = (By.ID, "nextenterinsurantdata")

    def enter_vehicle_date(self):

        self.driver.find_element(*self.nav_click).click()
        make = Select(self.driver.find_element(*self.make))
        make.select_by_value("Audi")

        self.driver.find_element(*self.engine_performance).send_keys("2000")

        self.driver.find_element(*self.date_of_manufacture).send_keys("04/12/2023")

        number_of_seats = Select(self.driver.find_element(*self.number_of_seats))
        number_of_seats.select_by_visible_text("4")

        fuel_type = Select(self.driver.find_element(*self.fuel_type))
        fuel_type.select_by_index(3)

        self.driver.find_element(*self.list_price).send_keys("5000")
        self.driver.find_element(*self.annual_milage).send_keys("250")

        self.driver.find_element(*self.next).click()
