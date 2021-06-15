from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


def element_existence(driver, element):
    try:
        driver.find_element(element)
    except NoSuchElementException as no_elem:
        raise AssertionError(no_elem, "Данный селектор не обнаружен")
    except Exception as err:
        raise AssertionError(err)


def wait_title(title, driver, timeout=3):
    try:
        WebDriverWait(driver, timeout).until(EC.title_is(title))
    except TimeoutException:
        # Выбрасываю своё исключение и добавляю сообщение
        raise AssertionError("Ждал что title будет: '{}' но он был '{}'".format(title, driver.title))

