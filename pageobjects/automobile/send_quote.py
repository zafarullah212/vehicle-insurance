import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from utils.browserUtils import BrowserUtils


class sendQuoute(BrowserUtils):

    def __init__(self, driver):
        super().__init__(driver)

        self.email = (By.ID, "email")
        self.username = (By.ID, "username")
        self.password = (By.ID, "password")
        self.c_password = (By.ID, "confirmpassword")
        self.sendemail = (By.ID, "sendemail")
        self.message = (By.CLASS_NAME, "sweet-alert")
        self.confirm = (By.CLASS_NAME, "confirm")


    def send_quote(self):

        self.driver.find_element(*self.email).send_keys("zafarullah212@gmail.com")
        self.driver.find_element(*self.username).send_keys("zafarullah212")
        self.driver.find_element(*self.password).send_keys("Anmolzafar@18")
        self.driver.find_element(*self.c_password).send_keys("Anmolzafar@18")
        self.driver.find_element(*self.sendemail).click()

        wait = WebDriverWait(self.driver , 10)
        wait.until(expected_conditions.presence_of_element_located(self.message))

        expected_message = "Sending e-mail success!"

        actual_message = self.driver.find_element(*self.message).text


        assert "Sending e-mail success!" in expected_message , f"Expected '{expected_message}', but got '{actual_message}'"



