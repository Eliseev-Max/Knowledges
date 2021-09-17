import pytest
from selenium import webdriver

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome")
    parser.addoption("--executor", action="store", default="192.168.1.84")
    parser.addoption("--bversion", action="store", default="88.0")
    parser.addoption("--vnc", action="store_true", default="False")
    parser.addoption("--logs", action="store_true", default="False")
    parser.addoption("--videos", action="store_true", default="False")
    parser.addoption("--mobile", action="store_true")


@pytest.fixture
def browser(request):
    browser = request.config.getoption("--browser")  # Имя браузера, который мы хотим запустить
    executor = request.config.getoption("--executor")  # где находится Selenium Server
    version = request.config.getoption("--bversion")
    vnc = request.config.getoption("--vnc")
    logs = request.config.getoption("--logs")
    videos = request.config.getoption("--videos")
    mobile = request.config.getoption("--mobile")

    executor_url = f"http://{executor}:4444/wd/hub"

    caps = {
        "browserName": browser,
        "browserVersion": version,
        "screenResolution": "1280x720",  # разрешение экрана
        "name": "Max E.",  # именовать прогоны тестов
        "selenoid:options": {
            "enableVNC": vnc,  # визуализация (прорисовка) выполнения тестов
            "enableVideo": videos,  # запись видео выполнения теста
            "enableLog": logs  # запись логов работы КОНТЕЙНЕРОВ
        },
        'goog:chromeOptions': {}
    }

    if browser == "chrome" and mobile:  # Эмуляция работы браузера на мобильном устройстве
        caps["goog:chromeOptions"]["mobileEmulation"] = {"deviceName": "iPhone 5/SE"}

    driver = webdriver.Remote(
        command_executor=executor_url,
        desired_capabilities=caps
    )

    if not mobile:
        driver.maximize_window()

    def fin():
        driver.quit()

    request.addfinalizer(fin)
    return driver