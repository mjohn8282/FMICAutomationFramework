import configparser
from selenium import webdriver
import pytest
from Utilities.readProperties import Readconfi


@pytest.fixture()
def intialiseconfigfile():
    config = configparser.RawConfigParser()
    config.read(".\\Configurations\\config.ini")
    return config


@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")


@pytest.fixture()
def setup(browser, intialiseconfigfile):
    config = Readconfi(intialiseconfigfile)

    if browser == "chrome":
        options = webdriver.ChromeOptions()
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        print("before Launching Chrome")
        driver = webdriver.Chrome(config.getchromedriverlocation, options=options)
        print("Launching Chrome")

    elif browser == "firefox":
        driver = webdriver.Firefox(config.getfirefoxdriverlocation())
        print("Launching Firefox")
    elif browser == "Edge":
        driver = webdriver.Edge(config.getedgedriverlocation())
    else:
        options = webdriver.ChromeOptions()
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        driver = webdriver.Chrome(config.getchromedriverlocation(), options=options)

    yield driver

    driver.quit()


def pytest_addoption(parser):  # will get the values from CLI /hooks
    parser.addoption("--browser")


def take_screenshot(browser,test_name):
    screenshots_dir="Screenshots"
    screenshot_file_path = "{}/{}.png".format(screenshots_dir, test_name)
    browser.save_screenshot(screenshot_file_path)


###pytest html report##
def pytest_configure(config):
    config._metadata['Project Name'] = 'Bench Mark Analytics'
    config._metadata['Module Name'] = 'Login'


def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Packages", None)
    metadata.pop("Plugins", None)
