from pageobjects.automobile.enter_insurant_data import EnterInsurantData
from pageobjects.automobile.enter_product_data import ProductData
from pageobjects.automobile.enter_vehicle_data import Automobile
from pageobjects.automobile.price_options import PriceOption
from pageobjects.automobile.send_quote import sendQuoute


def test_automobile(BrowserIntance):

    driver = BrowserIntance
    automobile = Automobile(driver)
    automobile.enter_vehicle_date()

    page_title = automobile.get_title()
    assert "Enter Insurant Data" in page_title , "Tab Title Doest not match"

    #Enter Insurant Data Tab activated#

    enterInsurantobj = EnterInsurantData(driver)
    enterInsurantobj.enterInsurantData()

    # Enter Product Data

    productData = ProductData(driver)
    productData.enter_product_data()

    # Price Option

    price_opt =  PriceOption(driver)
    price_opt.ChoosePrice()

    #send quote

    send_quote =  sendQuoute(driver)
    send_quote.send_quote()
