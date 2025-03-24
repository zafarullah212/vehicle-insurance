import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption(
        "--browser-name", action="store", default="chrome", help="browser selection"
    )

@pytest.fixture(scope="function")
def BrowserIntance(request):

    browser_name = request.config.getoption("--browser-name")
    if browser_name == "chrome":

        driver = webdriver.Chrome()


    elif browser_name == "firefox":

        driver = webdriver.Firefox()

    driver.get("https://sampleapp.tricentis.com/101/app.php")
    driver.maximize_window()
    driver.implicitly_wait(5)
    yield driver
    driver.close()