import os.path

import pytest

from selenium import webdriver

DRIVERS = os.path.expanduser("~/Downloads/drivers")

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
        options
        driver = webdriver.Chrome(executable_path=f"{DRIVERS}/chromedriver")
    elif browser == "firefox":
        driver = webdriver.Firefox()
    elif browser == "opera":
        driver = webdriver.Opera()
    else:
        raise ValueError(f"Driver not supported: {browser}")

    request.addfinalizer(driver.quit)

    if maximized:
        driver.maximize_window()

    return driver
