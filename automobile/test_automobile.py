from pageobjects.automobile.enter_insurant_data import EnterInsurantData
from pageobjects.automobile.enter_vehicle_data import Automobile


def test_automobile(BrowserIntance):

    driver = BrowserIntance
    automobile = Automobile(driver)
    automobile.enter_vehicle_date()

    page_title = automobile.get_title()
    assert "Enter Insurant Data" in page_title , "Tab Title Doest not match"

    #Enter Insurant Data Tab activated#

    enterInsurantobj = EnterInsurantData(driver)
    enterInsurantobj.enterInsurantData()

