import logging
import os
import pytest
from selenium import webdriver

DRIVERS = os.path.expanduser("~/webdrivers")

logging.basicConfig(level=logging.INFO,
                    filename="logs/selenium.log",
                    format='%(asctime)s %(levelname)s::%(name)s: %(message)s',
                    datefmt='%I:%M:%S')


def pytest_addoption(parser):
    parser.addoption("--maximized", action="store_true", help="Maximize browser windows")
    parser.addoption("--headless", action="store_true", help="Run headless")
    parser.addoption("--browser", action="store", choices=["chrome", "firefox", "opera"], default="chrome")
    parser.addoption("--url", action="store", default="http://172.19.16.229/")
    # parser.addoption("--url", action="store", default="http://10.0.2.15/")
    # parser.addoption("--url", action="store", default="http://192.168.1.48/")


@pytest.fixture(scope="session")
def get_environment(pytestconfig):
    props = {
        'Shell': os.getenv('SHELL'),
        'Terminal': os.getenv('TERM'),
        'Stand': 'Production'
    }

    tests_root = pytestconfig.rootdir
    with open(f'{tests_root}/allure-results/environment.properties', 'w') as f:
        for k, v in props.items():
            f.write(f'{k}={v}\n')


@pytest.fixture
def browser(request):
    browser = request.config.getoption("--browser")
    headless = request.config.getoption("--headless")
    maximized = request.config.getoption("--maximized")
    logger = logging.getLogger('BrowserLogger')
    test_name = request.node.name

    logger.info("\tTest \"{}\" is running".format(test_name))

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

    if maximized:
        driver.maximize_window()

    logger.info("Browser {} started with such capabilities: {}".format(browser, driver.desired_capabilities))


    def final():
        logger.info("\tTest \"{}\" completed\n".format(test_name))
        driver.quit()

    request.addfinalizer(final)

    return driver

@pytest.fixture
def base_url(request):
    return request.config.getoption("--url")