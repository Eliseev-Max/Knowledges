import os.path

import pytest

from selenium import webdriver

DRIVERS = os.path.expanduser("~/webdriver")

def pytest_addoption(parser):
    parser.addoption("--maximized", action="store_true", help="Maximize browser windows")
    parser.addoption("--headless", action="store_true", help="Run headless")
    parser.addoption("--browser", action="store", choices=["chrome", "firefox", "opera"], default="chrome")

# Headless-режим - режим без отрисовки окон, элементов HTML...
@pytest.fixture
def browser(request):
    browser = request.config.getoption("--browser")
    headless = request.config.getoption("--headless")
    maximized = request.config.getoption("--maximized")

#    drvier = None      # переменную объявлять необязательно, есть elif..else

    if browser == "chrome":
        options = webdriver.ChromeOptions()
        options.headless = headless
        driver = webdriver.Chrome(
            executable_path=f"{DRIVERS}/chromedriver",
            options=options
        )
    elif browser == "firefox":
        options = webdriver.FirefoxOptions()
        options.headless = headless
        driver = webdriver.Firefox(executable_path=f"{DRIVERS}/geckodriver",
                                   options=options
        )
    elif browser == "opera":
        driver = webdriver.Opera(executable_path=f"{DRIVERS}/operadriver")
    else:
        raise ValueError(f"Driver not supported: {browser}")

    request.addfinalizer(driver.quit)

    if maximized:
        driver.maximize_window()

    return driver
