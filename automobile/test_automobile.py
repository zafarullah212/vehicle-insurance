
from pageobjects.automobile.automobilePage import Automobile


def test_automobile(BrowserIntance):

    driver = BrowserIntance
    automobile = Automobile(driver)
    automobile.enter_vehicle_date()

    page_title = automobile.get_title()
    assert "Enter Insurant Data" in page_title


