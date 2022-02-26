from selenium import webdriver
import pytest


@pytest.fixture()
def setup(browser):
    if browser == 'chrome':
        driver = webdriver.Chrome()
        print('********** Launch Chrome browser **********')
    elif browser == 'firefox':
        driver = webdriver.Firefox()
        print('********** Launch Firefox browser **********')
    else:
        driver = webdriver.Edge()
    return driver


def pytest_addoption(parser): # This will get the value from CLI/hooks
    parser.addoption("--browser")


@pytest.fixture()
def browser(request): # This will return the Browser value to setup method
    return request.config.getoption("--browser")

##### PyTest HTML Report #####

# It is hook for Adding Environment info to HTML Report
def pytest_configure(config):
    config._metadata['Project Name'] = 'Happify'
    config._metadata['Module Name'] = 'Register'
    config._metadata['Tester Name'] = 'Gadzhi'

# It is hook for delete/modify Environment info to HTML Report
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)

# Run this command in terminal to generate pytest report ---> pytest -s -v -n=3 --html=Reports/report.html testCases/test_login.py --browser firefox