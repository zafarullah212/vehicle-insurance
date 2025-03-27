import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption(
        "--browser-name", action="store", default="chrome", help="browser selection"
    )

@pytest.fixture(scope="function")
def BrowserIntance(request):

    browser_name = request.config.getoption("--browser-name")
    if browser_name == "chrome":
        chrome_options = Options()
        chrome_options.add_experimental_option("prefs", {
            "download.default_directory": r"C:\Users\Zafar\Downloads",  # File download location
            "download.prompt_for_download": False,  # Download confirmation popup disable karega
            "download.directory_upgrade": True,
            "safebrowsing.enabled": True  # Safe browsing enabled
        })

        driver = webdriver.Chrome()



    elif browser_name == "firefox":

        driver = webdriver.Firefox()

    driver.get("https://sampleapp.tricentis.com/101/app.php")
    driver.maximize_window()
    driver.implicitly_wait(5)
    yield driver
    driver.close()